<template>
  <div>
    <div class="head">
      <img alt="Vue logo" src="../assets/logo.png" style="position:absolute;top:5%;height: 75%;left: 5%">


      <el-menu :default-active="activeIndex"
               class="el-menu-demo"
               mode="horizontal"
               @select="handleSelect"
               text-color="black"
               active-text-color="#6060ff">
        <el-menu-item index="1" style="position: absolute;left: 36%;" @click="toHome">我的问卷</el-menu-item>
        <!--        <el-submenu index="2" style="position: absolute;left: 60%;">-->
        <!--          <template slot="title">我的工作台</template>-->
        <!--          <el-menu-item index="2-1">选项1</el-menu-item>-->
        <!--          <el-menu-item index="2-2">选项2</el-menu-item>-->
        <!--          <el-menu-item index="2-3">选项3</el-menu-item>-->
        <!--        </el-submenu>-->
        <el-menu-item index="2" style="position: absolute;left: 45%;" @click="createQuiz">创建问卷</el-menu-item>
        <el-menu-item index="3" style="position: absolute;left: 54%;">回收站</el-menu-item>
      </el-menu>

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
      <a
          style="
        position: absolute;
        font-size: 17px;
        font-weight: bold;
        top: 7%;
        left: 17%;
        color: black;
      "
      >已删除问卷</a>
      <div class="bin" style="position: absolute;left: 15%;width: 70%;top: 12%">
        <el-table
            :data="tableData"
            style="width:1000px; margin-left: fill"
            border
            stripe
            :default-sort="{prop: 'date', order: 'descending'}"
        >
          <el-table-column
              align="center"
              label="创建日期"
              min-width="6">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 10px">{{ scope.row.date }}</span>
            </template>
          </el-table-column>
          <el-table-column
              align="center"
              prop="name"
              label="问卷名"
              min-width="6">
          </el-table-column>
          <el-table-column
              align="center"
              prop="count"
              label="答卷数"
              min-width="4">
          </el-table-column>
          <el-table-column
              align="center"
              prop="clear"
              label="清空问卷"
              min-width="4">
            <template slot-scope="scope">
              <el-button type="primary" size="mini" icon="el-icon-s-promotion" @click="clearR(scope.$index,scope.row)"
                         v-if="scope.row.count!==0">清空问卷
              </el-button>
            </template>
          </el-table-column>
          <el-table-column
              align="center"
              prop="recover"
              label="恢复"
              min-width="4">
            <template slot-scope="scope">
              <el-button type="success" size="mini" icon="el-icon-refresh-right"
                         @click="recoverR(scope.$index,scope.row)">恢复
              </el-button>
            </template>
          </el-table-column>
          <el-table-column
              align="center"
              prop="delete"
              label="删除"
              min-width="5">
            <el-popconfirm style="margin: auto"
                           title="确定要删除问卷吗？"
                           confirm-button-type="danger"
                           cancel-button-type="infomation"
                           icon="el-icon-info"
                           slot-scope="scope"
                           @confirm="deleteR(scope.$index,scope.row)">
              <el-tooltip slot="reference" effect="dark" content="删除该问卷" placement="top">
                <el-button type="danger" size="mini" icon="el-icon-delete">删除</el-button>
              </el-tooltip>
            </el-popconfirm>
          </el-table-column>
        </el-table>
      </div>
      <!--      <button-->
      <!--          type="button"-->
      <!--          class="button button&#45;&#45;login button&#45;&#45;round-s button&#45;&#45;text-thick button&#45;&#45;inverted button&#45;&#45;size"-->
      <!--          style="position:absolute;left: 5%; top: 7%;width: 200px; height: 60px"-->
      <!--      >创建问卷-->
      <!--      </button>-->
      <!--      &lt;!&ndash; menu菜单 &ndash;&gt;-->
      <!--      <button-->
      <!--          type="button"-->
      <!--          class="button button&#45;&#45;join button&#45;&#45;round-x button&#45;&#45;text-thick button&#45;&#45;inverted button&#45;&#45;size"-->
      <!--          style="-->
      <!--        position: absolute;-->
      <!--        left: 5%; top: 150px;-->
      <!--        width: 200px;-->
      <!--        height: 60px;-->
      <!--      "-->
      <!--          @click="toHome"-->
      <!--      >-->
      <!--        全部问卷-->
      <!--      </button>-->
      <!--      <button-->
      <!--          type="button"-->
      <!--          class="button button&#45;&#45;join button&#45;&#45;round-x button&#45;&#45;text-thick button&#45;&#45;beforeinverted button&#45;&#45;size"-->
      <!--          style="-->
      <!--        position: absolute;-->
      <!--        left: 5%; top: 210px;-->
      <!--        width: 200px;-->
      <!--        height: 60px;-->
      <!--      "-->
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
    </div>
  </div>
</template>

<script>
export default {
  name: 'bin',
  created() {
    this.fullscreenLoading = true;
    this.username = this.$cookies.get('username')
    // this.username = this.$cookies.get('username')
    this.$axios({
      method: "post",
      data: {userName: this.username},
      url: "/user_b/info",
    })
        .then(res => {
          console.log(res.data)
          let binlist;
          binlist = res.data.info.quizs
          for (let i = 0; i < binlist.length; i++) {
            this.tableData.push({
              qnid: binlist[i].ID,
              date: binlist[i].createDate,
              name: binlist[i].name,
              count: binlist[i].num
            })
          }
          console.log(this.tableData)
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
  },
  data() {
    return {
      tableData: [],
      username: '',
      activeIndex: '3'
    }
  },
  methods: {
    deleteR(index, row) {
      this.fullscreenLoading = true;
      this.$axios({
        method: "post",
        data: {qnid: this.tableData[index].qnid},
        url: "user_b/del",
      })
          .then(res => {
            if (res.data.success) {
              this.$notify({
                message: '问卷已删除',
                type: 'warning',
                position: 'bottom-left'
              })
              this.fullscreenLoading = false;
            }
          })
          .catch(res => {
            this.$notify({
              title: '错误',
              message: '连接失败',
              position: 'bottom-left',
              type: "error"
            });
            this.fullscreenLoading = false;
          });
      this.tableData.splice(this.tableData.indexOf(row), 1);
      console.log(this.tableData)
    },
    createQuiz() {
      this.$router.push({
        path: "/creatingQuestionnaire",
        query: {
          id: 0
        }
      });
    },
    recoverR(index, row) {
      console.log(index)
      console.log(this.tableData[index].qnid)
      this.fullscreenLoading = true;
      this.$axios({
        method: "post",
        data: {ID: this.tableData[index].qnid},
        url: "quiz/recover",
      })
          .then(res => {
            if (res.data.success) {
              this.$notify({
                message: '问卷已恢复',
                type: 'success',
                position: 'bottom-left'
              });
              this.fullscreenLoading = false;
            }
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
      this.tableData.splice(this.tableData.indexOf(row), 1);
    },
    clearR(index, row) {
      this.fullscreenLoading = true;
      this.$axios({
        method: "post",
        data: {qnid: this.tableData[index].qnid},
        url: "quiz/clear",
      })
          .then(res => {
            if (res.data.success) {
              this.$notify({
                message: '问卷已清空',
                type: 'info',
                position: 'bottom-left'
              });
              this.fullscreenLoading = false;
            }
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
      this.tableData[index].count = 0;
    },
    toInfo: function () {
      this.$router.push("/info");
    },
    toHome: function () {
      this.$router.push("/home");
    },
    logout(command) {
      console.log(command);
      this.$router.push("/login");
    },
  }
}
</script>

<style>
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
}


.demo-type {
  position: absolute;
  left: 90%;
  top: 30%;
  height: 40%;
}

.el-dropdown-link {
  cursor: pointer;
  color: #6a6a6a;
}

.el-icon-arrow-down {
  font-size: 6px;
}

.button > span {
  vertical-align: middle;
}


</style>