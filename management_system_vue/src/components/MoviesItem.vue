<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <img :src="movie.get_image" alt="Placeholder image">
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
                <router-link :to="{ name: 'Movie', params: { slug: movie.slug } }">更多</router-link>
            </div>

        </div>
    </div>
</template>

<script>


export default {
    props: ['movie']
}

</script>