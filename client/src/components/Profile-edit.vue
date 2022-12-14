<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {
      showModal: false,
    };
  },
});
</script>

<template>
  <button type="button" className="btn" @click="showModal = true">
    Edit Profile Details
  </button>
  <div className="popup" v-if="showModal">
    <h1>EDIT PROFILE DETAILS</h1>

    <h3>Email</h3>
    <input type="text" />
    <h3>Date of birth</h3>
    <textarea type="text" placeholder="Brief description about the product" />
    <h3>Upload Profile Image</h3>
    <input type="file" ref="fileInput" accept="image/*" />
    <button type="button" className="btn" @click="showModal = false">
      Confirm
    </button>
  </div>
</template>

<style scoped></style>
