<template>
  <div class="carousel">
    <div class="images" :style="{ transform: `translateX(${pos}em)`}">

      <template v-for="(project, index) in projects" :key="index">
        <div
            :class="{ active: index === currentImage,
              'opacity-0' :index <= currentImage-1 || index>=currentImage+1,
               'low': index<=currentImage-2,
                'more': index >=currentImage+2 }"/>
        <div class="card">
          <div class="d-flex justify-content-center"
               style="background: linear-gradient(to right, rgb(13, 10, 78), rgb(19, 16, 120)); ">
            <img :src="'http://localhost:8000'+ project.image"
                 class="card-img-top overflow-hidden">
          </div>
          <div class="card-body text-light"
               style="background: linear-gradient(to right, rgb(13, 10, 78), rgb(19, 16, 120)); ">
            <h5 class="card-title">{{ project.name }}</h5>
            <p class="card-text">{{ project.description }}</p>
            <p class="card-text"><small class="text-light">{{ project.release_date }}</small></p>
          </div>
        </div>
      </template>

    </div>
  </div>
  <div class="d-flex justify-content-center align-items-center" :class="{'d-none': projects.length===0}">
    <button @click="next" class="btn" :class="{'position-absolute ':projects.length !==0}"
            style="top: 90%; right: 39%;">
      <img src="/next.png">


    </button>
    <button @click="previous" class="btn" :class="{'position-absolute':projects.length !==0}"
            style="top: 90%; left: 30%; background-color: transparent ">
      <img src="/previus.png">
    </button>
  </div>
  <div class="">
    <button @onmouseenter="hovering" @onmouseleave="dishovering" class="btn" style="margin-left: 20%;" @click="toHome"
            :class="{'start-100 bottom-25':projects.length !==0,
     'animate__animated animate__pulse': isHovering}">
      <img src="/home.png" width="35rem">
      <div style="background-color: rgba(128,128,128,0.51); border-radius: 10px; padding: 5px"
           :class="{'d-none display-6': projects.length!==0}">
        Go Home
      </div>
    </button>

  </div>
  <div class="container" style="margin-left: 5% " v-if="projects.length===0">
    <h1 class="display-6">
      "As good minimalists, we have reduced this page to nothing. Another try?”
    </h1>
    <hr width="90%">
    <h3 style="color: blue;">404 </h3>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue';
import axios from "axios";
import router from "@/router/index.js";
import NotFound from "@/components/NotFound.vue";


const toHome = () => {
  router.push('/home')
}

let currentImage = ref(0);

let pos = ref(10)
const isHovering = ref(false)
const hovering = () => {
  isHovering.value = true
  console.log(isHovering.value)
}
const dishovering = () => {
  isHovering.value = false
  console.log(isHovering.value)

}
const next = () => {
  if (currentImage.value === projects.value.length) {
    currentImage.value = -1;
    pos.value = 15;
  } else {
    pos.value -= 15;
  }

  currentImage.value++;
};

const previous = () => {
  if (currentImage.value === 0) {
    currentImage.value = projects.value.length;
    pos.value = 15 - (projects.value.length - 1) * 20;
  } else {
    pos.value += 15;
  }
  currentImage.value--;
};


const projects = ref([])
const getProjects = async () => {
  try {
    const response = await axios.get('http://localhost:8000/projects/list_projects/')
    projects.value = response.data
    return true
  } catch (error) {
    console.error(error)
    return false
  }
}
onMounted(() => {
  getProjects()
})
</script>

<style scoped>
.carousel {

  display: flex;
  align-items: center;
  overflow: hidden;
  height: 25rem;
  position: relative;
}

.card {
  border: none;
  box-shadow: 10px 10px 20px black;
  width: 20rem;
}

.carousel .images {
  display: flex;
  justify-content: flex-start;
  gap: 10px;
  transition: transform 0.5s ease-in-out;
  border-radius: 30px;
}

.carousel img {
  width: 300px;
  height: 200px;
  object-fit: cover;
  opacity: 0.5;
  transition: opacity 0.5s ease-in-out;
}

.carousel img.active {
  opacity: 1;
  transform: scale(1.2);
  z-index: 1;
  box-shadow: black 0px 0px 20px;
}

.more {
  transform: translateX(-80px);
}

.low {
  transform: translateX(80px);
}
</style>