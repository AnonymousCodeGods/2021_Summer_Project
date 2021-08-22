<template>
  <div>
    <div class="head">
      <img alt="Vue logo" src="../assets/logo.png" style="position:absolute;top:10%;height: 80%;left: 5%">

      <el-badge :value="12" class="item">
        <el-button size="small">消息</el-button>
      </el-badge>

      <div class="demo-type">
        <div>
          <el-avatar icon="el-icon-user-solid"></el-avatar>
        </div>
<!--        <div>-->
<!--          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>-->
<!--        </div>-->
      </div>

      <a style="position:absolute;top:25%;height: 80%;left: 90%">{{this.$store.state.username}}</a>
    </div>

    <div class="body">
      <a
          style="
        position: absolute;
        font-size: 17px;
        font-weight: bold;
        top: 7%;
        left: 30%;
        color: black;
      "
      >问卷列表</a>

      <el-dropdown style="position: absolute;left: 50%;top: 8%" @command="sorted">
      <span class="el-dropdown-link">
        {{ sort }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="发布时间">发布时间</el-dropdown-item>
          <el-dropdown-item command="创建时间">创建时间</el-dropdown-item>
          <el-dropdown-item command="回收量">回收量</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-dropdown style="position: absolute;left: 58%;top: 8%" @command="handleCommand">
      <span class="el-dropdown-link">
        {{ value }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="正序">正序</el-dropdown-item>
          <el-dropdown-item command="倒序">倒序</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-dropdown style="position: absolute;left: 65%;top: 8%" @command="stated">
      <span class="el-dropdown-link">
        {{ state }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="已发布">已发布</el-dropdown-item>
          <el-dropdown-item command="未发布">未发布</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>


      <div style="position: absolute;left: 75%;top:6%;width: 18%">
        <img src="../assets/search.png" style="position:absolute;top:0;height: 40px;left: 0" alt="">
        <el-input v-model="input" placeholder="请输入关键字" style="position: absolute;left: 20%"></el-input>
      </div>


      <button
          type="button"
          class="button button--login button--round-s button--text-thick button--inverted button--size"
          style="position:absolute;left: 5%; top: 7%;width: 200px; height: 60px"
      >创建问卷
      </button>

      <!-- menu菜单 -->
      <button
          type="button"
          class="button button--join button--round-x button--text-thick button--beforeinverted button--size"
          style="
        position: absolute;
        left: 5%; top: 150px;
        width: 200px;
        height: 60px;
      "

      >
        全部问卷
      </button>
      <button
          type="button"
          class="button button--join button--round-x button--text-thick button--inverted button--size"
          style="
        position: absolute;
        left: 5%; top: 210px;
        width: 200px;
        height: 60px;
      "
          @click="toBin"
      >
        回收站
      </button>
      <button
          type="button"
          class="button button--join button--round-x button--text-thick button--inverted button--size"
          style="
        position: absolute;
        left: 5%; top: 270px;
        width: 200px;
        height: 60px;
      "
          @click="toInfo"
      >
        个人信息
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      sort: '发布时间',
      state: '状态',
      value: '正序',
      input: '',
    }
  },
  methods: {
    sorted(command) {
      // this.$message('click on item ' + command);
      this.sort = command;
    },
    stated(command) {
      // this.$message('click on item ' + command);
      this.state = command;
    },
    handleCommand(command) {
      // this.$message('click on item ' + command);
      this.value = command;
    },
    toInfo:function (){
      this.$router.push("/info");
    },
    toBin:function (){
      this.$router.push("/bin");
    }
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
  border-image: linear-gradient(0deg, #979696, #e7e7e7) 1 10;
}

.item {
  position: absolute;
  left: 70%;
  top: 20%;
  height: 50%;
}

.demo-type{
  position: absolute;
  left: 86%;
  top: 10%;
  height: 40%;
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
  font-weight: 300;
}

.button--round-s {
  border-radius: 2px;
}

.button--round-x {
  
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

// 加入按钮
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
