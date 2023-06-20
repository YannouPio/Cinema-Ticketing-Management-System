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
                            <li><a class="is-active">所有</a></li>
                            <li><a>电影</a></li>
                            <li><a>演出</a></li>
                            <li><a>演唱会</a></li>
                        </ul>
                    </aside>
                </div>

                <div class="column is-10">
                    <div class="columns is-multiline">
                        
                        <!--将数据从后端传输到前端-->
                        <div 
                            
                            class="column is-4"
                            v-for="movie in movies"
                            v-bind:key="movie.id"   
                        >
                            <div class="card">
                                <div class="card-image">
                                    <figure class="image is-4by3">
                                        <img src="http://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
                                    </figure>
                                </div>

                                <div class="card-content">
                                    <div class="media">
                                        <div class="media-content">
                                            <p class="is-size-5">{{ movie.title }}</p>
                                        </div>
                                    </div>

                                    <div class="content">
                                        <p>{{ movie.short_description }}</p>
                                        <router-link :to="{name: 'Movie', params: {slug: movie.slug}}">更多</router-link>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="column is-12">
                        <nav class="pagination">
                            <a class="pagination-previous">前一页</a>
                            <a class="pagination-next">下一页</a>

                            <ul class="pagination-list">
                                <!-- 添加页数 -->
                                <li>
                                    <a class="pagination-link is-current">1</a>
                                </li>
                                <li>
                                    <a class="pagination-link">2</a>
                                </li>
                            </ul>

                        </nav>
                    </div>

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
            movies: []
        }
    },

    mounted() {
        console.log('mounted')

        axios
            .get('/api/v1/movies')
            .then(response => {
                console.log(response.data)

                this.movies = response.data

            })
    }
}

</script>