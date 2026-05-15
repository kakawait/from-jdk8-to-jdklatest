<template>
  <div class="jdk-versions flex items-center gap-3">
    <div v-if="previews.length" class="flex items-center gap-1.5 opacity-80">
      <span class="text-[10px] uppercase font-bold tracking-wider mr-1 text-gray-400">Preview in</span>
      <JdkBadge v-for="v in previews" :key="v" :label="`JDK${v}`" size="small" />
    </div>
    <div v-if="releases.length" class="flex items-center gap-1.5">
      <JdkBadge v-for="v in releases" :key="v" :label="`JDK${v}`" size="medium" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  v?: string | number | (string | number)[]
  preview?: string | number | (string | number)[]
}>()

const releases = computed(() => {
  if (!props.v) return []
  if (typeof props.v === 'string' && props.v.includes(',')) return props.v.split(',').map(s => s.trim())
  return Array.isArray(props.v) ? props.v : [props.v]
})

const previews = computed(() => {
  if (!props.preview) return []
  if (typeof props.preview === 'string' && props.preview.includes(',')) return props.preview.split(',').map(s => s.trim())
  return Array.isArray(props.preview) ? props.preview : [props.preview]
})
</script>
