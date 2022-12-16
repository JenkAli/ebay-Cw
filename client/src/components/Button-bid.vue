<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  emits: ["updateTable"],
  props: {
    itemId: Number,
    name: String,
    des: String,
    currentPrice: Number,
    startingPrice: Number,
  },
  data() {
    return {
      showModal: false,
      value: this.currentPrice,
      itemName: this.name,
      itemCurrentPrice: this.currentPrice,
      itemStartingPrice: this.startingPrice,
      itemDes: this.des,
      error: "",
    };
  },
  methods: {
    bid() {
      if (this.value <= this.itemCurrentPrice) {
        this.error = "Please complete all fields as prompted";
      } else {
        this.showModal = false;
        fetch(`http://127.0.0.1:8000/api/items/${this.itemId}/`, {
          method: "PUT",
          body: JSON.stringify({
            current_price: this.value,
            current_bidder: localStorage.getItem("id"),
          }),
        });
        setTimeout(() => this.$emit("updateTable"), 100);
      }
    },
    cancel() {
      this.error = "";
      this.showModal = false;
    },
  },
});
</script>

<template>
  <button type="button" className="btn" @click="showModal = true">Bid</button>
  <div className="popup" v-if="showModal">
    <h1>{{ itemName }}</h1>
    <h3>{{ itemDes }}</h3>
    <h1>Current Price: £{{ itemCurrentPrice }}</h1>
    <h1>Starting Price: £{{ itemStartingPrice }}</h1>
    <vue-number-input
      v-if="itemCurrentPrice == 0 || itemCurrentPrice == null"
      v-model="value"
      :min="itemStartingPrice"
      inline
      controls
      size="medium"
    ></vue-number-input>
    <vue-number-input
      v-else-if="itemStartingPrice && itemCurrentPrice"
      v-model="value"
      :min="itemCurrentPrice"
      inline
      controls
      size="medium"
    ></vue-number-input>
    <div className="err">{{ error }}</div>
    <button type="button" className="btn" @click="bid">Bid</button>
    <button type="button" className="btn" @click="cancel">Cancel</button>
  </div>
</template>

<style scoped>
.vue-number-input {
  width: 25%;
}
</style>
