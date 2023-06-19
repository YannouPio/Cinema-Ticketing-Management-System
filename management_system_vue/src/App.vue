<template>
  <div>
    <!-- Nav组件，可能用于显示导航菜单 -->
    <Nav />
    <!-- router-view是Vue Router的一个组件，用于显示当前路由的内容 -->
    <router-view />
    <!-- Footer组件，可能用于显示页面底部的信息 -->
    <Footer />
  </div>
</template>

<script>
// 导入Nav和Footer组件
import axios from 'axios'
import Nav from '@/components/Nav.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'App', // 组件名称
  components: {
    Nav, // 在此处注册Nav和Footer组件，这样我们就可以在模板中使用它们
    Footer
  },

  // 在组件创建之前调用的一个生命周期钩子函数
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
