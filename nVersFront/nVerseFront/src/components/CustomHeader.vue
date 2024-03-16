<script setup>
import 'animate.css'
import {ref} from 'vue';
import router from "@/router/index.js";

const isAnimating = ref(true)

const stopAnimation = () => {
  isAnimating.value = false
  console.log(isAnimating.value)
}
const startAnimation = () => {
  isAnimating.value = true
  console.log(isAnimating.value)
}
const toServices = () => {
  router.push('/services')
}
const toBlog = () => {
  router.push('/blog')
}
const toContact = () => {
  router.push('/contact')
}
const toProjects = () => {
  router.push('projects')
}
</script>

<template>
  <div class="Principal d-flex justify-content-center align-items-center">
    <div id="logo">
      <img src="/Logo.png" width="400rem">
    </div>

    <div class="oval-container d-flex align-items-center " @click="">
      <div>
      </div>
      <button @click="toProjects" class="oval oval1" :class="{'animated': !isAnimating}" style="height: 20rem"
              @mouseenter="stopAnimation"
              @mouseleave="startAnimation">
        <img src="/projectsHome.png" :class="{'animate__animated animate__heartBeat':!isAnimating}">
      </button>

      <button class="oval oval2" :class="{'animated': !isAnimating}" @mouseenter="stopAnimation"
              @click="toServices"
              @mouseleave="startAnimation">
        <img class="img" src="/Services.png" width="100%"
             :class="{'animate__animated animate__heartBeat':!isAnimating}">

        </img>
      </button>
      <button class="oval oval3" style="height:25rem" :class="{'animated': !isAnimating}" @mouseenter="stopAnimation"
              @mouseleave="startAnimation" @click="toContact">
        <img src="/contactHome.png" alt="" width="130%" :class="{'animate__animated animate__heartBeat':!isAnimating}">
      </button>
      <div class="oval oval4" style="height: 20rem" :class="{'animated': !isAnimating}" @mouseenter="stopAnimation"
           @mouseleave="startAnimation" @click="toBlog">
        <img src="/blogHome.png" height="80%" width="100%"
             :class="{'animate__animated animate__heartBeat':!isAnimating}">
      </div>

    </div>

  </div>

</template>

<style scoped>
.oval {
  border-radius: 100px;
  background: linear-gradient(to bottom, rgb(13, 10, 78), rgb(19, 16, 120));
  width: 13rem;
  height: 25rem;
  overflow: hidden;
  margin-right: 4%;
  margin-top: 3%;
  //position: relative;
  border: none;
}

#logo {
  margin: 0;
}

.Principal {
  height: 48rem;
}


.oval1 {
  display: flex;
  justify-content: center;
  animation: resize-box-1 1.8s ease-in-out 0.55s infinite;

}

.oval:hover {
  box-shadow: 10px 10px 30px black;
  transition: all 0.5s ease-in-out;
}

.oval2 {
  animation: resize-box-2 1.8s ease-in-out 0.25s infinite;
}

.img {
  z-index: 2;
  width: 15rem;
}

.oval3 {
  animation: resize-box-3 1.8s ease-in-out 0.25s infinite;

  transform: scaleY(1.2);
}

.oval4 {
  animation: resize-box-4 1.8s ease-in-out 0.75s infinite;
}


@keyframes resize-box-1 {
  0% {
    transform: scaleY(0.7);
  }


  50% {
    transform: scaleY(1);
  }

  100% {
    transform: scaleY(0.7);
  }
}


@keyframes resize-box-2 {
  0% {
    transform: scaleY(1);
  }


  50% {
    transform: scaleY(0.7);
  }

  100% {
    transform: scaleY(1);
  }
}

@keyframes resize-box-3 {
  0% {
    transform: scaleY(1.1);
  }


  50% {
    transform: scaleY(0.8);
  }

  100% {
    transform: scaleY(1.1);
  }
}

@keyframes resize-box-4 {
  0% {
    transform: scaleY(1);
  }


  50% {
    transform: scaleY(0.6);
  }

  100% {
    transform: scaleY(1);
  }
}

.animated {
  animation-play-state: paused;
}
</style>