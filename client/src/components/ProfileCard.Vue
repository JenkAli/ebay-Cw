<script lang="ts">
import EditProfile from "../components/Profile-edit.vue";
import { defineComponent } from "vue";
export default defineComponent({
  components: {
    EditProfile,
  },
  data() {
    return {
      users: [],
    };
  },
  mounted() {
    fetch(`http://127.0.0.1:8000/api/users/`, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        this.users = data;
      })
      .catch((err) => console.log(err));
  },
  methods: {

  },
});
</script>
<template>
  <div v-for="user in users" >
    <div className="profile">
      <img className="cardimg" src="" alt="No Image Found" />
      <div className="details">
        <div className="cardTitle">
          <div class="green">{{ user.email }}</div>
        </div>
        <div className="profileDetails">
          <div class="green">{{  }}</div>
        </div>
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
