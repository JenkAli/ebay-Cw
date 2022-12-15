<script setup lang="ts">
import ProductCard from "../components/ProductCard.vue";
import AddButton from "../components/Button-add.vue";

</script>

<template>
  <div className="buttonStyling">
    <AddButton />
  </div>
  <ProductCard name="Car" des="Drives" startPrice="10" />
  <ProductCard name="Bottle" des="Made from plastic" />
  <ProductCard name="Bottle" des="Made from plastic" />
</template>

<style scoped>
.buttonStyling {
  display: flex;
  flex-direction: row-reverse;
  width: 100%;
}
</style>
