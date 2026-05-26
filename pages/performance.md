---
layout: section-title
image: /images/performance.png
---

# Performance


---
layout: feature
title: Compact Object Headers
---
<template #badge>
  <JdkVersions preview="24, 25" />
</template>

Reduces the size of the object header in the HotSpot JVM from 128 bits to 64 bits on 64-bit architectures.

<div class="flex justify-center mt- mb-10">
  <JdkObjectHeaderDiagram />
</div>

<div class="bg-white/5 rounded-xl border border-white/10 p-2">
<div class="grid grid-cols-3 gap-2 text-center">
  <div>
    <div class="text-lg font-bold text-[#60a5fa]">10-20%</div>
    <div class="text-[10px] uppercase tracking-wider opacity-70 leading-tight">Memory footprint reduction</div>
  </div>
  <div>
    <div class="text-lg font-bold text-[#4ade80]">Lower</div>
    <div class="text-[10px] uppercase tracking-wider opacity-70 leading-tight">GC pressure & bandwidth</div>
  </div>
  <div>
    <div class="text-lg font-bold text-[#f472b6]">Better</div>
    <div class="text-[10px] uppercase tracking-wider opacity-70 leading-tight">CPU Cache efficiency</div>
  </div>
</div>
</div>

<div class="text-center">
<p class="text-[13px] italic opacity-60">Enable with: <code>-XX:+UnlockExperimentalVMOptions -XX:+UseCompactObjectHeaders</code></p>
</div>

---
layout: feature
title: General
---

<JdkLabeledList
  dense
  :items="[
    { jdk: 'JDK25', text: 'Ahead-of-Time Class Loading & Linking (Project Leyden) to improve application startup time.' },
    { jdk: 'JDK24', text: 'Linking Run-Time Images without JMODs to reduce the size of the JDK and custom runtimes.' },
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
    { jdk: 'JDK25', text: 'Generational Shenandoah to improve efficiency by separating young and old generations.' },
    { jdk: 'JDK24', preview: true, text: 'Generational Shenandoah to improve efficiency by separating young and old generations.' },
    { jdk: 'JDK24', text: '<strong>Remove</strong> the Non-Generational mode of ZGC. Generational ZGC is now the default and only mode.' },
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

<JdkLabeledList
  :items="[
    { jdk: 'JDK24', text: 'Late Barrier Expansion for G1 to optimize GC barriers during JIT compilation.' },
    { jdk: 'JDK22', text: 'Remove the use of the GCLocker in G1. Improving JNI use cases.' },
    { jdk: 'JDK20', text: 'Reduces G1 native memory footprint by ~1.5% of Java heap size by removing one of the mark bitmaps spanning the entire Java heap.' },
    { jdk: 'JDK18', text: 'Allow G1 Heap Regions up to 512MB.' },
    { jdk: 'JDK14', text: 'NUMA-Aware Memory Allocation.' },
    { jdk: 'JDK12', text: 'Abortable mixed collections to meet user-supplied pause goals.' },
    { jdk: 'JDK12', text: 'Automatically return heap memory to the operating system when idle.' },
    { jdk: 'JDK10', text: 'Parallel Full GC to improve worst-case latencies.' },
  ]"
/>
