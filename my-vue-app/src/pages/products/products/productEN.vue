<script setup>
import Header from "../../../components/product/header.vue"
import axios from "axios";
import {ref, onMounted} from "vue";
import {useRoute} from "vue-router";

const product = ref(null);
const productImages = ref([]);
const route = useRoute();
const selectedImage = ref();

async function getProduct() {
    try {
        const response = await axios.get(
            `http://localhost:8000/products/products/${route.params.id}/`
        );
        product.value = response.data;
        console.log(product.value);
    } catch (error) {
        console.error("خطا در دریافت اطلاعات محصول:", error);
    }
}

async function getImages() {
    try {
        const response = await axios.get(
            `http://localhost:8000/products/products/${route.params.id}/get_product_image`
        );
        productImages.value = response.data.map(img => ({
            ...img,
            image: img.image.startsWith("http") ? img.image : `http://localhost:8000${img.image}`,
        }));
        selectedImage.value = productImages.value[0]?.image || null;
    } catch (error) {
        console.error("خطا در دریافت تصاویر محصول:", error);
    }
}

function getImageUrl(path) {
    return path || "http://localhost:8000/static/default-image.png";
}

onMounted(() => {
    getProduct();
    getImages();
});
</script>

<template>
    <!-- HEADER -->
    <Header v-if="product" :product="product"/>

    <!-- Breadcrumb -->
    <div class="breadcrumb-box">
        <nav class="breadcrumb">
            <router-link to="/">Home</router-link>
            /
            <router-link to="/products">Products</router-link>
            /
            <span v-if="product">{{ product.name }}</span>
        </nav>
    </div>


    <!-- PRODUCT GALLERY -->
    <!-- PRODUCT GALLERY -->
    <section class="product-gallery">
        <div class="gallery-main">
            <img :src="getImageUrl(selectedImage)" :alt="product?.name" class="main-image"/>
        </div>

        <div class="gallery-thumbnails">
            <div
                v-for="(img, idx) in productImages"
                :key="idx"
                class="thumbnail"
                :class="{ selected: selectedImage === img.image }"
                @click="selectedImage = img.image"
            >
                <img :src="getImageUrl(img.image)" :alt="`Thumbnail ${idx + 1}`"/>
            </div>
        </div>
    </section>


    <!-- PRODUCT INFO -->
    <section class="product-info" v-if="product">
        <h1>{{ product.name }}</h1>
        <p class="description">{{ product.description }}</p>
    </section>
</template>

<style scoped>
/* ---------------- Breadcrumb ---------------- */
.breadcrumb {
    width: 70%;
    margin: 0 auto 30px;
    padding: 20px 0;
    font-size: 14px;
    color: #555;
}


.breadcrumb a {
    color: #007bff;
    text-decoration: none;
}

.breadcrumb a:hover {
    text-decoration: underline;
}

/* ---------------- Product Gallery ---------------- */
.product-gallery {
    display: flex;
    flex-wrap: wrap;
    width: 70%;
    margin: 0 auto 40px;
    gap: 20px;
}

/* Main image */
.gallery-main {
    flex: 2 1 50%;
    min-width: 250px;
}

.gallery-main img {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    object-fit: contain;
    transition: transform 0.3s ease;
}

.gallery-main img:hover {
    transform: scale(1.02);
}

/* Thumbnails grid */
.gallery-thumbnails {
    flex: 1 1 30%;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    grid-auto-rows: 120px; /* ارتفاع مساوی با عرض برای مربع بودن */
    gap: 8px;
}

.thumbnail {
    width: 100%;
    height: 100%;
    overflow: hidden;
    border-radius: 8px;
    border: 2px solid transparent;
    cursor: pointer;
    transition: all 0.3s ease;
}

.thumbnail img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.thumbnail.selected,
.thumbnail:hover {
    border-color: #007bff;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

/* ---------------- Product Info ---------------- */
.product-info {
    width: 70%;
    margin: 20px auto 40px;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 12px;
}

.product-info h1 {
    margin-bottom: 15px;
    font-size: 28px;
    color: #333;
}

.product-info .description {
    font-size: 16px;
    color: #555;
    margin-bottom: 15px;
}

/* ---------------- Responsive ---------------- */
@media (max-width: 1024px) {
    .product-gallery {
        flex-direction: column;
    }

    .gallery-main, .gallery-thumbnails {
        flex: 1 1 100%;
    }

    .gallery-thumbnails {
        max-height: 450px;

    }
}

@media (max-width: 768px) {
    .gallery-thumbnails {
        grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
        grid-auto-rows: 70px;
        max-height: 300px;

    }

    .product-info h1 {
        font-size: 24px;
    }
}

@media (max-width: 480px) {
    .gallery-thumbnails {
        grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
        grid-auto-rows: 70px;
        max-height: 300px;
    }

    .product-info {
        padding: 15px;
    }

    .product-info h1 {
        font-size: 20px;
    }
}

</style>
