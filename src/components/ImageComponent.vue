<template>
  <div v-if="!loading && url.length" class="imageContainer">
    <img ref="imgElem" :src="url" />
  </div>
  <div v-if="!url.length" class="content">No media found</div>
</template>

<script setup lang="ts">
defineProps([
  'setIsOpen',
  'isBlackTheme',
  'url',
  'loading',
  'top',
  'right',
  'width',
  'height',
  'imgWidth',
  'imgHeight',
])
</script>

<style>
.imageContainer {
  overflow: hidden;
}

.imageContainer img {
  width: 100vw;
  height: 100vh;
}

.content {
  display: flex;
  align-items: center;
  align-self: center;
  justify-content: center;
  width: 100vw;
  height: 100vh;
}
</style>
