<script lang="ts">
import ProductTable from "../components/ProductCard.vue";
import AddButton from "../components/Button-add.vue";
import { defineComponent } from "vue";
import axios from "axios";
export default defineComponent ({
  components: {
    ProductTable,
  },
  mounted() {
    fetch(`http://127.0.0.1:8000/api/users/email/${localStorage.getItem("email")}`, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        localStorage.setItem("id", data.id);
        localStorage.setItem("date_of_birth", data.date_of_birth);
    })
    .catch((err) => console.log(err));
  }
})


</script>

<template>
  <ProductTable />
</template>

<style scoped></style>
