<script setup>
// import {ref} from 'vue'
//
// const searchText = ref('')
// const isSearching = ref(false)
//
// function handleSearch() {
//     if (!searchText.value.trim()) return
//     isSearching.value = true
//
//     setTimeout(() => {
//         alert(`جستجو برای: ${searchText.value}`)
//         isSearching.value = false
//     }, 1000)
// }
</script>

<template>
    <div class="header">
        <div class="header-box">
            <div class="header-content">
                <div class="right-box">
                    <div class="header-pages">
                        <a href="/">Home</a>
                        <a href="/about">About us</a>
                        <a href="/products">Products</a>
                        <a href="/contact/us">Contact us</a>
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
                                <button
                                    type="submit"
                                    aria-label="searching..."
                                    :disabled="isSearching"
                                >
                                    <font-awesome-icon icon="search" class="search-icon"/>
                                </button>
                            </div>
                        </form>
                    </div>
                    <div class="language-box">

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.header {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    background-color: #1f2937;
    padding: 30px 0;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    z-index: 100;
}

.header-box {
    max-width: 70%;
    margin: 0 auto;
    padding: 0 20px;
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
}

.right-box {
    display: flex;
    gap: 25px;
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

.left-box {
    display: flex;
    align-items: center;
}

.search-box form > div {
  display: flex;
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

/* واکنش‌گرایی */
@media (max-width: 600px) {
    .header-content {
        flex-direction: column;
        gap: 15px;
    }

    .right-box {
        gap: 15px;
        flex-wrap: wrap;
        justify-content: center;
    }

    #search-input {
        width: 100%;
    }

    button[type="submit"] {
        border-radius: 4px;
        margin-top: 5px;
        width: 100%;
    }

    .search-box form {
        flex-direction: column;
        width: 100%;
    }
}

</style>
