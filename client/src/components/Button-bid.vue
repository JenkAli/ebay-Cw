<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  props: {
    itemId: Number,
    name: String,
    des: String,
    currentPrice: String,
    startingPrice: String,
  },
  data() {
    return {
      showModal: false,
      value: this.currentPrice,
      itemName: this.name,
      itemCurrentPrice: this.currentPrice,
      itemStartingPrice: this.startingPrice,
      itemDes: this.des,
    };
  },
  methods: {
    bid() {
      this.showModal = false;
      this.$emit("updateTable");
      fetch(`http://127.0.0.1:8000/api/items/${this.itemId}/`, {
        method: "PUT",
        body: JSON.stringify({
          current_price: this.value,
          current_bidder: 1,
        }),
      });
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
      v-model="value"
      :min="itemStartingPrice"
      inline
      controls
      size="medium"
    ></vue-number-input>
    <button type="button" className="btn" @click="bid">Bid</button>
    <button type="button" className="btn" @click="showModal = false">
      Cancel
    </button>
  </div>
</template>

<style scoped>
.vue-number-input {
  width: 25%;
}
</style>
