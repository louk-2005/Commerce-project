<script setup>
import {ref} from "vue";
import CategoryEN from "./categoryEN.vue";
import CategoryAR from "./categoryAR.vue";
import CategoryRU from "./categoryRU.vue";

const currentLang = ref(localStorage.getItem('site_lang') || 'en')

</script>

<template>
    <CategoryEN v-if="currentLang === 'en'" :lang="currentLang"></CategoryEN>
    <CategoryAR v-else-if="currentLang === 'ar'" :lang="currentLang"></CategoryAR>
    <CategoryRU v-else-if="currentLang === 'ru'" :lang="currentLang"></CategoryRU>
</template>

<style scoped>

</style>
