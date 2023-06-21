<template>
    <div class="movies">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">{{ movie.title }}</h1>
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
                    {{ movie.long_description }}
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
            movie: []
        }
    },

    mounted() {
        console.log('mounted')

        const slug = this.$route.params.slug

        axios
            .get(`movies/${slug}/`)
            .then(response => {
                console.log(response.data)

                this.movie = response.data

            })
    }
}

</script>