<script setup>
import {ref} from "vue";
import HeaderEN from "./headerEN.vue";
import HeaderAR from "./headerAR.vue";
import HeaderRU from "./headerRU.vue";
const currentLang = ref(localStorage.getItem('site_lang') || 'en')

</script>

<template>
    <HeaderEN v-if="currentLang === 'en'" :lang="currentLang"></HeaderEN>
    <HeaderAR v-else-if="currentLang === 'ar'" :lang="currentLang"></HeaderAR>
    <HeaderRU v-else-if="currentLang === 'ru'" :lang="currentLang"></HeaderRU>
</template>

<style scoped>

</style>
