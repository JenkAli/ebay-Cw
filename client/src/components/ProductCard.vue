<script lang="ts">
import InfoButton from "./Button-info.vue";
import BidButton from "./Button-bid.vue";
import AddButton from "./Button-add.vue";
import { defineComponent } from "vue";
import moment from "moment";
export default defineComponent({
  filters: {
    moment: function (date) {
      return moment(date).format("MMMM Do YYYY, h:mm:ss a");
    },
  },
  components: {
    InfoButton,
    BidButton,
    AddButton,
  },
  data() {
    return {
      items: [],
      search: "",
    };
  },
  mounted() {
    fetch(`http://127.0.0.1:8000/api/items/`, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        this.items = data;
      })
      .catch((err) => console.log(err));
  },
  ready: function () {
    this.searched();
  },
  methods: {
    moment: function (item) {
      return moment(item);
    },
    async handleAdd() {
      await fetch(`http://127.0.0.1:8000/api/items/`, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((data) => {
          this.items = data;
        })
        .catch((err) => console.log(err));
    },

    async searched() {
      if (this.search !== "") {
        await fetch(`http://127.0.0.1:8000/api/items?q=${this.search}`, {
          method: "GET",
        })
          .then((response) => response.json())
          .then((data) => {
            this.items = data;
          })
          .catch((err) => console.log(err));
      } else {
        this.handleAdd();
      }
    },
  },
});
</script>

<template>
  <div className="buttonStyling">
    <AddButton @updateTable="handleAdd" />
    <button type="button" className="btn" @click="searched()">Search</button>
    <input type="text" v-model="search" placeholder="Search"/>
  </div>
  <div v-for="item in items" v-bind:key="item.id">
    <div className="card">
      <img className="cardimg" src:item.image alt="no image found" />
      <div className="details">
        <div className="cardTitle">
          <div class="green">{{ item.title }}</div>
          <div v-if="item.current_price != null" class="green">
            £{{ item.current_price }}
          </div>
          <div v-else-if="item.starting_price != null" class="green">
            £{{ item.starting_price }}
          </div>
        </div>
        <div className="description">
          <div class="green">{{ item.description }}</div>
        </div>
        <div className="btnContainer">
          <InfoButton
            :name="item.title"
            :des="item.description"
            :itemId="item.id"
          />
          <div class="green">
            Ending at
            {{ moment(item.expire_time).format("HH:mm, MMMM Do YYYY") }}
          </div>
          <BidButton
            :itemId="item.id"
            :name="item.title"
            :des="item.description"
            :currentPrice="Number(item.current_price)"
            :startingPrice="Number(item.starting_price)"
            @updateTable="handleAdd"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

.cardTitle {
  font-size: 35px;
  display: flex;
  justify-content: space-between;
}

.card {
  display: flex;
  flex-direction: row;
  background: #eee;
  box-shadow: 0 8px 8px -4px lightblue;
  margin: 10px;
  height: 15rem;
  max-height: 15rem;
  min-height: 15rem;
}
.cardimg {
  width: 35%;
}

.details {
  margin: 1%;
  display: flex;
  width: 65%;
  flex-direction: column;
  justify-content: space-between;
}

.btnContainer {
  display: flex;
  justify-content: space-between;
}
.buttonStyling {
  display: flex;
  flex-direction: row-reverse;
  width: 100%;
  align-items: center;
}
</style>
