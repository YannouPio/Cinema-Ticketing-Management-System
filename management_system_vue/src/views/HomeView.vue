<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">欢迎</h1>

        <h2 class="subtitle">在线浏览购票选座</h2>
      </div>
    </div>

    <section class="section">
      <div class="container">

        <div class="columns is-multiline">

          <div class="column is-12 has-text-centered">
            <a href="/sign-up" class="button is-info is-size-3 mt-6 mb-6">点击开始购票</a>
          </div>
          
          <div class="column is-6">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-clock"></i></span>

              <h2 class="is-size-4 mt-4 mb-4">影厅信息</h2>

              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-6">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-comments"></i></span>

              <h2 class="is-size-4 mt-4 mb-4">最近热映</h2>

              <p>This is just some random placeholder text</p>
            </div>
          </div>

        </div>
      </div>        
    </section>
  </div>
</template>

<script>

export default {
  name: 'HomeView',
}
</script>
