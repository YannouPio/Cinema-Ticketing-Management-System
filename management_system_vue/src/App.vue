<!-- 这是Vue应用的根组件。
  在模板部分，它包含了Nav、router-view和Footer组件。
  Nav和Footer组件分别用于显示导航菜单和页脚信息，
  而router-view则用于显示当前路由的内容-->


<template>
  <div>
    <!-- Nav组件，用于显示导航菜单 -->
    <Nav />
    <!-- router-view是Vue Router的一个组件，用于显示当前路由的内容 -->
    <router-view />
    <!-- Footer组件，用于显示页面底部的信息 -->
    <Footer />
  </div>
</template>

<script>
// 导入Nav和Footer组件，以及axios库和MoviesItem组件
import axios from 'axios'
import Nav from '@/components/Nav.vue'
import Footer from '@/components/Footer.vue'
import MoviesItem from "@/components/MoviesItem.vue"

export default {
  name: 'App', // 组件名称
  components: {
    // 在此处注册Nav、Footer和MoviesItem组件，这样我们就可以在模板中使用它们
    Nav,
    Footer,
    MoviesItem
  },

  // 在组件创建之前调用的一个生命周期钩子函数
  //调用了Vuex的commit方法来初始化应用的状态，
  //然后从Vuex的状态中获取了token。
  //如果token存在，就将其添加到axios的默认请求头中，
  //这样每次发送请求时就会自动包含这个token；
  //否则，就清空Authorization头。
  //这样做可以在用户登录后，让每个请求都自动携带token，
  //以便后端验证用户的身份

  beforeCreate() {
    // 使用Vuex的commit方法来提交一个mutation，初始化store
    this.$store.commit('initializeStore')

    // 从Vuex的state中获取token
    const token = this.$store.state.user.token

    // 如果存在token，则将其添加到axios的默认请求头中
    // 这样每次使用axios发送请求时，都会自动包含这个token
    // "Token " + token就是一种常见的token格式，不同的后端可能会需要不同的格式
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      // 如果不存在token，则清空Authorization头
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>

<style lang="scss">
  // 导入Bulma CSS框架，用于样式设置
  @import '../node_modules/bulma/';
</style>
