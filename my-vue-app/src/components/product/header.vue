<template>
    <!-- start header -->
    <header
        class="header"
        :style="backgroundStyle"
    >
        <div class="header-box">
            <div class="header-content">

            </div>
        </div>
    </header>
    <!-- end header -->
</template>

<script setup>
import {computed} from 'vue'

const props = defineProps({
    product: Object,
})

const backgroundStyle = computed(() => {
    return props.product?.image
        ? {
            background: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${props.product.image})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            backgroundRepeat: 'no-repeat',
        }
        : {}
})

</script>


<style scoped>
.header {
    height: 50vh;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 2rem;
}

.header-box {
    width: 85%;
    margin: 0 auto;
    height: 100%;
}

.header-content {
    height: 100%;
    display: flex;
    align-items: end;
}


</style>