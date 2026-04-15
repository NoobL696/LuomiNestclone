<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import {
  Store,
  Search,
  Filter,
  Grid3X3,
  List,
  Upload,
  GitBranch,
  Github,
  Star,
  Download,
  ChevronDown,
  X,
  SlidersHorizontal,
  RefreshCw,
  Package,
  ArrowUpDown,
  Loader2
} from 'lucide-vue-next'
import SkillDetailModal from '@/components/skill/SkillDetailModal.vue'
import SkillInstallDialog from '@/components/skill/SkillInstallDialog.vue'
import SkillUploadDialog from '@/components/skill/SkillUploadDialog.vue'
import type { SkillManifest, SkillCategory, SkillSource, SkillStatus, SkillSearchQuery } from '@/types'

const categoryOptions: { value: SkillCategory | 'all'; label: string }[] = [
  { value: 'all', label: '全部分类' },
  { value: 'conversation', label: '对话' },
  { value: 'productivity', label: '效率' },
  { value: 'creative', label: '创意' },
  { value: 'automation', label: '自动化' },
  { value: 'iot', label: 'IoT' },
  { value: 'social', label: '社交' },
  { value: 'knowledge', label: '知识' },
  { value: 'voice', label: '语音' },
  { value: 'vision', label: '视觉' },
  { value: 'other', label: '其他' }
]

const sourceOptions: { value: SkillSource | 'all'; label: string }[] = [
  { value: 'all', label: '全部来源' },
  { value: 'marketplace', label: '市场' },
  { value: 'github', label: 'GitHub' },
  { value: 'gitee', label: 'Gitee' },
  { value: 'gitlab', label: 'GitLab' },
  { value: 'git', label: 'Git' },
  { value: 'local', label: '本地' }
]

const statusOptions: { value: SkillStatus | 'all'; label: string }[] = [
  { value: 'all', label: '全部状态' },
  { value: 'available', label: '可安装' },
  { value: 'installed', label: '已安装' },
  { value: 'updating', label: '更新中' },
  { value: 'installing', label: '安装中' },
  { value: 'error', label: '异常' }
]

const sortOptions: { value: SkillSearchQuery['sortBy']; label: string }[] = [
  { value: 'name', label: '名称' },
  { value: 'rating', label: '评分' },
  { value: 'downloads', label: '下载量' },
  { value: 'updatedAt', label: '更新时间' }
]

const mockSkills: SkillManifest[] = [
  {
    id: 'skill-weather',
    name: '天气查询',
    description: '实时天气查询与预报，支持全球城市定位',
    longDescription: '支持全球城市的实时天气查询，包括温度、湿度、风速、空气质量等详细指标。提供未来7天天气预报和恶劣天气预警功能。可结合IoT设备自动调节室内环境。',
    version: '1.2.0',
    category: 'iot',
    tags: ['天气', 'IoT', '预报'],
    author: { name: 'LuomiNest Team', url: 'https://github.com/luominest' },
    icon: '🌤️',
    homepage: 'https://github.com/luominest/skill-weather',
    repository: 'https://github.com/luominest/skill-weather',
    license: 'MIT',
    resources: [{ type: 'github', url: 'https://github.com/luominest/skill-weather', branch: 'main' }],
    versions: [
      { version: '1.2.0', changelog: '新增空气质量指数', releasedAt: Date.now() - 86400000 },
      { version: '1.1.0', changelog: '修复定位问题', releasedAt: Date.now() - 86400000 * 7 }
    ],
    rating: 4.8,
    downloads: 3240,
    status: 'available'
  },
  {
    id: 'skill-code-review',
    name: '代码审查',
    description: 'AI驱动的代码审查与优化建议',
    longDescription: '利用大语言模型对代码进行深度审查，自动识别潜在Bug、安全漏洞、性能瓶颈和代码风格问题。支持多种编程语言，提供详细的修复建议和重构方案。',
    version: '2.0.1',
    category: 'productivity',
    tags: ['代码', '审查', 'AI'],
    author: { name: 'DevTools Lab', url: 'https://github.com/devtools-lab' },
    icon: '🔍',
    homepage: 'https://github.com/devtools-lab/skill-code-review',
    repository: 'https://github.com/devtools-lab/skill-code-review',
    license: 'Apache-2.0',
    resources: [{ type: 'github', url: 'https://github.com/devtools-lab/skill-code-review', branch: 'main' }],
    versions: [
      { version: '2.0.1', changelog: '支持更多语言', releasedAt: Date.now() - 86400000 * 2 }
    ],
    rating: 4.6,
    downloads: 5680,
    status: 'installed',
    installedAt: Date.now() - 86400000 * 30
  },
  {
    id: 'skill-storyteller',
    name: '故事工坊',
    description: '互动式故事创作与角色扮演引擎',
    longDescription: '沉浸式互动故事创作引擎，支持多分支剧情、角色养成和世界观构建。AI动态生成剧情走向，用户选择影响故事发展。内置多种题材模板。',
    version: '1.5.0',
    category: 'creative',
    tags: ['故事', '创作', '角色扮演'],
    author: { name: 'CreativeAI', url: 'https://gitee.com/creative-ai' },
    icon: '📖',
    homepage: 'https://gitee.com/creative-ai/skill-storyteller',
    repository: 'https://gitee.com/creative-ai/skill-storyteller',
    license: 'MIT',
    resources: [{ type: 'gitee', url: 'https://gitee.com/creative-ai/skill-storyteller', branch: 'master' }],
    versions: [
      { version: '1.5.0', changelog: '新增多结局系统', releasedAt: Date.now() - 86400000 * 5 }
    ],
    rating: 4.9,
    downloads: 8920,
    status: 'available'
  },
  {
    id: 'skill-home-ctrl',
    name: '智能家居',
    description: '全屋智能设备统一控制与场景编排',
    longDescription: '整合Home Assistant、小米IoT等平台的统一控制中心。支持语音控制、场景自动化、设备联动和能耗监控。可自定义自动化规则和定时任务。',
    version: '3.1.0',
    category: 'iot',
    tags: ['IoT', '智能家居', '自动化'],
    author: { name: 'SmartHome Hub', url: 'https://github.com/smarthome-hub' },
    icon: '🏠',
    homepage: 'https://github.com/smarthome-hub/skill-home-ctrl',
    repository: 'https://github.com/smarthome-hub/skill-home-ctrl',
    license: 'MIT',
    resources: [{ type: 'github', url: 'https://github.com/smarthome-hub/skill-home-ctrl', branch: 'main' }],
    versions: [
      { version: '3.1.0', changelog: '新增能耗统计', releasedAt: Date.now() - 86400000 * 3 }
    ],
    rating: 4.7,
    downloads: 12450,
    status: 'installed',
    installedAt: Date.now() - 86400000 * 60
  },
  {
    id: 'skill-voice-clone',
    name: '语音克隆',
    description: '个性化语音合成与声音克隆',
    longDescription: '基于少量语音样本实现声音克隆，支持自定义TTS音色。可创建独特的AI伴侣声音，让对话更加自然亲切。支持中英文混合语音合成。',
    version: '0.9.2',
    category: 'voice',
    tags: ['语音', 'TTS', '克隆'],
    author: { name: 'VoiceTech', url: 'https://github.com/voicetech' },
    icon: '🎙️',
    homepage: 'https://github.com/voicetech/skill-voice-clone',
    repository: 'https://github.com/voicetech/skill-voice-clone',
    license: 'CC-BY-NC-4.0',
    resources: [{ type: 'github', url: 'https://github.com/voicetech/skill-voice-clone', branch: 'dev' }],
    versions: [
      { version: '0.9.2', changelog: '提升音质', releasedAt: Date.now() - 86400000 * 10 }
    ],
    rating: 4.3,
    downloads: 2100,
    status: 'available'
  },
  {
    id: 'skill-knowledge-graph',
    name: '知识图谱',
    description: '构建与查询个人知识图谱',
    longDescription: '自动从对话中提取实体和关系，构建个人知识图谱。支持图谱可视化浏览、语义搜索和推理查询。帮助AI伴侣更深入地理解用户的知识体系。',
    version: '1.0.0',
    category: 'knowledge',
    tags: ['知识图谱', '语义', '推理'],
    author: { name: 'GraphMind', url: 'https://gitlab.com/graphmind' },
    icon: '🧠',
    homepage: 'https://gitlab.com/graphmind/skill-knowledge-graph',
    repository: 'https://gitlab.com/graphmind/skill-knowledge-graph',
    license: 'MIT',
    resources: [{ type: 'gitlab', url: 'https://gitlab.com/graphmind/skill-knowledge-graph', branch: 'main' }],
    versions: [
      { version: '1.0.0', changelog: '初始发布', releasedAt: Date.now() - 86400000 * 15 }
    ],
    rating: 4.5,
    downloads: 1890,
    status: 'available'
  },
  {
    id: 'skill-image-gen',
    name: '图像生成',
    description: 'AI图像生成与风格转换',
    longDescription: '集成Stable Diffusion等模型，支持文生图、图生图和风格转换。提供多种预设风格模板，支持自定义模型加载和LoRA微调。',
    version: '2.3.0',
    category: 'creative',
    tags: ['图像', 'AI绘画', '风格转换'],
    author: { name: 'ArtForge', url: 'https://github.com/artforge' },
    icon: '🎨',
    homepage: 'https://github.com/artforge/skill-image-gen',
    repository: 'https://github.com/artforge/skill-image-gen',
    license: 'MIT',
    resources: [{ type: 'github', url: 'https://github.com/artforge/skill-image-gen', branch: 'main' }],
    versions: [
      { version: '2.3.0', changelog: '新增LoRA支持', releasedAt: Date.now() - 86400000 * 1 }
    ],
    rating: 4.8,
    downloads: 7890,
    status: 'available'
  },
  {
    id: 'skill-task-flow',
    name: '任务流',
    description: '可视化任务编排与自动化执行',
    longDescription: '拖拽式任务编排工具，支持条件分支、循环、并行执行等流程控制。内置丰富的任务模板，可快速构建复杂的自动化工作流。',
    version: '1.8.0',
    category: 'automation',
    tags: ['自动化', '工作流', '任务'],
    author: { name: 'FlowEngine', url: 'https://gitee.com/flowengine' },
    icon: '⚡',
    homepage: 'https://gitee.com/flowengine/skill-task-flow',
    repository: 'https://gitee.com/flowengine/skill-task-flow',
    license: 'Apache-2.0',
    resources: [{ type: 'gitee', url: 'https://gitee.com/flowengine/skill-task-flow', branch: 'master' }],
    versions: [
      { version: '1.8.0', changelog: '新增并行执行', releasedAt: Date.now() - 86400000 * 4 }
    ],
    rating: 4.4,
    downloads: 4320,
    status: 'available'
  },
  {
    id: 'skill-social-hub',
    name: '社交聚合',
    description: '多平台社交消息聚合与智能回复',
    longDescription: '聚合QQ、微信、Discord、Telegram等平台消息，AI辅助生成回复建议。支持消息过滤、优先级排序和定时发送。',
    version: '1.3.0',
    category: 'social',
    tags: ['社交', '消息', '多平台'],
    author: { name: 'SocialBridge', url: 'https://github.com/socialbridge' },
    icon: '💬',
    homepage: 'https://github.com/socialbridge/skill-social-hub',
    repository: 'https://github.com/socialbridge/skill-social-hub',
    license: 'MIT',
    resources: [{ type: 'github', url: 'https://github.com/socialbridge/skill-social-hub', branch: 'main' }],
    versions: [
      { version: '1.3.0', changelog: '新增Telegram支持', releasedAt: Date.now() - 86400000 * 6 }
    ],
    rating: 4.2,
    downloads: 3560,
    status: 'available'
  },
  {
    id: 'skill-vision',
    name: '视觉理解',
    description: '图像内容识别与场景理解',
    longDescription: '多模态视觉理解能力，支持图像描述、OCR文字识别、物体检测和场景分析。可配合摄像头实现实时视觉交互。',
    version: '1.1.0',
    category: 'vision',
    tags: ['视觉', 'OCR', '多模态'],
    author: { name: 'VisionAI', url: 'https://github.com/visionai' },
    icon: '👁️',
    homepage: 'https://github.com/visionai/skill-vision',
    repository: 'https://github.com/visionai/skill-vision',
    license: 'MIT',
    resources: [{ type: 'github', url: 'https://github.com/visionai/skill-vision', branch: 'main' }],
    versions: [
      { version: '1.1.0', changelog: '提升OCR精度', releasedAt: Date.now() - 86400000 * 8 }
    ],
    rating: 4.6,
    downloads: 6230,
    status: 'available'
  },
  {
    id: 'skill-conversation-pro',
    name: '深度对话',
    description: '增强型对话引擎，支持多轮深度对话',
    longDescription: '增强型对话引擎，支持上下文深度理解、情感共鸣和多轮复杂对话。内置多种对话策略和人格模板，让AI伴侣的对话更加自然和深入。',
    version: '2.1.0',
    category: 'conversation',
    tags: ['对话', '情感', '深度理解'],
    author: { name: 'LuomiNest Team', url: 'https://github.com/luominest' },
    icon: '💭',
    homepage: 'https://github.com/luominest/skill-conversation-pro',
    repository: 'https://github.com/luominest/skill-conversation-pro',
    license: 'MIT',
    resources: [{ type: 'github', url: 'https://github.com/luominest/skill-conversation-pro', branch: 'main' }],
    versions: [
      { version: '2.1.0', changelog: '新增情感共鸣模块', releasedAt: Date.now() - 86400000 * 2 }
    ],
    rating: 4.9,
    downloads: 15600,
    status: 'installed',
    installedAt: Date.now() - 86400000 * 10
  },
  {
    id: 'skill-memo',
    name: '智能备忘',
    description: 'AI增强的备忘录与提醒系统',
    longDescription: '智能备忘系统，支持自然语言创建提醒、周期性任务管理和上下文感知提醒。AI自动识别对话中的待办事项并生成备忘。',
    version: '1.0.2',
    category: 'productivity',
    tags: ['备忘', '提醒', '效率'],
    author: { name: 'ProductivityX', url: 'https://github.com/productivityx' },
    icon: '📝',
    homepage: 'https://github.com/productivityx/skill-memo',
    repository: 'https://github.com/productivityx/skill-memo',
    license: 'MIT',
    resources: [{ type: 'github', url: 'https://github.com/productivityx/skill-memo', branch: 'main' }],
    versions: [
      { version: '1.0.2', changelog: '修复提醒延迟', releasedAt: Date.now() - 86400000 * 12 }
    ],
    rating: 4.1,
    downloads: 2870,
    status: 'available'
  }
]

const skills = ref<SkillManifest[]>(mockSkills)
const searchQuery = ref('')
const selectedCategory = ref<SkillCategory | 'all'>('all')
const selectedSource = ref<SkillSource | 'all'>('all')
const selectedStatus = ref<SkillStatus | 'all'>('all')
const sortBy = ref<SkillSearchQuery['sortBy']>('rating')
const sortOrder = ref<'asc' | 'desc'>('desc')
const viewMode = ref<'grid' | 'list'>('grid')
const showFilterPanel = ref(false)
const isRefreshing = ref(false)

const selectedSkill = ref<SkillManifest | null>(null)
const showDetailModal = ref(false)
const showInstallDialog = ref(false)
const showUploadDialog = ref(false)

const filteredSkills = computed(() => {
  let result = skills.value

  if (searchQuery.value.trim()) {
    const kw = searchQuery.value.toLowerCase()
    result = result.filter(s =>
      s.name.toLowerCase().includes(kw) ||
      s.description.toLowerCase().includes(kw) ||
      s.tags.some(t => t.toLowerCase().includes(kw)) ||
      s.author.name.toLowerCase().includes(kw)
    )
  }

  if (selectedCategory.value !== 'all') {
    result = result.filter(s => s.category === selectedCategory.value)
  }

  if (selectedSource.value !== 'all') {
    result = result.filter(s => s.resources.some(r => r.type === selectedSource.value))
  }

  if (selectedStatus.value !== 'all') {
    result = result.filter(s => s.status === selectedStatus.value)
  }

  result = [...result].sort((a, b) => {
    const order = sortOrder.value === 'asc' ? 1 : -1
    switch (sortBy.value) {
      case 'name':
        return order * a.name.localeCompare(b.name, 'zh')
      case 'rating':
        return order * ((a.rating ?? 0) - (b.rating ?? 0))
      case 'downloads':
        return order * ((a.downloads ?? 0) - (b.downloads ?? 0))
      default:
        return 0
    }
  })

  return result
})

const installedCount = computed(() => skills.value.filter(s => s.status === 'installed').length)
const totalCount = computed(() => skills.value.length)
const activeFilterCount = computed(() => {
  let count = 0
  if (selectedCategory.value !== 'all') count++
  if (selectedSource.value !== 'all') count++
  if (selectedStatus.value !== 'all') count++
  return count
})

const categoryLabel = (cat: SkillCategory) => categoryOptions.find(c => c.value === cat)?.label ?? cat
const sourceIcon = (src: SkillSource) => {
  switch (src) {
    case 'github': return Github
    case 'git':
    case 'gitee':
    case 'gitlab': return GitBranch
    default: return Package
  }
}
const sourceLabel = (src: SkillSource) => sourceOptions.find(s => s.value === src)?.label ?? src

const statusClass = (status: SkillStatus) => {
  switch (status) {
    case 'installed': return 'status-installed'
    case 'installing': return 'status-installing'
    case 'updating': return 'status-updating'
    case 'error': return 'status-error'
    default: return 'status-available'
  }
}

const statusLabel = (status: SkillStatus) => statusOptions.find(s => s.value === status)?.label ?? status

function openDetail(skill: SkillManifest) {
  selectedSkill.value = skill
  showDetailModal.value = true
}

function openInstall(skill: SkillManifest) {
  selectedSkill.value = skill
  showInstallDialog.value = true
}

function openUpload() {
  showUploadDialog.value = true
}

function closeDetail() {
  showDetailModal.value = false
  selectedSkill.value = null
}

function closeInstall() {
  showInstallDialog.value = false
}

function closeUpload() {
  showUploadDialog.value = false
}

function toggleSortOrder() {
  sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
}

function clearFilters() {
  selectedCategory.value = 'all'
  selectedSource.value = 'all'
  selectedStatus.value = 'all'
  searchQuery.value = ''
}

async function handleRefresh() {
  isRefreshing.value = true
  await new Promise(r => setTimeout(r, 800))
  isRefreshing.value = false
}

function handleInstallComplete(skillId: string) {
  const skill = skills.value.find(s => s.id === skillId)
  if (skill) {
    skill.status = 'installed'
    skill.installedAt = Date.now()
  }
  showInstallDialog.value = false
}

function handleUploadComplete(name: string) {
  showUploadDialog.value = false
}

function handleUninstall(skillId: string) {
  const skill = skills.value.find(s => s.id === skillId)
  if (skill) {
    skill.status = 'available'
    skill.installedAt = undefined
  }
  showDetailModal.value = false
}

function handleUpdate(skillId: string) {
  const skill = skills.value.find(s => s.id === skillId)
  if (skill) {
    skill.status = 'updating'
    setTimeout(() => {
      if (skill) skill.status = 'installed'
    }, 2000)
  }
  showDetailModal.value = false
}
</script>

<template>
  <div class="skill-market-view">
    <div class="market-header animate-fade-in">
      <div class="header-left">
        <div class="header-icon">
          <Store :size="24" />
        </div>
        <div>
          <h1 class="page-title">技能市场</h1>
          <p class="page-subtitle">
            发现、安装和管理 AI 技能 · 已安装 <span class="highlight">{{ installedCount }}</span> / {{ totalCount }}
          </p>
        </div>
      </div>
      <div class="header-actions">
        <button class="h-btn" :class="{ spinning: isRefreshing }" title="刷新" @click="handleRefresh">
          <RefreshCw :size="16" />
        </button>
        <button class="h-btn" title="本地上传" @click="openUpload">
          <Upload :size="16" />
          <span>上传技能</span>
        </button>
        <button class="h-btn primary" title="从仓库安装" @click="openInstall({ ...mockSkills[0], id: '__new__', status: 'available' } as any)">
          <GitBranch :size="16" />
          <span>从仓库安装</span>
        </button>
      </div>
    </div>

    <div class="market-toolbar animate-slide-up">
      <div class="toolbar-search">
        <Search :size="16" class="search-icon" />
        <input
          v-model="searchQuery"
          type="text"
          placeholder="搜索技能名称、描述、标签..."
          class="search-input"
        />
        <button v-if="searchQuery" class="search-clear" @click="searchQuery = ''">
          <X :size="14" />
        </button>
      </div>

      <div class="toolbar-filters">
        <div class="filter-select-wrap">
          <select v-model="selectedCategory" class="filter-select">
            <option v-for="opt in categoryOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
          </select>
          <ChevronDown :size="14" class="select-arrow" />
        </div>

        <div class="filter-select-wrap">
          <select v-model="selectedSource" class="filter-select">
            <option v-for="opt in sourceOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
          </select>
          <ChevronDown :size="14" class="select-arrow" />
        </div>

        <div class="filter-select-wrap">
          <select v-model="selectedStatus" class="filter-select">
            <option v-for="opt in statusOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
          </select>
          <ChevronDown :size="14" class="select-arrow" />
        </div>

        <button
          v-if="activeFilterCount > 0"
          class="filter-clear-btn"
          @click="clearFilters"
        >
          <X :size="12" />
          清除筛选 ({{ activeFilterCount }})
        </button>
      </div>

      <div class="toolbar-actions">
        <div class="sort-control">
          <div class="filter-select-wrap">
            <select v-model="sortBy" class="filter-select sort-select">
              <option v-for="opt in sortOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
            </select>
            <ChevronDown :size="14" class="select-arrow" />
          </div>
          <button class="sort-order-btn" :title="sortOrder === 'asc' ? '升序' : '降序'" @click="toggleSortOrder">
            <ArrowUpDown :size="14" />
          </button>
        </div>

        <div class="view-toggle">
          <button :class="['view-btn', { active: viewMode === 'grid' }]" @click="viewMode = 'grid'" title="网格视图">
            <Grid3X3 :size="16" />
          </button>
          <button :class="['view-btn', { active: viewMode === 'list' }]" @click="viewMode = 'list'" title="列表视图">
            <List :size="16" />
          </button>
        </div>
      </div>
    </div>

    <div class="market-content">
      <div v-if="filteredSkills.length === 0" class="empty-state animate-scale-in">
        <div class="empty-icon">
          <Package :size="48" />
        </div>
        <h3>未找到匹配的技能</h3>
        <p>尝试调整搜索关键词或筛选条件</p>
        <button v-if="activeFilterCount > 0" class="empty-clear-btn" @click="clearFilters">
          清除所有筛选
        </button>
      </div>

      <div v-else-if="viewMode === 'grid'" class="skill-grid">
        <div
          v-for="(skill, idx) in filteredSkills"
          :key="skill.id"
          class="skill-card animate-slide-up"
          :style="{ animationDelay: `${idx * 50}ms` }"
          @click="openDetail(skill)"
        >
          <div class="card-header">
            <div class="skill-icon">{{ skill.icon || '📦' }}</div>
            <span :class="['skill-status-badge', statusClass(skill.status)]">
              {{ statusLabel(skill.status) }}
            </span>
          </div>
          <div class="card-body">
            <h3 class="skill-name">{{ skill.name }}</h3>
            <p class="skill-desc">{{ skill.description }}</p>
            <div class="skill-tags">
              <span v-for="tag in skill.tags.slice(0, 3)" :key="tag" class="skill-tag">{{ tag }}</span>
            </div>
          </div>
          <div class="card-footer">
            <div class="skill-meta">
              <span class="meta-item">
                <Star :size="12" /> {{ skill.rating?.toFixed(1) ?? '-' }}
              </span>
              <span class="meta-item">
                <Download :size="12" /> {{ skill.downloads ?? 0 }}
              </span>
              <span class="meta-item source-item">
                <component :is="sourceIcon(skill.resources[0]?.type ?? 'marketplace')" :size="12" />
                {{ sourceLabel(skill.resources[0]?.type ?? 'marketplace') }}
              </span>
            </div>
            <div class="card-actions">
              <button
                v-if="skill.status === 'installed'"
                class="action-btn installed"
                @click.stop="openDetail(skill)"
              >
                已安装
              </button>
              <button
                v-else
                class="action-btn install"
                @click.stop="openInstall(skill)"
              >
                安装
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="skill-list">
        <div
          v-for="(skill, idx) in filteredSkills"
          :key="skill.id"
          class="skill-list-item animate-slide-up"
          :style="{ animationDelay: `${idx * 30}ms` }"
          @click="openDetail(skill)"
        >
          <div class="list-icon">{{ skill.icon || '📦' }}</div>
          <div class="list-info">
            <div class="list-top">
              <h3 class="skill-name">{{ skill.name }}</h3>
              <span class="skill-category-tag">{{ categoryLabel(skill.category) }}</span>
              <span :class="['skill-status-badge', statusClass(skill.status)]">
                {{ statusLabel(skill.status) }}
              </span>
            </div>
            <p class="skill-desc">{{ skill.description }}</p>
            <div class="list-meta">
              <span class="meta-item"><Star :size="12" /> {{ skill.rating?.toFixed(1) ?? '-' }}</span>
              <span class="meta-item"><Download :size="12" /> {{ skill.downloads ?? 0 }}</span>
              <span class="meta-item source-item">
                <component :is="sourceIcon(skill.resources[0]?.type ?? 'marketplace')" :size="12" />
                {{ sourceLabel(skill.resources[0]?.type ?? 'marketplace') }}
              </span>
              <span class="meta-item">{{ skill.version }}</span>
              <span class="meta-item">{{ skill.author.name }}</span>
            </div>
          </div>
          <div class="list-actions">
            <button
              v-if="skill.status === 'installed'"
              class="action-btn installed"
              @click.stop="openDetail(skill)"
            >
              已安装
            </button>
            <button
              v-else
              class="action-btn install"
              @click.stop="openInstall(skill)"
            >
              安装
            </button>
          </div>
        </div>
      </div>
    </div>

    <SkillDetailModal
      v-if="showDetailModal && selectedSkill"
      :skill="selectedSkill"
      @close="closeDetail"
      @install="openInstall(selectedSkill!)"
      @uninstall="handleUninstall(selectedSkill!.id)"
      @update="handleUpdate(selectedSkill!.id)"
    />

    <SkillInstallDialog
      v-if="showInstallDialog && selectedSkill"
      :skill="selectedSkill"
      @close="closeInstall"
      @complete="handleInstallComplete"
    />

    <SkillUploadDialog
      v-if="showUploadDialog"
      @close="closeUpload"
      @complete="handleUploadComplete"
    />
  </div>
</template>

<style scoped>
.skill-market-view {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: var(--workspace-bg);
  overflow: hidden;
}

.market-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 24px 28px 16px;
  flex-shrink: 0;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 14px;
}

.header-icon {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-lg);
  background: linear-gradient(135deg, rgba(13, 148, 136, 0.12), rgba(20, 184, 166, 0.08));
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--lumi-primary);
}

.page-title {
  font-size: 22px;
  font-weight: 700;
  color: var(--text-primary);
}

.page-subtitle {
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 2px;
}

.highlight {
  color: var(--lumi-primary);
  font-weight: 600;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.h-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 500;
  color: var(--text-secondary);
  transition: all var(--transition-fast);
  cursor: pointer;
  white-space: nowrap;
}

.h-btn:hover {
  background: var(--surface-hover);
  color: var(--text-primary);
}

.h-btn.primary {
  background: var(--lumi-primary);
  color: #fff;
}

.h-btn.primary:hover {
  background: var(--lumi-primary-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(13, 148, 136, 0.3);
}

.h-btn.spinning svg {
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.market-toolbar {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 28px 14px;
  flex-shrink: 0;
  flex-wrap: wrap;
}

.toolbar-search {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
  min-width: 200px;
  max-width: 400px;
  padding: 9px 14px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  transition: all var(--transition-fast);
}

.toolbar-search:focus-within {
  border-color: var(--lumi-primary);
  box-shadow: 0 0 0 3px var(--lumi-primary-glow);
}

.search-icon {
  color: var(--text-muted);
  flex-shrink: 0;
}

.search-input {
  flex: 1;
  background: transparent;
  font-size: 13px;
  color: var(--text-primary);
  min-width: 0;
}

.search-input::placeholder {
  color: var(--text-muted);
}

.search-clear {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  color: var(--text-muted);
  transition: all var(--transition-fast);
  flex-shrink: 0;
}

.search-clear:hover {
  background: var(--surface-hover);
  color: var(--text-secondary);
}

.toolbar-filters {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.filter-select-wrap {
  position: relative;
  display: flex;
  align-items: center;
}

.filter-select {
  appearance: none;
  padding: 8px 30px 8px 12px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 500;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all var(--transition-fast);
  font-family: inherit;
}

.filter-select:hover {
  border-color: var(--lumi-primary);
}

.filter-select:focus {
  outline: none;
  border-color: var(--lumi-primary);
  box-shadow: 0 0 0 3px var(--lumi-primary-glow);
}

.select-arrow {
  position: absolute;
  right: 10px;
  color: var(--text-muted);
  pointer-events: none;
}

.filter-clear-btn {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 6px 10px;
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-weight: 500;
  color: var(--lumi-accent);
  background: var(--lumi-accent-light);
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
}

.filter-clear-btn:hover {
  background: rgba(244, 63, 94, 0.15);
}

.toolbar-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: auto;
}

.sort-control {
  display: flex;
  align-items: center;
  gap: 4px;
}

.sort-select {
  min-width: 80px;
}

.sort-order-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  transition: all var(--transition-fast);
  cursor: pointer;
}

.sort-order-btn:hover {
  background: var(--surface-hover);
  color: var(--text-secondary);
}

.view-toggle {
  display: flex;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  overflow: hidden;
}

.view-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  color: var(--text-muted);
  transition: all var(--transition-fast);
  cursor: pointer;
}

.view-btn:hover {
  color: var(--text-secondary);
  background: var(--surface-hover);
}

.view-btn.active {
  color: var(--lumi-primary);
  background: var(--lumi-primary-light);
}

.market-content {
  flex: 1;
  overflow-y: auto;
  padding: 0 28px 28px;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 20px;
  text-align: center;
}

.empty-icon {
  width: 88px;
  height: 88px;
  border-radius: 50%;
  background: var(--workspace-panel);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  margin-bottom: 16px;
}

.empty-state h3 {
  font-size: 16px;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 6px;
}

.empty-state p {
  font-size: 13px;
  color: var(--text-muted);
  margin-bottom: 16px;
}

.empty-clear-btn {
  padding: 8px 18px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 500;
  color: var(--lumi-primary);
  background: var(--lumi-primary-light);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.empty-clear-btn:hover {
  background: rgba(13, 148, 136, 0.15);
}

.skill-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}

.skill-card {
  display: flex;
  flex-direction: column;
  padding: 18px;
  border-radius: var(--radius-lg);
  background: var(--workspace-card);
  border: 1px solid var(--border-light);
  cursor: pointer;
  transition: all var(--transition-normal);
  box-shadow: var(--shadow-xs);
}

.skill-card:hover {
  border-color: var(--lumi-primary);
  box-shadow: var(--shadow-md), 0 0 0 1px var(--lumi-primary-glow);
  transform: translateY(-2px);
}

.card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 14px;
}

.skill-icon {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-md);
  background: var(--surface-hover);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
}

.skill-status-badge {
  font-size: 10px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: var(--radius-full);
  letter-spacing: 0.3px;
}

.status-available {
  background: rgba(13, 148, 136, 0.1);
  color: var(--lumi-primary);
}

.status-installed {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
}

.status-installing {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.status-updating {
  background: rgba(234, 179, 8, 0.1);
  color: #ca8a04;
}

.status-error {
  background: var(--lumi-accent-light);
  color: var(--lumi-accent);
}

.card-body {
  flex: 1;
  margin-bottom: 14px;
}

.skill-name {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 6px;
}

.skill-desc {
  font-size: 12px;
  color: var(--text-muted);
  line-height: 1.5;
  margin-bottom: 10px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.skill-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.skill-tag {
  font-size: 10px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  background: var(--bg-secondary);
  color: var(--text-muted);
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 12px;
  border-top: 1px solid var(--border-light);
}

.skill-meta {
  display: flex;
  align-items: center;
  gap: 10px;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 3px;
  font-size: 11px;
  color: var(--text-muted);
}

.source-item {
  gap: 4px;
}

.card-actions {
  display: flex;
  gap: 6px;
}

.action-btn {
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
}

.action-btn.install {
  background: var(--lumi-primary);
  color: #fff;
}

.action-btn.install:hover {
  background: var(--lumi-primary-hover);
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(13, 148, 136, 0.3);
}

.action-btn.installed {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
}

.action-btn.installed:hover {
  background: rgba(34, 197, 94, 0.18);
}

.skill-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.skill-list-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 18px;
  border-radius: var(--radius-md);
  background: var(--workspace-card);
  border: 1px solid var(--border-light);
  cursor: pointer;
  transition: all var(--transition-fast);
  box-shadow: var(--shadow-xs);
}

.skill-list-item:hover {
  border-color: var(--lumi-primary);
  box-shadow: var(--shadow-sm);
  background: var(--surface-hover);
}

.list-icon {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-md);
  background: var(--surface-hover);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  flex-shrink: 0;
}

.list-info {
  flex: 1;
  min-width: 0;
}

.list-top {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.list-top .skill-name {
  margin-bottom: 0;
  font-size: 14px;
}

.skill-category-tag {
  font-size: 10px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  background: var(--lumi-primary-light);
  color: var(--lumi-primary);
}

.list-info .skill-desc {
  margin-bottom: 6px;
  -webkit-line-clamp: 1;
}

.list-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.list-actions {
  flex-shrink: 0;
}

@media (max-width: 1200px) {
  .skill-grid {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  }
}

@media (max-width: 960px) {
  .market-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
    padding: 20px 20px 12px;
  }

  .header-actions {
    width: 100%;
    justify-content: flex-end;
  }

  .market-toolbar {
    padding: 0 20px 12px;
    flex-direction: column;
    align-items: stretch;
  }

  .toolbar-search {
    max-width: none;
  }

  .toolbar-filters {
    overflow-x: auto;
    padding-bottom: 4px;
  }

  .toolbar-actions {
    margin-left: 0;
    justify-content: space-between;
  }

  .market-content {
    padding: 0 20px 20px;
  }

  .skill-grid {
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 12px;
  }
}

@media (max-width: 640px) {
  .skill-grid {
    grid-template-columns: 1fr;
  }

  .skill-list-item {
    flex-wrap: wrap;
  }

  .list-actions {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    margin-top: 8px;
    padding-top: 8px;
    border-top: 1px solid var(--border-light);
  }
}
</style>
