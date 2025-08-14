<script setup>
import {ref, onMounted} from "vue";
import axios from "axios";

const products = ref([]);

async function getProducts() {
    try {
        const response = await axios.get("http://localhost:8000/products/products");
        products.value = response.data;
    } catch (error) {
        console.error("خطا در دریافت محصولات:", error);
    }
}

onMounted(() => {
    getProducts();
});

// توابع کوتاه کردن متن
function shortText(text, length) {
    return text.length > length ? text.slice(0, length) + "..." : text;
}
</script>

<template>
    <div class="products">
        <div class="products-box">
            <div class="products-content">
                <div class="product" v-for="product in products" :key="product.id">
                    <div class="image-wrapper">
                        <img :src="product.image" alt="">
                        <div class="overlay">
                            <p class="short">{{ shortText(product.description, 100) }}</p>
                            <p class="full">
                                {{ shortText(product.description, 300) }}
                                <br>
                                <a href="">show more...</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="contact-us">
                <p>Do you have any enquiry?</p>
                <p>Do not hesitate to contact us or submit a business enquiry online.</p>
                <a href="">Contact Us</a>
            </div>
        </div>
    </div>
</template>

<style scoped>
.products {
    width: 70%;
    margin: 150px auto;
    padding: 20px 0;
    font-family: sans-serif;
}

.products-box {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.products-content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.product {
    background: #fff;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.product:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.image-wrapper {
    position: relative;
    overflow: hidden;
}

.image-wrapper img {
    max-width: 100%;
    object-fit: cover;
    display: block;
}

.overlay {
    position: absolute;
    bottom: 0;
    width: 100%;
    background: rgba(0,0,0,0.6);
    color: white;
    padding: 10px;
    transition: all 0.4s ease;
    height: 60px; /* حالت پیش‌فرض */
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.overlay .full {
    display: none;
    font-size: 13px;
}

.overlay .short {
    font-size: 13px;
}

.image-wrapper:hover .overlay {
    height: 100%; /* رشد بک‌گراند */
    justify-content: center;
}

.image-wrapper:hover .overlay .short {
    display: none;
}

.image-wrapper:hover .overlay .full {
    display: block;
}

.full a{
    color: #fbbf24;
    text-decoration: none;
    font-size: 16px;
    display: inline-block;
    margin-top: 20px;
}
.full a:hover{
    color: #8a6404;

}
/* Contact box under products */
.contact-us {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.contact-us p {
    margin: 5px 0;
    font-size: 15px;
    color: #333;
}

.contact-us a {
    display: inline-block;
    margin-top: 10px;
    background: #007bff;
    color: white;
    padding: 8px 16px;
    border-radius: 6px;
    text-decoration: none;
    transition: background 0.2s ease;
}

.contact-us a:hover {
    background: #0056b3;
}
</style>

