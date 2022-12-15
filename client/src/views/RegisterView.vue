<template>
  <div class="parent">
    <div class="popup">
      <h1>Register</h1>
      <form @submit.prevent="submitForm">
        <label for="email">Email</label>
        <input
          type="text"
          placeholder="enter your email"
          name="email"
          v-model="email"
        /><br />

        <label for="date_of_birth">Date of birth</label>
        <input
          type="date"
          placeholder="Enter your dob"
          name="date_of_birth"
          v-model="date_of_birth"
        /><br />

        <label for="image">Profile picture</label>
        <input type="file" id="img" name="image" /><br />

        <label for="password">Password</label>
        <input
          class="loginInput"
          type="password"
          placeholder="Enter your password"
          name="password"
          v-model="password"
        /><br />

        <input className="btn" type="submit" />
        <p>Already have an account? <a href="{% url 'login' %}">Login</a></p>
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
      date_of_birth: "",
    };
  },
  methods: {
    async submitForm() {
      const formData = {
        email: this.email,
        password: this.password,
        dob: this.date_of_birth,
      };
      axios
        .post("http://127.0.0.1:8000/api/register/", formData)
        .then((response) => {
          this.$router.push("/");
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
  },
};
</script>
