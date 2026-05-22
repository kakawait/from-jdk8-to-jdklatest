<script setup lang="ts">
import JdkBadge from './JdkBadge.vue'

type JdkLabeledListItem = {
  jdk: string
  text: string
}

defineProps<{
  items: JdkLabeledListItem[]
}>()
</script>

<template>
  <ul class="jdk-labeled-list">
    <li v-for="(item, index) in items" :key="`${item.jdk}-${index}`" class="jdk-labeled-list__item">
      <JdkBadge :label="item.jdk" size="medium" class="jdk-labeled-list__badge" />
      <span class="jdk-labeled-list__text">
        <span class="jdk-labeled-list__bullet" aria-hidden="true">•</span>
        <span class="jdk-labeled-list__copy" v-html="item.text" />
      </span>
    </li>
  </ul>
</template>

<style scoped>
.jdk-labeled-list {
  display: grid;
  gap: 0;
  width: 100%;
  margin: 0 !important;
  padding: 0 !important;
  list-style: none !important;
}

.jdk-labeled-list__item {
  display: grid;
  grid-template-columns: 106px minmax(0, 1fr);
  column-gap: 12px;
  align-items: start;
  margin: 0 !important;
  padding: 0 !important;
  list-style: none !important;
}

.jdk-labeled-list__badge {
  width: 100px;
  min-width: 100px;
  margin-top: 7px;
  justify-self: start;
}

.jdk-labeled-list__text {
  display: grid;
  grid-template-columns: 22px minmax(0, 1fr);
  min-width: 0;
  margin: 0 !important;
  padding: 0 !important;
  color: #fff;
  font-size: 23px;
  line-height: 1.18;
}

.jdk-labeled-list__bullet {
  font-size: 0.85em;
  line-height: inherit;
  color: currentColor;
}

.jdk-labeled-list__copy {
  min-width: 0;
}

.jdk-labeled-list__text :deep(code) {
  padding: 0;
  border-radius: 0;
  background: transparent;
  color: inherit;
  font-size: 0.95em;
}
</style>
