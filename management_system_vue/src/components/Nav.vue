<template>
  <nav class="navbar is-info" role="navigation" aria-label="main naviation" style="min-height: 5rem;">
    <div class="navbar-brand">
      <!-- 主页链接 -->
      <router-link class="navbar-item is-size-4" to="/">电影管理</router-link>
    </div>

    <div id="navbar-item" class="navbar-menu">
      <div class="navbar-start">
        <!-- 导航链接 -->
        <router-link to="/" class="navbar-item">主页</router-link>
        <router-link to="/about" class="navbar-item">关于</router-link>
        <router-link to="/movies" class="navbar-item">电影</router-link>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <!-- 如果用户已经认证，显示我的账户链接 -->
            <template v-if="$store.state.user.isAuthenticated">
              <router-link to="/dashboard/my-account" class="button is-info">我的账户</router-link>
            </template>
            <!-- 如果用户未认证，显示注册和登录链接 -->
            <template v-else>
              <router-link to="/sign-up" class="button is-primary"><strong>注册</strong></router-link>
              <router-link to="/log-in" class="button is-light">登陆</router-link>
            </template>
          </div>
        </div>
        <!-- 搜索表单 -->
        <div class="navbar-item">
          <form @submit.prevent="searchMovies">
            <div class="field has-addons">
              <div class="control">
                <!-- 绑定输入框到 searchQuery 属性 -->
                <input class="input" type="text" v-model="searchQuery" placeholder="搜索电影">
              </div>
              <div class="control">
                <!-- 提交按钮 -->
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
      // 绑定到搜索表单的输入框
      searchQuery: '',
    }
  },
  methods: {
    // 当搜索表单提交时被调用
    searchMovies() {
      // 如果查询不为空，导航到包含查询词的slug的路由
      if (this.searchQuery.trim() !== '') {
        const slug = this.searchQuery.toLowerCase().replace(/\s+/g, '-');
        this.$router.push({ path: `/movies/${slug}` });
      }
      // 清空查询
      this.searchQuery = '';
    },
  },
};
</script>
