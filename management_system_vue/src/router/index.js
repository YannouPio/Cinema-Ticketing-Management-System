// 导入创建路由和Web历史所需的库
import { createRouter, createWebHistory } from 'vue-router'

// 导入组件
import HomeView from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Movies from '../views/Movies.vue'
import Movie from '../views/Movie.vue'

// 定义路由
const routes = [
  // 路由对象，定义路径、路由名和绑定的组件
  {
    path: '/', // 路径
    name: 'home', // 路由名
    component: HomeView // 当路径匹配时，该组件会被渲染
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/movies',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/movies/:slug', // 带参数的路径
    name: 'Movie',
    component: Movie
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount
  },
]

// 创建路由实例
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL), // 使用HTML5历史模式
  routes // 加载路由定义
})

// 导出路由实例
export default router
