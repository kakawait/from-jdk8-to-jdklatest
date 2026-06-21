---
layout: section-title
image: /images/new-language-features.png
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
<JdkVersions v="9" />

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

<JdkLinkedCodeBlocks label1="JDK6" label2="JDK7" codeClass="text-[11px]">
  <template #code1>

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

  </template>
  <template #code2>

```java
try (BufferedReader br = new BufferedReader(...)) {
    return br.readLine();
}
```

  </template>
</JdkLinkedCodeBlocks>

<div class="mt-3 text-[13px]">
  in the Java 7 version, if you already have a variable that you want to handle with this construct, you had to introduce a dummy variable.

  To mitigate these criticisms, try-with-resources was enhanced to handle final or effectively final local variables in addition to newly created ones:
</div>

<div class="mt-1 flex justify-center text-[11px]">

```java
BufferedReader br1 = new BufferedReader(...);
BufferedReader br2 = new BufferedReader(...);
try (br1; br2) {
    System.out.println(br1.readLine() + br2.readLine());
}
```
</div>

---
layout: feature
title: Diamond operator for anonymous inner classes
---
<template #badge>
  <JdkVersions v="9" />
</template>

<JdkCodeBlock label="JDK8" color="#d0e0e3" textColor="#0e2a47" borderColor="#007bff" class="text-[11px]">

```java
List<Integer> numbers = new ArrayList<>();
```

</JdkCodeBlock>


However, this feature did not work with anonymous inner classes before.

With Java 9, this small rough edge is removed, making the operator more universally applicable



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
---
<template #badge>
  <JdkVersions v="11" preview="10" prefix="(Without lambda support in" suffix=")" />
</template>

::title::
Local-Variable Type Inference

::default::

<div class="text-center">

Probably the most significant language improvement since Java 8 is the addition of the var keyword. It was initially introduced in [Java 10](https://openjdk.java.net/jeps/286), and was further improved in [Java 11](https://openjdk.java.net/jeps/323).

This feature allows us to reduce the ceremony of a local variable declaration by omitting the explicit type specification:

<div class="flex justify-center my-4">

```java
var greetingMessage = "Hello, I'm batman!";
var map = new HashMap<>();
```

</div>

<JdkAlert image="/images/alert-warning.png">

### Make sure to read the official style guides

### Official [style guide](https://openjdk.java.net/projects/amber/LVTIstyle.html) and [FAQ](https://openjdk.java.net/projects/amber/LVTIFAQ.html) about `var`

</JdkAlert>

</div>

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
  <JdkVersions v="15" preview="14" prefix="(Enabled with -XX:+ShowCodeDetailsInExceptionMessages in" suffix=")" />
</template>

<JdkLinkedCodeBlocks label1="OLD" label2="JDK15" direction="vertical" size="small" codeClass="text-[10px]">
  <template #code1>

```java
node.getElementsByTagName("name").item(0).getChildNodes().item(0).getNodeValue();

---
Exception in thread "main" java.lang.NullPointerException
        at Unlucky.method(Unlucky.java:83)
```

  </template>
  <template #code2>

```java
node.getElementsByTagName("name").item(0).getChildNodes().item(0).getNodeValue();
---
Exception in thread "main" java.lang.NullPointerException:
  Cannot invoke "org.w3c.dom.Node.getChildNodes()" because
  the return value of "org.w3c.dom.NodeList.item(int)" is null
        at Unlucky.method(Unlucky.java:83)
```

  </template>
</JdkLinkedCodeBlocks>


---
layout: feature
title: Text Blocks
---
<template #badge>
  <JdkVersions v="15" preview="13, 14" />
</template>

<JdkLinkedCodeBlocks label1="JDK12" label2="JDK15" size="small">
  <template #code1>

```java
String html = "";
html += "<html>\n";
html += "  <body>\n";
html += "    <p>Hello, world</p>\n";
html += "  </body>\n";
html += "</html>\n";

System.out.println(html);
```

  </template>
  <template #code2>

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

  </template>
</JdkLinkedCodeBlocks>

<JdkAlert image="/images/alert-warning.png" class="mt-4">

### No variables interpolation

</JdkAlert>

---
layout: feature
title: Pattern Matching for instanceof
---
<template #badge>
  <JdkVersions v="16" preview="14, 15" />
</template>

<JdkLinkedCodeBlocks label1="JDK13" label2="JDK16" size="small">
  <template #code1>

```java
if (obj instanceof String s) {
    // use s
}
```

  </template>
  <template #code2>

```java
if (obj instanceof String s && s.length() > 5) {
  // use s
}
```

  </template>
</JdkLinkedCodeBlocks>

can be used in the second part of the condition because it’s only evaluated when the first one succeeds and the `instanceof` operator has a match

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

```java
public record Point(int x, int y) { }

var point = new Point(1, 2);
point.x(); // returns 1
point.y(); // returns 2
```

Java 16 improves on this, as now it’s also possible to define **Local Records** in a method body:

<JdkCodeWithText class="mt-4" codeClass="text-[11px]">
  <template #code>

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

  </template>

  This feature is useful to perform intermediate calculations on data, without having to declare a class that would only be used in this method.
</JdkCodeWithText>
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

Record Patterns extends the pattern matching capabilities of Java beyond simple type patterns to **match and deconstruct Record values**. It **supports nesting** to enable declarative, data focused programming.

```java
interface Point { }
record Point2D(int x, int y) implements Point { }
enum Color { RED, GREEN, BLUE }
record ColoredPoint(Point p, Color c) { }

Object r = new ColoredPoint(new Point2D(3, 4), Color.GREEN);
```

<JdkLinkedCodeBlocks label1="JDK16" label2="JDK21" size="small" codeClass="text-[11px]">
  <template #code1>

```java
if (r instanceof ColoredPoint cp 
  && cp.p() instanceof Point2D pt) {
    int x = pt.x();
    int y = pt.y();
    Color c = cp.c();

    // work with x, y, and c
}
```

  </template>
  <template #code2>

```java
if (r instanceof ColoredPoint(Point2D(int x, int y), Color c)) {
  // work with x, y, and c
}

var length = switch (r) {
	case ColoredPoint(Point2D(int x, int y), Color c) -> Math.sqrt(x*x + y*y);
	case ColoredPoint(Point p, Color c) -> 0;
}
```

  </template>
</JdkLinkedCodeBlocks>

---
layout: feature
title: Unnamed Patterns and Variables
---
<template #badge>
  <JdkVersions v="22" preview="21" />
</template>

now it's possible to use the underscore character wherever a variable name would be used. However, it's not a regular variable name: it means "don't care" as **underscore can be redeclared, and can not be referenced**

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

**unnamed patterns** which can be used in pattern matching to ignore subpatterns

<JdkLinkedCodeBlocks label1="JDK20" label2="JDK22" size="small" codeClass="text-[11px]">
  <template #code1>

```java
if (r instanceof ColoredPoint(Point(int x, int y), Color c)) {
  // do something with x and y, but c is not needed
}
```

  </template>
  <template #code2>

```java
if (r instanceof ColoredPoint(Point(int x, int y), _)) {
  // ... x ... y ...
}
```

  </template>
</JdkLinkedCodeBlocks>

---
layout: feature
title: String template
---
<template #badge>
<div class="flex items-center gap-1 text-[12px] font-bold">
<span class="opacity-80 text-[10px] font-bold tracking-wider mr-0 text-gray-400"">(PREVIEW IN</span>
<JdkBadge label="JDK21" size="small" />
<JdkBadge label="JDK22" size="small" />
<span class="opacity-80 text-[10px] font-bold tracking-wider ml-0 text-gray-400"">)</span>
<span class="opacity-80 text-[10px] font-bold tracking-wider text-gray-400"">⚠️ Removed from</span>
<JdkBadge label="JDK23" size="small" />
</div>
</template>

<div class="text-center text-[14px] mb-4 leading-relaxed">
String Templates are an extension to the single-line String literals and Text Blocks,<br>
allowing String interpolation and much more.
</div>

<JdkCodeBlock label="OLD JDK" color="#e3ead1" textColor="#0e2a47" borderColor="#a0a88a" size="small" contentClass="text-[10px]" class="mb-4">

```java
var name = "Thibaud";
var info = "My name is " + name;
info = new StringBuilder().append("My name is ").append(name);
// java 15
info = "My name is %s".formatter(name);
```

</JdkCodeBlock>

<div class="grid grid-cols-[1fr_1.3fr] gap-4">
<div>
<JdkCodeBlock label="JDK22" size="small" contentClass="text-[11px]" class="mb-4">

```java
var name = "Thibaud";
var info = STR."My name is \{name}";
```

</JdkCodeBlock>

<div class="flex items-center justify-center w-full bg-white p-2 rounded-xl shadow-sm border border-gray-200 overflow-hidden">

<script setup>
import stringTemplateSvg from '../assets/images/string-template-syntax.svg'
</script>

<img :src="stringTemplateSvg" class="w-full h-auto" />

</div>

<div class="text-[13px] font-bold mt-2">
Built-in processors: <span class="bg-gray-800 px-1 rounded">STR</span>, <span class="bg-gray-800 px-1 rounded">FMT</span>, <span class="bg-gray-800 px-1 rounded">RAW</span>
</div>
</div>

<div>
<JdkCodeBlock label="JDK22" size="small" contentClass="text-[11px]">

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

</JdkCodeBlock>
</div>
</div>

---
layout: feature
title: Unnamed Classes and Instance Main Methods
---
<template #badge>
  <JdkVersions v="25" preview="21, 22, 23, 24" />
</template>

In old Java versions, one needed write quite some boilerplate code even for the simplest of the applications:

<JdkCodeBlock label="OLD JDK" color="#e3ead1" textColor="#0e2a47" borderColor="#a0a88a" size="small" contentClass="text-[12px]">

```java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, World!");
  }
}
```

</JdkCodeBlock>

<div class="grid grid-cols-2 gap-8 mt-2">
<div>
<h3 class="text-[15px] font-bold mb-1">1. A more tolerant launch protocol</h3>
<p class="text-[12px] leading-tight mb-2 opacity-90">
Instance main methods makes the Java launch protocol more flexible, by making some aspects of the main method optional.
</p>
<JdkCodeBlock size="small" contentClass="text-[11px]">

```java
class HelloWorld {
  void main() {
    System.out.println("Hello, World!");
  }
}
```

</JdkCodeBlock>
</div>

<div>
<h3 class="text-[15px] font-bold mb-1 text-right">2. Unnamed classes</h3>
<p class="text-[12px] leading-tight mb-2 opacity-90 text-right">
Methods to exist outside of an enclosing class in which case they are automatically wrapped into a synthetic unnamed class.
</p>
<div class="flex gap-2">
<JdkCodeBlock label="JDK22" color="#710070" size="small" contentClass="text-[11px]" class="flex-1">

```java
void main() {
  System.out.println("Hello, World!");
}
```

</JdkCodeBlock>
<JdkCodeBlock label="JDK23" color="#854800" size="small" contentClass="text-[11px]" class="flex-1">

```java
void main() {
  println("Hello, World!");
}
```

</JdkCodeBlock>
</div>
</div>
</div>

---
layout: feature
title: Flexible Constructor Bodies
---
<template #badge>
  <JdkVersions v="25" preview="22, 23, 24" />
</template>

Allows instructions before the call to the parent constructor (super) as long as they do not access the instance being created. JDK 24 now allows **initialized fields** of the class to be accessed before `super()`.

<JdkLinkedCodeBlocks direction="vertical" size="small" codeClass="text-[12px]" arrowHeight="h-8">
  <template #code1>

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

  </template>
  <template #code2>

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

  </template>
</JdkLinkedCodeBlocks>

---
layout: feature
title: Module Import Declarations
---
<template #badge>
  <JdkVersions v="25" preview="23, 24" />
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
layout: feature
title: Prepare to Make Final Mean Final
---
<template #badge>
  <JdkVersions v="26" />
</template>

Restricts the ability to modify **final** fields via deep reflection. In Java 26, attempting to use `setAccessible(true)` on a final field will trigger a runtime warning, preparing for a future release where such mutations will be blocked by default.

```java
// This code will trigger a WARNING in Java 26
Field f = MyClass.class.getDeclaredField("someFinalField");
f.setAccessible(true);
f.set(instance, newValue); 

// Output: WARNING: Final field someFinalField in class MyClass 
// has been mutated reflectively...
```

<div class="mt-4 text-[13px] opacity-80">
Goal: Improve JVM integrity, security, and allow for better JIT optimizations like constant folding.
</div>

---
layout: feature
title: Primitive Types in Patterns, instanceof, and switch
---
<template #badge>
  <JdkVersions preview="23, 24, 25, 26" />
</template>

Allows primitive types to be used in pattern matching, `instanceof`, and `switch`. It also enables **primitive type patterns** to be used in record patterns.

<JdkLinkedCodeBlocks label1="OLD" label2="JDK24" size="small" codeClass="text-[10px]">
  <template #code1>

```java
if (obj instanceof Integer) {
    int i = (Integer) obj;
    // work with i
}
```

  </template>
  <template #code2>

```java
if (obj instanceof int i) {
    // work with i
}

switch (obj) {
    case int i -> System.out.println("int: " + i);
    case double d -> System.out.println("double: " + d);
    default -> System.out.println("other");
}
```

  </template>
</JdkLinkedCodeBlocks>

---
layout: feature
title: Lazy Constants (formerly Stable Values)
---
<template #badge>
  <JdkVersions preview="25, 26" />
</template>

Formerly known as **StableValue**, this API allows for constants that are initialized on demand rather than at startup, improving application startup performance.

```java
private static final StableValue<String> CONFIG = StableValue.newInstance();

public String getConfig() {
    return CONFIG.computeIfAbsent(() -> loadConfig());
}
```
