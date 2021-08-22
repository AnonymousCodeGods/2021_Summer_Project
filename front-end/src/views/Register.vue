<template>
  <div>
    <div style="display: flex;justify-content: center;margin-top: 150px">
      <el-card style="width: 400px">
        <div slot="header" class="clearfix">
          <el-page-header @back="$router.push('./Login')" content="注册">
          </el-page-header>
        </div>
        <table style="border-spacing: 20px">
          <tr>
            <td>用户名</td>
            <td>
              <el-input v-model="username" placeholder="请输入用户名"></el-input>
            </td>
          </tr>
          <tr>
            <td>密码</td>
            <td>
              <el-input type="password" v-model="password" placeholder="请输入密码"></el-input>
            </td>
          </tr>
          <tr>
            <td>确认密码</td>
            <td>
              <el-input type="password" v-model="confirmPassword" placeholder="请再次输入密码"></el-input>
            </td>
          </tr>
          <tr>
            <td colspan="2">
              <el-button style="width: 300px" type="primary" @click="doRegister"
                         v-loading.fullscreen.lock="fullscreenLoading">注册
              </el-button>
            </td>
          </tr>
        </table>
      </el-card>
    </div>
  </div>
</template>
<script>
import router from "../router";

export default {
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      fullscreenLoading: false
    }
  },
  methods: {
    doRegister() {
      if (this.username === '') {
        this.$notify({
          title: '错误',
          message: '用户名不能为空',
          position: 'bottom-left',
          type: "error"
        });
      } else if (!new RegExp('[0-9a-zA-Z_]{4,24}').test(this.username)) {
        this.$notify({
          title: '错误',
          message: '用户名应有4-24位，只包含数字、字母、下划线',
          position: 'bottom-left',
          type: "error"
        });
      } else if (this.password === '') {
        this.$notify({
          title: '错误',
          message: '密码不能为空',
          position: 'bottom-left',
          type: "error"
        });
      } else if (!new RegExp('[0-9a-zA-Z_]{8,24}').test(this.password)) {
        this.$notify({
          title: '错误',
          message: '密码应有8~24位，只包含数字、字母、下划线',
          position: 'bottom-left',
          type: "error"
        });
      } else if (this.password !== this.confirmPassword) {
        this.$notify({
          title: '错误',
          message: '确认密码不匹配',
          position: 'bottom-left',
          type: "error"
        });
      } else {
        this.fullscreenLoading = true;
        this.$axios({
          method: "post",
          url: "/Register",
          data: {username: this.username, password: this.password}
        })
            .then(res => {
              console.log(res)
              if (res.data.success) {
                this.$notify({
                  title: '成功',
                  message: '注册成功',
                  position: 'bottom-left',
                  type: "success"
                });
                router.push('/Login')
              } else {
                this.$notify({
                  title: '失败',
                  message: '用户名已存在',
                  position: 'bottom-left',
                  type: "error"
                });
              }
              this.fullscreenLoading = false;
            })
            .catch(res => {
              this.$notify({
                title: '失败',
                message: '连接失败',
                type: 'error',
                position: 'bottom-left'
              });
              this.fullscreenLoading = false;
              console.log(res)
            })
      }
    }
  },
  created() {
    this.$store.state.currentPage = "99"
  }
}
</script>