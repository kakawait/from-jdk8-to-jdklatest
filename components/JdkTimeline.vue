<template>
  <div class="jdk-timeline" aria-label="JDK release and EOL timeline">
    <template v-for="item in currentJdks" :key="item.version">
      <JdkBadge
        :label="item.version"
        :color="item.color"
        :x="item.x"
        :y="item.y"
        size="large"
      />
      <JdkBadge
        :label="item.trackLabel ?? item.version"
        :color="item.color"
        :x="item.trackX"
        :y="item.trackY"
        size="medium"
      />
      <JdkBadge
        v-if="item.smallX"
        :label="item.version"
        :color="item.color"
        :x="item.smallX"
        :y="item.smallY"
        size="small"
      />
      <ReleaseDates
        :release="item.release"
        :eol="item.eol"
        :x="item.datesX"
        :y="item.datesY"
      />
    </template>

    <template v-for="item in oldJdks" :key="item.version">
      <JdkBadge
        :label="item.version"
        :color="item.color"
        :text-color="oldTextColor"
        :border-color="item.borderColor"
        :x="item.x"
        :y="item.y"
        size="large"
      />
      <ReleaseDates
        :release="item.release"
        :eol="item.eol"
        :x="item.datesX"
        :y="item.datesY"
        compact
      />
    </template>

    <JdkBadge
      label="OLD JDK"
      color="#e3ead1"
      text-color="#0e2a47"
      border-color="#a0a88a"
      x="1006.25"
      y="247"
      size="large"
      old
    />

    <p class="legend">🚀 = Release date - ☠️ = EOL free support based on Eclipse Temurin</p>
  </div>
</template>

<script setup lang="ts">
import { computed, defineComponent, h } from 'vue'

type TimelineItem = {
  version: string
  release: string
  eol: string
  color: string
  x: number
  y: number
  trackX: number
  trackY: number
  datesX: number
  datesY: number
  smallX?: number
  smallY?: number
  trackLabel?: string
}

type OldJdkItem = {
  version: string
  release: string
  eol: string
  color: string
  borderColor: string
  x: number
  y: number
  datesX: number
  datesY: number
}

const oldTextColor = '#0e2a47'

const firstColumn: TimelineItem[] = [
  ['JDK9', 'Sept 2017', 'March 2018', '#007bff', 30, 31, 173.25, 38, 382.25, 25.5, undefined, undefined, 'JDK10'],
  ['JDK10', 'March 2018', 'Sept 2018', '#b60205', 30, 103, 173.25, 110, 382.25, 97.5],
  ['JDK11', 'Sept 2018', 'Oct 2027', '#28a745', 30, 175, 173.25, 182, 382.25, 169.5],
  ['JDK12', 'March 2019', 'Sept 2019', '#b6a842', 30, 247, 173.25, 254, 382.25, 241.5],
  ['JDK13', 'Sept 2019', 'March 2020', '#e200db', 30, 319, 173.25, 326, 382.25, 313.5],
  ['JDK14', 'March 2020', 'Sept 2020', '#ff990f', 30, 391, 173.25, 398, 382.25, 385.5, 296.25, 400.5],
  ['JDK15', 'Sept 2020', 'March 2021', '#0a9ca2', 30, 463, 173.25, 470, 382.25, 457.5, 296.25, 472.5],
  ['JDK16', 'March 2021', 'Sept 2021', '#6600cc', 30, 535, 173.25, 542, 382.25, 529.5, 296.25, 544.5],
  ['JDK17', 'Sept 2021', 'Oct 2027', '#a64d79', 30, 607, 173.25, 614, 382.25, 601.5, 296.25, 616.5],
].map(toTimelineItem)

const secondColumn: TimelineItem[] = [
  ['JDK18', 'March 2022', 'Sept 2022', '#454a8e', 518.25, 31, 658.25, 38, 861.75, 25.5, 778.25, 40.5],
  ['JDK19', 'Sept 2022', 'March 2023', '#e43333', 518.25, 103, 658.25, 110, 861.75, 97.5, 778.25, 112.5],
  ['JDK20', 'March 2023', 'Sept 2023', '#083d1c', 518.25, 175, 658.25, 182, 861.75, 169.5, 778.25, 184.5],
  ['JDK21', 'Sept 2023', 'Dec 2029', '#4acaec', 518.25, 247, 658.25, 254, 861.75, 241.5, 778.25, 256.5],
  ['JDK22', 'March 2024', 'Sept 2024', '#710070', 518.25, 319, 658.25, 326, 861.75, 313.5, 778.25, 328.5],
  ['JDK23', 'Sept 2024', 'March 2025', '#854800', 518.25, 391, 658.25, 398, 861.75, 385.5, 778.25, 400.5],
].map(toTimelineItem)

const currentJdks = computed(() => [...firstColumn, ...secondColumn])

const oldJdks: OldJdkItem[] = [
  {
    version: 'JDK6',
    release: 'Dec 2006',
    eol: 'Apr 2013',
    color: '#ead1dc',
    borderColor: '#007bff',
    x: 1006.25,
    y: 31,
    datesX: 1150,
    datesY: 25.5,
  },
  {
    version: 'JDK7',
    release: 'July 2011',
    eol: 'July 2015',
    color: '#d0e0e3',
    borderColor: '#007bff',
    x: 1006.25,
    y: 103,
    datesX: 1150,
    datesY: 97.5,
  },
  {
    version: 'JDK8',
    release: 'March 2014',
    eol: 'Nov 2026',
    color: '#d0e0e3',
    borderColor: '#007bff',
    x: 1006.25,
    y: 175,
    datesX: 1150,
    datesY: 169.5,
  },
]

function toTimelineItem(item: unknown[]): TimelineItem {
  const [
    version,
    release,
    eol,
    color,
    x,
    y,
    trackX,
    trackY,
    datesX,
    datesY,
    smallX,
    smallY,
    trackLabel,
  ] = item as [
    string,
    string,
    string,
    string,
    number,
    number,
    number,
    number,
    number,
    number,
    number | undefined,
    number | undefined,
    string | undefined,
  ]

  return { version, release, eol, color, x, y, trackX, trackY, datesX, datesY, smallX, smallY, trackLabel }
}

const JdkBadge = defineComponent({
  props: {
    label: { type: String, required: true },
    color: { type: String, required: true },
    textColor: { type: String, default: '#fff' },
    borderColor: { type: String, default: '' },
    x: { type: [String, Number], required: true },
    y: { type: [String, Number], required: true },
    size: { type: String, default: 'large' },
    old: { type: Boolean, default: false },
  },
  setup(props) {
    return () =>
      h(
        'div',
        {
          class: ['jdk-badge', `jdk-badge--${props.size}`, { 'jdk-badge--old': props.old }],
          style: {
            '--x': `${props.x}`,
            '--y': `${props.y}`,
            '--badge-bg': props.color,
            '--badge-color': props.textColor,
            '--badge-border': props.borderColor || props.color,
          },
        },
        props.label,
      )
  },
})

const ReleaseDates = defineComponent({
  props: {
    release: { type: String, required: true },
    eol: { type: String, required: true },
    x: { type: Number, required: true },
    y: { type: Number, required: true },
    compact: { type: Boolean, default: false },
  },
  setup(props) {
    return () =>
      h(
        'div',
        {
          class: ['release-dates', { 'release-dates--compact': props.compact }],
          style: {
            '--x': `${props.x}`,
            '--y': `${props.y}`,
          },
        },
        [h('p', `🚀 ${props.release}`), h('p', `☠️ ${props.eol}`)],
      )
  },
})
</script>

<style scoped>
.jdk-timeline {
  --slide-w: 1280;
  --slide-h: 720;
  position: absolute;
  inset: 0;
  container-type: size;
  overflow: hidden;
  background: #111;
  color: #f7f7f7;
  font-family: "Source Sans Pro", "Inter", "Segoe UI", Arial, sans-serif;
}

.jdk-badge,
.release-dates {
  position: absolute;
  left: calc(var(--x) / var(--slide-w) * 100%);
  top: calc(var(--y) / var(--slide-h) * 100%);
}

.jdk-badge {
  display: grid;
  place-items: center;
  height: calc(var(--h) / var(--slide-h) * 100%);
  width: calc(var(--w) / var(--slide-w) * 100%);
  border: max(1px, calc(1 / var(--slide-w) * 100cqw)) solid var(--badge-border);
  border-radius: 5px;
  background: var(--badge-bg);
  color: var(--badge-color);
  font-size: calc(var(--font) / var(--slide-w) * 100cqw);
  font-weight: 700;
  line-height: 1;
  letter-spacing: 0;
}

.jdk-badge--large {
  --w: 130;
  --h: 41;
  --font: 31;
}

.jdk-badge--medium {
  --w: 110;
  --h: 29;
  --font: 24;
}

.jdk-badge--small {
  --w: 65;
  --h: 22;
  --font: 17;
}

.jdk-badge--old {
  --font: 26;
  white-space: nowrap;
}

.release-dates {
  width: calc(170 / var(--slide-w) * 100%);
  font-size: calc(19 / var(--slide-w) * 100cqw);
  font-weight: 400;
  line-height: 1.28;
  text-align: left;
}

.release-dates--compact {
  width: calc(160 / var(--slide-w) * 100%);
}

.release-dates :deep(p),
.legend {
  margin: 0;
}

.release-dates :deep(p + p) {
  margin-top: calc(4 / var(--slide-h) * 100cqh);
}

.legend {
  position: absolute;
  left: calc(43.75 / var(--slide-w) * 100%);
  right: calc(27 / var(--slide-w) * 100%);
  bottom: calc(18 / var(--slide-h) * 100%);
  font-size: calc(24 / var(--slide-w) * 100cqw);
  font-weight: 400;
  text-align: center;
}

@container (max-aspect-ratio: 16 / 9) {
  .jdk-badge {
    font-size: calc(var(--font) / var(--slide-h) * 100cqh);
  }

  .release-dates {
    font-size: calc(19 / var(--slide-h) * 100cqh);
  }

  .legend {
    font-size: calc(24 / var(--slide-h) * 100cqh);
  }
}
</style>
