<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  emits: ["updateTable"],
  data() {
    return {
      showModal: false,
      itemData: {
        title: "",
        description: "",
        owner: 1,
        starting_price: 0,
        expire_time: "2022-12-15T15:15:00Z",
      },
    };
  },
  methods: {
    async sumbitted() {
      this.showModal = false;
      await fetch(`http://127.0.0.1:8000/api/items/`, {
        method: "POST",
        body: JSON.stringify({
          title: this.itemData.title,
          description: this.itemData.description,
          owner: this.itemData.owner,
          starting_price: this.itemData.starting_price,
          expire_time: this.itemData.expire_time,
        }),
      });
      setTimeout(() => this.$emit("updateTable"), 100);
    },
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
    <input type="text" v-model="itemData.title" />
    <h3>Description</h3>
    <textarea
      type="text"
      placeholder="Brief description about the product"
      v-model="itemData.description"
    />
    <h3>Starting Price</h3>
    <input type="Number" v-model="itemData.starting_price" />
    <h3>Expire Time</h3>
    <input type="date" v-model="itemData.expire_time" />
    <h3>Upload Image</h3>
    <input type="file" ref="fileInput" accept="image/*" />
    <button type="button" className="btn" @click="sumbitted">Confirm</button>
    <button type="button" className="btn" @click="showModal = false">
      Cancel
    </button>
  </div>
</template>

<style scoped></style>
