# Slidev Migration Guidelines

This document provides context and instructions for agents assisting in the migration of the Java presentation from Reveal.js to Slidev.

## 1. Project Overview
- **Source**: Original slides were created using [slides.com](https://slides.com), a WYSIWYG editor for Reveal.js.
- **Source Location**: Original files are in the `../revealjs/` directory (if available) or hosted on `:3031`.
- **Target**: A modern, maintainable Slidev project using Vue components and idiomatic CSS.

## 2. Core Mandates for Conversion
- **Do Not Literal-Convert**: The original HTML/CSS from slides.com is "crap"—it uses absolute positioning, nested `<div>` soup, and inline styles. 
- **Be Idiomatic**: 
    - Use **CSS Grid** and **Flexbox** for layouts.
    - Extract repeating elements into reusable **Vue Components** (e.g., `JdkBadge`, `JdkTimeline`).
    - Use **Slidev Layouts** (in `layouts/`) for consistent slide structures.
- **Visual Fidelity**: Maintain the "same visual aspect" (colors, typography, general feel) but without the technical debt of the original source.

## 3. Tooling & Comparison
- **Visual Validation**: `playwright-cli` is installed system-wide. Use it to compare the two versions.
- **Ports**:
    - **Slidev (New)**: `http://localhost:3030` (Start with `pnpm run dev`).
    - **Reveal.js (Old)**: `http://localhost:3031` (Start with `python3 -m http.server 3031` in the original project folder).
- **Comparison Strategy**:
    - Use `playwright-cli eval` to inspect the old HTML structures and styles.
    - Use `playwright-cli screenshot` to take visual snapshots of both versions for comparison when raw HTML inspection isn't enough to verify alignment or spacing.

## 4. Specific Components
- **JdkBadge**: Use this component for all JDK version indicators. It automatically handles colors based on the version label.
