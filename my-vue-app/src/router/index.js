import { createRouter, createWebHistory } from "vue-router"

const Home = () => import("../pages/home/home.vue")
const About = () => import("../pages/about/about.vue")
const ContactUs = () => import("../pages/contactUs/contactUs.vue")
const Products = () => import("../pages/products/products/products.vue")
const Category = () => import("../pages/category/category.vue")
const Product = () => import("../pages/products/product/product.vue")



const routes = [
    { path: "/", name: "Home", component: Home },
    { path: "/about", name: "About", component: About },
    { path: "/contact/us", name: "ContactUs", component: ContactUs },
    { path: "/products", name: "Products", component: Products },
    {path: '/category/:id', name: "Category", component: Category},
    {path: "/product/:id", name: "Product", component: Product}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to, from, savedPosition) {
        // اگر برگشت به عقب یا جلو (history) باشه
        if (savedPosition) {
            return savedPosition
        }
        // در حالت عادی برو بالای صفحه
        return { top: 0 }
    }
})

export default router
