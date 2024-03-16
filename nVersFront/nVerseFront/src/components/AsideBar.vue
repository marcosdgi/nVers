<template>
  <div class="aside">
    <div>
      <button class=" ovalside  text-light d-flex justify-content-center align-items-center text-center"
              @mouseenter="status[0]=true"
              @mouseleave="status[0]=false" :class="{'rotated':status[0],

           'rotated2':!status[0]}"
              @click="toServices"
      >
        <h1 class="display-5 w-100">
          Services
        </h1>
      </button>
      <button class=" ovalside text-light  d-flex justify-content-center align-items-center text-center"
              @mouseenter="status[2]=true"
              @mouseleave="status[2]=false" :class="{'rotated1':!status[2], 'rotated2':status[2]}"
        @click="toBlog"
      >
        <h1 class="display-5 w-100">
          Blog
        </h1>
      </button>
      <button class="ovalside  text-light d-flex justify-content-center align-items-center text-center"
              @mouseenter="status[1]=true"
              @mouseleave="status[1]=false" :class="{'rotated':status[1], 'rotated2':!status[1]}"
        @click="toProjects"
      >
        <h1 class="display-5 w-100">
          Projects

        </h1>
      </button>

    </div>
  </div>
</template>
<script setup>
import 'animate.css'
import {ref} from "vue";
import router from "@/router/index.js";

const status = ref([false, false, false])

const toServices = () => {
  router.push('/services')
}
const toBlog = () => {
  router.push('/blog')
}
const toProjects = () => {
  router.push('/projects')
}


</script>
<style scoped>
.ovalside {
  height: 10rem;
  width: 25rem;
  border-radius: 0 100px 100px 0;
  margin-top: 8%;
  background: linear-gradient(to right, rgb(13, 10, 78), rgb(19, 16, 120))

}

.rotated {
  width: 33rem;
  transition: 0.5s ease-in-out;
}

.rotated1 {
  width: 18rem;
  transition: 0.5s ease-in-out;
}

.rotated2 {
  width: 25rem;
  transition: 0.5s ease-in-out;
}


.aside {
  width: 40rem;
}
</style>