<script setup>
import {ref} from "vue";
import ContactUsEN from "./contactUsEN.vue";
import ContactUsAR from "./contactUsAR.vue";
import ContactUsRU from "./contactUsRU.vue";
const currentLang = ref(localStorage.getItem('site_lang') || 'en')

</script>

<template>
    <contact-us-e-n v-if="currentLang === 'en'" :lang="currentLang"></contact-us-e-n>
    <contact-us-a-r v-else-if="currentLang === 'ar'" :lang="currentLang"></contact-us-a-r>
    <contact-us-r-u v-else-if="currentLang === 'ru'" :lang="currentLang"></contact-us-r-u>
</template>

<style scoped>

</style>
