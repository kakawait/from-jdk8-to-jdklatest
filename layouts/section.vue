<template>
  <div class="section-layout h-full grid grid-cols-[1fr_1.5fr] items-center px-20 bg-[#111]">
    <div class="flex justify-center items-center">
      <img :src="image" class="w-full max-h-100 object-contain" />
    </div>
    <div class="flex flex-col items-start text-left">
      <slot />
      <div class="w-full h-1px bg-[#48FFD5] mt-4"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  image: string
}>()
</script>

<style>
.section-layout h1 {
  color: #48FFD5 !important;
  font-family: 'Montserrat', 'Helvetica', sans-serif;
  font-size: 5rem !important;
  line-height: 1.2;
  margin: 0 !important;
  font-weight: 700;
  text-transform: none !important;
}
</style>
