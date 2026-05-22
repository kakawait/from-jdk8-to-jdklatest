<script setup lang="ts">
import { computed } from 'vue'
import { getJdkConfig } from './jdk-utils'

const props = defineProps({
  label: { type: String, required: true },
  color: { type: String, default: '' },
  textColor: { type: String, default: '' },
  borderColor: { type: String, default: '' },
  size: { type: String, default: 'large' },
  old: { type: Boolean, default: false },
})

const config = computed(() => getJdkConfig(props.label))

const resolvedBg = computed(() => props.color || config.value.bg)
const resolvedText = computed(() => props.textColor || (props.color ? '#fff' : config.value.text))
const resolvedBorder = computed(() => props.borderColor || (props.color ? resolvedBg.value : config.value.border))

const styles = computed(() => ({
  '--badge-bg': resolvedBg.value,
  '--badge-color': resolvedText.value,
  '--badge-border': resolvedBorder.value,
}))
</script>

<template>
  <div
    class="jdk-badge"
    :class="[`jdk-badge--${size}`, { 'jdk-badge--old': old }]"
    :style="styles"
  >
    {{ label }}
  </div>
</template>

<style scoped>
.jdk-badge {
  --px: min(calc(100cqw / 1280), calc(100cqh / 720));
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--badge-border);
  border-radius: calc(5 * var(--px));
  background: var(--badge-bg);
  color: var(--badge-color);
  font-size: var(--badge-font);
  font-weight: 700;
  line-height: 1;
  letter-spacing: 0;
  white-space: nowrap;
  padding: var(--badge-padding);
}

.jdk-badge--large {
  --badge-font: calc(20 * var(--px));
  --badge-padding: calc(3 * var(--px)) calc(10 * var(--px));
  min-width: calc(80 * var(--px));
}

.jdk-badge--medium {
  --badge-font: calc(15 * var(--px));
  --badge-padding: calc(2 * var(--px)) calc(8 * var(--px));
  min-width: calc(65 * var(--px));
}

.jdk-badge--small {
  --badge-font: calc(12 * var(--px));
  --badge-padding: calc(1 * var(--px)) calc(6 * var(--px));
  min-width: calc(45 * var(--px));
}

.jdk-badge--xsmall {
  --badge-font: calc(6 * var(--px));
  --badge-padding: calc(1 * var(--px)) calc(4 * var(--px));
  min-width: calc(25 * var(--px));
}

.jdk-badge--old {
  --badge-font: calc(18 * var(--px));
}
</style>
