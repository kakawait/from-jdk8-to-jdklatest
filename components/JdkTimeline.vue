<template>
  <div class="jdk-timeline" aria-label="JDK release and EOL timeline">
    <main class="timeline-grid">
      <section
        v-for="column in modernColumns"
        :key="column.label"
        class="timeline-column"
        :class="column.className"
        :aria-label="column.label"
      >
        <article v-for="row in column.rows" :key="row.version" class="version-row">
          <div class="badge-stack">
            <JdkBadge :label="row.version" :color="row.color" size="large" />
            <JdkBadge :label="row.version" :color="row.color" size="medium" />
            <JdkBadge v-if="row.small" :label="row.version" :color="row.color" size="small" />
          </div>
          <ReleaseDates :release="row.release" :eol="row.eol" />
        </article>
      </section>

      <section class="timeline-column timeline-column--legacy" aria-label="Old JDKs">
        <article v-for="row in legacyRows" :key="row.version" class="legacy-row">
          <JdkBadge
            :label="row.version"
            :color="row.color"
            :border-color="row.borderColor"
            text-color="#0e2a47"
            size="large"
          />
          <ReleaseDates :release="row.release" :eol="row.eol" compact />
        </article>

        <JdkBadge
          label="OLD JDK"
          color="#e3ead1"
          border-color="#a0a88a"
          text-color="#0e2a47"
          size="large"
          old
        />
      </section>
    </main>

    <p class="legend">🚀 = Release date - ☠️ = EOL free support based on Eclipse Temurin</p>
  </div>
</template>

<script setup lang="ts">
import { defineComponent, h } from 'vue'
import JdkBadge from './JdkBadge.vue'

type VersionRow = {
  version: string
  release: string
  eol: string
  color: string
  small?: boolean
}

type LegacyRow = VersionRow & {
  borderColor: string
}

const modernColumns: Array<{ label: string; className?: string; rows: VersionRow[] }> = [
  {
    label: 'JDK 9 to 18',
    className: 'timeline-column--long',
    rows: [
      { version: 'JDK9', release: 'Sept 2017', eol: 'March 2018', color: '#007bff'},
      { version: 'JDK10', release: 'March 2018', eol: 'Sept 2018', color: '#b60205' },
      { version: 'JDK11', release: 'Sept 2018', eol: 'Oct 2027', color: '#28a745' },
      { version: 'JDK12', release: 'March 2019', eol: 'Sept 2019', color: '#b6a842' },
      { version: 'JDK13', release: 'Sept 2019', eol: 'March 2020', color: '#e200db' },
      { version: 'JDK14', release: 'March 2020', eol: 'Sept 2020', color: '#ff990f', small: true },
      { version: 'JDK15', release: 'Sept 2020', eol: 'March 2021', color: '#0a9ca2', small: true },
      { version: 'JDK16', release: 'March 2021', eol: 'Sept 2021', color: '#6600cc', small: true },
      { version: 'JDK17', release: 'Sept 2021', eol: 'Oct 2027', color: '#a64d79', small: true },
      { version: 'JDK18', release: 'March 2022', eol: 'Sept 2022', color: '#454a8e', small: true },
      { version: 'JDK19', release: 'Sept 2022', eol: 'March 2023', color: '#e43333', small: true },
    ],
  },
  {
    label: 'JDK 20 to 24',
    rows: [
      { version: 'JDK20', release: 'March 2023', eol: 'Sept 2023', color: '#083d1c', small: true },
      { version: 'JDK21', release: 'Sept 2023', eol: 'Dec 2029', color: '#4acaec', small: true },
      { version: 'JDK22', release: 'March 2024', eol: 'Sept 2024', color: '#710070', small: true },
      { version: 'JDK23', release: 'Sept 2024', eol: 'March 2025', color: '#854800', small: true },
      { version: 'JDK24', release: 'March 2025', eol: 'Sept 2025', color: '#3b82f6', small: true },
    ],
  },
]

const legacyRows: LegacyRow[] = [
  {
    version: 'JDK6',
    release: 'Dec 2006',
    eol: 'Apr 2013',
    color: '#ead1dc',
    borderColor: '#007bff',
  },
  {
    version: 'JDK7',
    release: 'July 2011',
    eol: 'July 2015',
    color: '#d0e0e3',
    borderColor: '#007bff',
  },
  {
    version: 'JDK8',
    release: 'March 2014',
    eol: 'Nov 2026',
    color: '#d0e0e3',
    borderColor: '#007bff',
  },
]

const ReleaseDates = defineComponent({

  props: {
    release: { type: String, required: true },
    eol: { type: String, required: true },
    compact: { type: Boolean, default: false },
  },
  setup(props) {
    return () =>
      h('div', { class: ['release-dates', { 'release-dates--compact': props.compact }] }, [
        h('p', `🚀 ${props.release}`),
        h('p', `☠️ ${props.eol}`),
      ])
  },
})
</script>

<style scoped>
.jdk-timeline {
  --px: min(calc(100cqw / 1280), calc(100cqh / 720));
  position: absolute;
  inset: 0;
  container-type: size;
  overflow: hidden;
  background: #111;
  color: #f7f7f7;
  font-family: "Source Sans Pro", "Inter", "Segoe UI", Arial, sans-serif;
}

.timeline-grid {
  position: absolute;
  inset: 4.3% 2.35% 8.2%;
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(0, 1.08fr) minmax(0, 0.58fr);
  gap: calc(18 * var(--px));
  align-items: start;
}

.timeline-column {
  display: grid;
  grid-auto-rows: min-content;
  gap: calc(18 * var(--px));
  min-width: 0;
}

.version-row,
.legacy-row {
  display: grid;
  align-items: center;
  min-width: 0;
}

.version-row {
  grid-template-columns: minmax(0, 1fr) calc(154 * var(--px));
  gap: calc(20 * var(--px));
}

.timeline-column--long .version-row {
  grid-template-columns: minmax(0, 1fr) calc(154 * var(--px));
}

.legacy-row {
  grid-template-columns: calc(130 * var(--px)) minmax(0, 1fr);
  gap: calc(16 * var(--px));
}

.timeline-column--legacy > .jdk-badge {
  margin-top: calc(10 * var(--px));
}

.badge-stack {
  display: grid;
  grid-template-columns: calc(130 * var(--px)) calc(98 * var(--px)) calc(56 * var(--px));
  align-items: center;
  gap: calc(8 * var(--px));
  min-width: 0;
}

.release-dates {
  font-size: calc(12 * var(--px));
  font-weight: 400;
  line-height: 1.12;
  text-align: left;
  white-space: nowrap;
}

.release-dates :deep(p),
.legend {
  margin: 0;
}

.release-dates :deep(p) {
  line-height: inherit;
}

.release-dates :deep(p + p) {
  margin-top: calc(2 * var(--px));
}

.legend {
  position: absolute;
  inset-inline: 2.35%;
  bottom: 2.5%;
  font-size: calc(20 * var(--px));
  font-weight: 400;
  text-align: center;
}
</style>
