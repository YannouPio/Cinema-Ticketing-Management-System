<template>
    <div class="card">
      <div class="card-image">
        <figure class="image is-4by3">
          <!-- 绑定电影的图片到 img 元素的 src 属性 -->
          <img :src="movie.get_image" alt="Placeholder image">
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <!-- 显示电影的标题 -->
            <p class="is-size-5">{{ movie.title }}</p>
          </div>
        </div>
        <div class="content">
          <!-- 显示电影的简短描述 -->
          <p>{{ movie.short_description }}</p>
          <!-- 为 "更多" 链接绑定路由，当点击时将导航到对应电影的详细信息页 -->
          <router-link :to="{ name: 'Movie', params: { slug: movie.slug } }">更多</router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['movie'] // 接收从父组件传来的 movie 对象
  }
  </script>
  