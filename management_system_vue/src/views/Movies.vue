<template>
    <div class="movies">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">电影</h1>
            </div>
        </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-2">
                    <aside class="menu">
                        <p class="menu-label">分类</p>

                        <ul class="menu-list">
                            <li><a v-bind:class="{ 'is-active': !activeCategory }" @click="setActiveCategory(null)">
                                    所有</a>

                            </li>
                            <li v-for="category in categories" v-bind:key="category.id"
                                @click="setActiveCategory(category)">
                                <a v-bind:class="{ 'is-active': activeCategory && activeCategory.id === category.id }">
                                    {{ category.title }}
                                </a>
                            </li>
                        </ul>
                    </aside>
                </div>

                <div class="column is-10">
                    <div class="columns is-multiline">
                        <div class="column is-4" v-for="movie in movies" v-bind:key="movie.id">
                            <MoviesItem :movie="movie" />
                        </div>
                    </div>
                    <div v-if="movies.length === 0 && !searchError" class="has-text-centered">
                        <p class="has-text-info">暂无数据</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>


  <script>
  import axios from 'axios'
  import MoviesItem from '@/components/MoviesItem.vue'
  export default {
    data() {
      return {
        movies: [],  // 用于存储电影列表
        categories: [],  // 用于存储电影类别
        activeCategory: null,  // 当前选中的电影类别
        searchError: false,  // 用于标记是否有搜索错误
      }
    },
    components: {
      MoviesItem
    },
    async mounted() {
      console.log('mounted')
  
      // 获取电影类别
      await axios
        .get('/movies/get_categories/')
        .then(response => {
          console.log(response.data)
  
          this.categories = response.data
        });
  
      // 根据路由参数获取电影列表
      if (this.$route.params.slug) {
        await axios.get(`/movies/${this.$route.params.slug}`).then(response => {
          console.log(response.data);
          this.movies = [response.data];
        });
      } else {
        this.getMovies();
      }
    },
    methods: {
      setActiveCategory(category) {
        console.log(category)
        this.activeCategory = category
        this.getMovies()  // 设置当前类别后，获取新的电影列表
      },
      async getMovies() {
        let url = '/movies/'
  
        // 如果有选中的类别，将类别ID添加到请求参数
        if (this.activeCategory) {
          url += '?category_id=' + this.activeCategory.id
        }
  
        try {
          const response = await axios.get(url);
          if (!response.data || !Array.isArray(response.data)) {
            console.error('Unexpected response data:', response.data);
            return;
          }
          for (let movie of response.data) {
            if (movie === null) {
              console.error('Found null movie in response data:', response.data);
              return;
            }
          }
  
          this.movies = response.data;  // 更新电影列表
          this.searchError = false;  // 清除搜索错误
        } catch (error) {
          console.error(error);
          this.movies = [];  // 清空电影列表
          this.searchError = true;  // 设置搜索错误标志
        }
      }
    }
  }
  </script>
  
