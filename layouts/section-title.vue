<template>
  <div class="section-title-layout h-full grid grid-cols-2 items-center px-25 bg-[#111]">
    <div class="flex justify-center items-center">
      <img :src="image" class="w-60 h-60 object-contain" />
    </div>
    <div class="flex flex-col items-start text-left pl-10">
      <h1 class="text-white text-5xl font-bold leading-tight mb-2">
        <slot />
      </h1>
      <div class="w-20 h-[2px] bg-[#48FFD5]"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  image: string
}>()
</script>

<style scoped>
.section-title-layout h1 {
  font-family: 'Montserrat', sans-serif;
  text-transform: none !important;
}
</style>
