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
  <JdkVersions v="25" preview="24" />
</template>

Reduces the size of the object header in the HotSpot JVM from 128 bits to 64 bits on 64-bit architectures.

<div class="flex justify-center mb-6">
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
<p class="text-[12.5px] italic opacity-60">Preview in <JdkBadge label="JDK24" size="small" />, final in <JdkBadge label="JDK25" size="small" />, default since <JdkBadge label="JDK27" size="small" /> - toggle with <code>-XX:[+|-]UseCompactObjectHeaders</code>.</p>
</div>

---
layout: feature
title: G1 is the Default GC Everywhere
jep: '523'
---
<template #badge>
  <JdkVersions v="27" />
</template>

G1 has been the default GC since JDK 9 **except** on machines with one CPU or less than ~1792 MB of heap, where the JVM selected **Serial GC**. Lower synchronization overhead (JEP 522) and a smaller native footprint now make G1 equal to or better than Serial everywhere, so it is used in **all** environments unless another GC is requested explicitly.

<div class="bg-white/5 rounded-xl border border-white/10 p-2 mt-4">
<div class="grid grid-cols-3 gap-2 text-center">
  <div>
    <div class="text-lg font-bold text-[#60a5fa]">All</div>
    <div class="text-[10px] uppercase tracking-wider opacity-70 leading-tight">Environments now default to G1</div>
  </div>
  <div>
    <div class="text-lg font-bold text-[#4ade80]">&asymp; Serial</div>
    <div class="text-[10px] uppercase tracking-wider opacity-70 leading-tight">Even with few CPUs / small heaps</div>
  </div>
  <div>
    <div class="text-lg font-bold text-[#f472b6]">Lower</div>
    <div class="text-[10px] uppercase tracking-wider opacity-70 leading-tight">Native memory footprint</div>
  </div>
</div>
</div>

<div class="text-center">
<p class="text-[13px] italic opacity-60">Opt back in to the old behavior with <code>-XX:+UseSerialGC</code> - and measure before choosing a GC.</p>
</div>

---
layout: feature
title: General 1/2
---

<JdkLabeledList
  dense
  :items="[
    { jdk: 'JDK21', text: 'Improvements in the conversion between primitives (e.g., from <code>long</code> to <code>int</code>) through the use of <code>VarHandle</code>.' },
    { jdk: 'JDK16', jep: '387', text: 'Elastic metaspace to return unused HotSpot class-metadata memory to the operating system more promptly' },
    { jdk: 'JDK13', jep: '350', text: 'Enable dynamic archiving of classes at the end of Java application execution' },
    { jdk: 'JDK12', jep: '341', text: 'Class-Data Sharing archive of the default class list is enabled by default to improve out-of-the-box startup time' },
    { jdk: 'JDK10', jep: '310', text: 'Application Class-Data Sharing to improve startup time and reduce footprint by sharing class metadata between Java processes' },
    { jdk: 'JDK9', jep: '254', text: 'Space-efficient, Compact Strings that stores Latin-1 only Strings more efficiently' },
    { jdk: 'JDK9', jep: '197', text: 'Code caches of profiled and non-profiled compiled code is separated, resulting in improved performance and memory footprint' },
    { jdk: 'JDK9', jep: '250', text: 'Store Interned Strings in Class-Data Sharing archives to reduce memory consumption' },
  ]"
/>

---
layout: feature
title: General 2/2
---

<JdkLabeledList
  dense
  :items="[
    { jdk: 'JDK27', text: '<code>HashMap.putAll()</code> fast path when the source is also a <code>HashMap</code>, for a 66-86% improvement.' },
    { jdk: 'JDK27', text: 'New <strong>AVX2 intrinsic</strong> for binary search, 1.5x to 2.35x faster above a size threshold (<code>int</code>=256, <code>long</code>=768, <code>short</code>/<code>char</code>=512).' },
    { jdk: 'JDK26', jep: '516', text: 'Ahead-of-Time Object Caching now GC-agnostic, improving application startup across different GC configurations.' },
    { jdk: 'JDK25', jep: '515', text: 'Ahead-of-Time Method Profiling to record method-execution profiles from previous runs and JIT compile immediately at startup.' },
    { jdk: 'JDK25', jep: '514', text: 'Ahead-of-Time Command-Line Ergonomics to simplify AOT cache creation into a single step.' },
    { jdk: 'JDK24', jep: '483', text: 'Ahead-of-Time Class Loading & Linking (Project Leyden) to improve application startup time.' },
    { jdk: 'JDK24', jep: '493', text: 'Linking Run-Time Images without JMODs to reduce the size of the JDK and custom runtimes.' },
  ]"
/>

---
layout: feature
title: GC 1/2
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK27', jep: '523', text: 'G1 becomes the default GC in <strong>all</strong> environments, including the single-CPU / small-heap deployments where Serial GC used to be chosen.' },
    { jdk: 'JDK21', jep: '439', text: ['Generational ZGC (using <code>-XX:+ZGenerational</code> or by default since ', { badge: 'JDK23', size: 'small' }, ').'] },
    { jdk: 'JDK18', text: 'SerialGC, ParallelGC and ZGC now supports String Deduplication.' },
    { jdk: 'JDK16', jep: '376', text: 'Z Garbage Collector concurrent thread-stack processing, offering even lower pause times.' },
    { jdk: 'JDK15', jep: '379', text: 'Shenandoah Garbage Collector, offering similar benefits as ZGC but based on a different algorithm.' },
    { jdk: 'JDK11', jep: '318', text: 'Epsilon Garbage Collector, which does not implement actual memory reclamation, striving for the lowest overhead possible.' },
    { jdk: 'JDK9', jep: '248', text: 'G1 Garbage Collector is now the default instead of Parallel GC.' },
  ]"
/>

---
layout: feature
title: GC 2/2
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK27', text: 'The JFR event <code>jdk.OldObjectSample</code> is disabled when using <strong>generational ZGC</strong>, because of an unacceptable performance overhead.' },
    { jdk: 'JDK26', jep: '522', text: 'G1 GC optimization to reduce synchronization overhead between application and GC threads.' },
    { jdk: 'JDK26', text: 'ArrayList fast path for <code>addAll()</code> when the source is also an ArrayList.' },
    { jdk: 'JDK25', jep: '521', text: 'Generational Shenandoah to improve efficiency by separating young and old generations.' },
    { jdk: 'JDK24', jep: '490', text: '<strong>Remove</strong> the Non-Generational mode of ZGC. Generational ZGC is now the default and only mode.' },
    { jdk: 'JDK23', text: 'Parallel GC has been the replacement of the existing Full GC algorithm with a more traditional parallel Mark-Sweep-Compact algorithm. Reduces heap usage by 1.5%.' },
  ]"
/>

---
layout: feature
title: GC - G1 Specific
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK27', text: 'New defaults for <code>-XX:MinHeapFreeRatio</code> (40/70) and <code>-XX:MaxHeapFreeRatio</code> (0/100), which effectively disables heap resizing by default and avoids resizing after a Full GC.' },
    { jdk: 'JDK24', jep: '475', text: 'Late Barrier Expansion for G1 to optimize GC barriers during JIT compilation.' },
    { jdk: 'JDK22', jep: '423', text: 'Remove the use of the GCLocker in G1. Improving JNI use cases.' },
    { jdk: 'JDK20', text: 'Reduces G1 native memory footprint by ~1.5% of Java heap size by removing one of the mark bitmaps spanning the entire Java heap.' },
    { jdk: 'JDK18', text: 'Allow G1 Heap Regions up to 512MB.' },
    { jdk: 'JDK14', jep: '345', text: 'NUMA-Aware Memory Allocation.' },
    { jdk: 'JDK12', jep: '344', text: 'Abortable mixed collections to meet user-supplied pause goals.' },
    { jdk: 'JDK12', jep: '346', text: 'Automatically return heap memory to the operating system when idle.' },
    { jdk: 'JDK10', jep: '307', text: 'Parallel Full GC to improve worst-case latencies.' },
  ]"
/>
