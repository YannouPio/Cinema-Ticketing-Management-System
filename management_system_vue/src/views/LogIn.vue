<template>
    <div class="about">
      <!-- 欢迎画面 -->
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">登陆</h1>
        </div>
      </div>
  
      <!-- 登录表单的部分 -->
      <section class="section">
        <div class="container">
          <div class="columns">
            <div class="column is-4 is-offset-4">
              <!-- 一个表单，当提交时阻止默认的提交事件并调用submitForm方法 -->
              <form v-on:submit.prevent="submitForm">
                <!-- 邮箱输入框 -->
                <div class="field">
                  <label>邮箱</label>
                  <div class="control">
                    <!-- 使用v-model绑定到数据对象的username属性 -->
                    <input type="email" class="input" v-model="username">
                  </div>
                </div>
  
                <!-- 密码输入框 -->
                <div class="field">
                  <label>密码</label>
                  <div class="control">
                    <!-- 使用v-model绑定到数据对象的password属性 -->
                    <input type="password" class="input" v-model="password">
                  </div>
                </div>
  
                <!-- 错误信息显示区域 -->
                <div class="notification is-danger" v-if="errors.length">
                  <!-- 使用v-for指令显示每个错误信息 -->
                  <p v-for="error in errors" v-bind:key="error">
                    {{ error }}
                  </p>
                </div>
  
                <!-- 提交按钮 -->
                <div class="field">
                  <div class="control">
                    <button class="button is-dark">登陆</button>
                  </div>
                </div>
              </form>
              <hr>
              <!-- 一个指向注册页面的链接 -->
              或者 <router-link to="/sign-up">点击这里</router-link> 注册
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  //在脚本部分，data函数返回一个数据对象，包含了用户名、密码和错误信息列表。
  //mounted钩子函数设置了页面的标题
  //submitForm方法在表单提交时被调用，
  //它首先清空了Authorization头和localStorage中的token，
  //然后进行表单验证，如果输入有效，则向后端发送POST请求进行登录，
  //如果登录成功，则将获取到的token存储在Vuex的state和localStorage中，
  //并设置Authorization头，然后跳转到账户页面，
  //如果登录失败，则将错误信息添加到错误信息列表中
  import axios from 'axios'
  
  export default {
    data() {
      return {
        // 数据对象，用户名、密码和错误信息列表
        username: '',
        password: '',
        errors: []
      }
    },
    mounted() {
      // 在组件挂载后，设置文档的标题
      document.title = 'Log in | ManagementSystem'
    },
    methods: {
      submitForm() {
        console.log('submitForm')
  
        // 清空Authorization头和localStorage中的token
        axios.defaults.headers.common['Authorization'] = ""
        localStorage.removeItem('token')
  
        // 清空错误信息列表
        this.errors = []
  
        // 验证输入是否有效
        if (this.username === '') {
          this.errors.push('请输入邮箱')
        }
  
        if (this.password === '') {
          this.errors.push('请输入密码')
        }
  
        // 如果输入有效，则向后端发送POST请求进行登录
        if (!this.errors.length) {
          const formData = {
            username: this.username,
            password: this.password
          }
  
          axios
            .post('http://127.0.0.1:8000/api/v1/token/login/', formData)
            .then(response => {
              // 如果请求成功，则将获取到的token存储在Vuex的state和localStorage中，并设置Authorization头
              const token = response.data.auth_token
              this.$store.commit('setToken', token)
              axios.defaults.headers.common['Authorization'] = "Token " + token
              localStorage.setItem('token', token)
  
              // 然后跳转到账户页面
              this.$router.push('/dashboard/my-account')
            })
            .catch(error => {
              // 如果请求失败，则将错误信息添加到错误信息列表中
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
  