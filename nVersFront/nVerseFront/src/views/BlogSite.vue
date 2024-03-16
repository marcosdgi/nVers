<script setup>
import router from "@/router/index.js";

const toServices = () => {
  router.push('/services')
}
const toContact = () => {
  router.push('/contact')
}
const toProjects = () => {
  router.push('/projects')
}
</script>

<template>
  <div class="container bg-light-subtle" style="height: 60rem; border-radius: 30px">

    <div class="logo d-flex justify-content-start align-items-center">
      <img src="/logo2.png" width="13%">
      <h1 class="display-3 fw-bold">Blog</h1>
    </div>

    <div class="menu d-flex  justify-content-around">
      <div class="card w-50 ">
        <p class="display-6">
          Our philosophy is based on the idea
          that to reveal the greatness of what
          we can see and experience, we must
          first understand and appreciate the
          tiniest, most hidden details.
          <br>
          <br>
          Our philosophy is based on the idea
          that to reveal the greatness of what
          we can see and experience, we must
          first understand and appreciate the
          tiniest, most hidden details.
        </p>
      </div>
      <div>
        <button class="oval display-4 d-flex justify-content-center align-items-center text-light"
                @click="toServices">
          Services
        </button>
        <button class="oval display-4 d-flex justify-content-center align-items-center text-light"
                @click="toContact">
          Contact
        </button>
        <button class="oval display-4 d-flex justify-content-center align-items-center text-light"
                @click="toProjects">
          Projects
        </button>
      </div>

    </div>
  </div>
</template>

<style scoped>
.oval {
  height: 10rem;
  width: 25rem;
  border-radius: 100px;
  margin-top: 8%;
  background: linear-gradient(to left, rgb(13, 10, 78), rgb(19, 16, 120));
  box-shadow: black 10px 10px 20px;
  border: none;
  transition: transform 0.5s ease-in-out;

}
.oval:hover{
  transform: scaleX(1.1);
}

.card {
  box-shadow: black 10px 10px 20px;
  padding: 2%;
  border-radius: 30px;
}

.logo {
  margin-bottom: 3%;
  margin-left: 4%;
}
</style>