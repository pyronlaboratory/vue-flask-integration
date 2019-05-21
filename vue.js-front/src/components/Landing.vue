<template>
  <div class="container" id="center">
    <p><b>{{msg}}</b></p>
    <router-link to="/" v-on:click.native="logout()" replace><button type="button" class="btn btn-primary">Logout</button></router-link>
  </div>
</template>

<script>
export default {
  name: 'Landing',
  data() {
    return {
      msg: 'Welcome, this is the Landing page!',
    };
  },
};
</script>
<style>
#center {

  margin-top: 100px;
  margin-left: auto;
  margin-right: auto;
  width: 60%;
  padding: 10px;
  font-family: 'Quicksand', sans-serif;

}
</style>