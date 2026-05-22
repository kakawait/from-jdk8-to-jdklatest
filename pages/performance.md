---
layout: section-title
image: /images/performance.png
---

# Performance


---
layout: feature
title: General
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK21', text: 'Improvements in the conversion between primitives (e.g., from <code>long</code>&nbsp;to <code>int</code>) through the use of <code>VarHandle</code>.' },
    { jdk: 'JDK16', text: 'Elastic metaspace to return unused HotSpot class-metadata memory to the operating system more promptly' },
    { jdk: 'JDK13', text: 'Enable dynamic archiving of classes at the end of Java application execution' },
    { jdk: 'JDK12', text: 'Class-Data Sharing archive of the default class list is enabled by default to improve out-of-the-box startup time' },
    { jdk: 'JDK10', text: 'Application Class-Data Sharing to improve startup time and reduce footprint by sharing class metadata between Java processes' },
    { jdk: 'JDK9', text: 'Space-efficient, Compact Strings that stores Latin-1 only Strings more efficiently' },
    { jdk: 'JDK9', text: 'Code caches of profiled and non-profiled compiled code is separated, resulting in improved performance and memory footprint' },
    { jdk: 'JDK9', text: 'Store Interned Strings in Class-Data Sharing archives to reduce memory consumption' },
  ]"
/>

---
layout: feature
title: GC
---
<template #badge>
  <JdkVersions v="9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 22, 23" />
</template>

- Parallel GC has been the replacement of the existing Full GC algorithm with a more traditional parallel Mark-Sweep-Compact algorithm. Reduces heap usage by 1.5%.
...
