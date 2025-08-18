<script setup>
import {ref} from "vue";
import AboutEN from "./aboutEN.vue";
import AboutAR from "./aboutAR.vue";
import AboutRU from "./aboutRU.vue";
const currentLang = ref(localStorage.getItem('site_lang') || 'en')

</script>

<template>
    <AboutEN v-if="currentLang === 'en'" :lang="currentLang"></AboutEN>
    <AboutAR v-else-if="currentLang === 'ar'" :lang="currentLang"></AboutAR>
    <AboutRU v-else-if="currentLang === 'ru'" :lang="currentLang"></AboutRU>
</template>

<style scoped>

</style>
