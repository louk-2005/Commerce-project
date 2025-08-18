<script setup>

</script>

<template>
    <div class="about">
        <div class="about-box">
            <div class="about-content">
                <div class="box">

                    <div class="info">
                        <h5>
                            About us
                        </h5>
                        <p>
                            Ishtar was the name of the Mesopotamian goddess and was name of the gate and main entrance
                            into
                            the great city of Babylon.

                            Ishtar is one of the brands which belongs to Barus Holding Group. The founders in the year
                            2007
                            have established the company with the aim of better providing and making use of Middle East
                            potentials in the field of Petroleum Products.
                            Our main focus is on sourcing, supplying and distribution of different kinds of Petroleum
                            Products, Petrochemicals and Minerals in the international markets. Our network of suppliers
                            and
                            buyers has grown over a period of time with reliability and transparency. During these 10
                            years,
                            our company has earned a great reputation and credibility in the market and a trust from our
                            clients by exporting different commodities to the countries of Asia and Europe such as
                        </p>
                    </div>
                    <div class="picture">
                        <img src="../../assets/AboutAboutUs/zitto_customize-min-2.png" alt="">
                    </div>
                </div>

                <div class="box">

                    <div class="info">
                        <h5>
                            OUR MISSION
                        </h5>
                        <p>

                            <br>
                            Our renowned coaching programs will allow you to:
                        </p>
                        <ul>
                            <li>
                                Attract and retain quality, high-paying customers
                            </li>
                            <li>
                                Work fewer hours — and make more money
                            </li>
                            <li>
                                Attract and retain quality, high-paying customers
                            </li>
                            <li>
                                Manage your time so you’ll get more done in less time
                            </li>
                            <li>
                                Hone sharp leadership skills to manage your team
                            </li>
                            <li>
                                Cut expenses without sacrificing quality
                            </li>
                            <li>
                                Automate your business, so you can leave for days, weeks, or even months at a time
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
    .about{
        margin: 0;
    }
    .about-content{
        padding-top: 0;
    }

;
}


</style>