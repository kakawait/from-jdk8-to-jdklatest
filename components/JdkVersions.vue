<template>
  <div class="jdk-versions flex items-center gap-3">
    <div v-if="previews.length" class="flex items-center gap-1.5 opacity-80">
      <span v-if="prefix" class="text-[10px] uppercase font-bold tracking-wider mr-1 text-gray-400">{{ prefix }}</span>
      <span v-else class="text-[10px] uppercase font-bold tracking-wider mr-1 text-gray-400">Preview in</span>
      <JdkBadge v-for="v in previews" :key="v" :label="`JDK${v}`" :size="previewSize" />
      <span v-if="suffix" class="text-[10px] uppercase font-bold tracking-wider ml-1 text-gray-400">{{ suffix }}</span>
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
  prefix: { type: String, default: '' },
  suffix: { type: String, default: '' },
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
