<script lang="ts">
import MyListingInfoButton from "./MyListingInfo.vue";
import { defineComponent } from "vue";
import moment from "moment";
export default defineComponent({
  filters: {
    moment: function (date) {
      return moment(date).format("MMMM Do YYYY, h:mm:ss a");
    },
  },
  components: {
    MyListingInfoButton,
  },
  data() {
    return {
      items: [],
      search: "",
      userId: localStorage.getItem("id"),
    };
  },
  mounted() {
    fetch(`http://127.0.0.1:8000/api/items/user/${this.userId}/`, {
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
  },
});
</script>

<template>
  <h1 class="green">MY LISTINGS</h1>
  <h2 class="green">You Can Reply To Questions Here</h2>
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
          <MyListingInfoButton
            :name="item.title"
            :des="item.description"
            :itemId="item.id"
          />
          <div class="green">
            Ending at
            {{ moment(item.expire_time).format("HH:mm, MMMM Do YYYY") }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.mylisting {
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
