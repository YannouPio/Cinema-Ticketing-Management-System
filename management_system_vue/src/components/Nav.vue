<template>

<nav class="navbar is-info" role="navigation" aria-label="main naviation" style="min-height: 5rem;">
      <div class="navbar-brand">
        <router-link class="navbar-item is-size-4" to="/">影院信息管理系统</router-link>
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
              <a href="/sign-up" class="button is-primary"><strong>注册</strong></a>
              <a href="/log-in" class="button is-light">登陆</a>
            </div>
          </div>

        </div>

      </div>

    </nav>

</template>