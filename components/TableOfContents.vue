<template>
  <div class="toc-slide" aria-label="Table of contents">
    <h1>TABLE OF CONTENTS</h1>
    <div class="divider" />

    <section
      v-for="item in items"
      :key="item.number"
      class="toc-item"
      :style="{ '--x': item.x, '--y': item.y }"
    >
      <h2>{{ item.title }}</h2>
      <p>{{ item.description }}</p>
      <strong class="toc-number">{{ item.number }}</strong>
      <img :src="item.icon" :alt="item.title" />
    </section>
  </div>
</template>

<script setup lang="ts">
const items = [
  {
    title: 'New language features',
    description: 'Anything related to new syntax or new keywords',
    number: '01',
    icon: 'https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193490/Picture3.png',
    x: 130.638,
    y: 282.3,
  },
  {
    title: 'New APIs',
    description: 'Focus on Java standard library and available APIs',
    number: '02',
    icon: 'https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193493/Picture4.png',
    x: 130.638,
    y: 426.3,
  },
  {
    title: 'Performance',
    description: 'Performance improvements from Java or JVM',
    number: '03',
    icon: 'https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193429/Picture2.png',
    x: 130.638,
    y: 570.3,
  },
  {
    title: 'Security',
    description: 'Security improvements from Java or JVM',
    number: '04',
    icon: 'https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193520/Picture6.png',
    x: 733.638,
    y: 282.45,
  },
  {
    title: 'Miscellaneous',
    description: 'Uncategorized improvements',
    number: '05',
    icon: 'https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193495/Picture5.png',
    x: 733.638,
    y: 426.45,
  },
  {
    title: 'Deprecations & removals',
    description: 'Any deprecations or removals',
    number: '06',
    icon: 'https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193534/Picture7.png',
    x: 701.638,
    y: 570.3,
  },
]
</script>

<style scoped>
.toc-slide {
  --slide-w: 1280;
  --slide-h: 720;
  --accent: rgb(72, 255, 213);
  position: absolute;
  inset: 0;
  container-type: size;
  overflow: hidden;
  background: #111;
  color: #f7f7f7;
  font-family: "Source Sans Pro", "Inter", "Segoe UI", Arial, sans-serif;
}

h1 {
  position: absolute;
  left: calc(102.5 / var(--slide-w) * 100%);
  top: calc(72 / var(--slide-h) * 100%);
  width: calc(1075 / var(--slide-w) * 100%);
  margin: 0;
  color: #f7f7f7;
  font-size: calc(64 / var(--slide-w) * 100cqw);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: 0;
  text-align: center;
}

.divider {
  position: absolute;
  left: calc(80 / var(--slide-w) * 100%);
  top: calc(171 / var(--slide-h) * 100%);
  width: calc(1120 / var(--slide-w) * 100%);
  height: max(1px, calc(1 / var(--slide-h) * 100cqh));
  background: var(--accent);
}

.toc-item {
  position: absolute;
  left: calc(var(--x) / var(--slide-w) * 100%);
  top: calc(var(--y) / var(--slide-h) * 100%);
  width: calc(440 / var(--slide-w) * 100%);
  height: calc(76 / var(--slide-h) * 100%);
}

.toc-item h2,
.toc-item p {
  position: absolute;
  margin: 0;
  letter-spacing: 0;
}

.toc-item h2 {
  left: 0;
  top: 0;
  width: calc(245 / 440 * 100%);
  color: #fff;
  font-size: calc(21 / var(--slide-w) * 100cqw);
  font-weight: 700;
  line-height: 1.12;
  text-align: center;
}

.toc-item p {
  left: 0;
  top: calc(35.7 / 76 * 100%);
  width: calc(244.5 / 440 * 100%);
  color: var(--accent);
  font-size: calc(15 / var(--slide-w) * 100cqw);
  font-weight: 400;
  line-height: 1.15;
  text-align: center;
}

.toc-number {
  position: absolute;
  left: calc(271 / 440 * 100%);
  top: calc(21.1 / 76 * 100%);
  width: calc(80 / 440 * 100%);
  color: var(--accent);
  font-size: calc(45 / var(--slide-w) * 100cqw);
  font-weight: 700;
  line-height: 1;
  text-align: center;
}

.toc-item img {
  position: absolute;
  left: calc(370 / 440 * 100%);
  top: calc(18 / 76 * 100%);
  width: calc(58 / 440 * 100%);
  height: calc(58 / 76 * 100%);
  object-fit: contain;
}

.toc-item:nth-of-type(4) img,
.toc-item:nth-of-type(6) img {
  width: calc(51 / 440 * 100%);
}

.toc-item:nth-of-type(6) {
  width: calc(480 / var(--slide-w) * 100%);
}

.toc-item:nth-of-type(6) h2 {
  width: calc(293 / 480 * 100%);
}

.toc-item:nth-of-type(6) p {
  left: calc(32 / 480 * 100%);
  width: calc(244.5 / 480 * 100%);
}

.toc-item:nth-of-type(6) .toc-number {
  left: calc(303 / 480 * 100%);
}

.toc-item:nth-of-type(6) img {
  left: calc(411 / 480 * 100%);
}

@container (max-aspect-ratio: 16 / 9) {
  h1 {
    font-size: calc(64 / var(--slide-h) * 100cqh);
  }

  .toc-item h2 {
    font-size: calc(21 / var(--slide-h) * 100cqh);
  }

  .toc-item p {
    font-size: calc(15 / var(--slide-h) * 100cqh);
  }

  .toc-number {
    font-size: calc(45 / var(--slide-h) * 100cqh);
  }
}
</style>
