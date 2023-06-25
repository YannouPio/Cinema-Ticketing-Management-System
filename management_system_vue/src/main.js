// 从Vue.js库导入 createApp 函数
import { createApp } from 'vue'

// 导入主组件 App
import App from './App.vue'

// 导入路由和数据存储库
import router from './router'
import store from './store'

// 导入发送HTTP请求的库
import axios from 'axios'

// 设置 axios 的默认基础URL
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/v1/'

// 创建 Vue 应用
createApp(App)
    // 注册数据存储库和路由
    .use(store)
    .use(router, axios)
    // 将 Vue 应用挂载到 id 为 'app' 的 HTML 元素上
    .mount('#app')
