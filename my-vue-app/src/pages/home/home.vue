<script setup>
import {ref} from "vue";
import HomeEN from "./homeEN.vue";
import HomeAR from "./homeAR.vue";
import HomeRU from "./homeRU.vue";
const currentLang = ref(localStorage.getItem('site_lang') || 'en')

</script>

<template>
    <HomeEN v-if="currentLang === 'en'" :lang="currentLang"></HomeEN>
    <HomeAR v-else-if="currentLang === 'ar'" :lang="currentLang"></HomeAR>
    <HomeRU v-else-if="currentLang === 'ru'" :lang="currentLang"></HomeRU>
</template>

<style scoped>

</style>
