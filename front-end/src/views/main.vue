<template>
  <div>
    <div class="head">
            <img alt="logo" src="../assets/logo.png" style="position:absolute;top:5%;height: 75%;left: 5%">
      <div class="demo-type">
        <div>
          <el-avatar icon="el-icon-user-solid" size="small"></el-avatar>
        </div>
      </div>
      <span class="el-dropdown-link" @click="toLogin" style="position:absolute;top:35%;height: 80%;left: 93%">
        请登录
      </span>
    </div>

    <div class="body">
      <div class="body-left" style="position:absolute;width: 50%;right: 50%;height: 100%;">
        <p class="left" style="font-size: 24px!important;top: 31%">免费专业的问卷网站</p>
        <p class="left" style="font-size: 16px!important;top: 39%">包含多种题型，支持多种问卷类型</p>
        <button
            type="button"
            class="button button--login button--round-s button--text-thick button--inverted button--size"
            style="position:absolute;right: 8%; top: 47%;width: 160px; height: 45px;cursor: pointer"
            @click="toLogin"
        >登录
        </button>

      </div>

      <div class="body-right" style="position:absolute;width: 50%;left: 50%;height: 100%;">
        <p class="right" style="font-size: 24px!important;top: 31%">方便快捷的数据收集</p>
        <p class="right" style="font-size: 16px!important;top: 39%">直观的问卷结果展示，快捷的原始数据导出</p>
        <button
            type="button"
            class="button button--join button--round-x button--text-thick button--beforeinverted button--size"
            style="
              cursor: pointer;
              position: absolute;
              left: 8%; top: 47%;
              width: 160px;
              height: 45px;
            "
            @click="toRegister"
        >
          注册
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "main",
  methods: {
    toRegister() {
      this.$router.push('/register')
    },
    toLogin() {
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.left {
  color: #ffffff;
  position: absolute;
  right: 9%;
}

.body-left {
  background-image: url("../assets/right1.jpg") ;
  background-repeat: no-repeat;
  background-position: center;
  /*background-attachment: fixed;*/
  /*background-size: cover;*/
  /*-webkit-background-size: cover;*/
  /*-moz-background-size: cover;*/
  /*-o-background-size: cover;*/
  background-size: 100% 100%;
}

.right {
  color: #ffffff;
  position: absolute;
  left: 9%;
}

.body-right {
  background-image: url("../assets/left1.jpg");
  background-repeat: no-repeat;
  background-position: center;
  /*background-attachment: fixed;*/
  /*background-size: cover;*/
  /*-webkit-background-size: cover;*/
  /*-moz-background-size: cover;*/
  /*-o-background-size: cover;*/
  background-size: 100% 100%;
}

.head {
  position: absolute;
  top: 0;
  left: 0;
  height: 62px;
  width: 100%;
  background-color: #ffffff;
}

.body {
  position: absolute;
  min-width: 1300px;
  top: 62px;
  left: 0;
  height: 92%;
  width: 100%;
  background-color: #f5f5f8;
  border-top: 1px transparent solid;
  box-shadow: #c6c5c5;
  border-image: linear-gradient(0deg, #979696, #e7e7e7) 1 10;
  /* background-image: url("../assets/background.png");*/
  /* background-repeat: no-repeat;*/
  /* background-position: center;*/
  /* background-attachment: fixed;*/
  /* background-size: cover;*/
  /* -webkit-background-size: cover;*/
  /* -moz-background-size: cover;*/
  /* -o-background-size: cover;*/
}

.block {
  position: absolute;
  margin-top: 45px;
  right: 17%;
}

.demo-type {
  position: absolute;
  left: 90%;
  top: 30%;
}

.el-dropdown-link {
  cursor: pointer;
  color: #6a6a6a;
}

.el-icon-arrow-down {
  font-size: 6px;
}

.button {
  float: left;
  min-width: 150px;
  max-width: 500px;
  display: block;
  margin: 1em;
  padding: 1em 2em;
  border: none;
  border-radius: 4px;
  background: none;
  color: inherit;
  position: relative;
  z-index: 1;
  -moz-osx-font-smoothing: grayscale;
}

.button:focus {
  outline: none;
}

.button > span {
  vertical-align: middle;
}

/* Sizes */
.button--size {
  font-size: 14px;
}

.button--size-x {
  font-size: 15px;
}

/* Typography and Roundedness */
.button--text-thick {
  font-weight: 400;
}

.button--round-s {
  border-radius: 4px;
}

.button--round-x {
  border-radius: 4px;
}

/* Wapasha */
.button.button--login {
  background: #ffffff;
  color: #004f7b;
  -webkit-transition: background-color 0.3s, color 0.3s;
  transition: background-color 0.3s, color 0.3s;
}

.button.button--join {
  background: #0493d7;
  color: #ffffff;
  -webkit-transition: background-color 0.3s, color 0.3s;
  transition: background-color 0.3s, color 0.3s;
}

.button--login.button--inverted {
  background: #ffffff;
  color: #006592;
}

.button--login::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  border-radius: inherit;
  opacity: 0;
  -webkit-transform: scale3d(0.6, 0.6, 1);
  transform: scale3d(0.6, 0.6, 1);
  -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
  transition: transform 0.3s, opacity 0.3s;
  -webkit-transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
  transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
}

.button--login:hover {
  background-color: #fff;
  color: #3f51b5;
}

.button--login.button--inverted:hover {
  background-color: #0493d7;
  color: #fcfcfd;
}

.button--join.button--inverted {
  background: #adadad;
  border: 1px solid #adadad;
  color: #000000;
}

.button--join::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  border-radius: inherit;
  opacity: 0;
  -webkit-transform: scale3d(0.6, 0.6, 1);
  transform: scale3d(0.6, 0.6, 1);
  -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
  transition: transform 0.3s, opacity 0.3s;
  -webkit-transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
  transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
}

.button--join:hover {
  background-color: #ffffff;
  color: #0493d7;
}

.button--join.button--inverted:hover {
  background-color: #55646d;
  color: #fcfcfd;
}
</style>