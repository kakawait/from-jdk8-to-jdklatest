<script setup lang="ts">
defineProps<{
  image?: string
}>()
</script>

<template>
  <div class="jdk-alert bg-[#48FFD5] p-4 flex items-center gap-6 rounded-sm text-[#0e2a47]">
    <div v-if="image || $slots.image" class="flex-none w-24 h-24 flex items-center justify-center">
      <slot name="image">
        <img :src="image" class="max-w-full max-h-full object-contain" />
      </slot>
    </div>
    <div class="flex-grow text-left">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.jdk-alert :deep(h1), .jdk-alert :deep(h2), .jdk-alert :deep(h3) {
  margin-top: 0.25rem;
  margin-bottom: 0.25rem;
  color: #0e2a47 !important;
  font-weight: 700;
}

.jdk-alert :deep(a) {
  color: #0e2a47 !important;
  text-decoration: underline;
}

.jdk-alert :deep(code) {
  background-color: rgba(14, 42, 71, 0.1) !important;
  color: #0e2a47 !important;
  padding: 0.1rem 0.3rem;
  border-radius: 0.2rem;
  font-family: inherit;
  font-weight: 600;
}
</style>
