<script setup>
import {ref} from "vue";
import FooterEN from "./footerEN.vue";
import FooterAR from "./footerAR.vue";
import FooterRU from "./footerRU.vue";
const currentLang = ref(localStorage.getItem('site_lang') || 'en')

</script>

<template>
    <FooterEN v-if="currentLang === 'en'" :lang="currentLang"></FooterEN>
    <FooterAR v-else-if="currentLang === 'ar'" :lang="currentLang"></FooterAR>
    <FooterRU v-else-if="currentLang === 'ru'" :lang="currentLang"></FooterRU>
</template>

<style scoped>

</style>
