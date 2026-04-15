<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import {
  X,
  GitBranch,
  Github,
  Download,
  Loader2,
  CheckCircle2,
  AlertCircle,
  FolderOpen,
  ChevronDown
} from 'lucide-vue-next'
import type { SkillManifest, SkillSource, SkillInstallConfig } from '@/types'

const props = defineProps<{
  skill: SkillManifest
}>()

const emit = defineEmits<{
  close: []
  complete: [skillId: string]
}>()

type InstallStep = 'config' | 'installing' | 'success' | 'error'

const step = ref<InstallStep>('config')
const selectedSource = ref<SkillSource>(props.skill.resources[0]?.type ?? 'github')
const repoUrl = ref(props.skill.repository || props.skill.resources[0]?.url || '')
const branch = ref(props.skill.resources[0]?.branch || 'main')
const tag = ref(props.skill.resources[0]?.tag || '')
const targetPath = ref('')
const overwrite = ref(false)
const errorMessage = ref('')
const installProgress = ref(0)

const sourceOptions: { value: SkillSource; label: string; icon: any }[] = [
  { value: 'github', label: 'GitHub', icon: Github },
  { value: 'gitee', label: 'Gitee', icon: GitBranch },
  { value: 'gitlab', label: 'GitLab', icon: GitBranch },
  { value: 'git', label: 'Git 仓库', icon: GitBranch },
  { value: 'marketplace', label: '技能市场', icon: Download }
]

const isNewInstall = computed(() => props.skill.id === '__new__')

const canInstall = computed(() => {
  if (selectedSource.value === 'marketplace') return true
  return repoUrl.value.trim().length > 0
})

const currentSourceOption = computed(() =>
  sourceOptions.find(s => s.value === selectedSource.value)
)

watch(selectedSource, () => {
  if (selectedSource.value !== 'marketplace') {
    const prefix = selectedSource.value === 'github'
      ? 'https://github.com/'
      : selectedSource.value === 'gitee'
        ? 'https://gitee.com/'
        : selectedSource.value === 'gitlab'
          ? 'https://gitlab.com/'
          : ''
    if (!repoUrl.value.startsWith(prefix) && prefix) {
      repoUrl.value = prefix
    }
  }
})

function handleOverlayClick() {
  emit('close')
}

async function handleInstall() {
  step.value = 'installing'
  installProgress.value = 0
  errorMessage.value = ''

  const config: SkillInstallConfig = {
    source: selectedSource.value,
    url: repoUrl.value,
    branch: branch.value || undefined,
    tag: tag.value || undefined,
    targetPath: targetPath.value || undefined,
    overwrite: overwrite.value
  }

  const progressInterval = setInterval(() => {
    if (installProgress.value < 90) {
      installProgress.value += Math.random() * 15
      if (installProgress.value > 90) installProgress.value = 90
    }
  }, 300)

  try {
    await new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() > 0.1) {
          resolve(true)
        } else {
          reject(new Error('网络连接超时，请检查网络后重试'))
        }
      }, 2500)
    })

    clearInterval(progressInterval)
    installProgress.value = 100
    step.value = 'success'

    setTimeout(() => {
      emit('complete', props.skill.id)
    }, 1200)
  } catch (err) {
    clearInterval(progressInterval)
    errorMessage.value = err instanceof Error ? err.message : '安装失败，请重试'
    step.value = 'error'
  }
}

function handleRetry() {
  step.value = 'config'
  installProgress.value = 0
  errorMessage.value = ''
}
</script>

<template>
  <Teleport to="body">
    <div class="modal-overlay" @click="handleOverlayClick">
      <div class="install-dialog animate-scale-in" @click.stop>
        <div class="dialog-header">
          <div class="dialog-title-area">
            <Download :size="20" class="dialog-icon" />
            <h2>{{ isNewInstall ? '从仓库安装技能' : `安装 ${skill.name}` }}</h2>
          </div>
          <button class="close-btn" @click="emit('close')">
            <X :size="18" />
          </button>
        </div>

        <div class="dialog-body">
          <div v-if="step === 'config'" class="config-step">
            <div v-if="!isNewInstall" class="skill-preview">
              <span class="preview-icon">{{ skill.icon || '📦' }}</span>
              <div class="preview-info">
                <span class="preview-name">{{ skill.name }}</span>
                <span class="preview-desc">{{ skill.description }}</span>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">来源平台</label>
              <div class="source-selector">
                <button
                  v-for="opt in sourceOptions"
                  :key="opt.value"
                  :class="['source-option', { active: selectedSource === opt.value }]"
                  @click="selectedSource = opt.value"
                >
                  <component :is="opt.icon" :size="16" />
                  <span>{{ opt.label }}</span>
                </button>
              </div>
            </div>

            <div v-if="selectedSource !== 'marketplace'" class="form-group">
              <label class="form-label">仓库地址</label>
              <input
                v-model="repoUrl"
                type="text"
                placeholder="输入 Git 仓库 URL..."
                class="form-input"
              />
              <span class="form-hint">支持 HTTPS 和 SSH 格式的 Git 仓库地址</span>
            </div>

            <div v-if="selectedSource !== 'marketplace'" class="form-row">
              <div class="form-group flex-1">
                <label class="form-label">分支</label>
                <input
                  v-model="branch"
                  type="text"
                  placeholder="main"
                  class="form-input"
                />
              </div>
              <div class="form-group flex-1">
                <label class="form-label">标签 / 版本</label>
                <input
                  v-model="tag"
                  type="text"
                  placeholder="可选"
                  class="form-input"
                />
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">安装路径（可选）</label>
              <div class="path-input-wrap">
                <input
                  v-model="targetPath"
                  type="text"
                  placeholder="默认安装到 skills 目录"
                  class="form-input path-input"
                />
                <button class="path-browse-btn" title="浏览">
                  <FolderOpen :size="16" />
                </button>
              </div>
            </div>

            <div class="form-group">
              <label class="form-check">
                <input v-model="overwrite" type="checkbox" class="form-checkbox" />
                <span class="check-label">覆盖已存在的同名技能</span>
              </label>
            </div>
          </div>

          <div v-if="step === 'installing'" class="installing-step">
            <div class="installing-animation">
              <Loader2 :size="40" class="install-spinner" />
            </div>
            <h3>正在安装{{ isNewInstall ? '' : ` ${skill.name}` }}...</h3>
            <p class="install-status">
              {{ selectedSource === 'marketplace' ? '从技能市场下载中' : `从 ${currentSourceOption?.label} 克隆仓库中` }}
            </p>
            <div class="progress-bar-wrap">
              <div class="progress-bar">
                <div class="progress-fill" :style="{ width: installProgress + '%' }"></div>
              </div>
              <span class="progress-text">{{ Math.round(installProgress) }}%</span>
            </div>
          </div>

          <div v-if="step === 'success'" class="success-step">
            <div class="success-animation">
              <CheckCircle2 :size="48" class="success-icon" />
            </div>
            <h3>安装成功！</h3>
            <p>{{ isNewInstall ? '技能' : skill.name }} 已成功安装到本地</p>
          </div>

          <div v-if="step === 'error'" class="error-step">
            <div class="error-animation">
              <AlertCircle :size="48" class="error-icon" />
            </div>
            <h3>安装失败</h3>
            <p class="error-message">{{ errorMessage }}</p>
            <button class="retry-btn" @click="handleRetry">
              重试
            </button>
          </div>
        </div>

        <div v-if="step === 'config'" class="dialog-footer">
          <button class="footer-btn cancel" @click="emit('close')">取消</button>
          <button class="footer-btn install" :disabled="!canInstall" @click="handleInstall">
            <Download :size="14" />
            开始安装
          </button>
        </div>

        <div v-if="step === 'error'" class="dialog-footer">
          <button class="footer-btn cancel" @click="emit('close')">关闭</button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2001;
  padding: 20px;
}

.install-dialog {
  width: 520px;
  max-width: 100%;
  background: var(--surface);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.dialog-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px 16px;
  border-bottom: 1px solid var(--border-light);
}

.dialog-title-area {
  display: flex;
  align-items: center;
  gap: 10px;
}

.dialog-icon {
  color: var(--lumi-primary);
}

.dialog-title-area h2 {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
}

.close-btn {
  width: 34px;
  height: 34px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  transition: all var(--transition-fast);
  cursor: pointer;
  flex-shrink: 0;
}

.close-btn:hover {
  background: var(--surface-hover);
  color: var(--text-primary);
}

.dialog-body {
  padding: 20px 24px;
  overflow-y: auto;
  max-height: 60vh;
}

.skill-preview {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  border-radius: var(--radius-md);
  background: var(--bg-secondary);
  margin-bottom: 20px;
}

.preview-icon {
  font-size: 28px;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
  background: var(--surface);
  flex-shrink: 0;
}

.preview-info {
  flex: 1;
  min-width: 0;
}

.preview-name {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 2px;
}

.preview-desc {
  display: block;
  font-size: 12px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.form-group {
  margin-bottom: 16px;
}

.form-row {
  display: flex;
  gap: 12px;
}

.flex-1 {
  flex: 1;
}

.form-label {
  display: block;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 6px;
}

.form-input {
  width: 100%;
  padding: 9px 12px;
  border-radius: var(--radius-sm);
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  font-size: 13px;
  color: var(--text-primary);
  transition: all var(--transition-fast);
}

.form-input:focus {
  border-color: var(--lumi-primary);
  box-shadow: 0 0 0 3px var(--lumi-primary-glow);
}

.form-input::placeholder {
  color: var(--text-muted);
}

.form-hint {
  display: block;
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 4px;
}

.path-input-wrap {
  display: flex;
  gap: 6px;
}

.path-input {
  flex: 1;
}

.path-browse-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  color: var(--text-muted);
  cursor: pointer;
  transition: all var(--transition-fast);
  flex-shrink: 0;
}

.path-browse-btn:hover {
  border-color: var(--lumi-primary);
  color: var(--lumi-primary);
}

.form-check {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.form-checkbox {
  width: 16px;
  height: 16px;
  accent-color: var(--lumi-primary);
  cursor: pointer;
}

.check-label {
  font-size: 13px;
  color: var(--text-secondary);
}

.source-selector {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.source-option {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  font-size: 12px;
  font-weight: 500;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.source-option:hover {
  border-color: var(--lumi-primary);
  color: var(--text-primary);
}

.source-option.active {
  border-color: var(--lumi-primary);
  background: var(--lumi-primary-light);
  color: var(--lumi-primary);
}

.installing-step,
.success-step,
.error-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 30px 0;
  text-align: center;
}

.installing-animation {
  margin-bottom: 16px;
}

.install-spinner {
  color: var(--lumi-primary);
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.installing-step h3,
.success-step h3,
.error-step h3 {
  font-size: 16px;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 6px;
}

.install-status,
.success-step p,
.error-step p {
  font-size: 13px;
  color: var(--text-muted);
  margin-bottom: 16px;
}

.progress-bar-wrap {
  width: 100%;
  max-width: 320px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.progress-bar {
  flex: 1;
  height: 6px;
  border-radius: 3px;
  background: var(--bg-secondary);
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: 3px;
  background: linear-gradient(90deg, var(--lumi-primary), #14b8a6);
  transition: width 300ms ease-out;
}

.progress-text {
  font-size: 12px;
  font-weight: 600;
  color: var(--lumi-primary);
  min-width: 36px;
  text-align: right;
}

.success-animation {
  margin-bottom: 16px;
}

.success-icon {
  color: #16a34a;
  animation: success-pop 0.4s ease-out;
}

@keyframes success-pop {
  0% { transform: scale(0.5); opacity: 0; }
  60% { transform: scale(1.1); }
  100% { transform: scale(1); opacity: 1; }
}

.error-animation {
  margin-bottom: 16px;
}

.error-icon {
  color: var(--lumi-accent);
}

.error-message {
  font-size: 13px;
  color: var(--lumi-accent);
  background: var(--lumi-accent-light);
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  max-width: 360px;
  word-break: break-word;
}

.retry-btn {
  padding: 8px 20px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 600;
  color: var(--lumi-primary);
  background: var(--lumi-primary-light);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.retry-btn:hover {
  background: rgba(13, 148, 136, 0.15);
}

.dialog-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  padding: 16px 24px;
  border-top: 1px solid var(--border-light);
}

.footer-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 9px 18px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.footer-btn.cancel {
  color: var(--text-secondary);
  background: var(--surface-hover);
}

.footer-btn.cancel:hover {
  background: var(--bg-secondary);
}

.footer-btn.install {
  background: var(--lumi-primary);
  color: #fff;
}

.footer-btn.install:hover:not(:disabled) {
  background: var(--lumi-primary-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(13, 148, 136, 0.3);
}

.footer-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

@media (max-width: 540px) {
  .install-dialog {
    border-radius: var(--radius-lg);
  }

  .source-selector {
    flex-direction: column;
  }

  .form-row {
    flex-direction: column;
    gap: 0;
  }
}
</style>
