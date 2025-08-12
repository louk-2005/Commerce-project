<script setup>
const props = defineProps({
  imagePath: {
    type: String,
    required: false,
    default: "",
  },
  altText: {
    type: String,
    required: false,
    default: "",
  }
})

function getImageUrl(path) {
  if (!path || typeof path !== "string") {
    return "http://localhost:8000/static/default-image.png";
  }
  return path.startsWith("http")
    ? path
    : `http://localhost:8000${path}`;
}
</script>

<template>
  <img
    :src="getImageUrl(imagePath)"
    :alt="altText || 'Home Image'"
    style="max-width: 100%; margin-bottom: 10px;"
  />
</template>

<style scoped>

</style>
