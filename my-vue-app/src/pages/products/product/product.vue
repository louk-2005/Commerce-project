<script setup>
import ProductEN from "./productEN.vue";
import ProductAR from "./productAR.vue";
import ProductRU from "./productRU.vue";

import {ref} from "vue";
const currentLang = ref(localStorage.getItem('site_lang') || 'en')

</script>

<template>
    <ProductEN v-if="currentLang === 'en'" :lang="currentLang"></ProductEN>
    <ProductAR v-else-if="currentLang === 'ar'" :lang="currentLang"></ProductAR>
    <ProductRU v-else-if="currentLang === 'ru'" :lang="currentLang"></ProductRU>
</template>

<style scoped>

</style>
