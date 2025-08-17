<script setup>
import Location from "../../components/Location/location.vue";
import ContactForm from "../../components/contact/form.vue"
import {ref, onMounted} from "vue";
import axios from "axios";


const contacts = ref([]);

async function getContacts() {
    try {
        const response = await axios.get("http://localhost:8000/accounts/contact");
        contacts.value = response.data;
        console.log("Contacts:", contacts.value);
    } catch (error) {
        console.error("خطا در دریافت اطلاعات تماس:", error);
    }
}

onMounted(() => {
    getContacts();
});
</script>

<template>
    <!-- start communication-location -->
    <div class="communication-location">
        <div class="communication-location-box">
            <div class="communication-location-content">
                <p> address in map</p>
                <Location/>
            </div>
        </div>
    </div>
    <!-- end communication-location -->
    <div class="communication-info">
        <div class="communication-info-box">

            <div class="communication-info-content">
                    <div v-for="contact in contacts" :key="contact.id" class="contact-item">
                        <div class="product-message">
                            <span v-if="contact.name === 'FACTORY'">factory</span>
                            <span v-if="contact.name === 'CENTRAL_OFFICE'">Central office</span>
                            <span v-if="contact.name === 'SHOW_ROOM'">Showroom</span>
                        </div>

                        <div class="icon-grid">
                            <div class="icon-box">
                                <font-awesome-icon class="icon" :icon="['fas', 'phone']"/>
                                <div class="icon-text">
                                    <span v-if="contact.phone">{{ contact.phone }}</span>
                                    <span v-else>
                                        Loading phone number...
                                    </span>
                                </div>
                            </div>
                            <div class="icon-box">
                                <font-awesome-icon class="icon" :icon="['fas', 'envelope']"/>
                                <div class="icon-text">
                                    <span v-if="contact.email">{{ contact.email }}</span>
                                    <span v-else>Loading phone email...</span>
                                </div>
                            </div>
                            <div class="icon-box">
                                <font-awesome-icon class="icon" :icon="['fas', 'map-marker-alt']"/>
                                <div class="icon-text">
                                    <span v-if="contact.address">{{ contact.address }}</span>
                                    <span v-else>Loading phone address...</span>
                                </div>
                            </div>
                        </div>
                    </div>

            </div>
        </div>
    </div>
    <!--    end communication info-->
    <!--    start communication-form-->
    <div class="communication-form">
        <div class="communication-form-box">
            <div class="communication-form-content">
                <p class="communication-form-header">Enter your message:</p>
                <ContactForm></ContactForm>
            </div>
        </div>

    </div>

</template>

<style scoped>
/* ===== Layout Containers ===== */
.communication-location-box {
    width: 80%;
    margin: 120px auto 30px;
    padding: 20px;
    background: linear-gradient(135deg, #1f2937, #111827);
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

/* ===== Map Section ===== */
.communication-location-content {
    margin: 60px 0;
    text-align: center;
}

.communication-location-content p {
    font-size: 26px;
    margin-bottom: 25px;
    font-weight: 700;
    color: #fbbf24;
    letter-spacing: 0.5px;
}

/* ===== Contact Info Section ===== */
.communication-info {
    margin: 80px 0;
}

.communication-info-content {
    display: flex;
    flex-wrap: wrap;
    gap: 40px;
    width: 80%;
    margin: 0 auto;
    justify-content: space-between;
}

.contact-item {
    background-color: #1f2937!important;
    padding: 25px 20px;
    border-radius: 16px !important;
    width: 100%;
    max-width: 450px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.contact-item:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.25);
}

.product-message {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #fbbf24;
    text-align: center;
    text-transform: uppercase;
}

/* ===== Icon Grid ===== */
.icon-grid {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 20px;
}

.icon-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 10px;
    background-color: white;
    border-radius: 10px;
    min-width: 120px;
    transition: background-color 0.3s ease;
}

.icon-box:hover {
    background-color: #c8c7c7;
}

.icon {
    font-size: 26px;
    color: #fbbf24;
    margin-bottom: 8px;
}

.icon-text {
    font-size: 15px;
    color: black;
    word-break: break-word;
}

/* ===== Contact Form Section ===== */
.communication-form-content {
    margin: 80px auto;
    background-color: #111827;
    padding: 35px 30px;
    border-radius: 14px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    text-align: center;
    width: 80%;
}

.communication-form-header {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 25px;
    color: #fbbf24;
    text-align: left;
}
.contact-item {
    width: 100%;
    display: block; /* هر باکس در یک خط */
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px; /* فاصله بین باکس‌ها */
    background-color: #fff;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.icon-grid {
    display: flex;
    flex-direction: column; /* آیکون‌ها زیر هم باشند */
    gap: 10px;
}

.icon-box {
    display: flex;
    align-items: center;
    gap: 10px;
}

.icon {
    font-size: 18px;
    color: #555;
}

.icon-text {
    font-size: 15px;
}

/* ===== Responsive ===== */
@media (max-width: 1024px) {
    .icon-grid {
        justify-content: center;
    }
}

@media (max-width: 768px) {
    .communication-info-content {
        flex-direction: column;
        align-items: center;
    }

    .contact-item {
        max-width: 100%;
    }

    .icon-grid {
        flex-direction: column;
        gap: 15px;
    }
}

</style>


