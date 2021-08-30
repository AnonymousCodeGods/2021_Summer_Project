<template>
  <div style="background-image: url('../assets/left.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  height: 100%;
  width: 100%;
position: absolute">
    <div style="display: flex;justify-content: center;margin-top: 150px;">
      <table style="border-spacing: 15px">
        <tr>
          <el-card style="width: 400px">
            <div slot="header" class="clearfix">
              <span>登录</span>
            </div>
            <table style="border-spacing: 20px" v-loading.fullscreen.lock="fullscreenLoading">
              <tr>
                <td>用户名</td>
                <td>
                  <el-input v-model="username" placeholder="请输入用户名"></el-input>
                </td>
              </tr>
              <tr>
                <td>密码</td>
                <td>
                  <el-input type="password" v-model="password" placeholder="请输入密码"
                            @keydown.enter.native="doLogin"></el-input>
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <el-button style="width: 300px" type="primary" @click="doLogin">登录</el-button>
                </td>
              </tr>
            </table>
          </el-card>
        </tr>
        <tr>
          <el-card style="width: 400px">
            <el-link @click="$router.push('/Register')">没有账号？点我注册</el-link>
          </el-card>
        </tr>
      </table>
    </div>
  </div>
</template>
<script>

export default {
  data() {
    return {
      username: '',
      password: '',
      fullscreenLoading: false
    }
  },
  methods: {
    doLogin() {
      if (this.username === '') {
        this.$notify({
          title: '错误',
          message: '用户名不能为空',
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
      } else {
        this.fullscreenLoading = true;
        this.$axios({
          method: "POST",
          data: {userName: this.username, pwd: this.password},
          url: "user/login",
        })
            .then(res => {
              if (!res.data.success) {
                this.$notify({
                  title: '错误',
                  message: '登陆失败',
                  position: 'bottom-left',
                  type: "error"
                });
              } else {
                this.$store.state.userType = res.data.userType;
                this.$store.state.username = this.username;
                this.$store.state.password = this.password;
                this.$cookies.set("username", this.username, 60 * 60 * 24);
                this.$notify({
                  title: '成功',
                  message: '登陆成功',
                  position: 'bottom-left',
                  type: "success"
                });
                this.$router.push({
                  //todo:change path
                  path: "/collectingSignUpQuestionnaire", query: {
                    id: this.$route.query.id
                  }
                })
              }
              this.fullscreenLoading = false;
            })
            .catch(res => {
              console.log(res)
              this.$notify({
                title: '错误',
                message: '连接失败',
                position: 'bottom-left',
                type: "error"
              });
              this.fullscreenLoading = false;
            });
      }
    }
  },
  created() {
    this.$store.state.currentPage = "99"
  }
}
</script>
