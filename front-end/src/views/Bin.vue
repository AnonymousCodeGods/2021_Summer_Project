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

      <el-dropdown style="position:absolute;top:40%;height: 80%;left: 90%" @command="logout">
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
        left: 29%;
        color: black;
      "
      >已删除问卷</a>

      <div class="bin" style="position: absolute;left: 27%;width: 70%;top: 12%">
        <el-table
            :data="tableData"
            style="width:1000px; margin-left: fill"
            border
            stripe
            :default-sort="{prop: 'date', order: 'descending'}"
        >
          <el-table-column
              align="center"
              label="发布日期"
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
              <el-button type="success" size="mini" icon="el-icon-refresh-right" @click="recoverR(scope.row)">恢复
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
                           @confirm="deleteR(scope.row)">
              <el-tooltip slot="reference" effect="dark" content="删除该问卷" placement="top">
                <el-button type="danger" size="mini" icon="el-icon-delete">删除</el-button>
              </el-tooltip>
            </el-popconfirm>
          </el-table-column>
        </el-table>

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
          class="button button--join button--round-x button--text-thick button--inverted button--size"
          style="
        position: absolute;
        left: 5%; top: 150px;
        width: 200px;
        height: 60px;
      "
          @click="toHome"
      >
        全部问卷
      </button>
      <button
          type="button"
          class="button button--join button--round-x button--text-thick button--beforeinverted button--size"
          style="
        position: absolute;
        left: 5%; top: 210px;
        width: 200px;
        height: 60px;
      "
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
  name: 'bin',
  created() {
    this.tableData = [{
      date: '2021-05-02',
      name: '时间统计',
      count: 0,
    }, {
      date: '2021-05-04',
      name: '作业统计',
      count: 7,
    }, {
      date: '2021-05-04',
      name: '作业统计',
      count: 7,
    }]
    this.username = 'quiz'
  },
  data() {
    return {
      tableData: [],
      username: ''
    }
  },
  methods: {
    deleteR(row) {
      this.$notify({
        message: '问卷已删除',
        type: 'warning',
        position: 'bottom-left'
      });
      this.tableData.splice(this.tableData.indexOf(row), 1);
    },
    recoverR(row) {
      this.$notify({
        message: '问卷已恢复',
        type: 'success',
        position: 'bottom-left'
      });
      this.tableData.splice(this.tableData.indexOf(row), 1);
    },
    clearR(index, row) {
      this.$notify({
        message: '问卷已清空',
        type: 'info',
        position: 'bottom-left'
      });
      this.tableData[index].count = 0;
      this.$set(this.tableData, index, row);
    },
    toInfo: function () {
      this.$router.push("/info");
    },
    toHome: function () {
      this.$router.push("/");
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
  height: 8%;
  width: 100%;
  background-color: #ffffff;

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