<template>
    <div class="signup">
      <!-- 欢迎画面 -->
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">注册</h1>
        </div>
      </div>
  
      <!-- 注册表单的部分 -->
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
  
                <!-- 重复密码输入框 -->
                <div class="field">
                  <label>重复密码</label>
                  <div class="control">
                    <!-- 使用v-model绑定到数据对象的password2属性 -->
                    <input type="password" class="input" v-model="password2">
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
                    <button class="button is-dark">注册</button>
                  </div>
                </div>
              </form>
              <hr>
              <!-- 一个指向登录页面的链接 -->
              已经有账号？ <router-link to="/log-in"> 登陆 </router-link> 
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
        // 数据对象，包含用户名、密码、重复密码和错误信息列表
        username: '',
        password: '',
        password2: '',
        errors: []
      }
    },
    mounted() {
      // 在组件挂载后，设置文档的标题
      document.title = 'Sign up | ManagementSystem'
    },
    methods: {
      submitForm() {
        console.log('submitForm')
  
        // 清空错误信息列表
        this.errors = []
  
        // 验证输入是否有效
        if (this.username === '') {
          this.errors.push('请输入邮箱')
        }
  
        if (this.password === '') {
          this.errors.push('请输入密码')
        }
  
        // 验证两次输入的密码是否一致
        if (this.password !== this.password2) {
          this.errors.push('密码不一致')
        }
  
        // 如果输入有效，则发送POST请求进行注册
        if (!this.errors.length) {
          const formData = {
            username: this.username,
            password: this.password
          }
  
          axios
            .post('http://127.0.0.1:8000/api/v1/users/', formData)
            .then(response => {
              // 注册成功后，跳转到登录页面
              this.$router.push('/log-in')
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
  