---
title: From jdk8 to jdk27
theme: default
colorSchema: dark
# Pin the fonts: the theme default is "Avenir Next,Nunito Sans", and Avenir Next
# only exists on macOS, so the deck rendered different fonts per OS. Both fonts
# are self-hosted from /fonts (see styles/index.css), hence provider: none.
fonts:
  sans: Nunito Sans
  mono: Fira Code
  provider: none
background: /images/background.png
class: text-white text-left
highlighter: shiki
lineNumbers: false
favicon: /favicon.ico
info: |
  From jdk8 to jdklatest
  Thibaud LEPRETRE
addons:
  - fancy-arrow
---

<div class="absolute top-[3.5rem]">
  <h1 class="!text-7xl !leading-tight font-bold">
    From <span class="bg-gradient-to-r from-[#00d4ff] to-[#00ffcc] bg-clip-text text-transparent">JDK8</span> to <span class="bg-gradient-to-r from-[#a855f7] to-[#d8b4fe] bg-clip-text text-transparent">JDK27</span>
  </h1>
  <div class="mt-4">
    <p class="text-4xl font-semibold text-[#60a5fa] opacity-90">The journey of innovation</p>
  </div>
  <p class="mt-10 text-sm font-light opacity-70 uppercase tracking-[0.3em]">
    Thibaud LEPRETRE
  </p>
</div>


---
layout: full
---

<JdkTimeline />


---
src: ./pages/toc.md
---

---
src: ./pages/new-language-features.md
---

---
src: ./pages/new-apis.md
---

---
src: ./pages/performance.md
---

---
src: ./pages/security.md
---

---
src: ./pages/miscellaneous.md
---

---
src: ./pages/deprecations-removals.md
---

---
src: ./pages/thank-you.md
---
