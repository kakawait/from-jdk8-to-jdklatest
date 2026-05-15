<template>
  <div class="jdk-versions flex items-center gap-3">
    <div v-if="previews.length" class="flex items-center gap-1.5 opacity-80">
      <span class="text-[10px] uppercase font-bold tracking-wider mr-1 text-gray-400">Preview in</span>
      <JdkBadge v-for="v in previews" :key="v" :label="`JDK${v}`" :size="previewSize" />
    </div>
    <div v-if="releases.length" class="flex items-center gap-1.5">
      <JdkBadge v-for="v in releases" :key="v" :label="`JDK${v}`" :size="size" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  v: { type: [String, Number, Array], default: '' },
  preview: { type: [String, Number, Array], default: '' },
  size: { type: String, default: 'large' },
  previewSize: { type: String, default: 'small' }
})

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
