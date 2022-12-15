<script lang="ts">import image from '/Users/pkonduru/ebay-Cw/client/src/pic.png'
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {
      users: [],
      showModal: false,
    };
  },
  mounted() {
    fetch(`http://127.0.0.1:8000/api/users/3/`, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        this.users = data;
      })
      .catch((err) => console.log(err));
  },
  methods: {
    update() {
      fetch(`http://127.0.0.1:8000/api/users/${3}/`, {
        method: "PUT",
        body: JSON.stringify({
          email: "hellohello@gmail.com",
          date_of_birth: "2006-05-06", 
        }),
      });
      setTimeout(() => this.$emit("updateTable"), 100);
    }
  },
});
</script>
<template>
  <div>
    <button type="button" className="btn" @click="showModal = true">
      Edit Profile Details
    </button>
    <div className="popup" >
      <h1>EDIT PROFILE DETAILS</h1>
      <h3>{{  }}</h3>
      <textarea type="text" placeholder="text"/>
      <h3>Date of birth</h3>
      <textarea type="text" placeholder="Brief description about the product" />
      <h3>Upload Profile Image</h3>
      <input type="file" ref="fileInput" accept="image/*" />
      <button type="button" className="btn" @click="update">
        Confirm
      </button>
    </div>
  </div>
</template>

<style scoped></style>
