<script setup>
import {ref, onMounted, onUnmounted} from "vue";
import {useRouter} from "vue-router";
import axios from "axios";

const contacts = ref([]);

const router = useRouter();
async function getContacts() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/accounts/contact/");
        contacts.value = response.data;
    } catch (error) {
        console.error("خطا در دریافت اطلاعات", error);
    }
}

const socialLink = ref([])

async function getSocialLink(id) {
    try {
        const response = await axios.get(`http://127.0.0.1:8000/accounts/contact/${id}/get_social_links/`);
        socialLink.value = response.data;
    } catch (error) {
        console.error("خطا در دریافت اطلاعات", error);
    }
}

function goPage(path){
    router.push(path);
}


onMounted(async () => {
    await getContacts();
    for (let c of contacts.value) {
        if (c.id && c.name === 'CENTRAL_OFFICE') {
            await getSocialLink(c.id);
        }
    }
});
</script>

<template>
    <div class="footer">
        <div class="footer-box">
            <div class="footer-content" v-for="contact in contacts" :key="contact.id">
                <div class="footer-row" v-if="contact.name === 'CENTRAL_OFFICE'">
                    <div class="footer-address">
                        <p>العنوان</p>
                        <ul>
                            <li v-if="contact.phone">
                                <font-awesome-icon class="icon" :icon="['fas', 'phone']"/>
                                <span v-text="contact.phone"></span>
                            </li>
                            <li v-else>در حال بارگذاری شماره تلفن...</li>
                            <li v-if="contact.email">
                                <font-awesome-icon class="icon" :icon="['fas', 'envelope']"/>
                                <span v-text="contact.email"></span>
                            </li>
                            <li v-else>در حال بارگذاری ایمیل...</li>
                            <li v-if="contact.address">
                                <font-awesome-icon class="icon" :icon="['fas', 'map-marker-alt']"/>
                                <span v-text="contact.address"></span>
                            </li>
                            <li v-else>در حال بارگذاری آدرس...</li>
                        </ul>
                    </div>

                    <div class="footer-quick-access">
                        <p>الوصول السريع</p>
                        <ul>
                            <li @click="goPage('/')">الرئيسية</li>
                            <li @click="goPage('/products')">المنتجات</li>
                            <li @click="goPage('/contact/us')">اتصل بنا</li>
                            <li @click="goPage('/about')">من نحن</li>
                        </ul>
                    </div>

                    <div class="footer-logo">
                        <img :src="contact.logo" alt="Logo"/>
                    </div>
                </div>
                <div class="social-link" v-if="contact.name === 'CENTRAL_OFFICE'">
                    <p class="footer-header">
                        تابعنا على الشبكات التالية:
                    </p>
                    <div class="social-links">
                        <a v-for="media in socialLink" :key="media.id" :href="media.url" target="_blank"
                           rel="noopener noreferrer" class="social-icon" :title="media.name">
                            <font-awesome-icon
                                :icon="[
                                            'fab',
                                            media.name.toLowerCase() === 'telegram' ? 'telegram-plane' :
                                            media.name.toLowerCase() === 'whatsapp' ? 'whatsapp' :
                                            media.name.toLowerCase() === 'instagram' ? 'instagram' :
                                            media.name.toLowerCase() === 'twitter' ? 'twitter' :
                                            media.name.toLowerCase() === 'facebook' ? 'facebook' : ''
                                        ]"
                            />
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
.footer {
    background-color: #1f2937;
    color: #e5e7eb;
    padding: 40px 20px;
    font-family: 'Vazir', 'Roboto', 'Helvetica Neue', sans-serif;
    font-size: 14px;
    line-height: 1.6;
    direction: rtl; /* راست‌چین */
    border-top: 3px solid #fbbf24;
}

.footer-box {
    width: 70%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 40px;
    padding-bottom: 20px;
}

.footer-content {
    width: 100%;
}

.footer-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 40px;
    flex-wrap: wrap;
    padding-bottom: 10px;
    border-bottom: 1px solid #34495E;
}

.footer-address,
.footer-quick-access,
.footer-logo {
    flex: 1 1 250px;
    min-width: 250px;
    display: flex;
    flex-direction: column;
    text-align: right; /* راست‌چین کردن متن */
}

.footer-address p,
.footer-quick-access p {
    font-weight: 700;
    font-size: 18px;
    margin-bottom: 18px;
    color: #fbbf24;
    letter-spacing: 0.05em;
}

.footer-address ul,
.footer-quick-access ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.footer-address li,
.footer-quick-access li {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
    color: #d1d5db;
    cursor: default;
    font-size: 15px;
    transition: color 0.3s ease;
    flex-direction: row; /* آیکون سمت راست، متن سمت چپ */
}

.footer-address li:hover,
.footer-quick-access li:hover {
    color: #fbbf24;
}

.footer-quick-access li {
    cursor: pointer;
}

.footer-quick-access li:not(:last-child) {
    margin-bottom: 14px;
}

.icon {
    margin-left: 10px; /* به جای margin-right برای راست‌چین */
    color: #fbbf24;
    min-width: 20px;
    font-size: 18px;
}

.footer-logo {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding-top: 10px;
}

.footer-logo img {
    max-width: 160px;
    height: auto;
    filter: brightness(0) invert(1);
    object-fit: contain;
    transition: transform 0.3s ease;
}

.footer-logo img:hover {
    transform: scale(1.05);
}

.social-link {
    width: 100%;
    margin-top: 30px;
    text-align: right; /* راست‌چین کردن شبکه‌های اجتماعی */
    padding-top: 25px;
}

.social-link .footer-header {
    font-weight: 700;
    font-size: 18px;
    margin-bottom: 18px;
    color: #fbbf24;
    letter-spacing: 0.05em;
}

.social-links {
    display: flex;
    justify-content: flex-start; /* راست‌چین کردن آیکون‌ها */
    gap: 25px;
    flex-wrap: wrap;
}

.social-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background-color: #374151;
    color: #fbbf24;
    font-size: 22px;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.social-icon:hover {
    background-color: #fbbf24;
    color: #1f2937;
    transform: scale(1.15);
    cursor: pointer;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
    .footer-row {
        gap: 30px;
    }

    .footer-address,
    .footer-quick-access,
    .footer-logo {
        min-width: 220px;
    }
}

@media (max-width: 768px) {
    .footer-row {
        flex-direction: column;
        align-items: center;
        text-align: right;
        gap: 25px;
        border-bottom: none;
    }

    .footer-address,
    .footer-quick-access,
    .footer-logo {
        min-width: 100%;
    }

    .footer-address p,
    .footer-quick-access p {
        font-size: 20px;
    }

    .footer-logo {
        padding-top: 0;
    }

    .social-links {
        justify-content: flex-end;
        gap: 18px;
    }

    .social-icon {
        width: 38px;
        height: 38px;
        font-size: 20px;
    }
}
</style>
