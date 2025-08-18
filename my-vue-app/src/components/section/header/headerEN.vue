<script setup>
import {ref, onMounted, defineProps} from 'vue'
import {useRouter} from 'vue-router'
import axios from "axios";

const searchText = ref('')
const isSearching = ref(false)
const router = useRouter()
const categories = ref([])
const props = defineProps({
    lang: {
        type: String,
        required: true
    }
})

function handleSearch() {
    if (!searchText.value.trim()) return
    isSearching.value = true

    router.push({name: 'Products', query: {search: searchText.value}})
    isSearching.value = false
}

async function getCategories() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/products/categories/",
            {
                params: {'lang': props.lang}
            })
        categories.value = response.data
    } catch (error) {
        console.error("خطا در دریافت دسته‌بندی‌ها", error)
    }
    console.log(localStorage)
}


const currentLang = ref(localStorage.getItem('site_lang') || 'en')
const dropdownOpen = ref(false)

const languages = {
    en: 'English',
    ar: 'عربی',
    ru: 'Русский',
}

const flags = {
    en: 'https://flagcdn.com/w20/gb.png', // پرچم انگلیس
    ar: 'https://flagcdn.com/w20/sa.png', // پرچم عربستان
    ru: 'https://flagcdn.com/w20/ru.png', // پرچم روسیه
}

function toggleDropdown() {
    dropdownOpen.value = !dropdownOpen.value
}

function changeLanguage(lang) {
    currentLang.value = lang
    localStorage.setItem('site_lang', lang)
    dropdownOpen.value = false
    window.location.reload()
}

onMounted(() => {
    getCategories()
})
</script>

<template>
    <div class="header">
        <div class="header-box">
            <div class="header-content">
                <div class="right-box">
                    <div class="header-pages">
                        <router-link to="/">Home</router-link>
                        <router-link to="/about">About us</router-link>

                        <!-- Dropdown -->
                        <div class="dropdown">
                            <div class="dropdown-title">
                                <router-link to="/products">Products ▾</router-link>
                            </div>
                            <div class="dropdown-menu">
                                <router-link
                                    v-for="category in categories"
                                    :key="category.id"
                                    :to="{ name: 'Category', params: { id: category.id } }"
                                >
                                    {{ category.name }}
                                </router-link>
                            </div>
                        </div>

                        <router-link to="/contact/us">Contact us</router-link>
                    </div>
                </div>

                <div class="left-box">
                    <div class="search-box">
                        <form @submit.prevent="handleSearch">
                            <div>
                                <input
                                    type="search"
                                    id="search-input"
                                    placeholder="search..."
                                    v-model="searchText"
                                />
                                <button type="submit" :disabled="isSearching">
                                    <font-awesome-icon icon="search" class="search-icon"/>
                                </button>
                            </div>
                        </form>
                    </div>
                    <div class="language-box">
                        <div class="custom-select" @click="toggleDropdown">
                            <div class="selected">
                                <img :src="flags[currentLang]" alt="" class="flag"/>
                                <span>{{ languages[currentLang] }}</span>
                                <span class="arrow">▾</span>
                            </div>
                            <div class="options" v-if="dropdownOpen">
                                <div
                                    v-for="(name, code) in languages"
                                    :key="code"
                                    class="option"
                                    @click="changeLanguage(code)"
                                >
                                    <img :src="flags[code]" alt="" class="flag"/>
                                    <span>{{ name }}</span>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
.language-box {
    position: relative;
    width: 140px;
    color: black;

    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.custom-select {
    border: 1px solid #ccc;
    border-radius: 6px;
    background: #fff;
    cursor: pointer;
    user-select: none;
}

.selected {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5px 10px;
}

.selected .flag {
    width: 20px;
    height: 14px;
    margin-right: 8px;
}

.arrow {
    margin-left: 5px;
}

.options {
    position: absolute;
    top: 100%;
    right: 0;
    width: 100%;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    z-index: 1000;
}

.option {
    display: flex;
    align-items: center;
    padding: 6px 10px;
    gap: 8px;
    transition: background 0.3s;
}

.option:hover {
    background-color: #fbbf24;
    color: #1f2937;
}

.option .flag {
    width: 20px;
    height: 14px;
}

.language-box select {
    padding: 6px 12px;
    border-radius: 6px;
    border: 1px solid #ccc;
    font-size: 14px;
    cursor: pointer;
    background-color: #fff;
    color: #1f2937;
    direction: rtl;
    transition: all 0.3s ease;
}

.language-box select:focus {
    outline: none;
    border-color: #fbbf24;
    box-shadow: 0 0 5px #fbbf24;
}

/* ---------------- Dropdown ---------------- */
.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-title {
    display: flex;
    align-items: center;
    gap: 4px;
    cursor: pointer;
}

.dropdown-menu {
    display: none;
    position: absolute;
    padding: 10px;
    top: 100%;
    left: 0;
    background: #3e4e6e;
    min-width: 180px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    border-radius: 6px;
    z-index: 200;
}

.dropdown-menu a {
    display: block;
    padding: 10px 15px;
    color: #ecf0f1;
    text-decoration: none;
    transition: background 0.3s;
}

.dropdown-menu a:hover {
    background: #374151;
    color: #fbbf24;
}

.dropdown:hover .dropdown-menu {
    display: block;
}

/* ---------------- Header ---------------- */
.header {
    position: relative; /* changed from absolute to relative for better mobile flow */
    top: 0;
    left: 0;
    right: 0;
    background-color: #1f2937;
    padding: 20px 0;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    z-index: 100;
}

.header-box {
    width: 70%;
    margin: 0 auto;
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    flex-wrap: wrap;
    gap: 15px;
}

/* ---------------- Right Box ---------------- */
.right-box {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    align-items: center;
}

.right-box a {
    color: #ecf0f1;
    text-decoration: none;
    font-weight: 600;
    padding: 6px 10px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.right-box a:hover {
    color: #fbbf24;
}

/* ---------------- Left Box ---------------- */
.left-box {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 10px;
}

.search-box form > div {
    display: flex;
    width: 100%;
}

#search-input {
    padding: 7px 12px;
    border: none;
    border-radius: 4px 0 0 4px;
    outline: none;
    font-size: 16px;
    width: 200px;
    transition: width 0.3s ease;
}

#search-input:focus {
    width: 280px;
    box-shadow: 0 0 5px #fbbf24;
}

button[type="submit"] {
    background-color: #fbbf24;
    border: none;
    color: white;
    padding: 0 15px;
    cursor: pointer;
    border-radius: 0 4px 4px 0;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.3s ease;
}

button[type="submit"]:disabled {
    background-color: #95a5a6;
    cursor: not-allowed;
}

button[type="submit"]:hover:not(:disabled) {
    background-color: #9f7406;
}

.search-icon {
    font-size: 18px;
}

/* ---------------- Responsive ---------------- */
@media (max-width: 1024px) {
    .header-content {
        flex-direction: column;
        align-items: flex-start;
        font-size: 15px;
        gap: 15px;
    }

    .right-box {
        justify-content: flex-start;
        gap: 15px;
        width: 100%;
        flex-wrap: wrap;
    }

    .left-box {
        justify-content: flex-start;
        width: 100%;
        gap: 10px;
    }

    #search-input {
        width: 100%;
    }

    button[type="submit"] {
        border-radius: 4px;
        width: 100%;
        margin-top: 5px;
    }

    .dropdown-menu {
        position: relative;
        top: 0;
        left: 0;
        min-width: 100%;
        box-shadow: none;
        background: #2d3a50;
    }

    .dropdown:hover .dropdown-menu {
        display: block;
    }
}

@media (max-width: 600px) {
    .right-box {
        flex-direction: column;
        align-items: flex-start;
    }

    .left-box {
        flex-direction: column;
        width: 100%;
    }

    #search-input {
        width: 100%;
    }

    button[type="submit"] {
        width: 100%;
    }
}

</style>
