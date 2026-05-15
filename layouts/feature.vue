<template>
  <div class="slidev-layout feature h-full px-16 py-10 bg-[#111]">
    <div class="flex justify-end items-center gap-6 mb-8">
      <div class="flex items-center">
        <slot name="badge" />
      </div>
      <div class="flex flex-col items-end">
        <h1 class="text-3xl font-bold text-white m-0 leading-none">
          <slot name="title">{{ $frontmatter.title }}</slot>
        </h1>
        <div class="w-full h-[1px] bg-[#48FFD5] mt-2"></div>
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
}

.feature h1 :deep(p) {
  margin: 0;
  display: inline;
}
</style>
