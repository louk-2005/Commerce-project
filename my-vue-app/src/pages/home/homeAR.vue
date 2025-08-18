<script setup>
import {ref, onMounted, onUnmounted, defineProps} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";

const HomeImages = ref([]);
const currentIndex = ref(0);
const categories = ref([]);
const products = ref([]);
const router = useRouter();
let timer = null;
const props = defineProps({
    lang: {
        type: String,
        required: true
    }
})

async function getHomeHeaderImage() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/home/images",
            {
                params: {'lang': props.lang}
            });
        HomeImages.value = response.data;
    } catch (error) {
        console.error("خطا در دریافت اطلاعات", error);
    }
}

async function getCategories() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/products/categories/",
            {
                params: {'lang': props.lang}
            });
        categories.value = response.data;
    } catch (error) {
        console.error("خطا در دریافت اطلاعات", error);
    }
}

async function getProducts() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/products/products/",
            {
                params: {'lang': props.lang}
            });
        products.value = response.data;
    } catch (error) {
        console.error("خطا در دریافت اطلاعات", error);
    }
}

function nextSlide() {
    if (HomeImages.value.length === 0) return;
    currentIndex.value = (currentIndex.value + 1) % HomeImages.value.length;
}

function prevSlide() {
    if (HomeImages.value.length === 0) return;
    currentIndex.value =
        (currentIndex.value - 1 + HomeImages.value.length) % HomeImages.value.length;
}

function goToSlide(index) {
    currentIndex.value = index;
    resetTimer();
}

function startTimer() {
    timer = setInterval(() => {
        nextSlide();
    }, 5000);
}

function stopTimer() {
    if (timer) {
        clearInterval(timer);
        timer = null;
    }
}

function resetTimer() {
    stopTimer();
    startTimer();
}

function goPage(routeName, id) {
    router.push({name: routeName, params: {id}});
}


onMounted(() => {
    getHomeHeaderImage();
    startTimer();
    getCategories();
    getProducts();
});

onUnmounted(() => {
    stopTimer();
});
</script>

<template>
    <div class="slider-container">
        <div v-if="HomeImages.length === 0" class="loading-text">در حال بارگذاری تصاویر...</div>
        <div v-else class="slider">
            <div
                v-for="(img, index) in HomeImages"
                :key="index"
                class="slide"
                :class="{ active: index === currentIndex }"
            >
                <img
                    :src="img.image"
                    :alt="img.alt || 'Slide ' + (index + 1)"
                    class="slider-image"
                />
            </div>
            <div class="slider-info">
                <p>شركة تجارية</p>
                <div class="slider-links">
                    <a href="/products" class="products-btn">منتجات</a>
                    <a href="/contact/us" class="contact-us-btn">اتصل بنا</a>
                </div>
            </div>

            <div class="overlay"></div>

            <button class="btn btn-left" @click="prevSlide">&#10094;</button>
            <button class="btn btn-right" @click="nextSlide">&#10095;</button>

            <!-- نقاط اسلایدر -->
            <div class="dots">
        <span
            v-for="(img, index) in HomeImages"
            :key="index"
            class="dot"
            :class="{ active: index === currentIndex }"
            @click="goToSlide(index)"
        ></span>
            </div>
        </div>
    </div>

    <!--    about us-->
    <div class="about-us">
        <div class="about-us-box">
            <div class="about-us-content">
                <div class="about-us-info">
                    <h5>
                        معلومات عنا
                    </h5>
                    <p>
                        عشتار شركة تابعة لمجموعة باروس القابضة، التي تأسست عام ٢٠٠٧. تعمل هذه المجموعة في توريد وتجارة
                        مختلف أنواع المنتجات النفطية والبتروكيماويات والمعادن. تتمتع المجموعة بخبرة تزيد عن ١٠ سنوات في
                        مجال التجارة الدولية، وتعمل بكامل طاقتها في أوروبا وآسيا. تُعد عشتار من أبرز الشركات الرائدة في
                        المنطقة، حيث تُصدر سلعًا متنوعة إلى دول مثل إسبانيا، وألمانيا، وهولندا، وروسيا، والصين، والهند،
                        ودول رابطة الدول المستقلة، والعراق، وباكستان، وعُمان، وقطر، والإمارات العربية المتحدة. تتعاون
                        هذه المجموعة مع أكبر الشركات المصنعة والمنتجين العالميين في مختلف الصناعات، مثل النفط والغاز
                        والتعدين، وتمتلك سلة سلع متنوعة.
                    </p>
                    <a href="/about">رؤية المزيد</a>
                </div>
                <div class="home-about-us-image">
                    <img src="../../assets/homeAboutUs/ocean1.png" alt="">
                </div>
            </div>
        </div>
    </div>

    <div class="home-category">
        <div class="home-category-contact">
            <div class="home-category-box">
                <h5>فئة المنتجات</h5>
                <div class="home-category-list">
                    <div
                        class="home-category-item"
                        v-for="category in categories"
                        @click="goPage('Category', category.id)"
                        :key="category.id"
                    >


                        <div class="category-image-wrapper">
                            <img
                                :src="category.image || '/default-category.jpg'"
                                :alt="category.name"
                                class="category-image"
                            />
                            <div class="category-overlay">
                                <p>{{ category.description || 'لا يوجد وصف متاح.' }}</p>
                            </div>
                        </div>
                        <router-link
                            :to="{ name: 'Category', params: { id: category.id } }"
                            class="category-link">
                            {{ category.name }}
                        </router-link>


                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="mission-statement">
        <div class="mission-statement-box">
            <div class="mission-statement-content">
                <p>
                    أولويتنا القصوى هي تلبية احتياجات عملائنا المتزايدة. نحتضن التنوع من أجل الابتكار والنمو.
                </p>
            </div>
        </div>
    </div>
    <div class="products">
        <div class="products-box">
            <div class="products-content">
                <h5>المنتجات</h5>
                <div class="home-product-list">
                    <div
                        class="home-product-item"
                        v-for="product in products"
                        :key="product.id"
                        @click="goPage('Product',product.id)"
                    >
                        <div class="product-image-wrapper">
                            <img
                                :src="product.image || '/default-product.jpg'"
                                :alt="product.name"
                                class="product-image"
                            />
                            <div class="product-overlay">
                                <p>{{ product.description || 'لا يوجد وصف متاح.' }}</p>
                            </div>
                        </div>
                        <router-link
                            :to="{ name: 'Product', params: { id: product.id } }"
                            class="product-link">
                            {{ product.name }}
                        </router-link>

                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<style scoped>
.slider-container {
    position: relative;
    height: 100vh;
    overflow: hidden;
    background-color: #000;
    display: flex;
    justify-content: center;
    align-items: center;
    user-select: none;
    direction: rtl;
    text-align: right;
}

.loading-text {
    color: #f0f0f0;
    font-size: 28px;
    font-weight: 600;
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.slider {
    position: relative;
    width: 100%;
    height: 100%;
}

.slide {
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: opacity 1s ease-in-out;
    z-index: 0;
}

.slide.active {
    opacity: 1;
    z-index: 2;
}

.slider-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    user-select: none;
}

.slider-info {
    position: absolute;
    bottom: 20%;
    right: 50%;
    transform: translateX(50%);
    color: #fff;
    font-weight: 700;
    z-index: 10;
    user-select: none;
    max-width: 90vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 50px;
    white-space: nowrap;
    pointer-events: none;
    text-align: center;
}

.slider-info p {
    margin: 0;
    pointer-events: auto;
    font-size: clamp(1.6rem, 4vw, 2.4rem);
}

.slider-links {
    display: flex;
    gap: 20px;
    pointer-events: auto;
}

.slider-links a {
    font-weight: 600;
    text-decoration: none;
    font-size: 1.5rem;
    padding: 10px 0;
    width: 200px;
    text-align: center;
    pointer-events: auto;
    display: inline-block;
    border-radius: 3px;
    transition: background-color 0.3s ease, color 0.3s ease;
    cursor: pointer;
}

.products-btn {
    background-color: white;
    color: black;
}

.products-btn:hover {
    background-color: #d5d2d2;
}

.contact-us-btn {
    background-color: #1f2937;
    color: white;
}

.contact-us-btn:hover {
    background-color: #10171b;
}

.overlay {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.3);
    pointer-events: none;
    z-index: 1;
}

.btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(30, 30, 30, 0.5);
    border: none;
    color: white;
    font-size: 48px;
    padding: 12px 22px;
    cursor: pointer;
    border-radius: 50%;
    user-select: none;
    transition: background-color 0.3s ease, transform 0.2s ease;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 3;
}

.btn:hover {
    background-color: rgba(30, 30, 30, 0.8);
    transform: translateY(-50%) scale(1.1);
}

.btn-left {
    right: 25px;
}

.btn-right {
    left: 25px;
}

.dots {
    position: absolute;
    bottom: 20px;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 12px;
    z-index: 4;
}

.dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.5);
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.dot.active {
    background-color: #3498db;
    box-shadow: 0 0 8px #3498db;
}

@media (max-width: 768px) {
    .btn {
        font-size: 36px;
        padding: 10px 18px;
    }

    .dot {
        width: 12px;
        height: 12px;
    }
}

.about-us {
    background-color: #1f2937;
    direction: rtl;
    text-align: right;
}

.about-us-box {
    width: 70%;
    margin: 0 auto;
}

.about-us-content {
    display: flex;
    gap: 20px;
}

.about-us-info {
    width: 45%;
    padding: 30px 0;
    text-align: right;
}

.about-us-info h5 {
    font-family: 'Vazir', sans-serif;
    font-weight: 700;
    font-size: 2rem;
    margin-bottom: 15px;
    color: white;
}

.about-us-info p {
    font-family: 'Vazir', sans-serif;
    font-weight: 400;
    font-size: 1.1rem;
    color: white;
    line-height: 1.7;
}

.about-us-info a {
    font-family: 'Vazir', sans-serif;
    color: #3498db;
    font-weight: 600;
    text-decoration: none;
    margin-top: 20px;
    display: inline-block;
}

.about-us-info a:hover {
    color: #1d6fa5;
    text-decoration: underline;
}

.home-about-us-image {
    width: 45%;
    padding: 30px 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.home-about-us-image img {
    width: 100%;
    max-width: 600px;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    object-fit: cover;
}

.home-category {
    background-color: #f9f9f9;
    padding: 40px 0;
    direction: rtl;
    text-align: right;
}

.home-category-contact {
    display: flex;
    justify-content: center;
}

.home-category-box {
    width: 70%;
    max-width: 1200px;
}

.home-category-box h5 {
    font-family: 'Vazir', sans-serif;
    font-weight: 700;
    font-size: 2rem;
    margin: 50px 0 40px;
    text-align: center;
    color: #2c3e50;
}

.home-category-list {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 25px;
}

.home-category-item {
    background-color: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    text-align: center;
    transition: all 0.3s ease;
    cursor: pointer;
}

.home-category-item:hover {
    background-color: #34495e;
    transform: translateY(-5px) scale(1.02);
}

.home-category-item:hover .category-link {
    color: #fff;
}

.category-image {
    width: 100%;
    max-height: 300px;
    object-fit: cover;
}

.category-link {
    display: block;
    padding: 14px;
    font-family: 'Vazir', sans-serif;
    font-weight: 600;
    color: #34495e;
    text-decoration: none;
    transition: color 0.3s ease;
}

.category-link:hover {
    color: #3498db;
}

@media (max-width: 768px) {
    .home-category-list {
        grid-template-columns: 1fr;
    }

    .home-about-us-image {
        width: 100%;
        padding: 20px 0;
    }
}

.category-image-wrapper {
    position: relative;
    overflow: hidden;
}

.category-overlay {
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background: rgba(52, 73, 94, 0.85);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 50px;
    text-align: center;
    font-family: 'Vazir', sans-serif;
    font-size: 1rem;
    opacity: 0;
    transform: translateY(100%);
    transition: all 0.4s ease;
}

.category-image-wrapper:hover .category-overlay {
    opacity: 1;
    transform: translateY(0);
}

.mission-statement {
    background-color: #1f2937;
    padding: 40px 20px;
    text-align: center;
    color: #f9fafb;
    font-family: 'Vazir', sans-serif;
    user-select: none;
    direction: rtl;
}

.mission-statement-box {
    max-width: 70%;
    margin: 0 auto;
}

.mission-statement-content p {
    font-weight: 600;
    font-size: 1.4rem;
    line-height: 1.2;
    letter-spacing: 0.02em;
    margin: 0;
}

.products {
    background-color: #f5f7fa;
    padding: 50px 0;
    direction: rtl;
    text-align: right;
}

.products-box {
    margin: 0 auto;
    width: 70%;
}

.products-content h5 {
    font-family: 'Vazir', sans-serif;
    font-weight: 700;
    font-size: 2.2rem;
    margin-bottom: 40px;
    color: #2c3e50;
    text-align: center;
}

.home-product-list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
}

.home-product-item {
    background-color: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
}

.home-product-item:hover {
    transform: translateY(-8px);
    background-color: #2c3e50;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.home-product-item:hover .product-link {
    color: #fff;
}

.product-image-wrapper {
    position: relative;
    width: 100%;
    padding-top: 70%;
    overflow: hidden;
}

.product-image {
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.home-product-item:hover .product-image {
    transform: scale(1.1);
}

.product-overlay {
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background: rgba(52, 73, 94, 0.85);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 50px;
    text-align: center;
    font-family: 'Vazir', sans-serif;
    font-size: 1rem;
    opacity: 0;
    transform: translateY(100%);
    transition: all 0.4s ease;
}

.product-image-wrapper:hover .product-overlay {
    opacity: 1;
    transform: translateY(0);
}

.product-link {
    display: block;
    padding: 15px 10px;
    font-family: 'Vazir', sans-serif;
    font-weight: 600;
    color: #2c3e50;
    font-size: 1.2rem;
    text-decoration: none;
    text-align: center;
    border-top: 1px solid #e1e4e8;
    transition: color 0.3s ease;
}

.product-link:hover {
    color: #3498db;
}

@media (max-width: 1024px) {
    .slider-container {
        height: 70vh;
    }
}

@media (max-width: 640px) {
    .about-us-content {
        flex-wrap: wrap;
        justify-content: center;
    }

    .about-us-box {
        margin: 0 auto;
    }

    .about-us-info {
        width: 100%;
    }

    .about-us-info p {
        font-size: 1rem;
        line-height: 1.5;
    }

    .home-about-us-image img {
        max-width: 100%;
    }
}

@media (max-width: 640px) {
    .home-category-box {
        width: 70%;
    }

    .home-category-list {
        grid-template-columns: 1fr;
        gap: 15px;
    }
}

@media (max-width: 1024px) {
    .home-product-list {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 640px) {
    .home-product-list {
        grid-template-columns: 1fr;
        gap: 15px;
    }

    .product-link {
        font-size: 1rem;
        padding: 10px 5px;
    }
}

@media (max-width: 480px) {
    .slider-info p {
        font-size: 1rem;
    }

    .slider-links a {
        font-size: 0.9rem;
        padding: 6px 10px;
        width: 120px;
    }
}

@media (max-width: 640px) {
    .mission-statement-box {
        width: 90%;
    }

    .mission-statement-content p {
        font-size: 1rem;
    }
}


</style>
