<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  emits: ["updateTable"],
  data() {
    return {
      showModal: false,
      error: "",
      img: {},
      fle: {},
      itemData: {
        id: "",
        title: "",
        description: "",
        owner: localStorage.getItem("id"),
        starting_price: 0,
        expire_time: "",
      },
    };
  },
  methods: {
    async sumbitted() {
      if (
        this.itemData.title == "" ||
        this.itemData.description == "" ||
        this.itemData.starting_price == 0 ||
        this.itemData.expire_time == ""
      ) {
        this.error = "Please complete all fields as prompted";
      } else {
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
        })
          .then((response) => response.json())
          .then((data) => {
            setTimeout(() => this.$emit("updateTable"), 100);
            setTimeout(() => this.submitImage(data.id), 200);
          })
          .catch((err) => console.log(err));
      }
    },
    cancel() {
      this.error = "";
      this.showModal = false;
    },
    async uploadImage() {
      const file = this.$refs.fileInput.files[0];
      this.fle = file;
    },
    async submitImage(id) {
      const formData = new FormData();
      formData.append("image", this.fle);
      try {
        const response = await fetch(
          `http://127.0.0.1:8000/api/items/${id}/image/`,
          {
            method: "POST",
            body: formData,
          }
        );
        console.log(response);
      } catch (error) {
        console.error(error);
      }
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
    <input type="datetime-local" v-model="itemData.expire_time" />
    <h3>Upload Image</h3>
    <input type="file" ref="fileInput" @change="uploadImage" />
    <div className="err">{{ error }}</div>
    <button type="button" className="btn" @click="sumbitted">Confirm</button>
    <button type="button" className="btn" @click="cancel">Cancel</button>
  </div>
</template>

<style scoped></style>
