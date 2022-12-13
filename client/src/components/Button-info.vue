<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  props: {
    name: String,
    des: String,
    img: Image,
  },
  data() {
    return {
      showModal: false,
    };
  },
});
</script>

<template>
  <button type="button" className="btn" @click="showModal = true">
    More Info
  </button>
  <div className="popup" v-if="showModal">
    <img className="cardimg" src:img alt="no image found" />
    <h1>{{ name }}</h1>
    <h2>Description</h2>
    <h3>{{ des }}</h3>
    <h2>Q&A</h2>
    <input type="text" placeholder="Add your own question" />
    <h2>Q&A</h2>
    <h2>Q&A</h2>
    <h2>Q&A</h2>
    <button type="button" className="btn" @click="showModal = false">
      Done
    </button>
  </div>
</template>

<style scoped>
.cardimg {
  height: 20rem;
  border: 1px solid;
  min-height: 20rem;
}
</style>
