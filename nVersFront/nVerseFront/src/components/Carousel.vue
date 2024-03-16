<template>
  <div class="carousel">
    <div class="images" :style="{ transform: `translateX(${pos}em)`}">

      <template v-for="(service, index) in services" :key="index">
        <div class="card text-light" style="width: 22rem; margin-right: 10%"
             :class="{ active: index === currentService,
              'opacity-0' :index <= currentService-3 || index>=currentService+2,
               'low': index<=currentService-2,
                'more': index >=currentService+2 }">

          <div class="card-header">
            {{ service.name }}
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item text-light " style="font-size: 18px; height: 10rem; margin-top: 5%"> . {{ service.description }}</li>
            <li class="list-group-item text-light"style="font-size: 25px">{{ service.price }}.00$/PACK</li>
          </ul>
        </div>
      </template>

    </div>
  </div>
  <button @click="next" class="btn position-absolute " style="top: 90%; right: 39%;">
    <img src="/next.png">
  </button>
  <button @click="previous" class="btn position-absolute" style="top: 90%; left: 30%; background-color: transparent ">
    <img src="/previus.png">
  </button>

</template>

<script setup>
import {onMounted, ref} from 'vue';
import axios from "axios";

const services = ref([]);

let currentService = ref(0);

let pos = ref(30)

const next = () => {
  if (currentService.value === services.value.length - 1) {
    currentService.value = -1;
    pos.value = 30;
  } else {
    pos.value -= 20;
  }

  currentService.value++;
};

const previous = () => {
  if (currentService.value === 0) {
    currentService.value = services.value.length;
    pos.value = 30 - (services.value.length - 1) * 20;
  } else {
    pos.value += 20;
  }
  currentService.value--;
};


const get_Services = async () => {
  try {
    const response = await axios.get('http://localhost:8000/services/list_services/')
    console.log(response.data)
    services.value = response.data
  } catch (error) {
    console.error(error)
  }
}
onMounted(
    () => {
      get_Services()
    }
)
</script>

<style scoped>
.carousel {

  display: flex;
  align-items: center;
  overflow: hidden;
  height: 25rem;
  position: relative;
}

.carousel .images {
  display: flex;
  justify-content: flex-start;
  gap: 10px;
  transition: transform 0.5s ease-in-out;
}

.card {
  background: linear-gradient(to right, rgb(13, 10, 78), rgb(19, 16, 120));;
  height: 18rem;
  margin-right: 5%;
  top: 0rem;
  box-shadow: 10px 10px 30px black;

}

li {
  background: linear-gradient(to right, rgb(13, 10, 78), rgb(19, 16, 120));;

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
  //z-index: 1;
  box-shadow: black 0px 0px 20px;
}

.more {
  transform: translateX(-80px);
}

.low {
  transform: translateX(80px);
}
</style>