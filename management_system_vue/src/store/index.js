// 导入Vuex的createStore函数
import { createStore } from 'vuex'

// 使用createStore函数创建并导出一个Vuex的store
export default createStore({
  // state是存储的状态，包括一个user对象，其中有一个token和一个isAuthenticated标志
  state: {
    user: {
      token: '', // 用户的token，初始值为空字符串
      isAuthenticated: false // 表示用户是否已经认证（即是否已经登录），初始值为false
    }
  },

  // mutations是改变状态的函数，每个函数接收state和可选的payload（负荷，通常是需要传递的数据）
  mutations: {
    // initializeStore是一个mutation，用于初始化store
    // 它会检查localStorage中是否有token，如果有，则设置用户的token并将isAuthenticated设为true
    // 如果没有，则清空用户的token并将isAuthenticated设为false
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.user.token = localStorage.getItem('token')
        state.user.isAuthenticated = true
      } else {
        state.user.token = ''
        state.user.isAuthenticated = false
      }
    },

    // setToken是一个mutation，用于设置用户的token
    // 它接收新的token作为参数，并将其设置到用户的token中，然后将isAuthenticated设为true
    setToken(state, token) {
      state.user.token = token
      state.user.isAuthenticated = true
    },

    // removeToken是一个mutation，用于移除用户的token
    // 它会清空用户的token并将isAuthenticated设为false
    removeToken(state) {
      state.user.token = ''
      state.user.isAuthenticated = false
    }
  },

  // actions是可以提交mutation的函数，用于异步操作，这里为空
  actions: {
  },

  // modules允许将store分割成模块，每个模块拥有自己的state、mutation、action、getter等，这里为空
  modules: {
  }
})
