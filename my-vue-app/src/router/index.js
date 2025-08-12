import { createRouter, createWebHistory } from "vue-router"

const Home = () => import("../pages/home/home.vue")

const routes = [
    { path: "/", name: "Home", component: Home },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
