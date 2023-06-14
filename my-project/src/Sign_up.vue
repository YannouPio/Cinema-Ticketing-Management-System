<template>
  <div id="app">
    <div v-if="page === 'login'">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <label>Email: <input v-model="loginEmail" type="email"></label>
        <label>Password: <input v-model="loginPassword" type="password"></label>
        <button type="submit">Login</button>
      </form>
      <p>Don't have an account? <button @click="page = 'register'">Register</button></p>
    </div>

    <div v-if="page === 'register'">
      <h2>Register</h2>
      <form @submit.prevent="register">
        <label>Email: <input v-model="registerEmail" type="email"></label>
        <label>Password: <input v-model="registerPassword" type="password"></label>
        <button type="submit">Register</button>
      </form>
      <p>Already have an account? <button @click="page = 'login'">Login</button></p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      page: 'login',
      loginEmail: '',
      loginPassword: '',
      registerEmail: '',
      registerPassword: '',
    };
  },
  methods: {
    login() {
      // Handle login
      console.log('Login:', this.loginEmail, this.loginPassword);
    },
    register() {
      // Handle register
      console.log('Register:', this.registerEmail, this.registerPassword);
    },
  },
};
</script>
