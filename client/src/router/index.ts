import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProfileView from "../views/AboutView.vue";
import Login from "../views/LoginView.vue";
import Register from "../views/RegisterView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/market",
      name: "marketplace",
      component: HomeView,
      beforeEnter: () => {
        if (localStorage.getItem("token") == null) router.push("/");
      },
    },
    {
      path: "/",
      name: "login",
      component: Login,
    },
    {
      path: "/register",
      name: "register",
      component: Register,
    },
    {
      path: "/profile",
      name: "profile",
      component: ProfileView,
      beforeEnter: () => {
        if (localStorage.getItem("token") == null) router.push("/");
      },
    },
  ],
});

export default router;
