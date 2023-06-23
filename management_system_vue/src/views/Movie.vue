<template>
    <!-- 展示电影的标题和长描述 -->
    <div class="movies">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">{{ movie.title }}</h1> <!-- 渲染电影标题 -->
        </div>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns content">
          <div class="column is-2">
            <h2>电影上映信息</h2>
            <ul>
              <li><a href="#">影厅</a></li>
              <li><a href="#">上映时间</a></li>
            </ul>
          </div>
          <div class="column is-10">
            {{ movie.long_description }} <!-- 渲染电影长描述 -->
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        movie: [] // 存储电影详细信息
      }
    },
    mounted() {
      console.log('mounted')
  
      // 从路由参数中获取电影的slug
      const slug = this.$route.params.slug
  
      // 发送GET请求获取电影详细信息
      axios
        .get(`movies/${slug}/`)
        .then(response => {
          console.log(response.data)
  
          // 更新movie的值
          this.movie = response.data
        })
    }
  }
  </script>
  