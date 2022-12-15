<script>
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";

export default {
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push("/");
    },
  },
};
</script>

<template>
  <div className="wrapper">
    <nav>
      <div className="logoclass">
        <RouterLink to="/market">Logo</RouterLink>
      </div>
      <div className="items">
        <a v-on:click="logout" href="#">Log Out</a>
        <RouterLink to="/market">Market Place</RouterLink>
        <RouterLink to="/profile">Profile</RouterLink>
      </div>
    </nav>
    <RouterView />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 1.5rem;
  padding: 1;
  display: "flex";
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: #00cfc1;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.wrapper {
  display: flex;
  flex-direction: column;
}

.logoclass {
  text-align: "right";
}

.items {
  text-align: "left";
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    margin-left: -1rem;
    font-size: 1.5rem;
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
