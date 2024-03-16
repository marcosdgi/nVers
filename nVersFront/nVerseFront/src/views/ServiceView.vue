<script setup>

import Carousel from "@/components/Carousel.vue";
import {ref} from 'vue';
import router from "@/router/index.js";

const showOverlay = ref(false);

const handleMouseEnter = () => {
  showOverlay.value = true;
  console.log(showOverlay.value)
};

const handleMouseLeave = () => {
  showOverlay.value = false;
  console.log(showOverlay.value)

};
const toHome = () => {
  router.push('/home')
}
const toProjects = () => {
  router.push('/projects')
}
const toContact = () => {
  router.push('/contact')
}
const toBlog = () => {
  router.push('/blog')
}
</script>

<template>
  <div :class="{'overlay':showOverlay}">
    <button class="corner button top-left" style="border-bottom-right-radius: 70px"
            @mouseenter="handleMouseEnter"
            @click="toHome"
            @mouseleave="handleMouseLeave">
      <img src="/home.png" width="60rem">
      <div class="title display-4">
        Home
      </div>

    </button>
    <button class="corner button top-right" style="border-bottom-left-radius: 70px" @mouseenter="handleMouseEnter"
            @click="toProjects"
            @mouseleave="handleMouseLeave">
      <img src="/projects4.png" width="60rem">

      <div class="title display-4">
        Projects
      </div>

    </button>
    <button class="corner button bottom-left" style="border-top-right-radius: 70px"
            @mouseenter="handleMouseEnter"
            @mouseleave="handleMouseLeave"
            @click="toBlog">

      <img src="/blog.png" width="60rem">

      <div class="title display-4">
        Blog
      </div>

    </button>
    <button class="corner button bottom-right" style="border-top-left-radius: 70px" @mouseenter="handleMouseEnter"
            @mouseleave="handleMouseLeave" @click="toContact">

      <img src="/contact.png" width="60rem">

      <div class="title display-4">
        Contact
      </div>

    </button>

    <div class="center-content w-100">
      <div class="d-flex justify-content-center">
        <h1 class="display-3 fw-bolder">
          Services and Pricing
          <hr>
          <p class="display-6">
            ( just one payment )
          </p>
        </h1>

      </div>
      <div>
        <Carousel/>
      </div>
    </div>
    <div>

    </div>
  </div>
</template>

<style scoped>
.containers {
  width: 100vw;
  height: 100vh;
}

.corner {
  position: absolute;
  width: 18rem;
  height: 10rem;
  background: linear-gradient(to right, rgb(13, 10, 78), rgb(19, 16, 120));
  color: white;
  text-align: center;
  line-height: 50px;
  transition: all 0.5s ease;
  z-index: 2;
  border: none;
  pointer-events: all;
}

.corner:hover {
  width: 30rem;
  height: 20rem;

}

.title {
  opacity: 0;
  transition: opacity 0.5s ease;
}

.button:hover .title {
  opacity: 1;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1;
  pointer-events: none;
}


.top-left {
  top: 0;
  left: 0;
}

.top-right {
  top: 0;
  right: 0;
}

.bottom-left {
  bottom: 0;
  left: 0;
}

.bottom-right {
  bottom: 0;
  right: 0;
}

.center-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>