---
layout: section-title
image: /images/deprecations-removals.png
---

# Deprecations &amp; Removals


---
layout: feature
title: Syntax
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK16', text: 'Deprecate the constructors of primitive wrapper classes.' },
    { jdk: 'JDK10', text: '<code>var</code> is no longer a valid class name.' },
    { jdk: 'JDK9', text: 'Underscore is no longer a valid identifier (new keyword).' },
  ]"
/>

---
layout: feature
title: Projects
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK17', deprecatedJdk: 'JDK15', text: 'Remove RMI Activation, affecting the java.rmi.activation package and the rmid tool, does not affect Java RMI in general.' },
    { jdk: 'JDK15', text: 'Remove the Nashorn Javascript Engine and the jjs tool.' },
    { jdk: 'JDK11', text: 'Remove Java EE.' },
    { jdk: 'JDK11', text: 'Remove CORBA.' },
  ]"
/>

---
layout: feature
title: API
---

<JdkLabeledList
  dense
  :items="[
    { jdk: 'JDK23', text: '<strong>Remove</strong> <code>Thread.resume()</code>, <code>Thread.suspend()</code>, <code>ThreadGroup.resume()</code>, <code>ThreadGroup.stop()</code> and <code>ThreadGroup.suspend()</code>.' },
    { jdk: 'JDK23', text: 'Deprecate the Memory-Access Methods in sun.misc.Unsafe for <strong>removal</strong>. In total, more than 79 out of the 87 methods in the <code>Unsafe</code> class are affected.' },
    { jdk: 'JDK19', text: 'The constructors of the <code>Locale</code> class have been deprecated. Instead use <code>Locale.of()</code>.' },
    { jdk: 'JDK18', text: 'Deprecate Thread.stop for <strong>removal</strong>.' },
    { jdk: 'JDK18', text: 'Deprecate Finalization for <strong>removal</strong>.' },
    { jdk: 'JDK17', text: 'Strongly encapsulate internal API’s (sun.*) except for <a href=\'https://openjdk.java.net/jeps/260#Description\' target=\'_blank\'>critical APIs</a> such as sun.misc.Unsafe. Remove the option for <a href=\'https://openjdk.java.net/jeps/261#Relaxed-strong-encapsulation\' target=\'_blank\'>relaxed strong encapsulation</a> via the <a href=\'https://openjdk.java.net/jeps/396#Description\' target=\'_blank\'>--illegal-access launcher option</a>.' },
    { jdk: 'JDK17', text: 'Deprecate Applet API (java.applet.*, javax.swing.JApplet and java.beans.AppletInitializer) for <strong>removal</strong>.' },
    { jdk: 'JDK15', text: 'Deprecate Unsafe::defineAnonymousClass().' },
    { jdk: 'JDK11', text: '<strong>Remove</strong> Thread.destroy() and Thread.stop(Throwable).' },
    { jdk: 'JDK9', text: '<strong>Remove</strong> apple.applescript and com.apple packages.' },
  ]"
/>

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
