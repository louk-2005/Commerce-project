<script setup>

</script>

<template>
    <div class="about">
        <div class="about-box">
            <div class="about-content">
                <div class="box">

                    <div class="info">
                        <h5>

                            О нас
                        </h5>
                        <p>
                            Иштар – имя месопотамской богини, а также ворот и главного входа в великий город Вавилон.
                            Ishtar – один из брендов, принадлежащих Barus Holding Group. Основатели основали компанию в
                            2007 году с целью лучшего обеспечения и использования потенциала Ближнего Востока в сфере
                            нефтепродуктов. Наша основная деятельность сосредоточена на поиске, поставке и дистрибуции
                            различных видов нефтепродуктов, нефтехимической продукции и минералов на международных
                            рынках. Наша сеть поставщиков и покупателей за это время расширилась благодаря надежности и
                            прозрачности. За эти 10 лет наша компания заслужила отличную репутацию и авторитет на рынке,
                            а также доверие клиентов, экспортируя различные товары в страны Азии и Европы, такие как:
                        </p>
                    </div>
                    <div class="picture">
                        <img src="../../assets/AboutAboutUs/zitto_customize-min-2.png" alt="">
                    </div>
                </div>

                <div class="box">

                    <div class="info">
                        <h5>

                            НАША МИССИЯ
                        </h5>
                        <p>

                            <br>

                            Наши известные коучинговые программы позволят вам:
                        </p>
                        <ul>
                            <li>
                                Привлекать и удерживать качественных, высокооплачиваемых клиентов
                            </li>
                            <li>
                                Работать меньше часов и зарабатывать больше
                            </li>
                            <li>
                                Привлекать и удерживать качественных, высокооплачиваемых клиентов
                                Управлять своим временем, чтобы успевать больше за меньшее время
                            </li>
                            <li>
                                Оттачивать лидерские навыки для управления командой
                            </li>
                            <li>

                            </li>
                            <li>
                                Сокращать расходы без ущерба для качества
                            </li>
                            <li>
                                Автоматизировать свой бизнес, чтобы вы могли уезжать на несколько дней, недель или даже
                                месяцев
                            </li>
                        </ul>
                    </div>
                    <div class="picture">
                        <img src="../../assets/AboutAboutUs/wall2-min-2.png" alt="">
                    </div>
                </div>


            </div>
        </div>
    </div>
</template>

<style scoped>
.about-box {
    margin: 100px auto;
    width: 70%;
    font-family: 'Poppins', sans-serif;
    color: #333;
}

.about-content {
    display: flex;
    flex-direction: column;
    padding: 80px 0;
    gap: 120px;
}

/* Each section as a visual card */
.box {
    display: flex;
    align-items: center;
    gap: 50px;
    position: relative;
    min-height: 400px;
    text-align: justify;
}

.box:nth-child(1) {
    flex-direction: row;
}

.box:nth-child(2) {
    flex-direction: row-reverse;
}

/* Background Image Effect */
.picture {
    flex: 1 1 50%;
    position: relative;
    overflow: hidden;
}

.picture img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
    filter: brightness(0.85);
}

.picture::after {
    content: "";
    position: absolute;
    inset: 0;
}

.picture img:hover {
    transform: scale(1.08);
}

/* Text Styling */
.info {
    flex: 1 1 50%;
    font-size: 16px;
    line-height: 1.8;
    color: #222;
    padding: 20px 25px;
}

.info h5:first-child {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 15px;
    color: #1a1a1a;
    letter-spacing: 0.5px;
}

.info ul {
    list-style: none;
    padding: 0;
    margin-top: 15px;
}

.info ul li {
    position: relative;
    padding-left: 28px;
    margin-bottom: 10px;
}

.info ul li::before {
    content: "✔";
    position: absolute;
    left: 0;
    color: #ff6600;
    font-weight: bold;
}

/* Responsive */
@media (max-width: 992px) {
    .box {
        flex-direction: column !important;
        gap: 30px;
    }

    .info {
        padding: 0 10px;
        font-size: 16px;
    }

    .picture {
        width: 100%;
        max-height: 350px;
    }

    .about {
        margin: 0;
    }

    .about-content {
        padding-top: 0;
    }

;
}


</style>