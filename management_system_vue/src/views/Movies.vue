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
                                <a>{{ category.title }}</a>
                            </li>


                        </ul>
                    </aside>
                </div>

                <div class="column is-10">
                    <div class="columns is-multiline">

                        <!--将数据从后端传输到前端-->
                        <div class="column is-4" v-for="movie in movies" v-bind:key="movie.id">
                            <MoviesItem :movie="movie" />
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
import MoviesItem from '@/components/MoviesItem.vue'
export default {
    data() {
        return {
            movies: [],
            categories: [],
            activeCategory: null
        }
    },
    components: {
        MoviesItem
    },
    async mounted() {
        console.log('mounted')

        await axios
            .get('/movies/get_categories/')
            .then(response => {
                console.log(response.data)

                this.categories = response.data
            })


        await axios
            .get('/movies')
            .then(response => {
                console.log(response.data)

                this.movies = response.data

            })
        this.getMovies()
    },
    methods: {
        setActiveCategory(category) {
            console.log(category)
            this.activeCategory = category


            this.getMovies()

        },
        getMovies() {
            let url = '/movies/'

            if (this.activeCategory) {
                url += '?category_id=' + this.activeCategory.id
            }
            axios
                .get(url)
                .then(response => {
                    console.log(response.data)

                    this.movies = response.data

                })

        }
    }
}

</script>