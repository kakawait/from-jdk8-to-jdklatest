---
layout: section-title
image: /images/new-apis.png
---

# New APIs


---

# Disclaimer

<JdkAlert>

I'll focus only on (personal point of view) new APIs that we can use in day-to-day coding.

If you are curious about all the API level differences between Java 8 later versions, check the [AdoptOpenJDK/jdk-api-diff on GitHub](https://github.com/AdoptOpenJDK/jdk-api-diff) or the [The Java Version Almanac](https://github.com/marchof/java-almanac/).

</JdkAlert>

---
layout: feature
---
::badge::
<JdkVersions v="9" />

::title::
`since` and `forRemoval` for `@Deprecated`

::default::
The `since` attribute requires a string that lets us define in which version the element was deprecated. The default value is an empty string.

And `forRemoval` is a boolean that allows us to specify if the element will be removed in the next release. Its default value is `false`

```java
public class Worker {
    /**
     * Calculate period between versions
     * @deprecated
     * This method is no longer acceptable to compute time between versions.
     * <p> Use {@link Utils#calculatePeriod(Machine)} instead.
     *
     * @param machine instance
     * @return computed time
     */
    @Deprecated(since = "4.5", forRemoval = true)
    public int calculate(Machine machine) {
        return machine.exportVersions().size() * 10;
    }
}
```


---
layout: feature
title: Convenience Factory Methods for Collections
---
<template #badge>
  <JdkVersions v="9" />
</template>

Ease the pain of not having collection literals

```java
Set<Integer> mySet = Set.of(1, 2, 3);
List<Integer> myList = List.of(1, 2, 3);
Map<String, Integer> myMap = Map.of("one", 1, "two", 2);
```


---
layout: feature
title: More Concurrency Updates
---
<template #badge>
  <JdkVersions v="9" />
</template>

Reactive Streams publish-subscribe framework for asynchronous stream processing with non-blocking backpressure

- Publisher: A producer of data items that are received by subscribers

```java
void subscribe(Flow.Subscriber<? super T> subscriber)
```

- Subscriber: A receiver of data items.

```java
void onSubscribe(Flow.Subscription subscription)
void onComplete()
void onError(Throwable throwable)
void onNext(T item)
```

- Subscription: Linkage between a Publisher and a Subscriber.

```java
void request(long n)
void cancel()
```

- Processor: A combination of Publisher and Subscriber for specifying a data-transformation function.

---
layout: feature
title: Stack-walking API
---
<template #badge>
  <JdkVersions v="9" />
</template>

Allows laziness and stack-frame filtering

```java
// return class/method only for our classes.
private static List<String> walkAndFilterStackframe() {
  return StackWalker.getInstance().walk(s ->
    s.map(frame -> frame.getClassName() + "/" + frame.getMethodName())
           .filter(name -> name.startsWith("com.dassaultsystemes"))
           .limit(10)
           .collect(Collectors.toList()));
}
```


---
layout: feature
title: Process API updates
---
<template #badge>
  <JdkVersions v="9" />
</template>

The new interface `ProcessHandle` can provide the operating system specific process id and can return various other useful objects related to the process

```java
ProcessBuilder processBuilder = new ProcessBuilder("notepad.exe");
Process process = processBuilder.start();

System.out.println("-- process handle --");
ProcessHandle processHandle = process.toHandle();
System.out.printf("PID: %s%n", processHandle.pid());
System.out.printf("isAlive: %s%n", processHandle.isAlive());

System.out.println("-- process info --");
ProcessHandle.Info info = processHandle.info();
info.command().ifPresent(str -> System.out.printf("Command: %s%n", str));
info.commandLine().ifPresent(str -> System.out.printf("CommandLine: %s%n", str));
info.arguments().ifPresent(array -> System.out.printf("Arguments: %s%n", array));
info.startInstant().ifPresent(instant -> System.out.printf("StartInstant: %s%n", instant));
info.totalCpuDuration().ifPresent(duration ->
System.out.printf("CpuDuration: %s millis%n", duration.toMillis()));
info.user().ifPresent(str -> System.out.printf("User: %s%n", str));

System.out.println("-- destroying --");
processHandle.destroy();
```


---
layout: feature
title: Arrays utilities
---
<template #badge>
  <JdkVersions v="9" />
</template>

Newly introduced Java 9 Arrays utility class methods for comparing arrays

<jdkCodeBlock contentClass="text-[11px] [&_pre]:!leading-[1rem]">

```java
int[] i1 = {2, 4, 6, 8, 10};
int[] i2 = {2, 4, 6, 8, 11};
int[] i3 = {2, 4, 12, 8, 10};

Arrays.equals(i1, i2); // false
Arrays.equals(i1, 0, 3, i2, 0, 3); // true

Arrays.compare(i1, i2); // -1
Arrays.compare(i1, i3); // -1
Arrays.compare(i3, i1); // 1

Arrays.compare(i1, 0, 3, i2, 0, 3); // 0
Arrays.compare(i1, 0, 3, i3, 0, 3); // -1
Arrays.compare(i3, 0, 3, i1, 0, 3); // 1

Arrays.mismatch(i1, i2); // 4
Arrays.mismatch(i1, i3); // 2
Arrays.mismatch(i3, i1); // 2

Arrays.mismatch(i1, 0, 3, i2, 0, 3); // -1
Arrays.mismatch(i1, 0, 3, i3, 0, 3); // 2
Arrays.mismatch(i3, 0, 3, i1, 0, 3); // 2
```

</jdkCodeBlock>

---
layout: feature

---
::badge::
<JdkVersions v="9" />

::title::
Stream &amp; Collectors new APIs

::default::
```java
Stream.of(2, 4, 6, 8, 9, 10, 12).takeWhile(n -> n % 2 == 0).forEach(System.out::println);
// 2, 4, 6, 8
Stream.of(2, 4, 6, 8, 9, 10, 12).dropWhile(n -> n % 2 == 0).forEach(System.out::println);
// 9, 10, 12
Stream.ofNullable(null).forEach(System.out::println);
// <PRINT NOTHING>
Stream.iterate(0, i -> i < 10, i -> i + 1).forEach(System.out::println);
// 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
Stream.of(1, 2, 3, 5, 5)
    .collect(Collectors.groupingBy(i -> i, Collectors.filtering(val -> val > 3, Collectors.counting())));
// {1=0, 2=0, 3=0, 5=2}
Stream.of(List.of(1, 2, 3, 4), List.of(5, 6, 7, 8))
    .collect(Collectors.flatMapping(l -> l.stream().filter(i -> i % 2 == 0), Collectors.toList()));
// [2, 4, 6, 8]
```


---
layout: feature
title: Optional new APIs
---
<template #badge>
  <JdkVersions v="9" />
</template>

```java
// Optional.or - a lazy version of orElse
Optional<String> value = ...;
Optional<String> defaultValue = Optional.of(() -> bigComputation());
value.or(defaultValue); // bigComputation will be called only if value is empty
// Optional.ifPresent
Optional<String> value = ...;
AtomicInteger successCounter = new AtomicInteger(0);
value.ifPresent(v -> successCounter.incrementAndGet());
// Optional.ifPresentOrElse
Optional<String> value = ...;
AtomicInteger successCounter = new AtomicInteger(0);
AtomicInteger onEmptyOptionalCounter = new AtomicInteger(0);
value.ifPresentOrElse(v -> successCounter.incrementAndGet(), onEmptyOptionalCounter::incrementAndGet);
// Optional.stream - unify the stream and Optional API
Optional<String> value = Optional.of("a");
List<String> collect = value.stream().map(String::toUpperCase).collect(Collectors.toList()); 
// ["A"]
```


---
layout: feature
title: New APIs (JDK10)
---
<template #badge>
  <JdkVersions v="10" />
</template>

```java
// copyOf to newly created immutable collections
List.copyOf(Collection<? extends E> coll);
Set.copyOf(Collection<? extends E> coll);
Map.copyOf(Map<? extends K,? extends V> map);

// Collectors to create Unmodifiable collections
Collectors.toUnmodifiableList();
Collectors.toUnmodifiableSet();
Collectors.toUnmodifiableMap(keyFunc, valueFunc);
Collectors.toUnmodifiableMap(keyFunc, valueFunc, mergeFunc);

// Should replace Optional.get()
Optional.orElseThrow();

// To directly transfer Reader input to Writer
Reader.transferTo(Writer);
```


---
layout: feature
title: Standard HTTP Client
---
<template #badge>
  <JdkVersions v="11, 21" preview="9" />
</template>

Standard HTTP Client featuring HTTP/2, WebSocket support and non-blocking API

```java
HttpClient httpClient = HttpClient.newBuilder().build();

HttpRequest request =
  HttpRequest.newBuilder()
    .uri(URI.create("https://thibaud.dev/"))
    .GET()
    .build();

HttpResponse<String> response =
  httpClient.send(request, BodyHandlers.ofString());
```

Since <JdkBadge label="JDK21" size="small" /> `HttpClient` now implements `AutoCloseable` and can therefore be used more easily in a *try-with-resources block.

---
layout: feature
title: Unicode 10
---
<template #badge>
  <JdkVersions v="11" />
</template>

Unicode 10.0, adding roughly 27,000 characters, 10 blocks, and more than 30 scripts


---
layout: feature
title: New String APIs
---
<template #badge>
  <JdkVersions v="11" />
</template>

```java
// Repeat strings
"Hello".repeat(3);
// HelloHelloHello
// strip is UTF8 compatible version of existing trim()
" Hello World ".strip();
// "Hello World"
" Hello World ".stripLeading();
// "Hello World "
" Hello World ".stripTrailing();
// " Hello World"
" ".isBlank();
// true
"notblank".isBlank();
// false
// A more powerful split (because is lazy)
"A \n B \n C \n D".lines().forEach(System.out::println);
// A
// B
// C
// D
```


---
layout: feature
title: New APIs (JDK12)
---
<template #badge>
  <JdkVersions v="12" />
</template>

```java
// String indent
String multilineStr = "This is\na multiline\nstring.";
String outputStr = "   This is\n   a multiline\n   string.\n";
String postIndent = multilineStr.indent(3);
postIndent.equals(outputStr);
// true
// String transform
String result = "hello".transform(input -> input + " world!");
// "hello world!"

// Files mismatch
Path filePath3 = Files.createTempFile("file3", ".txt");
Path filePath4 = Files.createTempFile("file4", ".txt");
Files.writeString(filePath3, "Java 12 Article");
Files.writeString(filePath4, "Java 12 Tutorial");
Files.mismatch(filePath3, filePath4);
// 8

// Collectors teeing
Stream.of(1, 2, 3, 4, 5)
      .collect(Collectors.teeing(Collectors.summingDouble(i -> i), 
        Collectors.counting(), (sum, count) -> sum / count));
// 3.0
```


---
layout: feature
title: New Stream APIs
---
<template #badge>
  <JdkVersions v="16" />
</template>

```java
// Stream.mapMulti to replace each element of this stream 
// with zero or more elements, an alternative to flatMap
Stream.of(1, 2, 3, 4)
    .mapMulti((number, downstream) -> downstream.accept(number))
    .forEach(System.out::print); 
// prints 1234

// Stream.toList as convenience for the most typical 
// collection method (instead of relying on .collect(Collectors.toList())) 
List<String> result =
  Stream.of("one", "two", "three").stream()
    .filter(s -> s.length() == 3)
    .toList();
```


---
layout: feature
title: UTF-8 by default
---
<template #badge>
  <JdkVersions v="18" />
</template>

- Java APIs that depend on the default charset will use UTF-8 by default (e.g. InputStreamReader, FileReader, OutputStreamWriter, FileWriter, PrintStream, Formatter, Scanner)


---
layout: feature
title: Sequenced Collections
---
<template #badge>
  <JdkVersions v="21" />
</template>

<div class="text-[13px] leading-tight mb-2 opacity-90">
Java collections do not have a type representing an ordered sequence of elements. Java 21 fills this gap by introducing the interfaces <code>SequencedCollection</code>, <code>SequencedSet</code>, and <code>SequencedMap</code>. These interfaces provide methods for adding, modifying, or removing elements at the beginning or end of the collection, as well as iterating over a collection in reverse order.
</div>

<div class="grid grid-cols-[1fr_2.2fr] gap-2 items-start">
<div>
<JdkCodeBlock size="small" contentClass="text-[12px]">

```java
interface SequencedCollection<E> 
    extends Collection<E> {
  SequencedCollection<E> reversed();
  void addFirst(E);
  void addLast(E);
  E getFirst();
  E getLast();
  E removeFirst();
  E removeLast();
}
```

</JdkCodeBlock>
</div>



<div class="bg-white p-1 rounded-lg shadow-sm border border-gray-200 overflow-hidden flex justify-center">

<script setup>
import hierarchySvg from '../assets/images/sequenced-collections-hierarchy.svg'
</script>
<img :src="hierarchySvg" class="w-full h-auto" />

</div>
</div>



---
layout: feature
title: 😅 😗 😆 🧐 🤫 😱 🥳 😍 😴 🤓 😃
---
<template #badge>
  <JdkVersions v="21" />
</template>

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div>
<JdkCodeBlock size="small" contentClass="text-[10px]">

```java
String messageWithEmoji = "Hello Java 21! 😄";
String messageWithoutEmoji = "Hello Java!";

assertTrue(messageWithEmoji.codePoints()
  .anyMatch(Character::isEmoji));
assertFalse(messageWithoutEmoji.codePoints()
  .anyMatch(Character::isEmoji));

String emojiPresentationMessage = "Hello Java 21! 🔥😄";
String nonEmojiPresentationMessage = "Hello Java 21!";

assertTrue(emojiPresentationMessage.codePoints()
  .anyMatch(Character::isEmojiPresentation));
assertFalse(nonEmojiPresentationMessage.codePoints()
  .anyMatch(Character::isEmojiPresentation));
```

</JdkCodeBlock>
</div>

<div>
<JdkCodeBlock size="small" contentClass="text-[10px]">

```java
assertTrue(Character.isEmojiModifier(0x1F3FB)); // light skin tone
assertTrue(Character.isEmojiModifier(0x1F3FD)); // medium skin tone
assertTrue(Character.isEmojiModifier(0x1F3FF)); // dark skin tone

assertTrue(Character.isEmojiModifierBase(
  Character.codePointAt("👍", 0)));
assertTrue(Character.isEmojiModifierBase(
  Character.codePointAt("👶", 0)));

assertTrue(Character.isEmojiComponent(0x200D)); // ZWJ
assertTrue(Character.isEmojiComponent(0x1F3FD)); // medium skin tone

assertTrue(Character.isExtendedPictographic(
  Character.codePointAt("✔️", 0)));

String msg = "Hello Java 21! 😄";
Matcher m = Pattern.compile("\\p{IsEmoji}").matcher(msg);
assertTrue(m.find());
```

</JdkCodeBlock>
</div>
</div>


---
layout: feature
title: Virtual Threads
---
<template #badge>
  <JdkVersions v="21" preview="19, 20" />
</template>

Virtual threads are lightweight threads that dramatically reduce the effort of writing, maintaining, and observing high-throughput concurrent applications.

```java
// With OS threads, this would be very problematic
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 10_000).forEach(i -> {
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1));
            System.out.println("" + i);
            return i;
        });
    });
}
```

There are limitations in the current implementation of virtual threads.

- ~~The use of the `synchronized` keyword~~ (fixed in <JdkBadge label="JDK24" size="small" />)
- The use of native methods or the Foreign Function API from JEP 424

Due to these limitations, virtual threads are not necessarily the solution to all concurrency problems.


---
layout: feature
title: Foreign linker API and Foreign memory access API
---
<template #badge>
  <div class="foreign-memory-badge">
    <JdkVersions v="22" preview="14, 15, 16, 17, 18, 19, 20, 21" previewThreshold="3" />
    <FancyArrow
      from="[data-jdk-label='JDK14']@(85%,350%)"
      to="[data-jdk-label='JDK14']@bottom"
      color="white"
      static
    />
    <FancyArrow
      from="[data-jdk-label='JDK15']@(15%,350%)"
      to="[data-jdk-label='JDK15']@bottom"
      color="white"
      static
    />
    <div class="foreign-memory-note">Only Foreign memory access</div>
  </div>
</template>

- The *foreign linker API* provides a flexible way to access native code on the host machine
  - Can replace JNI/JNA
- The *foreign memory access AP*I provides a supported, safe, and efficient API to access both heap and native memory

Good blog post for pratical use case

[https://blog.arkey.fr/2021/02/20/a-practical-look-at-jep-389-in-jdk16-with-libsodium/](https://blog.arkey.fr/2021/02/20/a-practical-look-at-jep-389-in-jdk16-with-libsodium/)

<style>
.foreign-memory-badge {
  --px: min(calc(100cqw / 1280), calc(100cqh / 720));
  position: relative;
  padding-bottom: calc(55 * var(--px));
}

.foreign-memory-note {
  position: absolute;
  left: calc(65 * var(--px));
  top: calc(65 * var(--px));
  width: calc(220 * var(--px));
  color: #fff;
  font-size: calc(14 * var(--px));
  font-weight: 700;
  line-height: 1;
  text-align: center;
  white-space: nowrap;
}
</style>

---
layout: feature
title: Class-File API
---
<template #badge>
  <JdkVersions v="25" preview="22, 23, 24" />
</template>

Standard API for parsing, generating, and transforming Java class files.

The Java ecosystem has many libraries that allow for parsing and generating Java class files: ASM, BCEL, Javassist, etc. Most frameworks that generate bytecode use them.

The format of Java class files evolves every 6 months with each new Java release, so generation frameworks must evolve at the same time to avoid not supporting the latest language developments.

The Class-File API addresses this problem by providing an API within the JDK for parsing, generating, and transforming class files.


---
layout: feature
title: Stream Gatherers
---
<template #badge>
  <JdkVersions v="25" preview="22, 23, 24" />
</template>

Enhances the Stream API with support for custom intermediate operations. 

The Stream API provides a fixed set of intermediate and terminal operations. It allows extending terminal operations via the `Stream::collect(Collector)` method, but does not allow extending intermediate operations.

```java
var numbers = List.of(1, 2, 3, 4, 5);

var slidingWindows = numbers.stream()
    .gather(Gatherers.windowSliding(3))
    .toList();

System.out.println(slidingWindows);
// [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
```

---
layout: feature
title: Prepare to Restrict the Use of JNI
---
<template #badge>
  <JdkVersions v="24" />
</template>

Since <JdkBadge label="JDK22" size="small" />, it is possible to invoke native code via the Java Native Interface (JNI) or the Foreign Function & Memory (FFM) API. However, loading native code is restricted in the FFM API, which triggers a runtime warning by default. To ensure consistency between JNI and FFM, calling native code via JNI also generates a warning during runtime.

Using a native function will generate a WARNING at JVM startup unless the JVM `--enable-native-access` option is used to authorize it. It is also possible to use the manifest entry `Enable-Native-Access`.

```
WARNING: A restricted method in java.lang.System has been called
WARNING: System::load has been called by com.foo.Server in module com.foo (file:/path/to/com.foo.jar)
WARNING: Use --enable-native-access=com.foo to avoid a warning for callers in this module
WARNING: Restricted methods will be blocked in a future release unless native access is enabled
```

It defaults to warn, and can take the following values:

- `allow`: use is authorized without restriction,
- `warn`: **the default in Java 24**, a warning will be emitted in the JVM logs,
- `deny`: use is refused, an IllegalCallerException will be thrown.


---
layout: feature
title: Vector API
---
<template #badge>
  <JdkVersions preview="15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25" />
</template>

The idea of this API is to provide a means of vector computations that will ultimately be able to perform more optimally (on supporting CPU architectures) than the traditional scalar method of computations.

multiply two arrays

<JdkLinkedCodeBlocks label1="JDK15" codeClass="text-[11px]">
  <template #code1>

```java
int[] a = {1, 2, 3, 4};
int[] b = {5, 6, 7, 8};

var vectorA = IntVector.fromArray(IntVector.SPECIES_128, a, 0);
var vectorB = IntVector.fromArray(IntVector.SPECIES_128, b, 0);
var vectorC = vectorA.mul(vectorB);
vectorC.intoArray(c, 0);
```

  </template>
  <template #code2>

```java
int[] a = {1, 2, 3, 4};
int[] b = {5, 6, 7, 8};

var c = new int[a.length];

for (int i = 0; i < a.length; i++) {
    c[i] = a[i] * b[i];
}
```

  </template>
</JdkLinkedCodeBlocks>

---
layout: feature
title: Structured concurrency API
---
<template #badge>
  <JdkVersions preview="19, 20, 21, 22, 23, 24, 25" />
</template>

<div class="text-[13px] leading-tight mb-3 opacity-90">
Structured concurrency API to define subtask relations between threads to streamline error handling and cancellation, improve reliability, and enhance observability
</div>

<div class="grid grid-cols-[1.3fr_1fr] gap-x-8 items-start mt-2">

<JdkLinkedCodeBlocks 
  label1="OLD JDK" 
  label2="JDK21" 
  direction="vertical" 
  size="small"
  codeClass="text-[8px] leading-tight"
  arrowHeight="h-6"
>
  <template #code1>

```java
ExecutorService ex = Executors.newFixedThreadPool(nbCores);
Response handle() throws ExecutionException, InterruptedException {
    Future<String>  user  = es.submit(() -> findUser());
    Future<Integer> order = es.submit(() -> fetchOrder());
    String theUser  = user.get();   // Join findUser 
    int    theOrder = order.get();  // Join fetchOrder
    return new Response(theUser, theOrder);
}
```

  </template>
  <template #code2>

```java
Response handle() throws ExecutionException, InterruptedException {
    try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
        Future<String>  user  = scope.fork(() -> findUser()); 
        Future<Integer> order = scope.fork(() -> fetchOrder());

        scope.join();          // Join both forks
        scope.throwIfFailed(); // ... and propagate errors

        // Here, both forks have succeeded, so compose their results
        return new Response(user.resultNow(), order.resultNow());
    }
}
```

  </template>
</JdkLinkedCodeBlocks>

<div class="text-[11.5px] leading-snug space-y-4 pt-1 opacity-90 text-white/90">

- If an error occurs in the `fetchOrder()` method, we will still wait for the `findUser()` task to complete.
- If an error occurs in the `findUser()` method, then the `handle()` method will terminate, but the thread executing `fetchOrder()` will continue to run, resulting in a thread leak.
- If the `handle()` method is interrupted, this interruption is not propagated to the subtasks, and their threads will continue to run, resulting in a thread leak.

</div>

</div>

---
layout: feature
title: Scoped Values
---
<template #badge>
  <JdkVersions v="25" preview="20, 21, 22, 23, 24" />
</template>

An alternative to ThreadLocal that allows sharing immutable data with limit visibility. JDK 24 removes `callWhere` and `runWhere` in favor of `call` and `run`.

ThreadLocal are mutable and require a complex data structure whose cost is not in line with virtual threads, which are lightweight and inexpensive to create.


```java
private static final ScopedValue<String> USERNAME = ScopedValue.newInstance();

ScopedValue.where(USERNAME, "duke") // bind a value to the scope
    // start a thread that could access this value
    .run(() -> System.out.println("User: " + USERNAME.get()));
```
