<template>
  <div class="jdk-versions flex items-center gap-3">
    <div v-if="previews.length" class="flex items-center gap-1.5 opacity-80">
      <span v-if="prefix" class="text-[10px] font-bold tracking-wider mr-0 text-gray-400">{{ prefix }}</span>
      <JdkBadge
        v-for="v in previews"
        :key="v"
        :label="formatLabel(v)"
        :size="previewSize"
        :data-jdk-label="formatLabel(v)"
      />
      <span v-if="suffix" class="text-[10px] font-bold tracking-wider ml-0 text-gray-400">{{ suffix }}</span>
    </div>
    <div v-if="releases.length" class="flex items-center gap-1.5">
      <JdkBadge
        v-for="v in releases"
        :key="v"
        :label="formatLabel(v)"
        :size="size"
        :data-jdk-label="formatLabel(v)"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  v: { type: [String, Number, Array], default: '' },
  preview: { type: [String, Number, Array], default: '' },
  prefix: { type: String, default: '(PREVIEW IN' },
  suffix: { type: String, default: ')' },
  size: { type: String, default: 'large' },
  previewSize: { type: String, default: 'small' }
})

const formatLabel = (v: string | number) => {
  const s = String(v).trim()
  if (s.startsWith('JDK') || s === 'OLD JDK') return s
  if (s === 'OLD') return 'OLD JDK'
  return `JDK${s}`
}

const releases = computed(() => {
  if (!props.v) return []
  const val = props.v
  if (typeof val === 'string' && val.includes(',')) return val.split(',').map(s => s.trim())
  return Array.isArray(val) ? val : [val]
})

const previews = computed(() => {
  if (!props.preview) return []
  const val = props.preview
  if (typeof val === 'string' && val.includes(',')) return val.split(',').map(s => s.trim())
  return Array.isArray(val) ? val : [val]
})
</script>
