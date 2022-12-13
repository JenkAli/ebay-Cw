<script setup lang="ts">
import InfoButton from "./Button-info.vue";
import BidButton from "./Button-bid.vue";
defineProps<{
  name: string;
  des: string;
  startPrice: number;
}>();
</script>

<template>
  <div className="card">
    <img className="cardimg" src="" alt="no image found" />
    <div className="details">
      <div className="cardTitle">
        <div class="green">{{ name }}</div>
        <div class="green">£{{ startPrice }}</div>
      </div>
      <div className="description">
        <div class="green">{{ des }}</div>
      </div>
      <div className="btnContainer">
        <InfoButton :name="name" :des="des" />
        <BidButton :name="name" :des="des" :currentPrice="startPrice" />
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
</style>
