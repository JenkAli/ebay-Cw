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
    Add a listing
  </button>
  <div className="popup" v-if="showModal">
    <h1>ADD A LISITING</h1>

    <h3>Title</h3>
    <input type="text" />
    <h3>Description</h3>
    <textarea type="text" placeholder="Brief description about the product" />
    <h3>Starting Price</h3>
    <input type="text" />
    <h3>Upload Image</h3>
    <input type="file" ref="fileInput" accept="image/*" />
    <button type="button" className="btn" @click="showModal = false">
      Confirm
    </button>
  </div>
</template>

<style scoped></style>
