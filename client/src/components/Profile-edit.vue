<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {
      showModal: false,
      id: localStorage.getItem("id"),
      email: localStorage.getItem("email") || "",
      dob: localStorage.getItem("date_of_birth") || "",
    };
  },
  methods: {
    update() {
      this.showModal = false;
      fetch(`http://127.0.0.1:8000/api/users/${this.id}`, {
        method: "PUT",
        body: JSON.stringify({
          email: this.email,
          date_of_birth: this.dob,
        }),
      }).then(
        localStorage.setItem("email", this.email),
        localStorage.setItem("date_of_birth", this.dob),
        window.location.reload(),
        setTimeout(() => this.$emit("updateProfileCard"), 100)
      );
    },
  },
});
</script>
<template>
  <div>
    <button type="button" className="btn" @click="showModal = true">
      Edit Profile Details
    </button>
    <div className="popup" v-if="showModal">
      <h1>EDIT PROFILE DETAILS</h1>
      <textarea type="text" placeholder="enter email" v-model="email" />
      <h3>Date of birth</h3>
      <textarea type="text" placeholder="enter dob" v-model="dob" />
      <h3>Upload Profile Image</h3>
      <input type="file" ref="fileInput" accept="image/*" />
      <button type="button" className="btn" @click="update">Confirm</button>
    </div>
  </div>
</template>

<style scoped></style>
