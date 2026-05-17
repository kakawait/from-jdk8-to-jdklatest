---
layout: section-title
image: /images/deprecations-removals.png
---

# Deprecations &amp; Removals


---
layout: feature
title: Syntax
---
<template #badge>
  <JdkVersions v="9, 10, 16" />
</template>

- Deprecate the constructors of primitive wrapper classes
...

---
layout: feature
title: Projects
---
<template #badge>
  <JdkVersions v="11, 15, 17" />
</template>

- Remove [RMI Activation](https://docs.oracle.com/javase/9/docs/specs/rmi/activation.html), affecting the java.rmi.activation package and the rmid tool, does not affect Java RMI in general
...

---
layout: feature
title: API
---
<template #badge>
  <JdkVersions v="9, 11, 15, 17, 18, 19, 23" />
</template>

- `Remove&nbsp;Thread.resume()`, `Thread.suspend()`, `ThreadGroup.resume()`, `ThreadGroup.stop()`&nbsp;and `ThreadGroup.suspend()`.
...

---
layout: feature
title: Tools
---
<template #badge>
  <JdkVersions v="9, 10, 11, 14, 15" />
</template>

- Remove the jjs tool (linked to Nashorn)
...

---
layout: feature
title: Security
---
<template #badge>
  <JdkVersions v="9, 17, 18" />
</template>

- JARs signed with SHA-1 algorithms are now restricted by default and treated as if they were unsigned
...

---
layout: feature
title: Platform
---
<template #badge>
  <JdkVersions v="15, 21" />
</template>

- Deprecate the Windows 32-bit x86 Port for **removal**.
...

---
layout: feature
title: GC
---
<template #badge>
  <JdkVersions v="9, 14" />
</template>

- Remove the Concurrent Mark Sweep (CMS) Garbage Collector
...

---
layout: feature
title: CLI flags
---
<template #badge>
  <JdkVersions v="9, 15" />
</template>

- Disable [Biased Locking](https://stackoverflow.com/questions/9439602/biased-locking-in-java) by default, deprecate related command-line flags
...

---
layout: feature
title: Misc
---
<template #badge>
  <JdkVersions v="9, 15, 17, 21" />
</template>

- Prepare to Disallow the Dynamic Loading of Agents to improve the integrity and security of the platform
...
