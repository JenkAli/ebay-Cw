<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  props: {
    name: String,
    des: String,
    currentPrice: Number,
  },
  data() {
    return {
      showModal: false,
    };
  },
});
</script>

<template>
  <button type="button" className="btn" @click="showModal = true">Bid</button>
  <div className="popup" v-if="showModal">
    <h1>Bidding for : {{ name }}</h1>
    <h1>Current Price: £{{ currentPrice }}</h1>
    <vue-number-input
      v-model="value"
      :min="currentPrice"
      inline
      controls
      size="medium"
    ></vue-number-input>
    <button type="button" className="btn" @click="showModal = false">
      Confirm
    </button>
  </div>
</template>

<style scoped>
.vue-number-input {
  width: 50%;
}
</style>
