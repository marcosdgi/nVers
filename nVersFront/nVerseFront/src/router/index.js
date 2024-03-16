import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ServiceView from "@/views/ServiceView.vue";
import ProjectsView from "@/views/ProjectsView.vue";
import ContactView from "@/views/ContactView.vue";
import BlogSite from "@/views/BlogSite.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/home',
            name: 'home',
            component: HomeView
        },
        {
            path: '/contact',
            name: 'contact',
            component: ContactView
        },
        {
            path: '/services',
            name: 'services',
            component: ServiceView
        },
        {
            path: '/projects',
            name: 'projects',
            component: ProjectsView
        },
        {
            path:'/blog',
            name:'blogsite',
            component:BlogSite
        }


    ]
})

export default router
