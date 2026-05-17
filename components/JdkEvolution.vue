<script setup lang="ts">
import JdkCodeBlock from './JdkCodeBlock.vue'

defineProps<{
  label1?: string
  label2?: string
  label3?: string
  label4?: string
  size?: 'small' | 'medium' | 'large'
  codeClass?: string
}>()

const id1 = 'evol-' + Math.random().toString(36).substring(2, 9)
const id2 = 'evol-' + Math.random().toString(36).substring(2, 9)
const id3 = 'evol-' + Math.random().toString(36).substring(2, 9)
const id4 = 'evol-' + Math.random().toString(36).substring(2, 9)
</script>

<template>
  <div class="jdk-evolution grid grid-cols-2 gap-x-12 gap-y-6 mt-4 relative">
    <JdkCodeBlock :label="label1" :size="size || 'small'" :data-id="id1" :contentClass="codeClass">
      <slot name="code1" />
    </JdkCodeBlock>

    <JdkCodeBlock :label="label2" :size="size || 'small'" :data-id="id2" :contentClass="codeClass">
      <slot name="code2" />
    </JdkCodeBlock>

    <JdkCodeBlock :label="label3" :size="size || 'small'" :data-id="id3" :contentClass="codeClass">
      <slot name="code3" />
    </JdkCodeBlock>

    <JdkCodeBlock :label="label4" :size="size || 'small'" :data-id="id4" :contentClass="codeClass">
      <slot name="code4" />
    </JdkCodeBlock>

    <!-- Arrows -->
    <FancyArrow :from="`[data-id=${id1}]`" :to="`[data-id=${id2}]`" static />
    <FancyArrow :from="`[data-id=${id2}]`" :to="`[data-id=${id3}]`" static />
    <FancyArrow :from="`[data-id=${id3}]`" :to="`[data-id=${id4}]`" static />
  </div>
</template>

<style scoped>
.jdk-evolution {
  width: 100%;
}
</style>
