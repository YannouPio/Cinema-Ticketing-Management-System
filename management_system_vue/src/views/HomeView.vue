<!-- HomeView.vue组件的模板部分包含了一个欢迎画面和主要内容部分。
  欢迎画面是一个使用Bulma的hero组件实现的欢迎消息，
  主要内容部分则包含了一个指向注册页面的按钮和一个电影列表。
  电影列表是通过一个v-for指令和MoviesItem组件来渲染的，
  每部电影都会渲染一个MoviesItem组件-->


<template>
  <div class="home">
    <!-- 欢迎画面 -->
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">欢迎</h1>
      </div>
    </div>

    <!-- 页面主要内容的部分 -->
    <section class="section">
      <div class="container">
        <!-- 使用Bulma的columns和column组件进行布局 -->
        <div class="columns is-multiline">
          <!-- 一个指向注册页面的按钮 -->
          <div class="column is-12 has-text-centered">
            <a href="/sign-up" class="button is-info is-size-3 mt-6 mb-6">点击开始</a>
          </div>

          <hr>

          <!-- 为每部电影渲染一个MoviesItem组件 -->
          <div class="column is-3" v-for="movie in movies" v-bind:key="movie.id">
            <Moviesltem :movie="movie" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
//定义了一个数据对象movies用于存储电影列表
//注册了MoviesItem组件，并在组件挂载后使用axios从后端获取电影列表
//并将获取到的数据存储在movies中
//这样，在模板中就可以访问到这个电影列表，并将其传递给MoviesItem组件进行渲染

import axios from 'axios'
import Moviesltem from '@/components/MoviesItem.vue'
export default {
  name: 'HomeView',
  data() {
    return {
      // 数据对象，用于存储电影列表
      movies: []
    }
  },
  components: {
    // 注册MoviesItem组件
    Moviesltem
  },
  mounted() {
    console.log('mounted')

    // 在组件挂载后，从后端获取电影列表
    axios
      .get('movies/get_frontpage_movies/')
      .then(response => {
        console.log(response.data)

        // 将获取到的电影列表存储在数据对象中
        this.movies = response.data
      })
  }
}
</script>
