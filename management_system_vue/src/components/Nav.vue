<template>
  <nav class="navbar is-info" role="navigation" aria-label="main naviation" style="min-height: 5rem;">
    <div class="navbar-brand">
      <router-link class="navbar-item is-size-4" to="/">电影管理</router-link>
    </div>

    <div id="navbar-item" class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/" class="navbar-item">主页</router-link>
        <router-link to="/about" class="navbar-item">关于</router-link>
        <router-link to="/movies" class="navbar-item">电影</router-link>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="$store.state.user.isAuthenticated">
              <router-link to="/dashboard/my-account" class="button is-info">我的账户</router-link>
            </template>
            <template v-else>
              <router-link to="/sign-up" class="button is-primary"><strong>注册</strong></router-link>
              <router-link to="/log-in" class="button is-light">登陆</router-link>
            </template>
          </div>
        </div>
        <!-- Add the following search form -->
        <div class="navbar-item">
          <form @submit.prevent="searchMovies">
            <div class="field has-addons">
              <div class="control">
                <input class="input" type="text" v-model="searchQuery" placeholder="搜索电影">
              </div>
              <div class="control">
                <button class="button is-primary" type="submit">搜索</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '', // Add a new data property for search query
    }
  },
  methods: {
  searchMovies() {
    if (this.searchQuery.trim() !== '') {
      const slug = this.searchQuery.toLowerCase().replace(/\s+/g, '-');
      this.$router.push({ path: `/movies/${slug}` });
    }
    this.searchQuery = '';
  },
},

};
</script>
