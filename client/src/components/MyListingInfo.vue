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
      replyText: "",
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
          this.QandA = data;
          this.questions = JSON.parse(JSON.stringify(this.QandA));
        })
        .catch((err) => console.log(err));
    },
    reply(questionId) {
      if (this.replyText !== "") {
        fetch(`http://127.0.0.1:8000/api/items/${questionId}/answer/ `, {
          method: "POST",
          body: JSON.stringify({
            answer_text: this.replyText,
            userId: localStorage.getItem("id"),
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            this.answers = data;
          })
          .catch((err) => console.log(err));
        setTimeout(() => this.getInfo(), 100);
        this.asking.question = "";
      }
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
    <div v-for="q in questions" v-bind:key="q.id">
      <h3>Q: {{ q.question }}</h3>
      <h3 v-if="q.answer">A: {{ q.answer }}</h3>
      <div v-else-if="!q.answer">
        <input type="text" placeholder="Add your reply" v-model="replyText" />
        <button type="button" className="btn" @click="reply(q.id)">
          Reply
        </button>
      </div>
    </div>
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
