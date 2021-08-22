<template>
  <div>
    <div class="head">
      <img alt="Vue logo" src="../assets/logo.png" style="position:absolute;top:10%;height: 80%;left: 5%">
    </div>

    <div class="body">
      <button
          type="button"
          class="button button--login button--round-s button--text-thick button--inverted button--size"
          style="position:absolute;left: 5%; top: 4%;width: 3%; height: 7%"
          @click="login"
      >创建问卷
      </button>

      <!-- menu菜单 -->
    <button
      type="button"
      class="button button--login button--round-x button--text-thick button--beforeinverted button--size"
      style="
        position: absolute;
        left: 5%; top: 20%;
        width: 4%;
        height: 7%;
      "
    >
      我的帐户
    </button>
    <button
      type="button"
      class="button button--login button--round-x button--text-thick button--inverted button--size"
      style="
        position: absolute;
        left: 5%; top: 27%;
        width: 4%;
        height: 7%;
      "
      @click="toFutureFlight"
    >
      未出发的航班
    </button>
    <button
      type="button"
      class="button button--login button--round-x button--text-thick button--inverted button--size"
      style="
        position: absolute;
        left: 5%; top: 34%;
        width: 4%;
        height: 7%;
      "
      @click="toHistoryFlight"
    >
      以往的航班
    </button>
    <button
      type="button"
      class="button button--login button--round-x button--text-thick button--inverted button--size"
      style="
        position: absolute;
        left: 5%; top: 41%;
        width: 4%;
        height: 7%;
      "
      @click="toUpdate"
    >
      更新个人信息
    </button>

    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
.head {
  position: absolute;
  top: 0;
  left: 0;
  height: 8%;
  width: 100%;
  background-color: #ffffff;
  //border:2px solid #000000;
}

.body {
  position: absolute;
  top: 8%;
  left: 0;
  height: 92%;
  width: 100%;
  background-color: #f5f4f4;
  border-top: 1px transparent solid;
  box-shadow: #c6c5c5;
  border-image: linear-gradient(to right, #979696, #e7e7e7) 1 10;
}
.button {
  float: left;
  min-width: 150px;
  max-width: 500px;
  display: block;
  margin: 1em;
  padding: 1em 2em;
  border: none;
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
  font-size: 8px;
}

/* Typography and Roundedness */
.button--text-thick {
  font-weight: 300;
}

.button--round-s {
  border-radius: 2px;
}
.button--round-x {
  border-radius: 0px;
}
/* Wapasha */
.button.button--login {
  background: #176c97;
  color: #fff;
  -webkit-transition: background-color 0.3s, color 0.3s;
  transition: background-color 0.3s, color 0.3s;
}

.button.button--join {
  background: #fff;
  color: #37a2e2;
  -webkit-transition: background-color 0.3s, color 0.3s;
  transition: background-color 0.3s, color 0.3s;
}

.button--login.button--inverted {
  background: #0b92e8;
  color: #fdfeff;
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
  background-color: #0d78ad;
  color: #fcfcfd;
}

// 加入按钮
.button--join.button--inverted {
  background: #fdfeff;
  border: 1px solid #0d78ad;
  color: #2d44a8;
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
  background-color: #fff;
  color: #3f51b5;
}

.button--join.button--inverted:hover {
  background-color: #0d78ad;
  color: #fcfcfd;
}
</style>
