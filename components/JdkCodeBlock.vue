<script setup lang="ts">
import JdkBadge from './JdkBadge.vue'

defineProps<{
  label?: string
  color?: string
  textColor?: string
  borderColor?: string
  size?: 'small' | 'medium' | 'large'
}>()
</script>

<template>
  <div class="jdk-code-block flex flex-col gap-1">
    <JdkBadge 
      v-if="label"
      :label="label" 
      :color="color" 
      :textColor="textColor" 
      :borderColor="borderColor" 
      :size="size || 'small'" 
      class="w-max" 
    />
    <div class="jdk-code-content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.jdk-code-block :deep(div.slidev-code-wrapper) {
  margin-top: 0 !important;
}

.jdk-code-block :deep(pre) {
  margin: 0 !important;
}
</style>
