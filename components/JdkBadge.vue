<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  label: { type: String, required: true },
  color: { type: String, default: '' },
  textColor: { type: String, default: '#fff' },
  borderColor: { type: String, default: '' },
  size: { type: String, default: 'large' },
  old: { type: Boolean, default: false },
})

const jdkColors: Record<string, string> = {
  JDK6: '#ead1dc',
  JDK7: '#d0e0e3',
  JDK8: '#d0e0e3',
  JDK9: '#007bff',
  JDK10: '#b60205',
  JDK11: '#28a745',
  JDK12: '#b6a842',
  JDK13: '#e200db',
  JDK14: '#ff990f',
  JDK15: '#0a9ca2',
  JDK16: '#6600cc',
  JDK17: '#a64d79',
  JDK18: '#454a8e',
  JDK19: '#e43333',
  JDK20: '#083d1c',
  JDK21: '#4acaec',
  JDK22: '#710070',
  JDK23: '#854800',
  'OLD JDK': '#e3ead1'
}

const resolvedColor = computed(() => props.color || jdkColors[props.label] || '#333')

const styles = computed(() => ({
  '--badge-bg': resolvedColor.value,
  '--badge-color': props.textColor,
  '--badge-border': props.borderColor || resolvedColor.value,
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

.jdk-badge--old {
  --badge-font: calc(18 * var(--px));
}
</style>
