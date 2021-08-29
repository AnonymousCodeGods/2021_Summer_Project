<template>
  <div id="sentout" :style="heightAndWidth">
    <div class="head">
      <img alt="Vue logo" src="../assets/logo.png" style="position:absolute;top:5%;height: 75%;left: 5%">

      <div class="demo-type">
        <div>
          <el-avatar icon="el-icon-user-solid" size="small"></el-avatar>
        </div>
        <!--        <div>-->
        <!--          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>-->
        <!--        </div>-->
      </div>

      <el-dropdown style="position:absolute;top:40%;height: 80%;left: 93%" @command="logout">
      <span class="el-dropdown-link">
        {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="退出">退出</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
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
                text-align: center;border-radius: 4px;box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
                  <div class="qrcode" ref="qrCodeUrl"></div>
                </div>
              </el-col>
              <el-col :span="14">
                <div style="width:370px;height: 300px;display: table-cell;vertical-align: middle;text-align: center;">
                  <el-input
                      placeholder="无"
                      v-model="address"
                      :readonly="true"
                      style="width: 320px;">
                  </el-input>

                  <el-button style="margin-top: 30px" @click="refresh">
                    刷新
                  </el-button>
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
import QRCode from 'qrcodejs2'

export default {
  name: "SentOut",
  data() {
    return {
      id: '',
      heightAndWidth: 'margin:0; height:' +
          (window.innerHeight).toString() +
          'px; width:' +
          (window.innerWidth).toString() +
          'px;',
      address: '',
      username: '',
      dialog1:false,
    }
  },
  created() {
    this.id = this.$route.query.id;
    this.type = this.$route.query.type;
    this.username = this.$cookies.get('username')
    if(this.type === '2')
    this.address = 'http://localhost:8080/#/collectingSignUpQuestionnaire?id=' + this.id;
    else if(this.type === '3'){
      this.address = 'http://localhost:8080/#/examQuestionnaire?id=' + this.id;
    }else{
      this.address = 'http://localhost:8080/#/collectingQuestionnaire?type='+this.type+'&id=' + this.id;
    }
  },
  methods: {
    toInfo: function () {
      this.$router.push("/info");
    },
    toHome: function () {
      this.$router.push("/home");
    },
    logout(command) {
      console.log(command);
      this.$cookies.remove('username');
      this.$router.push("/");
    },
    refresh() {
      let chars = 'ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwsyz0123456789';//这里没有加其他字符，需要可自行添加
      let tempLen = chars.length;
      let tempStr = '';
      for (let i = 0; i < 8; ++i) {
        tempStr += chars.charAt(Math.floor(Math.random() * tempLen));
      }
      console.log(this.id)
      this.$axios.post('/quiz/refresh', {"qnid": this.id, "key": tempStr})
          .then(result => {
            this.id = result.data.newId;
            this.$router.push('/home');
            // this.$router.go(0)
          })
    },
    creatQrCode() {
      const qrcode = new QRCode(this.$refs.qrCodeUrl, {
        text: this.address, // 需要转换为二维码的内容
        width: 200,
        height: 200,
        colorDark: '#000000',
        colorLight: '#ffffff',
        correctLevel: QRCode.CorrectLevel.H
      });
    },
  },
  mounted() {
    this.creatQrCode();
  },
}
</script>

<style scoped>

.qrcode {
  margin-left: 18%;
}

.head {
  position: absolute;
  top: 0;
  left: 0;
  height: 62px;
  min-height: 60px;
  width: 100%;
  background-color: #ffffff;
}

.demo-type {
  position: absolute;
  left: 90%;
  top: 30%;
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


/* Typography and Roundedness */
.button--text-thick {
  font-weight: 300;
}

.button--round-s {
  border-radius: 2px;
}


/* Wapasha */
.button.button--login {
  background: #176c97;
  color: #fff;
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


</style>