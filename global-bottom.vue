<script setup lang="ts">
import { useNav } from '@slidev/client'
import { watchEffect, nextTick, ref, watch } from 'vue'
import { useRouter } from 'vue-router'

const { slides, go, currentSlideNo } = useNav()
const router = useRouter()

const prevSlideNo = ref(currentSlideNo.value)

function extractJdkVersions(slide: any): number[] {
  const versions: number[] = []
  
  const metaSlide = slide.meta?.slide || {}
  const text = (metaSlide.raw || '') + 
               (metaSlide.content || '') + 
               (slide.raw || '') + 
               (slide.content || '') +
               (slide.meta?.slide?.frontmatterRaw || '')
  
  if (!text) return []

  const componentRegex = /(?:v|label|preview)\s*=\s*["']([^"']+)["']/g
  let match
  while ((match = componentRegex.exec(text)) !== null) {
    const parts = match[1].split(',')
    parts.forEach(p => {
      const cleaned = p.trim().replace(/JDK/i, '').trim()
      const v = parseInt(cleaned)
      if (!isNaN(v)) versions.push(v)
    })
  }

  const jsRegex = /jdk\s*:\s*["']?([^"',\s}]+)["']?/g
  while ((match = jsRegex.exec(text)) !== null) {
    const cleaned = match[1].trim().replace(/JDK/i, '').trim()
    const v = parseInt(cleaned)
    if (!isNaN(v)) versions.push(v)
  }

  const generalRegex = /\b(?:JDK|Java)\s*(\d+)\b/gi
  while ((match = generalRegex.exec(text)) !== null) {
    const v = parseInt(match[1])
    if (!isNaN(v)) versions.push(v)
  }

  if (/\bOLD\s+JDK\b|\bOLD\b/i.test(text)) {
    versions.push(8)
  }

  const frontmatter = metaSlide.frontmatter || slide.frontmatter || {}
  if (frontmatter.jdk) {
    const v = parseInt(String(frontmatter.jdk).replace(/JDK/i, ''))
    if (!isNaN(v)) versions.push(v)
  }

  return [...new Set(versions)]
}

// Separate effect for calculation to avoid recursive triggers
watchEffect(() => {
  const queryValue = router.currentRoute.value?.query?.startsFrom as string
  if (!slides.value || slides.value.length === 0) return

  const totalSlides = slides.value.length
  const minJdk = queryValue ? parseInt(queryValue.toLowerCase().replace('jdk', '')) : null

  // Reset and Re-calculate
  slides.value.forEach((slide, index) => {
    const slideNo = index + 1
    const metaSlide = slide.meta?.slide || {}
    const frontmatter = metaSlide.frontmatter || slide.frontmatter || {}
    const layout = slide.meta?.layout || frontmatter.layout

    if (frontmatter) {
      frontmatter.disabled = false
      frontmatter.hide = false
    }

    if (minJdk === null || isNaN(minJdk)) return

    if (slideNo <= 3 || slideNo > totalSlides - 2) return

    const versions = extractJdkVersions(slide)
    const isFeature = layout === 'feature'
    const hasVersion = versions.length > 0
    
    if (isFeature || hasVersion) {
      const maxJdk = hasVersion ? Math.max(...versions) : -1
      if (maxJdk !== -1 && maxJdk < minJdk) {
        frontmatter.disabled = true
        frontmatter.hide = true
      }
    }
  })

  if (minJdk !== null && !isNaN(minJdk)) {
    let currentSectionSlide: any = null
    let hasVisibleContent = false

    slides.value.forEach((slide, index) => {
      const slideNo = index + 1
      const metaSlide = slide.meta?.slide || {}
      const frontmatter = metaSlide.frontmatter || slide.frontmatter || {}
      const layout = slide.meta?.layout || frontmatter.layout
      
      const isSectionTitle = layout === 'section-title'
      const isDisabled = frontmatter.disabled

      if (isSectionTitle) {
        const isLastSection = slideNo > totalSlides - 2
        if (currentSectionSlide && !hasVisibleContent) {
          const f = currentSectionSlide.meta?.slide?.frontmatter || currentSectionSlide.frontmatter
          if (f) {
            f.disabled = true
            f.hide = true
          }
        }
        currentSectionSlide = isLastSection ? null : slide
        hasVisibleContent = false
      } else if (!isDisabled) {
        const versions = extractJdkVersions(slide)
        if (layout === 'feature' || versions.length > 0) {
          hasVisibleContent = true
        }
      }
    })
    
    if (currentSectionSlide && !hasVisibleContent) {
      const f = currentSectionSlide.meta?.slide?.frontmatter || currentSectionSlide.frontmatter
      if (f) {
        f.disabled = true
        f.hide = true
      }
    }
  }
})

// Handle Redirection with direction awareness
watch(currentSlideNo, async (newVal, oldVal) => {
  const direction = newVal > oldVal ? 1 : -1
  prevSlideNo.value = newVal

  await nextTick()
  const current = slides.value[newVal - 1]
  const currentF = current?.meta?.slide?.frontmatter || current?.frontmatter
  
  if (currentF?.disabled) {
    if (direction === 1) {
      // Navigating forward, find next valid slide
      const nextIdx = slides.value.findIndex((s, i) => i >= newVal && !(s.meta?.slide?.frontmatter?.disabled || s.frontmatter?.disabled))
      if (nextIdx !== -1) {
        go(nextIdx + 1)
      } else {
        // Fallback to previous valid if no next valid found
        const prevIdx = [...slides.value].reverse().findIndex((s, i) => (slides.value.length - 1 - i) < newVal && !(s.meta?.slide?.frontmatter?.disabled || s.frontmatter?.disabled))
        if (prevIdx !== -1) go(slides.value.length - prevIdx)
      }
    } else {
      // Navigating backward, find previous valid slide
      const prevIdx = [...slides.value].reverse().findIndex((s, i) => (slides.value.length - 1 - i) < newVal - 1 && !(s.meta?.slide?.frontmatter?.disabled || s.frontmatter?.disabled))
      if (prevIdx !== -1) {
        go(slides.value.length - prevIdx)
      } else {
        // Fallback to next valid if no previous valid found
        const nextIdx = slides.value.findIndex((s, i) => i >= newVal && !(s.meta?.slide?.frontmatter?.disabled || s.frontmatter?.disabled))
        if (nextIdx !== -1) go(nextIdx + 1)
      }
    }
  }
})
</script>

<template>
  <!-- This component manages global state for JDK version filtering -->
</template>
