<template>
  <div class="about">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">我的账户</h1>
      </div>
    </div>

    <section class="section">
      <!-- 注销按钮，点击时调用 logout 方法 -->
      <button @click="logout()" class="button is-danger">退出账户</button>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  methods: {
    async logout() {
      console.log('logout')

      // 发送 POST 请求到后端的 /token/logout/ 接口
      await axios
        .post('token/logout/')
        .then(response => {
          console.log('Logged out')
        })
        .catch(error => {
          console.log(error)
        })

      // 移除 axios 的 headers 中的 Authorization 字段
      axios.defaults.headers.common['Authorization'] = ""

      // 移除 localStorage 中的 token
      localStorage.removeItem('token')

      // 从 Vuex 的 store 中移除 token
      this.$store.commit('removeToken')

      // 导航到首页
      this.$router.push('/')
    }
  }
}
</script>
