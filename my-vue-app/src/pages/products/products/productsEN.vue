<script setup>
import {ref, computed, onMounted, defineProps} from 'vue'
import {useRoute} from 'vue-router'
import axios from 'axios'

const products = ref([])
const route = useRoute()

const props = defineProps({
    lang: {
        type: String,
        required: true
    }
})
async function getProducts() {
    try {
        const response = await axios.get("http://localhost:8000/products/products",
            {
                params: { 'lang': props.lang }
            })
        products.value = response.data
    } catch (error) {
        console.error("خطا در دریافت محصولات:", error)
    }
}

onMounted(() => {
    getProducts()
})

function shortText(text, length) {
    return text.length > length ? text.slice(0, length) + "..." : text
}

const filteredProducts = computed(() => {
    const search = route.query.search?.toLowerCase() || ""
    if (!search) return products.value
    return products.value.filter(
        p =>
            p.name.toLowerCase().includes(search)
    )
})
</script>

<template>
    <div class="products">
        <div class="products-box">
            <div class="products-content">
                <div class="product" v-for="product in filteredProducts" :key="product.id">
                    <div class="image-wrapper">
                        <img :src="product.image" alt="">
                        <div class="overlay">
                            <p class="short">{{ shortText(product.description, 100) }}</p>
                            <p class="full">
                                {{ shortText(product.description, 300) }}
                                <br>
                                <a :href="`/product/${product.id}`">show more...</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="contact-us">
                <p>Do you have any enquiry?</p>
                <p>Do not hesitate to contact us or submit a business enquiry online.</p>
                <a href="/contact/us">Contact Us</a>
            </div>
        </div>
    </div>
</template>


<style scoped>
.products {
    width: 90%;
    max-width: 1200px;
    margin: 100px auto 50px;
    font-family: 'Vazir', sans-serif;
}

.products-box {
    display: flex;
    flex-direction: column;
    gap: 40px;
}

.products-content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.product {
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}

.product:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.image-wrapper {
    position: relative;
    overflow: hidden;
}

.image-wrapper img {
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    display: block;
    transition: transform 0.4s ease;
}

.product:hover img {
    transform: scale(1.05);
}

.overlay {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    color: white;
    padding: 12px;
    transition: all 0.4s ease;
    max-height: 60px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    overflow: hidden;
}

.overlay .full {
    display: none;
    font-size: 13px;
    line-height: 1.4;
}

.overlay .short {
    font-size: 14px;
}

.image-wrapper:hover .overlay {
    max-height: 100%;
    justify-content: center;
}

.image-wrapper:hover .overlay .short {
    display: none;
}

.image-wrapper:hover .overlay .full {
    display: block;
}

.full a {
    color: #fbbf24;
    text-decoration: none;
    font-weight: 500;
    font-size: 15px;
    display: inline-block;
    margin-top: 12px;
}

.full a:hover {
    color: #e09e00;
}

/* Contact box under products */
.contact-us {
    background: #f8f9fa;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.contact-us:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.contact-us p {
    margin: 6px 0;
    font-size: 15px;
    color: #333;
}

.contact-us a {
    display: inline-block;
    margin-top: 12px;
    background: #007bff;
    color: white;
    padding: 10px 20px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    transition: background 0.3s ease, transform 0.3s ease;
}

.contact-us a:hover {
    background: #0056b3;
    transform: translateY(-2px);
}

/* Responsive adjustments */
@media (max-width: 1024px) {
    .full a {
        font-size: 14px;
    }
}

@media (max-width: 768px) {
    .products {
        margin: 80px auto 40px;
    }

    .products-content {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }

    .overlay {
        padding: 10px;
    }

    .overlay .short,
    .overlay .full {
        font-size: 13px;
    }

    .full a {
        font-size: 13px;
    }

    .contact-us {
        padding: 20px;
    }

    .contact-us p {
        font-size: 14px;
    }

    .contact-us a {
        padding: 8px 16px;
        font-size: 14px;
    }
}

@media (max-width: 480px) {
    .products {
        margin: 60px auto 30px;
    }

    .overlay {
        padding: 8px;
    }

    .full a {
        margin-top: 8px;
        font-size: 13px;
    }

    .products-content {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        gap: 20px;
    }

}
</style>


