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
    { jdk: 'JDK16', jep: '390', text: 'Deprecate the constructors of primitive wrapper classes.' },
    { jdk: 'JDK10', jep: '286', text: '<code>var</code> is no longer a valid class name.' },
    { jdk: 'JDK9', jep: '213', text: 'Underscore is no longer a valid identifier (new keyword).' },
  ]"
/>

---
layout: feature
title: Projects
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK26', deprecatedJdk: 'JDK17', jep: '504', text: '<strong>Remove</strong> the Applet API (java.applet package and related classes).' },
    { jdk: 'JDK17', deprecatedJdk: 'JDK15', jep: '407', text: 'Remove RMI Activation, affecting the java.rmi.activation package and the rmid tool, does not affect Java RMI in general.' },
    { jdk: 'JDK15', jep: '372', text: 'Remove the Nashorn Javascript Engine and the jjs tool.' },
    { jdk: 'JDK11', jep: '320', text: 'Remove Java EE.' },
    { jdk: 'JDK11', jep: '320', text: 'Remove CORBA.' },
  ]"
/>

---
layout: feature
title: API
---

<JdkLabeledList
  dense
  :items="[
    { jdk: 'JDK26', jep: '500', text: 'Warn upon reflective mutation of <code>final</code> fields.' },
    { jdk: 'JDK24', jep: '498', text: 'Warn upon Use of Memory-Access Methods in <code>sun.misc.Unsafe</code>.' },
    { jdk: 'JDK23', text: '<strong>Remove</strong> <code>Thread.resume()</code>, <code>Thread.suspend()</code>, <code>ThreadGroup.resume()</code>, <code>ThreadGroup.stop()</code> and <code>ThreadGroup.suspend()</code>.' },
    { jdk: 'JDK23', jep: '471', text: 'Deprecate the Memory-Access Methods in sun.misc.Unsafe for <strong>removal</strong>. In total, more than 79 out of the 87 methods in the <code>Unsafe</code> class are affected.' },
    { jdk: 'JDK19', text: 'The constructors of the <code>Locale</code> class have been deprecated. Instead use <code>Locale.of()</code>.' },
    { jdk: 'JDK18', text: 'Deprecate Thread.stop for <strong>removal</strong>.' },
    { jdk: 'JDK18', jep: '421', text: 'Deprecate Finalization for <strong>removal</strong>.' },
    { jdk: 'JDK17', jep: '403', text: 'Strongly encapsulate internal API’s (sun.*) except for <a href=\'https://openjdk.java.net/jeps/260#Description\' target=\'_blank\'>critical APIs</a> such as sun.misc.Unsafe. Remove the option for <a href=\'https://openjdk.java.net/jeps/261#Relaxed-strong-encapsulation\' target=\'_blank\'>relaxed strong encapsulation</a> via the <a href=\'https://openjdk.java.net/jeps/396#Description\' target=\'_blank\'>--illegal-access launcher option</a>.' },
    { jdk: 'JDK15', jep: '371', text: 'Deprecate Unsafe::defineAnonymousClass().' },
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
    { jdk: 'JDK15', deprecatedJdk: 'JDK11', jep: '372', text: 'Remove the jjs tool (linked to Nashorn).' },
    { jdk: 'JDK14', deprecatedJdk: 'JDK11', jep: '367', text: 'Remove the Pack200 Tools and API.' },
    { jdk: 'JDK10', jep: '313', text: 'Remove the javah tool.' },
    { jdk: 'JDK9', jep: '241', text: 'Remove the jhat tool.' },
    { jdk: 'JDK9', jep: '240', text: 'Remove the JVM TI hprof Agent.' },
    { jdk: 'JDK9', jep: '220', text: 'Remove rt.jar from the JRE.' },
  ]"
/>

---
layout: feature
title: Security
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK24', jep: '486', text: 'Permanent disabling and removal of the Security Manager.' },
    { jdk: 'JDK18', text: 'JARs signed with SHA-1 algorithms are now restricted by default and treated as if they were unsigned.' },
    { jdk: 'JDK17', jep: '411', text: 'Deprecate the Security Manager for Removal (removed in <JdkBadge label=\'JDK24\' size=\'small\' />).' },
    { jdk: 'JDK9', text: 'Disable X.509 certificate chains with SHA-1 based signatures.' },
  ]"
/>

---
layout: feature
title: Platform
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK25', jep: '503', text: '<strong>Remove</strong> the 32-bit x86 Ports.' },
    { jdk: 'JDK24', jep: '501', text: 'Deprecate the remaining 32-bit x86 Ports for removal.' },
    { jdk: 'JDK21', jep: '449', text: 'Deprecate the Windows 32-bit x86 Port for removal. Windows 10, the last Windows operating system to support 32-bit operation, will reach End of Life in October 2025.' },
    { jdk: 'JDK15', jep: '381', text: 'Remove the Solaris and SPARC Ports.' },
  ]"
/>

---
layout: feature
title: GC
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK25', deprecatedJdk: 'JDK24', jep: '503', text: '<strong>Remove</strong> the 32-bit x86 Ports.' },
    { jdk: 'JDK24', deprecatedJdk: 'JDK23', jep: '490', text: '<strong>Remove</strong> the Non-Generational mode of ZGC. Generational ZGC is now the default and only mode.' },
    { jdk: 'JDK24', jep: '501', text: 'Deprecate the remaining 32-bit x86 Ports for removal.' },
    { jdk: 'JDK21', jep: '449', text: 'Deprecate the Windows 32-bit x86 Port for removal. Windows 10, the last Windows operating system to support 32-bit operation, will reach End of Life in October 2025.' },
    { jdk: 'JDK15', jep: '381', text: 'Remove the Solaris and SPARC Ports.' },
  ]"
/>

---
layout: feature
title: CLI flags
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK15', jep: '374', text: 'Disable <a href=\'https://stackoverflow.com/questions/9439602/biased-locking-in-java\' target=\'_blank\'>Biased Locking</a> by default, deprecate related command-line flags.' },
    { jdk: 'JDK9', jep: '231', text: 'Remove Launch-Time JRE Version Selection directives: JRE-Version manifest entry and -version: cli option.' },
  ]"
/>

---
layout: feature
title: Misc
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK21', jep: '451', text: 'Prepare to Disallow the Dynamic Loading of Agents to improve the integrity and security of the platform.' },
    { jdk: 'JDK17', jep: '306', text: 'Make floating-point operations consistently strict by default, warn when the strictfp modifier is used.' },
    { jdk: 'JDK15', jep: '383', text: 'Remove the Experimental <a href=\'https://openjdk.org/jeps/295\' target=\'_blank\'>AOT</a> and <a href=\'https://openjdk.org/jeps/317\' target=\'_blank\'>JIT</a> compiler due to lack of interest.' },
    { jdk: 'JDK9', jep: '220', text: 'Remove the Endorsed Standards Override (lib/endorsed) and Extensions (lib/ext) mechanisms from the JRE.' },
  ]"
/>
