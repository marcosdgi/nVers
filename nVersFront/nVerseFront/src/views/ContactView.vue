<script setup>

import AsideBar from "@/components/AsideBar.vue";
</script>

<template>
  <div class="d-flex align-items-center ">
    <AsideBar/>
    <div class="blog flex-md-column justify-content-end m-5">
      <h1 class="display-3">
        Contact direct by eMail
      </h1>
      <form>
        <input type="email" class="fs-4" id="inputMail" placeholder="your@gmail.com">
        <hr>
      </form>
      <div>
        <h1 class="display-3">
          Did you want call you back?
        </h1>
        <form>
          <input type="text" class="fs-4" id="inputPhone" placeholder="let your phone number">
          <hr>
          <p class="display-6">we will call you into next ten minutes.</p>
        </form>
        <div class="direct-contact">
          <h1 class="display-5">
            No have time? direct contact.
          </h1>
        </div>
            <div class="mt-5 d-flex justify-content-between gap-4">
              <button class="btn rounded-pill w-50 btn-dark">+1 786 353 5916</button>
              <button class="btn rounded-pill w-50 btn-dark">info@nvers.com</button>
            </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

#inputMail {
  border: none;
  outline: none;
  padding-top: 5%;
  width: 40rem;

}

#inputPhone {
  border: none;
  outline: none;
  padding-top: 5%;
  width: 40rem;
}

.direct-contact {
  margin-top: 5%;
}
</style>