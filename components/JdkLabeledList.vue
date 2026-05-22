<script setup lang="ts">
import JdkBadge from './JdkBadge.vue'

type JdkLabeledListTextPart = string | {
  badge: string
  size?: 'small' | 'medium' | 'large'
}

type JdkLabeledListItem = {
  jdk: string
  deprecatedJdk?: string
  text: string | JdkLabeledListTextPart[]
}

defineProps<{
  items: JdkLabeledListItem[]
  dense?: boolean
}>()

function asParts(text: JdkLabeledListItem['text']): JdkLabeledListTextPart[] {
  return Array.isArray(text) ? text : [text]
}
</script>

<template>
  <ul class="jdk-labeled-list" :class="{ 'jdk-labeled-list--dense': dense }">
    <li v-for="(item, index) in items" :key="`${item.jdk}-${index}`" class="jdk-labeled-list__item" :class="{ 'jdk-labeled-list__item--dense': dense }">
      <div class="jdk-labeled-list__badge-wrapper">
        <span v-if="item.deprecatedJdk" class="jdk-labeled-list__deprecated">
          (deprecated <JdkBadge :label="item.deprecatedJdk" size="small" />)
        </span>
        <JdkBadge :label="item.jdk" size="medium" class="jdk-labeled-list__badge" />
      </div>
      <div class="jdk-labeled-list__text">
        <template v-for="(part, partIndex) in asParts(item.text)" :key="partIndex">
          <JdkBadge
            v-if="typeof part !== 'string'"
            :label="part.badge"
            :size="part.size || 'small'"
            class="jdk-labeled-list__inline-badge"
          />
          <span v-else v-html="part" />
        </template>
      </div>
    </li>
  </ul>
</template>

<style scoped>
.jdk-labeled-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 100%;
  margin: 0 !important;
  padding: 0 !important;
  list-style: none !important;
}

.jdk-labeled-list--dense {
  gap: 0.2rem;
}

.jdk-labeled-list__item {
  display: grid;
  grid-template-columns: 210px minmax(0, 1fr);
  column-gap: 16px;
  align-items: start;
  margin: 0 !important;
  padding: 0 !important;
}

.jdk-labeled-list__item--dense {
  grid-template-columns: 180px minmax(0, 1fr);
  column-gap: 12px;
}

.jdk-labeled-list__badge-wrapper {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  font-size: 1.2rem;
  line-height: 1.4;
  height: 1.4em;
  gap: 8px;
}

.jdk-labeled-list__item--dense .jdk-labeled-list__badge-wrapper {
  font-size: 1.05rem;
  line-height: 1.3;
  height: 1.3em;
}

.jdk-labeled-list__badge {
  width: 100px;
  min-width: 100px;
}

.jdk-labeled-list__item--dense .jdk-labeled-list__badge {
  width: 80px;
  min-width: 80px;
  transform: scale(0.9);
  transform-origin: right center;
}

.jdk-labeled-list__deprecated {
  white-space: nowrap;
  font-size: 0.7rem;
  color: #aaa;
  display: flex;
  align-items: center;
  gap: 4px;
}

.jdk-labeled-list__item--dense .jdk-labeled-list__deprecated {
  font-size: 0.6rem;
}

.jdk-labeled-list__text {
  min-width: 0;
  margin: 0 !important;
  padding: 0 !important;
  color: #fff;
  font-size: 1.2rem;
  line-height: 1.4;
}

.jdk-labeled-list--dense .jdk-labeled-list__text {
  font-size: 1.05rem;
  line-height: 1.3;
}

.jdk-labeled-list__inline-badge {
  display: inline-flex;
  vertical-align: 0.08em;
  margin: 0 0.18em;
}

.jdk-labeled-list__text :deep(code) {
  padding: 0;
  border-radius: 0;
  background: transparent;
  color: inherit;
  font-size: 0.95em;
}
</style>
