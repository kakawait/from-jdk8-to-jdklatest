# Slidev JDK Evolution Agent Instructions

You are an expert at creating and maintaining the "From JDK 9 to JDK Latest" Slidev project. This project tracks Java language features, APIs, and changes from JDK 9 onwards.

## Project Context
- **Tech Stack:** [Slidev](https://sli.dev/), Vue 3, TypeScript, Tailwind CSS.
- **Goal:** Provide a comprehensive, visually consistent overview of JDK evolution.
- **Current Status:** Updated up to JDK 23. Tasked with adding JDK 24, 25, and 26.

## Slide Structure
The project uses multiple Markdown files imported into `slides.md`:
- `pages/new-language-features.md`: Syntax and language changes.
- `pages/new-apis.md`: Library and standard API additions.
- `pages/performance.md`: GC improvements, JIT changes, etc.
- `pages/security.md`: Security-related changes.
- `pages/miscellaneous.md`: Tools (jlink, jpackage), etc.
- `pages/deprecations-removals.md`: Features marked for removal or removed.

## Core Components & Usage

### 1. `JdkVersions`
Used to display version badges at the top of a feature slide.
```vue
<template #badge>
  <JdkVersions v="23" preview="22" />
</template>
```
- `v`: The version(s) where the feature is stable (comma-separated).
- `preview`: The version(s) where it was in preview/incubation.

### 2. `JdkLinkedCodeBlocks`
Used for side-by-side or vertical comparisons between versions.
```vue
<JdkLinkedCodeBlocks label1="JDK8" label2="JDK16" size="small">
  <template #code1>
    ```java
    // Old way
    ```
  </template>
  <template #code2>
    ```java
    // New way
    ```
  </template>
</JdkLinkedCodeBlocks>
```

### 3. `JdkCodeBlock`
A styled code block with a version label.
```vue
<JdkCodeBlock label="JDK21" color="#4acaec">
  ```java
  // code
  ```
</JdkCodeBlock>
```

### 4. `JdkAlert`
For warnings or important notes.
```vue
<JdkAlert image="/images/alert-warning.png">
  ### Warning title
  Warning content.
</JdkAlert>
```

## Adding New JDK Versions (24, 25, 26)

### Step 1: Update Configuration
1.  **`components/jdk-utils.ts`**: Add unique colors for the new versions to `jdkColors`.
2.  **`components/JdkTimeline.vue`**: Add the new versions to the `modernColumns` array with their release and EOL dates.

### Step 2: Research & Implementation
1.  **Research:** Use Google Search or official OpenJDK JEPs to find features for JDK 24, 25, and 26.
2.  **Categorize:** Assign features to the correct `pages/*.md` file.
3.  **Draft Slides:** Use the `feature` layout and appropriate components.
    - Always include `<template #badge><JdkVersions ... /></template>`.
    - Use code snippets to demonstrate the feature.
    - Add presenter notes if useful.

### Step 3: Visual Consistency
- Ensure code snippets are concise.
- Use `JdkLinkedCodeBlocks` for "Before vs. After" scenarios.
- Keep descriptions brief and focused on the value of the feature.

## Skill Integration
Utilize the `slidev` skill for:
- Exporting to PDF (`slidev export`).
- Starting the dev server (`slidev dev`).
- Understanding base Slidev features (animations, layouts).

## Standard Layouts
- `section-title`: Used for category headers.
- `feature`: Used for individual feature slides.
- `section`: Used for sub-sections.
