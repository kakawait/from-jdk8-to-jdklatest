<script setup lang="ts">
import JdkCodeBlock from './JdkCodeBlock.vue'

defineProps<{
  label?: string
  color?: string
  textColor?: string
  borderColor?: string
  size?: 'small' | 'medium' | 'large'
  reverse?: boolean
}>()
</script>

<template>
  <div class="jdk-code-with-text flex gap-8 items-start" :class="reverse ? 'flex-row-reverse' : 'flex-row'">
    <div class="flex-[3] min-w-0">
      <JdkCodeBlock 
        :label="label" 
        :color="color" 
        :textColor="textColor" 
        :borderColor="borderColor" 
        :size="size || 'small'"
      >
        <slot name="code" />
      </JdkCodeBlock>
    </div>
    <div class="flex-1 text-[13px] text-white/80 leading-relaxed pt-8">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.jdk-code-with-text {
  width: 100%;
}
</style>
