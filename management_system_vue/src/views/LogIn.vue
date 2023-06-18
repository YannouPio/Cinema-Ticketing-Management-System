<template>
    <div class="about">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">登陆</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-4 is-offset-4">
                        <form>
                            <div class="field">
                                <label>邮箱</label>
                                <div class="control">
                                    <input type="email" class="input">
                                </div>
                            </div>

                            <div class="field">
                                <label>密码</label>
                                <div class="control">
                                    <input type="password" class="input">
                                </div>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button class="button is-dark">登陆</button>
                                </div>
                            </div>
                        </form>
                        <hr>
                        或者 <router-link to="/sign-up">点击这里</router-link> 注册
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>
  