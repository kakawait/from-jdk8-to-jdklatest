---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  Migrated Presentation
---

# From Java 8 to Java 23

Thibaud Lepretre


---
layout: full
---

<JdkTimeline />


---
layout: full
---

<TableOfContents />


---
layout: section-title
image: https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193490/Picture3.png
---

# New language features


---
layout: feature
title: Improved warnings
---
<template #badge>
  <JdkVersions v="9" />
</template>

The **@SafeVarargs** annotation was introduced in Java 7. This annotation applies to both **final** **and **static methods** or **constructors** that take varargs parameters. This annotation used to make sure that a method does not perform unsafe operations on its varargs parameters. Since Java 9, **@SafeVarargs** annotation also applies to **private instance methods**.

```java
@SafeVarargs
private void methodName(...) {
   // some statements
}
```

---
layout: feature
---
::badge::
<JdkVersions size="medium" v="9" />

::title::
No deprecation warnings on `import` statement

::default::
While working with Java applications, if you import any deprecated APIs/ use deprecated member , java compiler will throw warnings at the time of compilation. Most of these warnings are uninformative and should not be required.

From Java 9 onwards, compiler suppress deprecated warnings if one of the following case occur.

- The use is within an entity that is itself annotated with the annotation @Deprecated
- The use is within an entity that is annotated to suppress the warning with the annotation @SuppressWarnings("deprecation")
- The use and declaration are both within the same outermost class
- The use is within an import statement

---
layout: feature
title: Allow effectively-final variables to be used as resources in try-with-resources statements
---
<template #badge>
  <JdkVersions v="9" />
</template>

in the Java 7 version, if you already have a variable that you want to handle with this construct, you had to introduce a dummy variable.

To mitigate these criticisms, try-with-resources was enhanced to handle final or effectively final local variables in addition to newly created ones:

```java
BufferedReader br1 = new BufferedReader(...);
BufferedReader br2 = new BufferedReader(...);
try (br1; br2) {
    System.out.println(br1.readLine() + br2.readLine());
}
```

```java
try (BufferedReader br = new BufferedReader(...)) {
    return br.readLine();
}
```

```java
BufferedReader br = new BufferedReader(...);
try {
    return br.readLine();
} finally {
    if (br != null) {
        br.close();
    }
}
```

---
layout: feature
title: Diamond operator for anonymous inner classes
---
<template #badge>
  <JdkVersions v="9" />
</template>

However, this feature did not work with anonymous inner classes before.

With Java 9, this small rough edge is removed, making the operator more universally applicable

```java
List<Integer> numbers = new ArrayList<>();
```

```java
List<Integer> numbers = new ArrayList<>() {
    // ...
}
```

---
layout: feature
title: Allow private methods in interfaces
---
<template #badge>
  <JdkVersions v="9" />
</template>

```java
public interface CustomInterface {
     
    public abstract void method1();
     
    public default void method2() {
        method4();  //private method inside default method
        method5();  //static method inside other non-static method
        System.out.println("default method");
    }
     
    public static void method3() {
        method5(); //static method inside other static method
        System.out.println("static method");
    }
     
    private void method4(){
        System.out.println("private method");
    } 
     
    private static void method5(){
        System.out.println("private static method");
    } 
}
```

---
layout: feature
title: Opt-in and backwards-compatible Module System
---
<template #badge>
  <JdkVersions v="9" />
</template>

```java
module com.dassaultsystemes.helloworld {
    requires com.dassaultsystemes.somedependency;
    exports com.dassaultsystemes.hello
}
```

---
layout: feature
title: Local-Variable Type Inference
---
<template #badge>
  <JdkVersions v="11" preview="10" />
</template>

Probably the most significant language improvement since Java 8 is the addition of the var keyword. It was initially introduced in [Java 10](https://openjdk.java.net/jeps/286), and was further improved in [Java 11](https://openjdk.java.net/jeps/323).

This feature allows us to reduce the ceremony of a local variable declaration by omitting the explicit type specification:

### Make sure to read the official style guides

### Official [style guide](https://openjdk.java.net/projects/amber/LVTIstyle.html) and [FAQ](https://openjdk.java.net/projects/amber/LVTIFAQ.html) about `var`

```java
var greetingMessage = "Hello, I'm batman!";
var map = new HashMap<>();
```

---
layout: feature
title: Switch Expressions
---
<template #badge>
  <JdkVersions v="14" preview="12, 13" />
</template>

The good old `switch` got a facelift in Java 14. While Java keeps supporting the old [switch statement](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html), it adds the new **switch expression** to the language

```java
int numLetters = switch (day) {
    case MONDAY, FRIDAY, SUNDAY -> 6;
    case TUESDAY                -> 7;
    default      -> {
        String s = day.toString();
        int result = s.length();
        yield result;
    }
};
```

---
layout: feature
title: Helpful NullPointerExceptions describing precisely which variable was null
---
<template #badge>
  <JdkVersions v="15" preview="14" />
</template>

(Enabled with `-XX:+ShowCodeDetailsInExceptionMessages` in &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )

```java
node.getElementsByTagName("name").item(0).getChildNodes().item(0).getNodeValue();
---
Exception in thread "main" java.lang.NullPointerException:
  Cannot invoke "org.w3c.dom.Node.getChildNodes()" because
  the return value of "org.w3c.dom.NodeList.item(int)" is null
        at Unlucky.method(Unlucky.java:83)
```

```java
node.getElementsByTagName("name").item(0).getChildNodes().item(0).getNodeValue();

---
Exception in thread "main" java.lang.NullPointerException
        at Unlucky.method(Unlucky.java:83)
```


---
layout: feature
title: Text Blocks
---
<template #badge>
  <JdkVersions v="15" preview="13, 14" />
</template>

### No variables interpolation

```java
String html = """
          <html>
            <body>
              <p>Hello, world</p>
            </body>
          </html>
          """;

System.out.println(html);
```

```java
String html = "";
html += "<html>\n";
html += "  <body>\n";
html += "    <p>Hello, world</p>\n";
html += "  </body>\n";
html += "</html>\n";

System.out.println(html);
```

---
layout: feature
title: Pattern Matching for instanceof
---
<template #badge>
  <JdkVersions v="16" preview="14, 15" />
</template>

can be used in the second part of the condition because it’s only evaluated when the first one succeeds and the `instanceof` operator has a match

```java
if (obj instanceof String s) {
    // use s
}
```

```java
if (obj instanceof String s && s.length() > 5) {
  // use s
}
```

```java
if (obj instanceof String) {
    String s = (String) obj;
    // use s
}
```

---
layout: feature
title: Record classes
---
<template #badge>
  <JdkVersions v="16" preview="14, 15" />
</template>

Record Classes introduce a new type declaration to the language to define immutable data classes. Instead of the usual ceremony with private fields, getters and constructors, it allows us to use a **compact syntax**:

Java 16 improves on this, as **now it’s also possible to define Local Records** in a method body:

```java
public record Point(int x, int y) { }

var point = new Point(1, 2);
point.x(); // returns 1
point.y(); // returns 2
```

```java
public List<Product> findProductsWithMostSaving(List<Product> products) {
  record ProductWithSaving(Product product, double savingInEur) {}

  products.stream()
    .map(p -> new ProductWithSaving(p, p.basePriceInEur * p.discountPercentage))
    .sorted((p1, p2) -> Double.compare(p2.savingInEur, p1.savingInEur))
    .map(ProductWithSaving::product)
    .limit(5)
    .collect(Collectors.toList());
}
```
---
layout: feature
title: Sealed Classes
---
<template #badge>
  <JdkVersions v="17" preview="15, 16" />
</template>

Sealed classes and interfaces can be used to restrict which other classes or interfaces may extend or implement them. It gives a tool to better design public APIs, and provides an alternative to Enums to model fixed number of alternatives.

```java
public abstract sealed class Shape
    permits Circle, Rectangle {...}

public final class Circle extends Shape {...} // OK
public final class Rectangle extends Shape {...} // OK
public final class Triangle extends Shape {...} // Compile error

// No need for default case if all permitted types are covered
double area = switch (shape) {
    case Circle c    -> Math.pow(c.radius(), 2) * Math.PI
    case Rectangle r -> r.a() * r.b()
};
```

---
layout: feature
title: Pattern Matching for switch
---
<template #badge>
  <JdkVersions v="21" preview="17, 18, 19, 20" />
</template>

Pattern Matching for `switch` supporting type patterns and guarded patterns

```java
String formatted = switch (o) {
    case null                -> "Oups";
    case Integer i && i > 10 -> String.format("a large Integer %d", i);
    case Integer i           -> String.format("a small Integer %d", i);
    case Long l              -> String.format("a Long %d", l);
    default                  -> "something else";
};
```
---
layout: feature
title: Record Patterns
---
<template #badge>
  <JdkVersions v="21" preview="19, 20" />
</template>

Record Patterns extends the pattern matching capabilities of Java beyond simple type patterns to **match and deconstruct Record values**. It **supports nesting**&nbsp;to enable declarative, data focused programming.

```java
interface Point { }
record Point2D(int x, int y) implements Point { }
enum Color { RED, GREEN, BLUE }
record ColoredPoint(Point p, Color c) { }

Object r = new ColoredPoint(new Point2D(3, 4), Color.GREEN);
```

```java
if (r instanceof ColoredPoint cp 
  && cp.p() instanceof Point2D pt) {
    int x = pt.x();
    int y = pt.y();
    Color c = cp.c();

    // work with x, y, and c
}
```

```java
if (r instanceof ColoredPoint(Point2D(int x, int y), Color c)) {
  // work with x, y, and c
}

var length = switch (r) {
	case ColoredPoint(Point2D(int x, int y), Color c) -> Math.sqrt(x*x + y*y);
	case ColoredPoint(Point p, Color c) -> 0;
}
```

---
layout: feature
title: Unnamed Patterns and Variables
---
<template #badge>
  <JdkVersions v="22" preview="21" />
</template>

now it's possible to use the underscore character wherever a variable name would be used. However, it's not a regular variable name: it means "don't care" as **underscore can be redeclared, and can not be referenced**

**unnamed patterns**&nbsp;which can be used in pattern matching to ignore subpatterns

```java
if (r instanceof ColoredPoint(Point(int x, int y), Color c)) {
  // do something with x and y, but c is not needed
}
```

```java
var _ = mySet.add(x); // ignore the return value
try {
   // ...
} catch (Exception _) { // ignore the exception object
   // ...
}
list.stream()
  .map((_) -> /* ... */) // ignore the parameter
  .toList();
```

```java
if (r instanceof ColoredPoint(Point(int x, int y), _)) {
  // ... x ... y ...
}
```

---
layout: feature
title: Unnamed Classes and Instance Main Methods
---
<template #badge>
  <JdkVersions v="23" preview="21, 22" />
</template>

In old Java versions, one needed write quite some boilerplate code even for the simplest of the applications:

1. A more tolerant launch protocol
2. Unnamed classes

**Instance main methods**&nbsp;makes the Java launch protocol more flexible, by making some aspects of the `main`&nbsp;method optional.

**Methods to exist outside of an enclosing class**&nbsp;in which case they are automatically wrapped into a synthetic **unnamed class**.

```java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, World!");
  }
}
```

```java
class HelloWorld {
  void main() {
    System.out.println("Hello, World!");
  }
}
```

```java
void main() {
  System.out.println("Hello, World!");
}
```

```java
void main() {
  println("Hello, World!");
}
```

---
layout: feature
title: String template
---
<template #badge>
  <JdkVersions v="22" preview="21" />
</template>

String Templates are an extension to the single-line String literals and Text Blocks, allowing String interpolation and much more.

Built-in processors:

`STR, FMT, RAW`

⚠️ Removed from **JDK23**

```java
var name = "Thibaud";
var info = "My name is " + name;
info = new StringBuilder().append("My name is ").append(name);
// java 15
info = "My name is %s".formatter(name);
```

```java
var JSON = StringTemplate.Processor.of(
  (StringTemplate st) -> new JSONObject(st.interpolate())
);

JSONObject doc = JSON."""
{
   "name":   "\{name}",
   "phone":  "\{phone}",
   "adress": "\{address}"
};
""";
```

```java
var name = "Thibaud";
var info = STR."My name is \{name}";
```

---
layout: feature
title: Statements before super
---
<template #badge>
  <JdkVersions v="23" preview="22" />
</template>

Allows instructions before the call to the parent constructor (super) as long as they do not access the instance being created

```java
public class PositiveBigInteger extends BigInteger {
    public PositiveBigInteger(long value) {
        super(value); // Potentially unnecessary work
        if (value <= 0) {
            throw new IllegalArgumentException("non-positive value");
        }
    }
}
```

```java
public class PositiveBigInteger extends BigInteger {
    public PositiveBigInteger(long value) {
        if (value <= 0) {
            throw new IllegalArgumentException("non-positive value");
        }
        super(value);
    }
}
```

---
layout: feature
title: Module Import Declarations
---
<template #badge>
  <JdkVersions v="23" />
</template>

In Java, it is possible to import:

- All classes of a package with the instruction `import java.util.*;`
- A class with the instruction `import java.util.Map;`
- All static methods and variables of a class with the instruction `import static org.junit.jupiter.api.Assertions.*;`
- A static method or variable with the instruction `import static org.junit.jupiter.api.Assertions.assertTrue;`

However, it was not possible to import all classes of a module in a single instruction.

```java
import module java.base;
```

---
layout: section-title
image: https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193493/Picture4.png
---

# New APIs


---

# Disclaimer

I'll focus only on (personal point of view) new APIs that we can use in day-to-day coding.

If you are curious about all the API level differences between Java 8 later versions, check the [AdoptOpenJDK/jdk-api-diff on GitHub](https://github.com/AdoptOpenJDK/jdk-api-diff) or the [The Java Version Almanac](https://github.com/marchof/java-almanac/).


---
layout: feature
title: "`since` and `forRemoval` for `@Deprecated`"
---
<template #badge>
  <JdkVersions v="9" />
</template>

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

- Subscriber: A receiver of data items.

- Subscription: Linkage between a Publisher and a Subscriber.

- Processor: A combination of Publisher and Subscriber for specifying a data-transformation function.

```java
void subscribe(Flow.Subscriber<? super T> subscriber)
```

```java
void onSubscribe(Flow.Subscription subscription)
void onComplete()
void onError(Throwable throwable)
void onNext(T item)
```

```java
void request(long n)
void cancel()
```


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


---
layout: feature
title: Stream &amp; Collectors new APIs
---
<template #badge>
  <JdkVersions v="9" />
</template>

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

`HttpClient`&nbsp;now implements `AutoCloseable`&nbsp;and can therefore be used more easily in a *try-with-resources*&nbsp;block

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

Java collections do not have a type representing an ordered sequence of elements. Java 21 fills this gap by introducing the interfaces `SequencedCollection`, `SequencedSet`, and `SequencedMap`. These interfaces provide methods for adding, modifying, or removing elements at the beginning or end of the collection, as well as iterating over a collection in reverse order.

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


---
layout: feature
title: 😅 😗 😆 🧐 🤫 😱 🥳 😍 😴 🤓 😃
---
<template #badge>
  <JdkVersions v="21" />
</template>

```java
String messageWithEmoji = "Hello Java 21! 😄";
String messageWithoutEmoji = "Hello Java!";

assertTrue(messageWithEmoji.codePoints().anyMatch(Character::isEmoji));
assertFalse(messageWithoutEmoji.codePoints().anyMatch(Character::isEmoji));

String emojiPresentationMessage = "Hello Java 21! 🔥😄";
String nonEmojiPresentationMessage = "Hello Java 21!";

assertTrue(emojiPresentationMessage.codePoints().anyMatch(Character::isEmojiPresentation));
assertFalse(nonEmojiPresentationMessage.codePoints().anyMatch(Character::isEmojiPresentation));

assertTrue(Character.isEmojiModifier(0x1F3FB)); // light skin tone
assertTrue(Character.isEmojiModifier(0x1F3FD)); // medium skin tone
assertTrue(Character.isEmojiModifier(0x1F3FF)); // dark skin tone

assertTrue(Character.isEmojiModifierBase(Character.codePointAt("👍", 0)));
assertTrue(Character.isEmojiModifierBase(Character.codePointAt("👶", 0)));
assertFalse(Character.isEmojiModifierBase(Character.codePointAt("🍕", 0)));

assertTrue(Character.isEmojiComponent(0x200D)); // Zero width joiner
assertTrue(Character.isEmojiComponent(0x1F3FD)); // medium skin tone

assertTrue(Character.isExtendedPictographic(Character.codePointAt("✔️", 0)));  // Checkmark,

String messageWithEmoji = "Hello Java 21! 😄";
Matcher isEmojiMatcher = Pattern.compile("\\p{IsEmoji}").matcher(messageWithEmoji);
    
assertTrue(isEmojiMatcher.find());
```


---
layout: feature
title: Virtual Threads
---
<template #badge>
  <JdkVersions v="21" preview="19, 20" />
</template>

Virtual threads are lightweight threads that dramatically reduce the effort of writing, maintaining, and observing high-throughput concurrent applications.

There are limitations in the current implementation of virtual threads. In some cases, a virtual thread will pin the carrier thread, which will not be able to handle other virtual threads:

- The use of the `synchronized`&nbsp;keyword

- The use of native methods or the Foreign Function API from JEP 424

Due to these limitations, virtual threads are not necessarily the solution to all concurrency problems.

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


---

Structured concurrency API

**JDK21**

(Preview in &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;)

**JDK20**

**JDK19**

Structured concurrency API to define subtask relations between threads to streamline error handling and cancellation, improve reliability, and enhance observability

**OLD JDK**

**JDK21**

- If an error occurs in the `fetchOrder()`&nbsp;method, we will still wait for the `findUser()`&nbsp;task to complete.

- If an error occurs in the `findUser()`&nbsp;method, then the `handle()`&nbsp;method will terminate, but the thread executing `fetchOrder()`&nbsp;will continue to run, resulting in a thread leak.

- If the `handle()`&nbsp;method is interrupted, this interruption is not propagated to the subtasks, and their threads will continue to run, resulting in a thread leak.

```java
ExecutorService ex = Executors.newFixedThreadPool(nbCores);
Response handle() 
  throws ExecutionException, InterruptedException {
    Future<String>  user  = es.submit(() -> findUser());
    Future<Integer> order = es.submit(() -> fetchOrder());
    String theUser  = user.get();   // Join findUser 
    int    theOrder = order.get();  // Join fetchOrder
    return new Response(theUser, theOrder);
}
```

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


---

Foreign linker API and Foreign memory access API

(Preview in &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;)

-
The *foreign linker API* provides a flexible way to access native code on the host machine

- Can replace JNI/JNA

- The *foreign memory access AP*I provides a supported, safe, and efficient API to access both heap and native memory

Only Foreign memory access

**JDK14**

**JDK15**

**JDK16**

**JDK17**

**JDK18**

**JDK19**

**JDK20**

**JDK21**

**JDK22**

Good blog post for pratical use case

[https://blog.arkey.fr/2021/02/20/a-practical-look-at-jep-389-in-jdk16-with-libsodium/](https://blog.arkey.fr/2021/02/20/a-practical-look-at-jep-389-in-jdk16-with-libsodium/)


---

Vector API

**JDK16**

(Preview in &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )

The idea of this API is to provide a means of vector computations that will ultimately be able to perform more optimally (on supporting CPU architectures) than the traditional scalar method of computations.

multiply two arrays

**JDK15**

**JDK17**

**JDK18**

**JDK19**

**JDK20**

**JDK21**

**JDK22**

**JDK23**

```java
int[] a = {1, 2, 3, 4};
int[] b = {5, 6, 7, 8};

var vectorA = IntVector.fromArray(IntVector.SPECIES_128, a, 0);
var vectorB = IntVector.fromArray(IntVector.SPECIES_128, b, 0);
var vectorC = vectorA.mul(vectorB);
vectorC.intoArray(c, 0);
```

```java
int[] a = {1, 2, 3, 4};
int[] b = {5, 6, 7, 8};

var c = new int[a.length];

for (int i = 0; i < a.length; i++) {
    c[i] = a[i] * b[i];
}
```


---

Scoped Values

**JDK21**

(Preview in &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;)

**JDK22**

**JDK23**

**JDK20**

An alternative to ThreadLocal that allows sharing immutable data with limit visibility.

ThreadLocal are mutable and require a complex data structure whose cost is not in line with virtual threads, which are lightweight and inexpensive to create.

```java
private static final ScopedValue<String> USERNAME = ScopedValue.newInstance();

ScopedValue.where(USERNAME, "duke") // bind a value to the scope
    // start a thread that could access this value
    .run(() -> System.out.println("User: " + USERNAME.get()));
```


---

Class-File API

(Preview in &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;)

**JDK22**

**JDK23**

Standard API for parsing, generating, and transforming Java class files.

&nbsp;

The Java ecosystem has many libraries that allow for parsing and generating Java class files: ASM, BCEL, Javassist, etc. Most frameworks that generate bytecode use them.

&nbsp;

The format of Java class files evolves every 6 months with each new Java release, so generation frameworks must evolve at the same time to avoid not supporting the latest language developments.

&nbsp;

The Class-File API addresses this problem by providing an API within the JDK for parsing, generating, and transforming class files.


---

Stream Gatherers

(Preview in &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;)

**JDK22**

**JDK23**

Enhances the Stream API with support for custom intermediate operations.

&nbsp;

The Stream API provides a fixed set of intermediate and terminal operations. It allows extending terminal operations via the `Stream::collect(Collector)`&nbsp;method, but does not allow extending intermediate operations.

```java
var numbers = List.of(1, 2, 3, 4, 5);

var slidingWindows = numbers.stream()
    .gather(Gatherers.windowSliding(3))
    .toList();

System.out.println(slidingWindows);
// [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
```


---
layout: section-title
image: https://media.slid.es/uploads/18162/images/9193429/Picture2.png
---

# Performance


---

General

**JDK16**

- Improvements in the conversion between primitives (e.g., from `long`&nbsp;to `int`) through the use of `VarHandle`.

- Elastic metaspace to return unused HotSpot class-metadata memory to the operating system more promptly

- Enable dynamic archiving of classes at the end of Java application execution

- Class-Data Sharing archive of the default class list is enabled by default to improve out-of-the-box startup time

- Application Class-Data Sharing to improve startup time and reduce footprint by sharing class metadata between Java processes

- Space-efficient, Compact Strings that stores Latin-1 only Strings more efficiently

- Code caches of profiled and non-profiled compiled code is separated, resulting in improved performance and memory footprint

- Store Interned Strings in Class-Data Sharing archives to reduce memory consumption

**JDK13**

**JDK12**

**JDK10**

**JDK9**

**JDK9**

**JDK9**

**JDK21**


---

GC

**JDK18**

**JDK18**

**JDK12**

**JDK10**

**JDK9**

**JDK15**

**JDK11**

**JDK12**

**JDK14**

**JDK16**

**JDK20**

**JDK22**

**JDK23**

**JDK21**

- Parallel GC has been the replacement of the existing Full GC algorithm with a more traditional parallel Mark-Sweep-Compact algorithm. Reduces heap usage by 1.5%.

- Generational ZGC (using `-XX:+ZGenerational`&nbsp;or by default since &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;).

- SerialGC, ParallelGC and ZGC now supports String Deduplication.

- Z Garbage Collector, offering very low pause times on large heaps.

- Shenandoah Garbage Collector, offering similar benefits as ZGC but based on a different algorithm.

- Epsilon Garbage Collector, which does not implement actual memory reclamation, striving for the lowest overhead possible.

- G1 Garbage Collector is now the default instead of Parallel GC.

- Parallel Full GC to improve worst-case latencies.

- Automatically return heap memory to the operating system when idle.

- Abortable mixed collections to meet user-supplied pause goals.

- NUMA-Aware Memory Allocation.

- Allow G1 Heap Regions up to 512MB.

- Reduces G1 native memory footprint by ~1.5% of Java heap size by removing one of the mark bitmaps spanning the entire Java heap.

- Remove the use of the GCLocker in G1. Improving JNI use cases.

**JDK23**


---
layout: section-title
image: https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193520/Picture6.png
---

# Security


---

General

**JDK18**

**JDK18**

**JDK17**

- Use `java -XshowSettings:security`&nbsp;to view the security-related configuration information of the JVM.

- Support for Leighton-Micali Signature (LMS) signature verification and PBES2 cryptographic algorithms.

- Key Encapsulation Mechanism (KEM) API, a cryptographic technique for securing symmetric keys using public-key cryptography.

- The cacerts keystore file is now a passwordless PKCS12 file.

- Calling keyStore.store(outputStream, null) on a PKCS12 KeyStore creates a passwordless PKCS12 file.

- Validate Incoming Serialization Data.

- Edwards-Curve Digital Signature Algorithm (EdDSA).

- TLS 1.3 support.

- Key Agreement with Curve25519 and Curve448.

- ChaCha20 and Poly1305 Cryptographic Algorithms.

- Default set of root Certification Authority (CA) certificates are provided with the JDK, so TLS connections are working out of the box.

- Default keystore type is the standard PKCS12 instead of the proprietary JKS.

- DRBG-Based SecureRandom.

- Disable X.509 certificate chains with SHA-1 based signatures.

- SHA-3 Hash Algorithms.

**JDK11**

**JDK10**

**JDK9**

**JDK9**

**JDK9**

**JDK15**

**JDK11**

**JDK11**

**JDK9**

**JDK21**

**JDK21**

**JDK22**


---
layout: section-title
image: https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193495/Picture5.png
---

# Miscellaneous


---

Launching and tools

- Launch Multi-File Source-Code Programs.

- Flight Recorder Event Streaming: profiling data is available via an API, making it suitable for continuous monitoring.

- Microbenchmark Suite based on JMH.

- Flight Recorder is part of OpenJDK.

- Low-Overhead Heap Profiling via JMTI.

- Launch Single-File Source-Code Programs, including support for shebang (#!) line on Unix.

- jshell: the Java REPL.

**JDK14**

**JDK9**

**JDK11**

**JDK11**

**JDK11**

**JDK12**

**JDK22**


---

Packaging

- javac now assumes that source files are encoded with the new default UTF-8 charset

- Packaging Tool to create self-contained applications, also supporting native package formats: msi, exe, pkg, dmg, deb and rpm

- jlink Java Linker that can build an optimized, slim run-time image for a modular Java application that contains only the required parts of the JDK

- Multi-Release JAR Files to allow multiple, Java-release-specific versions of class in a single archive

**JDK16**

**JDK9**

**JDK9**

**JDK18**


---

Javadoc

- The Javadoc tool now emits HTML5 markup instead of a frame-based layout and the documentation contains a search box to ease navigation

-
@snippet tag, a modern alternative for @code that supports multi-line code, supports styling and the inclusion of external snippets

**JDK9**

**JDK18**

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


---

New supported platforms

- Linux/RISC-V

- macOS/AArch64

- Alpine

- Windows/AArch64

- Linux/AArch64

- Linux/s390x

- Unified arm32/arm64

**JDK9**

**JDK16**

**JDK16**

**JDK9**

**JDK9**

**JDK17**

**JDK19**


---

New release train

**JDK9**


---

Simple web server

jwebserver command line utility to serve static files
(similar to Python’s SimpleHTTPServer or PHP's php -S, for development and education purposes)

**JDK18**


---

Markdown Documentation Comments

**JDK23**

**JDK23**

**OLD JDK**

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


---
layout: section-title
image: https://s3.amazonaws.com/media-p.slid.es/uploads/18162/images/9193534/Picture7.png
---

# Deprecations &amp; Removals


---

Syntax

- Deprecate the constructors of primitive wrapper classes

- var is no longer a valid class name

- Underscore is no longer a valid identifier (new keyword)

**JDK9**

**JDK10**

**JDK16**


---

Projects

- Remove [RMI Activation](https://docs.oracle.com/javase/9/docs/specs/rmi/activation.html), affecting the java.rmi.activation package and the rmid tool, does not affect Java RMI in general

- Remove the Nashorn Javascript Engine and the jjs tool

- Remove Java EE

- Remove CORBA

**JDK11**

**JDK11**

**JDK15**

**JDK15**

(deprecated &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; )

**JDK17**


---

API

**JDK17**

**JDK17**

**JDK18**

**JDK18**

**JDK9**

**JDK15**

**JDK11**

-
`Remove&nbsp;Thread.resume()`, `Thread.suspend()`, `ThreadGroup.resume()`, `ThreadGroup.stop()`&nbsp;and `ThreadGroup.suspend()`.

- Deprecate the Memory-Access Methods in sun.misc.Unsafe for **removal**. In total, more than 79 out of the 87 methods in the `Unsafe`&nbsp;class are affected.

- The constructors of the `Locale`&nbsp;class have been deprecated. Instead use `Locale.of()`.

- Deprecate Thread.stop for **removal**.

- Deprecate Finalization for **removal**.

- Strongly encapsulate internal API’s (sun.*) except for [critical APIs](https://openjdk.java.net/jeps/260#Description)&nbsp;such as sun.misc.Unsafe.
Remove the option for [relaxed strong encapsulation](https://openjdk.java.net/jeps/261#Relaxed-strong-encapsulation)&nbsp;via the [--illegal-access launcher option](https://openjdk.java.net/jeps/396#Description).

- Deprecate Applet API (java.applet.*, javax.swing.JApplet and java.beans.AppletInitializer) for **removal**.

- Deprecate Unsafe::defineAnonymousClass().

-
**Remove**&nbsp;Thread.destroy() and Thread.stop(Throwable).

-
**Remove**&nbsp;apple.applescript and com.apple packages.

**JDK19**

**JDK23**

**JDK23**


---

Tools

**JDK10**

**JDK14**

- Remove the jjs tool (linked to Nashorn)

- Remove the Pack200 Tools and API

- Remove the javah tool

- Remove the jhat tool

- Remove the JVM TI hprof Agent

- Remove rt.jar from the JRE

**JDK9**

**JDK9**

**JDK9**

**JDK11**

(deprecated &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; )

**JDK11**

(deprecated &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; )

**JDK15**


---

Security

- JARs signed with SHA-1 algorithms are now restricted by default and treated as if they were unsigned

- Deprecate the Security Manager for Removal
Work ongoing to consider use cases where the Security Manager is useful and provide alternatives (e.g. [JDK-8199704](https://bugs.openjdk.java.net/browse/JDK-8199704))

- Disable X.509 certificate chains with SHA-1 based signatures

**JDK9**

**JDK18**

**JDK17**


---

Platform

- Deprecate the Windows 32-bit x86 Port for **removal**.
Windows 10, the last Windows operating system to support 32-bit operation, will reach End of Life in October 2025

- Remove the Solaris and SPARC Ports

**JDK15**

**JDK21**


---

GC

**JDK14**

- Remove the Concurrent Mark Sweep (CMS) Garbage Collector

- Deprecate the ParallelScavenge + SerialOld GC Combination

- Remove GC Combinations Deprecated in JDK 8

**JDK9**

**JDK9**

(deprecated &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; )

**JDK14**


---

CLI flags

- Disable [Biased Locking](https://stackoverflow.com/questions/9439602/biased-locking-in-java) by default, deprecate related command-line flags

- Remove Launch-Time JRE Version Selection directives: JRE-Version manifest entry and -version: cli option

**JDK9**

**JDK15**


---

Misc

**JDK17**

- Prepare to Disallow the Dynamic Loading of Agents to improve the integrity and security of the platform

- Make floating-point operations consistently strict by default, warn when the strictfp modifier is used

- Remove the Experimental [AOT](https://openjdk.java.net/jeps/295)&nbsp;and [JIT](https://openjdk.java.net/jeps/317)&nbsp;compiler due to lack of interest

- Remove the Endorsed Standards Override (lib/endorsed) and Extensions (lib/ext) mechanisms from the JRE

**JDK9**

**JDK15**

**JDK21**
