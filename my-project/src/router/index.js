import Vue from 'vue'
import Router from 'vue-router'
import App from '../App.vue'
import SignUp from '../components/SignUp.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: App
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    }
  ]
})
