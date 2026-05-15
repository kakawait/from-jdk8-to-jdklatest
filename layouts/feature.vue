<template>
  <div class="slidev-layout feature h-full px-12 py-6 bg-[#111]">
    <div class="flex justify-end items-center gap-4 mb-4">
      <div class="flex items-center">
        <slot name="badge" />
      </div>
      <div class="flex flex-col items-end max-w-xl">
        <h1 class="font-bold text-white m-0 leading-tight text-right">
          <slot name="title">{{ $frontmatter.title }}</slot>
        </h1>
        <div class="w-full h-[1px] bg-[#48FFD5] mt-1"></div>
      </div>
    </div>
    <div class="feature-content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.feature h1 {
  font-family: 'Montserrat', sans-serif;
  letter-spacing: -0.02em;
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.feature h1 :deep(p) {
  margin: 0;
  display: inline;
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}
</style>
