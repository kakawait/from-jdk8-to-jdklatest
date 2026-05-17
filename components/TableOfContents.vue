<template>
  <div class="toc-slide" aria-label="Table of contents">
    <header class="toc-header">
      <h1>TABLE OF CONTENTS</h1>
      <div class="divider" />
    </header>

    <main class="toc-grid">
      <article v-for="item in items" :key="item.number" class="toc-item" :class="item.className">
        <div class="toc-copy">
          <h2>{{ item.title }}</h2>
          <p>{{ item.description }}</p>
        </div>
        <strong class="toc-number">{{ item.number }}</strong>
        <img :src="item.icon" :alt="item.title" />
      </article>
    </main>
  </div>
</template>

<script setup lang="ts">
const items = [
  {
    title: 'New language features',
    description: 'Anything related to new syntax or new keywords',
    number: '01',
    icon: '/images/new-language-features.png',
  },
  {
    title: 'Security',
    description: 'Security improvements from Java or JVM',
    number: '04',
    icon: '/images/security.png',
    className: 'toc-item--narrow-icon',
  },
  {
    title: 'New APIs',
    description: 'Focus on Java standard library and available APIs',
    number: '02',
    icon: '/images/new-apis.png',
  },
  {
    title: 'Miscellaneous',
    description: 'Uncategorized improvements',
    number: '05',
    icon: '/images/miscellaneous.png',
  },
  {
    title: 'Performance',
    description: 'Performance improvements from Java or JVM',
    number: '03',
    icon: '/images/performance.png',
  },
  {
    title: 'Deprecations & removals',
    description: 'Any deprecations or removals',
    number: '06',
    icon: '/images/deprecations-removals.png',
    className: 'toc-item--narrow-icon',
  },
]
</script>

<style scoped>
.toc-slide {
  --accent: rgb(72, 255, 213);
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-rows: 9.7rem 1fr;
  overflow: hidden;
  background: #111;
  color: #f7f7f7;
  font-family: "Source Sans Pro", "Inter", "Segoe UI", Arial, sans-serif;
}

.toc-header {
  display: grid;
  align-content: end;
  gap: 1.45rem;
  padding-inline: 5rem;
}

h1 {
  margin: 0;
  color: #f7f7f7;
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: 0;
  text-align: center;
}

.divider {
  height: 1px;
  background: var(--accent);
}

.toc-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  grid-template-rows: repeat(3, minmax(0, 1fr));
  column-gap: 5.8rem;
  row-gap: 1.6rem;
  padding: 3.6rem 7.95rem 2.5rem 8.15rem;
}

.toc-item {
  display: grid;
  grid-template-columns: 1fr 3.4rem 3rem;
  align-items: center;
  gap: 1.05rem;
  min-width: 0;
}

.toc-copy {
  display: grid;
  align-content: center;
  gap: 0.65rem;
  min-width: 0;
  text-align: center;
}

.toc-item h2,
.toc-item p {
  margin: 0;
  letter-spacing: 0;
}

.toc-item h2 {
  color: #fff;
  font-size: 0.96rem;
  font-weight: 700;
  line-height: 1.12;
}

.toc-item p {
  color: var(--accent);
  font-size: 0.68rem;
  font-weight: 400;
  line-height: 1.15;
}

.toc-number {
  color: var(--accent);
  font-size: 2.05rem;
  font-weight: 700;
  line-height: 1;
  text-align: center;
  justify-self: center;
}

.toc-item img {
  width: 2.65rem;
  max-height: 2.75rem;
  object-fit: contain;
  justify-self: center;
}

.toc-item--narrow-icon img {
  width: 2.35rem;
}
</style>
