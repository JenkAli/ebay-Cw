<script setup lang="ts">
defineProps<{
  name: string;
  des: string;
}>();
</script>

<template>
  <div className="card">
    <img className="cardimg" src="" alt="no image found" />
    <div className="details">
      <div className="cardTitle">
        <div class="green">{{ name }}</div>
      </div>
      <div className="description">
        <div class="green">{{ des }}</div>
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
  margin-bottom: 1%;
}

.card {
  display: flex;
  flex-direction: row;
  background: #eee;
  box-shadow: 0 8px 8px -4px lightblue;
  margin: 10px;
  height: 10rem;
}
.cardimg {
  width: 35%;
}

.details {
  margin-left: 1%;
  width: 65%;
}
</style>
