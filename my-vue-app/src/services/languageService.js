import { ref, watch } from 'vue'

export const currentLang = ref(localStorage.getItem('site_lang') || 'en')

watch(currentLang, (newLang) => {
    localStorage.setItem('site_lang', newLang)
})
