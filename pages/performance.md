---
layout: section-title
image: /images/performance.png
---

# Performance


---
layout: feature
title: General
---
<template #badge>
  <JdkVersions v="9, 10, 12, 13, 16, 21" />
</template>

- Improvements in the conversion between primitives (e.g., from `long`&nbsp;to `int`) through the use of `VarHandle`.
...

---
layout: feature
title: GC
---
<template #badge>
  <JdkVersions v="9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 22, 23" />
</template>

- Parallel GC has been the replacement of the existing Full GC algorithm with a more traditional parallel Mark-Sweep-Compact algorithm. Reduces heap usage by 1.5%.
...
