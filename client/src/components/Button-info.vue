<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  props: {
    name: String,
    des: String,
    img: Image,
    itemId: Number,
  },
  data() {
    return {
      showModal: false,
      questions: [],
      answers: [],
      QandA: [],
      asking: {
        question: "",
        item: this.itemId,
        user: 2,
      },
    };
  },
  methods: {
    getInfo() {
      this.showModal = true;
      fetch(`http://127.0.0.1:8000/api/items/${this.itemId}/questions/ `, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((data) => {
          this.questions = data;
        })
        .catch((err) => console.log(err));
      fetch(`http://127.0.0.1:8000/api/items/${this.itemId}/answers/ `, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((data) => {
          this.answers = data;
        })
        .catch((err) => console.log(err));
      this.QandA = this.questions.map((q) => ({
        ...q,
        ...this.answers.find((a) => a.question === q.id),
      }));
    },
    ask() {
      fetch(`http://127.0.0.1:8000/api/items/${this.itemId}/questions/ `, {
        method: "POST",
        body: JSON.stringify({
          question: this.asking.question,
          item: this.itemId,
          user: 1,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          this.answers = data;
        })
        .catch((err) => console.log(err));
      setTimeout(() => this.getInfo(), 100);
      this.asking.question = "";
    },
  },
});
</script>

<template>
  <button type="button" className="btn" @click="getInfo">More Info</button>
  <div className="popup" v-if="showModal">
    <img className="cardimg" src:img alt="no image found" />
    <h1>{{ name }}</h1>
    <h2>Description</h2>
    <h3>{{ des }}</h3>
    <h2>Q&A</h2>
    <div v-for="item in QandA" v-bind:key="item.id">
      <h3>Q: {{ item.question }}</h3>
      <h3>A: {{ item.answer }}</h3>
    </div>
    <input
      type="text"
      placeholder="Add your own question"
      v-model="asking.question"
    />
    <button type="button" className="btn" @click="ask">Ask</button>
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
