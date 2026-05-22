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
    { jdk: 'JDK21', text: 'Improvements in the conversion between primitives (e.g., from <code>long</code> to <code>int</code>) through the use of <code>VarHandle</code>.' },
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

<JdkLabeledList
  :items="[
    { jdk: 'JDK23', text: 'Parallel GC has been the replacement of the existing Full GC algorithm with a more traditional parallel Mark-Sweep-Compact algorithm. Reduces heap usage by 1.5%.' },
    { jdk: 'JDK21', text: ['Generational ZGC (using <code>-XX:+ZGenerational</code> or by default since ', { badge: 'JDK23', size: 'small' }, ').'] },
    { jdk: 'JDK18', text: 'SerialGC, ParallelGC and ZGC now supports String Deduplication.' },
    { jdk: 'JDK16', text: 'Z Garbage Collector, offering very low pause times on large heaps.' },
    { jdk: 'JDK15', text: 'Shenandoah Garbage Collector, offering similar benefits as ZGC but based on a different algorithm.' },
    { jdk: 'JDK11', text: 'Epsilon Garbage Collector, which does not implement actual memory reclamation, striving for the lowest overhead possible.' },
    { jdk: 'JDK9', text: 'G1 Garbage Collector is now the default instead of Parallel GC.' },
  ]"
/>

---
layout: feature
title: GC - G1 Specific
---
