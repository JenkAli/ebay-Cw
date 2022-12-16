<script lang="ts">
import EditProfile from "../components/Profile-edit.vue";
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {
      email: localStorage.getItem("email"),
      dob: localStorage.getItem("date_of_birth"),
    };
  },
  methods: {
    getlocalstorage() {
      this.email = localStorage.getItem("email");
      this.dob = localStorage.getItem("date_of_birth");
    },
  },
  components: {
    EditProfile,
  },
});
</script>
<template>
  <div className="profile">
    <img className="cardimg" src="" alt="No Image Found" />
    <div className="details">
      <div className="cardTitle">
        <div class="green">{{this.email}}</div>
        <div class="green">{{this.dob}}</div>
      </div>
      <div className="profileDetails">
        <div class="green">{{  }}</div>
      </div>
    </div>
  </div>
  <EditProfile @updateProfile="getlocalstorage"/>
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
