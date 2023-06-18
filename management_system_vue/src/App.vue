<template>
  <div>
  <nav class = "navbar" role ="navigation" aria-label="main naviation" style="min-height: 5rem;">
    <div class="navbar-brand">
      <a class="navbar-item is-size-4" href="/">影院信息管理系统</a>
    </div>
  
    <div id ="navbar-item" class="navbar-menu"> 
      <div class ="navbar-start">
        <a class ="navbar-item">主页</a>
        <a class ="navbar-item">关于</a>
      </div>

      <div class="navbar-end">

        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-primary"><strong>注册</strong></a>
            <a class="button is-light">登陆</a>
          </div>
        </div>

      </div>

    </div>

  </nav>
  <router-view/>

  <footer class="'footer'">
    <p class="has-text-centered">3210421119彭靖强 (c) 2023</p>
  </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma/';
</style>
