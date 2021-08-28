<template>
  <div>
    <div class="head">
      <img alt="Vue logo" src="../assets/logo.png" style="position:absolute;top:5%;height: 75%;left: 5%">

      <!--      <el-badge :value="12" class="item">-->
      <!--        <el-button size="small">消息</el-button>-->
      <!--      </el-badge>-->
      <el-menu :default-active="activeIndex"
               class="el-menu-demo"
               mode="horizontal"
               text-color="black"
               active-text-color="#6060ff">
        <el-menu-item index="1" style="position: absolute;left: 36%;">我的问卷</el-menu-item>
        <!--        <el-submenu index="2" style="position: absolute;left: 60%;">-->
        <!--          <template slot="title">我的工作台</template>-->
        <!--          <el-menu-item index="2-1">选项1</el-menu-item>-->
        <!--          <el-menu-item index="2-2">选项2</el-menu-item>-->
        <!--          <el-menu-item index="2-3">选项3</el-menu-item>-->
        <!--        </el-submenu>-->
        <el-menu-item index="2" style="position: absolute;left: 45%;" @click="createQuiz">创建问卷</el-menu-item>
        <el-menu-item index="3" style="position: absolute;left: 54%;" @click="bin">回收站</el-menu-item>
      </el-menu>


      <div class="demo-type" >
        <div>
          <el-avatar icon="el-icon-user-solid" size="small" ></el-avatar>
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
      <a style="
        position: absolute;
        font-size: 20px;
        font-weight: bold;
        top: 7%;
        left: 20%;
        color: black;
      "
      >问卷列表</a>
      <el-dropdown style="position: absolute;left: 35%;top: 8%" @command="sorted">
      <span class="el-dropdown-link">
        {{ sort }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="创建时间">创建时间</el-dropdown-item>
          <el-dropdown-item command="发布日期">发布时间</el-dropdown-item>
          <el-dropdown-item command="回收量">回收量</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <el-dropdown style="position: absolute;left: 50%;top: 8%" @command="stated">
      <span class="el-dropdown-link">
        {{ state }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="已发布">已发布</el-dropdown-item>
          <el-dropdown-item command="未发布">未发布</el-dropdown-item>
          <el-dropdown-item command="状态">全部</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-dropdown style="position: absolute;left: 43%;top: 8%" @command="handleCommand">
      <span class="el-dropdown-link">
        {{ value }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="正序">正序</el-dropdown-item>
          <el-dropdown-item command="倒序">倒序</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <div style="position: absolute;left: 56%;top:6%;width: 22%">
        <img src="../assets/search.png" style="position:absolute;top:0;height: 40px;left: 90%;cursor: pointer" @click="search">
        <el-input v-model="input" placeholder="请输入关键字" style="position: absolute;left: 10%;width: 80%"></el-input>
      </div>


      <!--      <button-->
      <!--          type="button"-->
      <!--          class="button button&#45;&#45;login button&#45;&#45;round-s button&#45;&#45;text-thick button&#45;&#45;inverted button&#45;&#45;size"-->
      <!--          style="position:absolute;left: 5%; top: 7%;width: 200px; height: 60px"-->
      <!--          @click="createQuiz"-->
      <!--      >创建问卷-->
      <!--      </button>-->

      <!--      &lt;!&ndash; menu菜单 &ndash;&gt;-->
      <!--      <button-->
      <!--          type="button"-->
      <!--          class="button button&#45;&#45;join button&#45;&#45;round-x button&#45;&#45;text-thick button&#45;&#45;beforeinverted button&#45;&#45;size"-->
      <!--          style="-->
      <!--        position: absolute;-->
      <!--        left: 5%; top: 150px;-->
      <!--        width: 200px;-->
      <!--        height: 60px;-->
      <!--      "-->
      <!--      >-->
      <!--        全部问卷-->
      <!--      </button>-->
      <!--      <button-->
      <!--          type="button"-->
      <!--          class="button button&#45;&#45;join button&#45;&#45;round-x button&#45;&#45;text-thick button&#45;&#45;inverted button&#45;&#45;size"-->
      <!--          style="-->
      <!--        position: absolute;-->
      <!--        left: 5%; top: 210px;-->
      <!--        width: 200px;-->
      <!--        height: 60px;-->
      <!--      "-->
      <!--          @click="bin"-->
      <!--      >-->
      <!--        回收站-->
      <!--      </button>-->
      <!--      <button-->
      <!--          type="button"-->
      <!--          class="button button&#45;&#45;join button&#45;&#45;round-x button&#45;&#45;text-thick button&#45;&#45;inverted button&#45;&#45;size"-->
      <!--          style="-->
      <!--        position: absolute;-->
      <!--        left: 5%; top: 270px;-->
      <!--        width: 200px;-->
      <!--        height: 60px;-->
      <!--      "-->
      <!--          @click="toInfo"-->
      <!--      >-->
      <!--        个人信息-->
      <!--      </button>-->

      <!--           问卷信息-->
      <div style="margin-top: 10%; margin-left:20%;margin-right:20%;background: transparent; height: 75%">
        <div
            v-for="it in list"
            :key="it.index"
            style="margin-top: 20px;"
        >
          <each-quiz
              :type="it.name"
              :date="it.createDate"
              :id="it.ID.toString()"
              :num="it.num.toString()"
              :state="it.state"
          ></each-quiz>
        </div>
        <!--没有问卷-->
        <img src="../assets/empty.png" v-if="this.list.length===0">
        <p style="color: #a5a5a5" v-if="this.list.length===0">快去创建一个问卷吧</p>
        <!--分页-->
        <div class="block">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page.sync="page"
              :page-size="3"
              layout="total, prev, pager, next"
              :total=this.total>
          </el-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EachQuiz from "../components/EachQuiz.vue";

export default {
  name: 'HelloWorld',
  components: {
    EachQuiz,
  },
  props: {
    msg: String
  },
  created() {
    console.log(this.$route.query)
    this.username = this.$cookies.get('username')
    this.$axios.post('/user/info', {"userName": this.username})
        .then(result => {
          this.allList = result.data.info.quizs;
          console.log(this.allList)
          this.myList = [];
          console.log(this.allList.length)
          for (let i = 0; i < this.allList.length; i++)
            if (this.allList[i].bin === false)
              this.myList.push(this.allList[i]);
          console.log(this.myList)
          this.total = this.myList.length;
          if (this.myList.length <= 3) {
            this.list = this.myList;
            console.log(this.list);
          } else {
            for (let i = 0; i < 3; i++)
              this.list.push(this.myList[i]);
            console.log(this.list);
          }
        })
  },
  data() {
    return {
      sort: '创建时间',
      state: '状态',
      value: '正序',
      input: '',
      username: 'quiz',
      myList: [],
      allList: [],
      list: [],
      total: 1,
      page: 1,
      order: 0,
      activeIndex: '1'
    }
  },
  methods: {
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      this.page = val;
      console.log(`当前页: ${val}`);
      this.list = [];
      if (val * 3 > this.total) {
        for (let i = val * 3 - 3; i < this.total; i++)
          this.list.push(this.myList[i]);
      } else {
        for (let i = 0; i < 3; i++)
          this.list.push(this.myList[val * 3 - 3 + i]);
      }
    },
    bin() {
      this.$router.push("/bin");
    },
    sorted(command) {
      // this.$message('click on item ' + command);
      this.sort = command;
      if (command === "回收量") {
        this.allList.sort(function (a, b) {
          return a.num - b.num;
        });
        this.myList.sort(function (a, b) {
          return a.num - b.num;
        });
      } else if (command === "发布日期") {
        this.allList.sort(function (a, b) {
          return Date.parse(b.pubDate) - Date.parse(a.pubDate);
        });
        this.myList.sort(function (a, b) {
          return Date.parse(b.pubDate) - Date.parse(a.pubDate);
        });
      } else {
        this.allList.sort(function (a, b) {
          return Date.parse(b.createDate) - Date.parse(a.createDate);
        });
        this.myList.sort(function (a, b) {
          return Date.parse(b.createDate) - Date.parse(a.createDate);
        });
      }
      this.list = [];
      const val = this.page;
      if (val * 3 > this.total) {
        for (let i = val * 3 - 3; i < this.total; i++)
          this.list.push(this.myList[i]);
      } else {
        for (let i = 0; i < 3; i++)
          this.list.push(this.myList[val * 3 - 3 + i]);
      }
    },
    stated(command) {
      // this.$message('click on item ' + command);
      this.state = command;
      this.myList = [];
      if (command === "已发布") {
        for (let i = 0; i < this.allList.length; i++)
          if (this.allList[i].state === true)
            this.myList.push(this.allList[i]);
      } else if (command === "未发布") {
        for (let i = 0; i < this.allList.length; i++)
          if (this.allList[i].state === false)
            this.myList.push(this.allList[i]);
      } else {
        this.myList = this.allList;
      }
      this.total = this.myList.length;
      this.list = [];
      this.page = 1;
      const val = this.page;
      if (val * 3 > this.total) {
        for (let i = val * 3 - 3; i < this.total; i++)
          this.list.push(this.myList[i]);
      } else {
        for (let i = 0; i < 3; i++)
          this.list.push(this.myList[val * 3 - 3 + i]);
      }
    },
    handleCommand(command) {
      // this.$message('click on item ' + command);
      this.value = command;
      if (command === "倒序" && this.order === 0) {
        this.order = 1;
        // this.allList.reverse();
        this.allList.reverse();
        this.myList = this.allList;
        this.list = [];
        const val = this.page;
        if (val * 3 > this.total) {
          for (let i = val * 3 - 3; i < this.total; i++)
            this.list.push(this.myList[i]);
        } else {
          for (let i = 0; i < 3; i++)
            this.list.push(this.myList[val * 3 - 3 + i]);
        }
      } else if (command === "正序" && this.order === 1) {
        this.order = 0;
        // this.allList.reverse();
        this.allList.reverse();
        this.myList = this.allList;
        this.list = [];
        const val = this.page;
        if (val * 3 > this.total) {
          for (let i = val * 3 - 3; i < this.total; i++)
            this.list.push(this.myList[i]);
        } else {
          for (let i = 0; i < 3; i++)
            this.list.push(this.myList[val * 3 - 3 + i]);
        }
      }
    },
    toInfo: function () {
      this.$router.push("/info");
    },
    logout(command) {
      console.log(command);
      this.$cookies.remove('username');
      this.$router.push("/");
    },
    // 查找
    search() {
      console.log(this.input);
      console.log(this.state);
      this.myList.splice(0)
      console.log(":::::", this.myList)
      if (this.input === '') {
        this.$router.go(0);
      } else {
        if (this.state === '状态') {
          this.myList = this.allList.filter(item => item.name.indexOf(this.input) !== -1)
        } else if (this.state === '已发布') {
          this.myList = this.allList.filter(item => item.name.indexOf(this.input) !== -1 && item.state === true)
        } else {
          this.myList = this.allList.filter(item => item.name.indexOf(this.input) !== -1 && item.state === false)
        }

        this.total = this.myList.length;
        this.list = [];
        this.page = 1;
        const val = this.page;
        if (val * 3 > this.total) {
          for (let i = val * 3 - 3; i < this.total; i++)
            this.list.push(this.myList[i]);
        } else {
          for (let i = 0; i < 3; i++)
            this.list.push(this.myList[val * 3 - 3 + i]);
        }
      }
    },
    addNew() {

    },
    createQuiz() {
      this.$router.push({
        path: "/creatingQuestionnaire",
        query: {
          id: 0
        }
      });
    },

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
.head {
  position: absolute;
  top: 0;
  left: 0;
  height: 62px;
  min-height: 60px;
  width: 100%;
  background-color: #ffffff;
  //background-color:#545c64
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
}

.block {
  position: absolute;
  margin-top: 45px;
  right: 17%;
}

.item {
  position: absolute;
  left: 80%;
  top: 30%;
  height: 50%;
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
  border-radius: 0;
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
