<template>
  <div>
    
    <form role="form" id="center">
    				<p><b>{{ msg }}</b></p>
                    <div class="form-group float-label-control">
                        <label for="">Email Address: </label> 
                        <input type="email" class="form-control" placeholder="Please enter email address.." v-model="email">
                        
                        <br>
                        <button type="button" v-on:click="login()" class="btn btn-primary">Login</button>
                        
                    </div>
    </form>

  </div>
</template>



<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      input: {
        email: ''             
      },
      msg: 'This is the Vue-Flask Integrated Login Page!',
    };
  },
  methods: {
    
    login(email) {
      console.log(this.email)

      //const path = 'http://localhost:5000/';
      //axios.post(path, this.email)
        .then(() => {
          this.login();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.login();
        });


    }, 
}

}
</script>



<style>
body {
	background-color: #0DF5EE;
}
p {
	font-size: 50px;
	font-family: 'Quicksand', sans-serif;
}
#center {

  margin-top: 100px;
  margin-left: auto;
  margin-right: auto;
  width: 60%;
  padding: 10px;
  font-family: 'Quicksand', sans-serif;

}
</style>