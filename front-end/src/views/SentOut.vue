
<template>
  <div id="sentout" :style="heightAndWidth">
    <div class="head">
      <img alt="Vue logo" src="../assets/logo.png" style="position:absolute;top:10%;height: 80%;left: 5%">

      <el-badge :value="12" class="item">
        <el-button size="small">消息</el-button>
      </el-badge>

      <div class="demo-type">
        <div>
          <el-avatar icon="el-icon-user-solid"></el-avatar>
        </div>
      </div>

      <a style="position:absolute;top:25%;height: 80%;left: 90%">{{this.$store.state.username}}</a>
    </div>
    <div class="body">
      <el-col :span="24">
        <div style="display: flex;justify-content: center;margin-top: 100px;">
          <el-card style="width: 800px;height: 400px" :body-style="{ padding: '0px' }">
            <div slot="header" class="clearfix">
              <span>问卷链接与二维码</span>
            </div>
            <el-row :gutter="20" style="margin-left: 3px;margin-top: 11px;">
              <el-col :span="10">
                <div style="
                width: 300px;height: 300px;
                display: table-cell;vertical-align: middle;
                text-align: center;border-radius: 4px;box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)" >
                  <img alt="QR code" src="../assets/QRcode.jpg" style="height: 90%;width: 90%">
                </div>
              </el-col>
              <el-col :span="14">
                <div style="width:370px;height: 300px;display: table-cell;vertical-align: middle;text-align: center;">
                  <el-input
                      placeholder="请输入内容"
                      v-model="address"
                      :readonly="true"
                      style="width: 320px;">
                  </el-input>
                </div>
              </el-col>
            </el-row>
          </el-card>
        </div>
      </el-col>
      <button
          type="button"
          class="button button--login button--round-s button--text-thick button--inverted button--size"
          style="position:absolute;left: 5%; top: 10%;width: 200px; height: 65px"
          @click="toHome"
      >返回列表
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SentOut",
  data() {
    return{
      heightAndWidth: 'margin:0; height:'+
          (window.innerHeight).toString()+
          'px; width:'+
          (window.innerWidth).toString()+
          'px;',
      address: 'https://www.wjx.top/jq/52268413.aspx',
    }
  },
  methods:{
    toInfo:function (){
      this.$router.push("/info");
    },
    toHome:function (){
      this.$router.push("/");
    },
    toBin:function (){
      this.$router.push("/bin");
    }
  }
}
</script>

<style scoped>
.bg-purple {
  background: #d3dce6;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

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
  border-image: linear-gradient(0deg, #979696, #e7e7e7) 1 10;
}

.item {
  position: absolute;
  left: 80%;
  top: 30%;
  height: 50%;
}

.demo-type {
  position: absolute;
  left: 86%;
  top: 25%;
  height: 40%;
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
  font-size: 16px;

}

.button--size-x {
  font-size: 15px;
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
  background: #d2d1d1;
  color: #000000;
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

/*  加入按钮*/
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
  background-color: #dcd8d8;
  color: #000000;
}

.button--join.button--inverted:hover {
  background-color: #55646d;
  color: #fcfcfd;
}

</style>