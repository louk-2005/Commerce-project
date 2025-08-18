<script setup>

</script>

<template>
    <div class="about">
        <div class="about-box">
            <div class="about-content">
                <div class="box">

                    <div class="info">
                        <h5>
                            نبذة عنا
                        </h5>
                        <p>
                            عشتار هو اسم إلهة بلاد ما بين النهرين، واسم البوابة والمدخل الرئيسي لمدينة بابل العظيمة.
                            عشتار هي إحدى العلامات التجارية التابعة لمجموعة باروس القابضة. أسس مؤسسو الشركة عام ٢٠٠٧
                            بهدف توفير أفضل المنتجات النفطية والاستفادة من إمكانات الشرق الأوسط في مجال المنتجات
                            النفطية. ينصب تركيزنا الرئيسي على توريد وتوزيع مختلف أنواع المنتجات النفطية والبتروكيماويات
                            والمعادن في الأسواق العالمية. نمت شبكتنا من الموردين والمشترين على مر الزمن بفضل الموثوقية
                            والشفافية. خلال هذه السنوات العشر، اكتسبت شركتنا سمعة طيبة ومصداقية في السوق وثقة عملائنا من
                            خلال تصدير سلع متنوعة إلى دول آسيا وأوروبا، مثل:
                        </p>
                    </div>
                    <div class="picture">
                        <img src="../../assets/AboutAboutUs/zitto_customize-min-2.png" alt="">
                    </div>
                </div>

                <div class="box">

                    <div class="info">
                        <h5>
                            مهمتنا
                        </h5>
                        <p>

                            <br>
                           برامجنا التدريبية المرموقة ستمكنك من:
                        </p>
                        <ul>
                            <li>
                                جذب عملاء متميزين وذوي رواتب عالية والاحتفاظ بهم
                            </li>
                            <li>
                                العمل لساعات أقل - وكسب المزيد من المال
                            </li>
                            <li>
                                جذب عملاء متميزين وذوي رواتب عالية والاحتفاظ بهم
                            </li>
                            <li>
                                إدارة وقتك لإنجاز المزيد في وقت أقل
                            </li>
                            <li>
                                صقل مهاراتك القيادية لإدارة فريقك
                            </li>
                            <li>
                                خفض النفقات دون التضحية بالجودة
                            </li>
                            <li>
                                أتمتة أعمالك، لتتمكن من ترك العمل لأيام أو أسابيع أو حتى أشهر متتالية
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
.about {
    direction: rtl;       /* نوشتار راست به چپ */
    text-align: right;    /* همه متن‌ها از راست شروع بشن */
}

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
    padding-right: 28px;   /* چون راست‌چینه باید جایگزین padding-left بشه */
    margin-bottom: 10px;
}

.info ul li::before {
    content: "✔";
    position: absolute;
    right: 0;              /* جایگزین left برای راست‌چین */
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
}



</style>