export interface AgentProfile {
  id: string
  name: string
  description: string
  avatar?: string
  color: string
  systemPrompt: string
  model: string
  capabilities: string[]
  isActive: boolean
}

export interface WorkflowNode {
  id: string
  name: string
  type: 'agent' | 'tool' | 'condition' | 'output' | 'input'
  agentId?: string
  config: Record<string, any>
  position: { x: number; y: number }
}

export interface WorkflowConnection {
  id: string
  sourceNodeId: string
  targetNodeId: string
  label?: string
}

export interface WorkflowDefinition {
  id: string
  name: string
  description: string
  nodes: WorkflowNode[]
  connections: WorkflowConnection[]
  createdAt: number
  updatedAt: number
}

export interface ChatMessage {
  id: string
  role: 'user' | 'assistant' | 'system'
  content: string
  timestamp: number
  agentId?: string
}

export interface Tab {
  id: string
  title: string
  url: string
  favicon?: string
  loading?: boolean
  error?: TabError
  active?: boolean
  captchaDetected?: boolean
  sleeping?: boolean
}

export interface TabError {
  code: number
  title: string
  message: string
}

export interface Bookmark {
  name: string
  url: string
}

export type SkillSource = 'git' | 'github' | 'gitee' | 'gitlab' | 'local' | 'marketplace'

export type SkillStatus = 'available' | 'installed' | 'updating' | 'installing' | 'error'

export type SkillCategory =
  | 'conversation'
  | 'productivity'
  | 'creative'
  | 'automation'
  | 'iot'
  | 'social'
  | 'knowledge'
  | 'voice'
  | 'vision'
  | 'other'

export interface SkillAuthor {
  name: string
  avatar?: string
  url?: string
}

export interface SkillVersion {
  version: string
  changelog: string
  releasedAt: number
  minAppVersion?: string
}

export interface SkillResource {
  type: SkillSource
  url: string
  branch?: string
  tag?: string
}

export interface SkillManifest {
  id: string
  name: string
  description: string
  longDescription?: string
  version: string
  category: SkillCategory
  tags: string[]
  author: SkillAuthor
  icon?: string
  coverImage?: string
  homepage?: string
  repository?: string
  license?: string
  minAppVersion?: string
  dependencies?: string[]
  resources: SkillResource[]
  versions?: SkillVersion[]
  rating?: number
  downloads?: number
  installedAt?: number
  status: SkillStatus
}

export interface SkillInstallConfig {
  source: SkillSource
  url: string
  branch?: string
  tag?: string
  targetPath?: string
  overwrite?: boolean
}

export interface SkillUploadConfig {
  filePath: string
  name: string
  overwrite?: boolean
}

export interface SkillSearchQuery {
  keyword: string
  category?: SkillCategory
  source?: SkillSource
  status?: SkillStatus
  sortBy?: 'name' | 'rating' | 'downloads' | 'updatedAt'
  sortOrder?: 'asc' | 'desc'
}

export {}
