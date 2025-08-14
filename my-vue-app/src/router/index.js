import { createRouter, createWebHistory } from "vue-router"

const Home = () => import("../pages/home/home.vue")
const About = () => import("../pages/about/about.vue")
const ContactUs = () => import("../pages/contactUs/contactUs.vue")
const Products = () => import("../pages/products/products.vue")



const routes = [
    { path: "/", name: "Home", component: Home },
    {path: "/about", name: "About", component: About},
    {path: "/contact/us", name: "ContactUs", component: ContactUs},
    {path: "/products", name: "Products", component: Products}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
