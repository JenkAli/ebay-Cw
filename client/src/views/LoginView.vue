<template>
  <div class="parent">
    <div class="loginForm">
      <h1>Login Page</h1>

      <form @submit.prevent="submitForm">
        <label>Email:</label>
        <input
          class="loginInput"
          type="text"
          placeholder="Enter your email"
          name="email"
          v-model="email"
        /><br />

        <label>Password:</label>
        <br />
        <input
          class="loginInput"
          type="password"
          placeholder="Enter your password"
          name="password"
          v-model="password"
        /><br />

        <button class="loginButton" type="submit">Submit</button>
        <p>dont have an account? <a href="/register">Register</a></p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async submitForm() {
      const formData = {
        email: this.email,
        password: this.password,
      };
      axios
        .post("http://127.0.0.1:8000/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token, this.email);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          localStorage.setItem("email", this.email);
          this.$router.push("/market");
      }).catch((error) => {
        console.log("error", error);
      })
    },
  },
};
</script>
