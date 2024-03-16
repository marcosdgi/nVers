<script setup>

import Carousel from "@/components/Carousel.vue";
import {ref} from "vue";
import CarouselProjects from "@/components/CarouselProjects.vue";

const clicked = ref(false)

</script>

<template>
  <div class="d-flex align-items-center">
    <div class="w-25">
          <img src="/logo2.png" width="40%" style="top: 10rem">
      <div class=" d-flex align-items-start" style="margin-top: 30%">
          <h1 class="vertical-text display-1 fw-bolder">Projects. </h1>
        <div style="top: 10rem;">
        </div>
        <div class="">
          <p class="horizontal-text display-6">
            <img src="/Logo.png" width="100%"></p>
          <p class="horizontal-text display-6 text-center">was
            born from
            the need
            to turn
            digital noise
            into clear
            messages</p>
        </div>
      </div>
    </div>
    <CarouselProjects/>
  </div>
</template>

<style scoped>

.vertical-text {
  writing-mode: vertical-rl;
  height: 18rem;
  transform: rotate(180deg);
  opacity: 0.5;
  margin-left: 0;
  margin-top: 5%;
  margin-right: 0;
  box-shadow: white 5px 5px 20px;
}

.horizontal-text {
  font-size: 170%;
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 0;
  align-self: center;
  text-align: justify;
  transition: opacity 0.5s ease-in-out;
}
</style>