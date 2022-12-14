<script setup lang="ts">
import EditProfile from "../components/Profile-edit.vue";
defineProps<{
  name: string;
  des: string;
  email: string;
  bday: string;
}>();
</script>

<template>
  <div className="profile">
    <img className="cardimg" src="" alt="No Image Found" />
    <div className="details">
      <div className="cardTitle">
        <div class="green">{{ name }}</div>
      </div>
      <div className="profileDetails">
        <div class="green">{{ des }}</div>
        <div class="green">{{ email }}</div>
        <div class="green">{{ bday }}</div>
      </div>
    </div>
  </div>
  <EditProfile />
</template>

<style scoped>
.cardTitle {
  font-size: 35px;
  margin-bottom: 1%;
}

.profile {
  display: flex;
  flex-direction: row;
  background: #eee;
  box-shadow: 0 8px 8px -4px lightblue;
  margin: 10px;
  height: 25rem;
}

.cardimg {
  width: 35%;
}

.profileDetails {
  height: 75%;
}

.details {
  margin-left: 1%;
  width: 65%;
}
</style>
