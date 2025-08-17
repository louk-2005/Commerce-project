<script setup>
import ProductsEN from "./productsEN.vue";
import ProductsAR from "./productsAR.vue";
import ProductsRU from "./productsRU.vue";

import {ref} from "vue";
const currentLang = ref(localStorage.getItem('site_lang') || 'en')

</script>

<template>
    <ProductsEN v-if="currentLang === 'en'" :lang="currentLang"></ProductsEN>
    <ProductsAR v-else-if="currentLang === 'ar'" :lang="currentLang"></ProductsAR>
    <ProductsRU v-else-if="currentLang === 'ru'" :lang="currentLang"></ProductsRU>
</template>

<style scoped>

</style>
