---
layout: section-title
image: /images/miscellaneous.png
---

# Miscellaneous


---
layout: feature
title: Launching and tools
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK25', preview: true, jep: '509', text: 'Flight Recorder: CPU-Time Profiling for more accurate profiling on Linux.' },
    { jdk: 'JDK25', jep: '520, 518', text: 'Flight Recorder: Method Timing & Tracing and more accurate Cooperative Sampling (JEP 518).' },
    { jdk: 'JDK22', jep: '458', text: 'Launch Multi-File Source-Code Programs.' },
    { jdk: 'JDK14', jep: '349', text: 'Flight Recorder Event Streaming: profiling data is available via an API, making it suitable for continuous monitoring.' },
    { jdk: 'JDK12', jep: '230', text: 'Microbenchmark Suite based on JMH.' },
    { jdk: 'JDK11', jep: '328', text: 'Flight Recorder is part of OpenJDK.' },
    { jdk: 'JDK11', jep: '331', text: 'Low-Overhead Heap Profiling via JVMTI.' },
    { jdk: 'JDK11', jep: '330', text: 'Launch Single-File Source-Code Programs, including support for shebang (#!) line on Unix.' },
    { jdk: 'JDK9', jep: '222', text: 'jshell: the Java REPL.' },
  ]"
/>

---
layout: feature
title: Packaging
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK18', jep: '400', text: 'javac now assumes that source files are encoded with the new default UTF-8 charset.' },
    { jdk: 'JDK16', jep: '392', text: 'Packaging Tool to create self-contained applications, also supporting native package formats: msi, exe, pkg, dmg, deb and rpm.' },
    { jdk: 'JDK9', jep: '282', text: 'jlink Java Linker that can build an optimized, slim run-time image for a modular Java application that contains only the required parts of the JDK.' },
    { jdk: 'JDK9', jep: '238', text: 'Multi-Release JAR Files to allow multiple, Java-release-specific versions of class in a single archive.' },
  ]"
/>

---
layout: feature
title: Javadoc
---
<template #badge>
  <JdkVersions v="9, 18" />
</template>

<JdkLabeledList
  :items="[
    { jdk: 'JDK9', jep: '224, 225', text: 'The Javadoc tool now emits HTML5 markup instead of a frame-based layout and the documentation contains a search box to ease navigation.' },
    { jdk: 'JDK18', jep: '413', text: '<code>@snippet</code> tag, a modern alternative for <code>@code</code> that supports multi-line code, supports styling and the inclusion of external snippets.' },
  ]"
/>

<div class="grid grid-cols-2 gap-4 mt-2">

<JdkCodeBlock label="JDK18" size="small" contentClass="text-[9px] leading-tight">

```java
/**
 * Highlighting based on regex:
 * {@snippet :
 * if (v.isPresent()) {
 *  System.out.println("Hello!"); // @highlight regex='".*"'
 * }
 *}
 */
public void myMethod() {
  // ...
}
```

</JdkCodeBlock>

<JdkCodeBlock label="JDK18" size="small" contentClass="text-[9px] leading-tight">

```java
/**
 * {@snippet class="com.ds.Example" region="optional" }
 */
public void myMethod() {
    // ...
}

public void exampleSnippetCode() {
    var v = Optional.empty();
    // @start region=optional
    if (v.isPresent()) {
        System.out.println("v: " + v.get());
    }
    // @end region=optional
}
```

</JdkCodeBlock>

</div>


---
layout: feature
title: New supported platforms
---

<JdkLabeledList
  :items="[
    { jdk: 'JDK19', jep: '422', text: 'Linux/RISC-V.' },
    { jdk: 'JDK17', jep: '391', text: 'macOS/AArch64.' },
    { jdk: 'JDK16', jep: '386', text: 'Alpine.' },
    { jdk: 'JDK16', jep: '388', text: 'Windows/AArch64.' },
    { jdk: 'JDK9', jep: '237', text: 'Linux/AArch64.' },
    { jdk: 'JDK9', jep: '294', text: 'Linux/s390x.' },
    { jdk: 'JDK9', jep: '297', text: 'Unified arm32/arm64.' },
  ]"
/>

---
layout: feature
title: New release train
---

<script setup lang="ts">
// Extract the base URL here, where import.meta is fully supported
const baseUrl = import.meta.env.BASE_URL
</script>

<template #badge>
  <JdkVersions v="9" />
</template>

<img
  :src="`${baseUrl}images/new-release-train-white.png`"
  class="mx-auto max-h-[470px] max-w-full object-contain"
/>
  
---
layout: feature
title: Simple web server
---
<template #badge>
  <JdkVersions v="18" />
</template>

jwebserver command line utility to serve static files
(similar to Python’s SimpleHTTPServer or PHP's php -S, for development and education purposes)


---
layout: feature
title: Markdown Documentation Comments
---
<template #badge>
  <JdkVersions v="23" />
</template>

<JdkLinkedCodeBlocks label2="JDK23" size="small" codeClass="text-[8px]" arrowHeight="h-8">
  <template #code1>

```java
/**
 * Returns a hash code value for the object. This method is
 * supported for the benefit of hash tables such as those provided by
 * {@link java.util.HashMap}.
 * <p>
 * The general contract of {@code hashCode} is:
 * <ul>
 * <li>Whenever it is invoked on the same object more than once during
 *     an execution of a Java application, the {@code hashCode} method
 *     must consistently return the same integer, provided no information
 *     used in {@code equals} comparisons on the object is modified.
 *     This integer need not remain consistent from one execution of an
 *     application to another execution of the same application.
 * </li><li>If two objects are equal according to the {@link
 *     #equals(Object) equals} method, then calling the {@code
 *     hashCode} method on each of the two objects must produce the
 *     same integer result.
 * </li><li>It is $ly;em>not$lt;/em> required that if two objects are unequal
 *     according to the {@link #equals(Object) equals} method, then
 *     calling the {@code hashCode} method on each of the two objects
 *     must produce distinct integer results.  However, the programmer
 *     should be aware that producing distinct integer results for
 *     unequal objects may improve the performance of hash tables.
 * </li></ul>
 *
 * @implSpec
 * As far as is reasonably practical, the {@code hashCode} method defined
 * by class {@code Object} returns distinct integers for distinct objects.
 *
 * @return  a hash code value for this object.
 * @see     java.lang.Object#equals(java.lang.Object)
 * @see     java.lang.System#identityHashCode
 */
```

  </template>
  <template #code2>

```java
/// Returns a hash code value for the object. This method is
/// supported for the benefit of hash tables such as those provided by
/// [java.util.HashMap].
///
/// The general contract of `hashCode` is:
///
///   - Whenever it is invoked on the same object more than once during
///     an execution of a Java application, the `hashCode` method
///     must consistently return the same integer, provided no information
///     used in `equals` comparisons on the object is modified.
///     This integer need not remain consistent from one execution of an
///     application to another execution of the same application.
///   - If two objects are equal according to the
///     [equals][#equals(Object)] method, then calling the
///     `hashCode` method on each of the two objects must produce the
///     same integer result.
///   - It is _not_ required that if two objects are unequal
///     according to the [equals][#equals(Object)] method, then
///     calling the `hashCode` method on each of the two objects
///     must produce distinct integer results.  However, the programmer
///     should be aware that producing distinct integer results for
///     unequal objects may improve the performance of hash tables.
///
/// @implSpec
/// As far as is reasonably practical, the `hashCode` method defined
/// by class `Object` returns distinct integers for distinct objects.
///
/// @return  a hash code value for this object.
/// @see     java.lang.Object#equals(java.lang.Object)
/// @see     java.lang.System#identityHashCode
```

  </template>
</JdkLinkedCodeBlocks>
