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
                        <form v-on:submit.prevent="submitForm">
                            <div class="field">
                                <label>邮箱</label>
                                <div class="control">
                                    <input type="email" class="input" v-model="username">
                                </div>
                            </div>

                            <div class="field">
                                <label>密码</label>
                                <div class="control">
                                    <input type="password" class="input" v-model="password">
                                </div>
                            </div>

                            <div class="notification is-danger" v-if="errors.length">
                                <p v-for="error in errors" v-bind:key="error">
                                    {{ error }}
                                </p>
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
<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Sign up | ManagementSystem'
    },
    methods: {
        submitForm() {
            console.log('submitForm')

            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            this.errors = []

            if (this.username === '') {
                this.errors.push('请输入邮箱')
            }

            if (this.password === '') {
                this.errors.push('请输入密码')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                    .post('http://127.0.0.1:8000/api/v1/token/login/', formData)

                    .then(response => {
                        const token = response.data.auth_token

                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] = "Token " + token

                        localStorage.setItem('token', token)

                        this.$router.push('/dashboard/my-account')
                    })

                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('出错了，请再试一遍')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>