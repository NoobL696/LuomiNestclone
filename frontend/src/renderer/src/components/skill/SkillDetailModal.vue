<script setup lang="ts">
import { computed, ref } from 'vue'
import {
  X,
  Star,
  Download,
  ExternalLink,
  GitBranch,
  Github,
  Package,
  Clock,
  User,
  Tag,
  FileText,
  Shield,
  ChevronRight,
  Trash2,
  RefreshCw,
  Loader2,
  CheckCircle2,
  AlertCircle
} from 'lucide-vue-next'
import type { SkillManifest, SkillSource } from '@/types'

const props = defineProps<{
  skill: SkillManifest
}>()

const emit = defineEmits<{
  close: []
  install: [skill: SkillManifest]
  uninstall: [skillId: string]
  update: [skillId: string]
}>()

const activeTab = ref<'info' | 'versions' | 'readme'>('info')

const sourceIcon = (src: SkillSource) => {
  switch (src) {
    case 'github': return Github
    case 'git':
    case 'gitee':
    case 'gitlab': return GitBranch
    default: return Package
  }
}

const sourceLabel = (src: SkillSource) => {
  switch (src) {
    case 'github': return 'GitHub'
    case 'gitee': return 'Gitee'
    case 'gitlab': return 'GitLab'
    case 'git': return 'Git'
    case 'local': return '本地'
    case 'marketplace': return '市场'
    default: return src
  }
}

const categoryLabel = (cat: string) => {
  const map: Record<string, string> = {
    conversation: '对话',
    productivity: '效率',
    creative: '创意',
    automation: '自动化',
    iot: 'IoT',
    social: '社交',
    knowledge: '知识',
    voice: '语音',
    vision: '视觉',
    other: '其他'
  }
  return map[cat] ?? cat
}

const statusLabel = (status: string) => {
  const map: Record<string, string> = {
    available: '可安装',
    installed: '已安装',
    updating: '更新中',
    installing: '安装中',
    error: '异常'
  }
  return map[status] ?? status
}

const statusClass = (status: string) => {
  switch (status) {
    case 'installed': return 'status-installed'
    case 'installing': return 'status-installing'
    case 'updating': return 'status-updating'
    case 'error': return 'status-error'
    default: return 'status-available'
  }
}

const formatDate = (ts: number) => {
  const d = new Date(ts)
  return d.toLocaleDateString('zh-CN', { year: 'numeric', month: 'short', day: 'numeric' })
}

const isInstalled = computed(() => props.skill.status === 'installed')
const isUpdating = computed(() => props.skill.status === 'updating')

function handleOverlayClick() {
  emit('close')
}

function handleInstall() {
  emit('install', props.skill)
}

function handleUninstall() {
  emit('uninstall', props.skill.id)
}

function handleUpdate() {
  emit('update', props.skill.id)
}
</script>

<template>
  <Teleport to="body">
    <div class="modal-overlay" @click="handleOverlayClick">
      <div class="detail-modal animate-scale-in" @click.stop>
        <div class="modal-header">
          <div class="modal-header-left">
            <div class="detail-icon">{{ skill.icon || '📦' }}</div>
            <div class="detail-title-area">
              <h2>{{ skill.name }}</h2>
              <div class="detail-badges">
                <span class="detail-version">v{{ skill.version }}</span>
                <span :class="['skill-status-badge', statusClass(skill.status)]">
                  {{ statusLabel(skill.status) }}
                </span>
                <span class="detail-category">{{ categoryLabel(skill.category) }}</span>
              </div>
            </div>
          </div>
          <button class="close-btn" @click="emit('close')">
            <X :size="18" />
          </button>
        </div>

        <div class="modal-tabs">
          <button
            v-for="tab in (['info', 'versions', 'readme'] as const)"
            :key="tab"
            :class="['tab-btn', { active: activeTab === tab }]"
            @click="activeTab = tab"
          >
            {{ tab === 'info' ? '详情' : tab === 'versions' ? '版本历史' : '说明文档' }}
          </button>
        </div>

        <div class="modal-body">
          <div v-if="activeTab === 'info'" class="tab-content info-tab">
            <div class="info-section">
              <h4>描述</h4>
              <p class="info-desc">{{ skill.longDescription || skill.description }}</p>
            </div>

            <div class="info-section">
              <h4>基本信息</h4>
              <div class="info-grid">
                <div class="info-row">
                  <span class="info-label"><User :size="14" /> 作者</span>
                  <span class="info-value">
                    <a v-if="skill.author.url" :href="skill.author.url" target="_blank" class="info-link">
                      {{ skill.author.name }}
                      <ExternalLink :size="10" />
                    </a>
                    <span v-else>{{ skill.author.name }}</span>
                  </span>
                </div>
                <div class="info-row">
                  <span class="info-label"><Shield :size="14" /> 许可证</span>
                  <span class="info-value">{{ skill.license || '未指定' }}</span>
                </div>
                <div class="info-row">
                  <span class="info-label"><Star :size="14" /> 评分</span>
                  <span class="info-value rating-value">
                    <Star :size="14" class="star-icon" />
                    {{ skill.rating?.toFixed(1) ?? '-' }}
                  </span>
                </div>
                <div class="info-row">
                  <span class="info-label"><Download :size="14" /> 下载量</span>
                  <span class="info-value">{{ skill.downloads?.toLocaleString() ?? '0' }}</span>
                </div>
                <div v-if="skill.installedAt" class="info-row">
                  <span class="info-label"><Clock :size="14" /> 安装时间</span>
                  <span class="info-value">{{ formatDate(skill.installedAt) }}</span>
                </div>
                <div v-if="skill.minAppVersion" class="info-row">
                  <span class="info-label"><Package :size="14" /> 最低版本</span>
                  <span class="info-value">{{ skill.minAppVersion }}</span>
                </div>
              </div>
            </div>

            <div class="info-section">
              <h4>来源</h4>
              <div class="source-list">
                <div v-for="res in skill.resources" :key="res.url" class="source-item">
                  <component :is="sourceIcon(res.type)" :size="16" class="source-icon" />
                  <div class="source-info">
                    <span class="source-type">{{ sourceLabel(res.type) }}</span>
                    <a :href="res.url" target="_blank" class="source-url">
                      {{ res.url }}
                      <ExternalLink :size="10" />
                    </a>
                  </div>
                  <span v-if="res.branch" class="source-branch">{{ res.branch }}</span>
                </div>
              </div>
            </div>

            <div v-if="skill.homepage || skill.repository" class="info-section">
              <h4>链接</h4>
              <div class="link-list">
                <a v-if="skill.homepage" :href="skill.homepage" target="_blank" class="link-item">
                  <ExternalLink :size="14" /> 主页
                </a>
                <a v-if="skill.repository" :href="skill.repository" target="_blank" class="link-item">
                  <GitBranch :size="14" /> 仓库
                </a>
              </div>
            </div>

            <div v-if="skill.tags.length > 0" class="info-section">
              <h4><Tag :size="14" /> 标签</h4>
              <div class="tag-list">
                <span v-for="tag in skill.tags" :key="tag" class="tag-item">{{ tag }}</span>
              </div>
            </div>

            <div v-if="skill.dependencies && skill.dependencies.length > 0" class="info-section">
              <h4>依赖</h4>
              <div class="dep-list">
                <span v-for="dep in skill.dependencies" :key="dep" class="dep-item">{{ dep }}</span>
              </div>
            </div>
          </div>

          <div v-if="activeTab === 'versions'" class="tab-content versions-tab">
            <div v-if="!skill.versions || skill.versions.length === 0" class="empty-versions">
              <FileText :size="32" />
              <p>暂无版本记录</p>
            </div>
            <div v-else class="version-list">
              <div
                v-for="ver in skill.versions"
                :key="ver.version"
                :class="['version-item', { current: ver.version === skill.version }]"
              >
                <div class="version-marker">
                  <CheckCircle2 v-if="ver.version === skill.version" :size="16" class="current-marker" />
                  <span v-else class="version-dot"></span>
                </div>
                <div class="version-info">
                  <div class="version-top">
                    <span class="version-number">v{{ ver.version }}</span>
                    <span v-if="ver.version === skill.version" class="current-badge">当前</span>
                    <span class="version-date">{{ formatDate(ver.releasedAt) }}</span>
                  </div>
                  <p class="version-changelog">{{ ver.changelog }}</p>
                  <span v-if="ver.minAppVersion" class="version-min-ver">需要 v{{ ver.minAppVersion }}+</span>
                </div>
              </div>
            </div>
          </div>

          <div v-if="activeTab === 'readme'" class="tab-content readme-tab">
            <div class="readme-content">
              <h3>{{ skill.name }}</h3>
              <p>{{ skill.longDescription || skill.description }}</p>
              <h4>安装方式</h4>
              <div class="readme-code">
                <code>luominest skill install {{ skill.id }}</code>
              </div>
              <h4>使用说明</h4>
              <p>安装完成后，在对话中通过自然语言调用此技能。你也可以在工作流编辑器中将此技能作为节点添加到自动化流程中。</p>
              <div v-if="skill.resources.length > 0" class="readme-source">
                <h4>获取源码</h4>
                <p>访问 <a :href="skill.repository || skill.resources[0].url" target="_blank">项目仓库</a> 获取最新源码和贡献指南。</p>
              </div>
            </div>
          </div>
        </div>

        <div class="modal-footer">
          <template v-if="isInstalled">
            <button class="footer-btn danger" @click="handleUninstall">
              <Trash2 :size="14" />
              卸载
            </button>
            <button class="footer-btn update" :disabled="isUpdating" @click="handleUpdate">
              <RefreshCw v-if="!isUpdating" :size="14" />
              <Loader2 v-else :size="14" class="spinning" />
              {{ isUpdating ? '更新中...' : '检查更新' }}
            </button>
          </template>
          <template v-else>
            <button class="footer-btn cancel" @click="emit('close')">取消</button>
            <button class="footer-btn install" @click="handleInstall">
              <Download :size="14" />
              安装技能
            </button>
          </template>
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
  z-index: 2000;
  padding: 20px;
}

.detail-modal {
  width: 640px;
  max-width: 100%;
  max-height: 85vh;
  background: var(--surface);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.modal-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 24px 24px 16px;
  border-bottom: 1px solid var(--border-light);
}

.modal-header-left {
  display: flex;
  align-items: flex-start;
  gap: 14px;
}

.detail-icon {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-lg);
  background: var(--surface-hover);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  flex-shrink: 0;
}

.detail-title-area h2 {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 6px;
}

.detail-badges {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.detail-version {
  font-size: 11px;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  background: var(--bg-secondary);
  color: var(--text-secondary);
}

.skill-status-badge {
  font-size: 10px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: var(--radius-full);
  letter-spacing: 0.3px;
}

.status-available { background: rgba(13, 148, 136, 0.1); color: var(--lumi-primary); }
.status-installed { background: rgba(34, 197, 94, 0.1); color: #16a34a; }
.status-installing { background: rgba(59, 130, 246, 0.1); color: #3b82f6; }
.status-updating { background: rgba(234, 179, 8, 0.1); color: #ca8a04; }
.status-error { background: var(--lumi-accent-light); color: var(--lumi-accent); }

.detail-category {
  font-size: 10px;
  font-weight: 500;
  padding: 3px 8px;
  border-radius: var(--radius-full);
  background: var(--lumi-primary-light);
  color: var(--lumi-primary);
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

.modal-tabs {
  display: flex;
  gap: 2px;
  padding: 0 24px;
  border-bottom: 1px solid var(--border-light);
}

.tab-btn {
  padding: 12px 16px;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-muted);
  cursor: pointer;
  transition: all var(--transition-fast);
  position: relative;
}

.tab-btn:hover {
  color: var(--text-secondary);
}

.tab-btn.active {
  color: var(--lumi-primary);
}

.tab-btn.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--lumi-primary);
  border-radius: 2px 2px 0 0;
}

.modal-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px 24px;
}

.tab-content {
  animation: lumi-fade-in 0.2s ease-out;
}

.info-section {
  margin-bottom: 20px;
}

.info-section h4 {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--text-muted);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.info-desc {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.7;
}

.info-grid {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.info-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  background: var(--bg-secondary);
}

.info-label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--text-muted);
}

.info-value {
  font-size: 13px;
  font-weight: 500;
  color: var(--text-primary);
}

.info-link {
  display: flex;
  align-items: center;
  gap: 4px;
  color: var(--lumi-primary);
  transition: opacity var(--transition-fast);
}

.info-link:hover {
  opacity: 0.8;
}

.rating-value {
  display: flex;
  align-items: center;
  gap: 4px;
}

.star-icon {
  color: #eab308;
}

.source-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.source-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: var(--radius-sm);
  background: var(--bg-secondary);
}

.source-icon {
  color: var(--text-muted);
  flex-shrink: 0;
}

.source-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.source-type {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-secondary);
}

.source-url {
  font-size: 11px;
  color: var(--lumi-primary);
  display: flex;
  align-items: center;
  gap: 4px;
  word-break: break-all;
}

.source-branch {
  font-size: 10px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  background: var(--surface);
  color: var(--text-muted);
  flex-shrink: 0;
}

.link-list {
  display: flex;
  gap: 10px;
}

.link-item {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  background: var(--bg-secondary);
  font-size: 12px;
  font-weight: 500;
  color: var(--lumi-primary);
  transition: all var(--transition-fast);
}

.link-item:hover {
  background: var(--lumi-primary-light);
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tag-item {
  font-size: 11px;
  font-weight: 500;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  background: var(--bg-secondary);
  color: var(--text-secondary);
}

.dep-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.dep-item {
  font-size: 11px;
  font-weight: 500;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  background: rgba(59, 130, 246, 0.08);
  color: #3b82f6;
}

.empty-versions {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 0;
  color: var(--text-muted);
  gap: 10px;
}

.version-list {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.version-item {
  display: flex;
  gap: 12px;
  padding: 14px 0;
  border-bottom: 1px solid var(--border-light);
}

.version-item:last-child {
  border-bottom: none;
}

.version-item.current {
  background: none;
}

.version-marker {
  display: flex;
  align-items: flex-start;
  padding-top: 2px;
  flex-shrink: 0;
}

.current-marker {
  color: #16a34a;
}

.version-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--border);
  margin-top: 4px;
}

.version-info {
  flex: 1;
}

.version-top {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.version-number {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
}

.current-badge {
  font-size: 10px;
  font-weight: 600;
  padding: 1px 6px;
  border-radius: var(--radius-full);
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
}

.version-date {
  font-size: 11px;
  color: var(--text-muted);
  margin-left: auto;
}

.version-changelog {
  font-size: 12px;
  color: var(--text-secondary);
  line-height: 1.5;
}

.version-min-ver {
  font-size: 10px;
  color: var(--text-muted);
  margin-top: 4px;
  display: inline-block;
}

.readme-content h3 {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.readme-content h4 {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 16px 0 8px;
}

.readme-content p {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 8px;
}

.readme-content a {
  color: var(--lumi-primary);
}

.readme-content a:hover {
  text-decoration: underline;
}

.readme-code {
  padding: 12px 16px;
  border-radius: var(--radius-sm);
  background: var(--bg-secondary);
  border: 1px solid var(--border-light);
  margin: 8px 0 16px;
}

.readme-code code {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 12px;
  color: var(--lumi-primary);
}

.modal-footer {
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

.footer-btn.install:hover {
  background: var(--lumi-primary-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(13, 148, 136, 0.3);
}

.footer-btn.danger {
  color: var(--lumi-accent);
  background: var(--lumi-accent-light);
}

.footer-btn.danger:hover {
  background: rgba(244, 63, 94, 0.15);
}

.footer-btn.update {
  color: var(--lumi-primary);
  background: var(--lumi-primary-light);
}

.footer-btn.update:hover {
  background: rgba(13, 148, 136, 0.15);
}

.footer-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.spinning {
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 640px) {
  .detail-modal {
    max-height: 95vh;
    border-radius: var(--radius-lg);
  }

  .modal-header {
    padding: 18px 18px 12px;
  }

  .modal-body {
    padding: 16px 18px;
  }

  .modal-footer {
    padding: 12px 18px;
  }
}
</style>
