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

<JdkLabeledList
  :items="[
    { jdk: 'JDK15', deprecatedJdk: 'JDK11', text: 'Remove the jjs tool (linked to Nashorn).' },
    { jdk: 'JDK14', deprecatedJdk: 'JDK11', text: 'Remove the Pack200 Tools and API.' },
    { jdk: 'JDK10', text: 'Remove the javah tool.' },
    { jdk: 'JDK9', text: 'Remove the jhat tool.' },
    { jdk: 'JDK9', text: 'Remove the JVM TI hprof Agent.' },
    { jdk: 'JDK9', text: 'Remove rt.jar from the JRE.' },
  ]"
/>

---
layout: feature
title: Security
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK18', text: 'JARs signed with SHA-1 algorithms are now restricted by default and treated as if they were unsigned.' },
    { jdk: 'JDK17', text: 'Deprecate the Security Manager for Removal Work ongoing to consider use cases where the Security Manager is useful and provide alternatives (e.g. <a href=\'https://bugs.openjdk.org/browse/JDK-8199704\' target=\'_blank\'>JDK-8199704</a>).' },
    { jdk: 'JDK9', text: 'Disable X.509 certificate chains with SHA-1 based signatures.' },
  ]"
/>

---
layout: feature
title: Platform
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK21', text: 'Deprecate the Windows 32-bit x86 Port for removal. Windows 10, the last Windows operating system to support 32-bit operation, will reach End of Life in October 2025.' },
    { jdk: 'JDK15', text: 'Remove the Solaris and SPARC Ports.' },
  ]"
/>

---
layout: feature
title: GC
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK14', deprecatedJdk: 'JDK9', text: 'Remove the Concurrent Mark Sweep (CMS) Garbage Collector.' },
    { jdk: 'JDK14', text: 'Deprecate the ParallelScavenge + SerialOld GC Combination.' },
    { jdk: 'JDK9', text: 'Remove GC Combinations Deprecated in JDK 8.' },
  ]"
/>

---
layout: feature
title: CLI flags
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK15', text: 'Disable <a href=\'https://stackoverflow.com/questions/9439602/biased-locking-in-java\' target=\'_blank\'>Biased Locking</a>) by default, deprecate related command-line flags.' },
    { jdk: 'JDK9', text: 'Remove Launch-Time JRE Version Selection directives: JRE-Version manifest entry and -version: cli option.' },
  ]"
/>

---
layout: feature
title: Misc
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK21', text: 'Prepare to Disallow the Dynamic Loading of Agents to improve the integrity and security of the platform.' },
    { jdk: 'JDK17', text: 'Make floating-point operations consistently strict by default, warn when the strictfp modifier is used.' },
    { jdk: 'JDK15', text: 'Remove the Experimental <a href=\'https://openjdk.org/jeps/295\' target=\'_blank\'>AOP</a> and <a href=\'https://openjdk.org/jeps/317\' target=\'_blank\'>JIT</a> compiler due to lack of interest.' },
    { jdk: 'JDK9', text: 'Remove the Endorsed Standards Override (lib/endorsed) and Extensions (lib/ext) mechanisms from the JRE.' },
  ]"
/>
