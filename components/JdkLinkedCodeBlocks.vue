<script setup lang="ts">
import JdkCodeBlock from './JdkCodeBlock.vue'

defineProps<{
  label1: string
  label2: string
  size?: 'small' | 'medium' | 'large'
  codeClass?: string
}>()

const id1 = 'anchor-' + Math.random().toString(36).substring(2, 9)
const id2 = 'anchor-' + Math.random().toString(36).substring(2, 9)
</script>

<template>
  <div class="jdk-linked-code-blocks grid grid-cols-[1fr_100px_1fr] items-center gap-4 mt-1">
    <JdkCodeBlock :label="label1" :size="size || 'small'" :data-id="id1" :class="codeClass">
      <slot name="code1" />
    </JdkCodeBlock>

    <div class="flex justify-center">
      <FancyArrow :from="`[data-id=${id1}]`" :to="`[data-id=${id2}]`" static />
    </div>

    <JdkCodeBlock :label="label2" :size="size || 'small'" :data-id="id2" :class="codeClass">
      <slot name="code2" />
    </JdkCodeBlock>
  </div>
</template>

<style scoped>
.jdk-linked-code-blocks {
  width: 100%;
}
</style>
