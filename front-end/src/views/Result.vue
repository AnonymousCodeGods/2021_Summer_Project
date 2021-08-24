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
      </div>
      <a style="position:absolute;top:25%;height: 80%;left: 90%">{{ this.$store.state.username }}</a>
    </div>
    <div class="body" style="overflow-y:scroll">
      <el-col :span="6" style="height: 100%">
      </el-col>
      <el-col :span="18">
        <div style="display: flex;justify-content: left;margin-top: 60px; ">
          <el-card style="width: 1200px;height: 100%" :body-style="{ padding: '0px' }">
            <div slot="header" class="clearfix">
              <span> {{ this.que.title }} </span>
              <el-button style="float: right;" type="primary" @click="ExportData">导出数据</el-button>
            </div>
            <div v-for="(item,index) in que.QList" :key="item.qid" style="margin: 20px;">
              <div >
                <div class="queLabel">
                  {{ index + 1 }}.{{ item.title }}
                </div>
<!--                单选多选-->
                <div v-if="item.type===0||item.type===1" style="margin-left: 5%;margin-right: 5%;text-align: center">
                  <el-row style="margin-top:1%">
                    <el-col :span="24" style="height: 100%;width: 100%;margin-top:2%">
                      <el-table
                          margin-left: fill
                          border
                          stripe
                          :data="item.option"
                          style="width: 100%"
                          :summary-method="getSummaries"
                          show-summary>
                        <el-table-column
                            align="center"
                            prop="content"
                            label="选项"
                            sortable
                        >
                        </el-table-column>
                        <el-table-column
                            align="center"
                            prop="count"
                            label="小计"
                            sortable
                            width="100">
                        </el-table-column>
                        <el-table-column
                            show-overflow-tooltip
                            align="center"
                            prop="percentage"
                            label="比例">
                          <template slot-scope="scope">
                            <el-progress :percentage="scope.row.percentage" :format="format"></el-progress>
                          </template>
                        </el-table-column>
                      </el-table>
                    </el-col>
                  </el-row>
                </div>
<!--                填空-->
                <div v-else-if="item.type===2" style="margin-left: 5%;margin-right: 5%;text-align: center">
                  <el-row style="margin-top:1%">
                    <el-col :span="24" style="height: 100%;width: 100%;margin-top:2%">
                      <el-table
                          margin-left: fill
                          border
                          stripe
                          :data="item.Inputlist"
                          style="width: 100%">
                        <el-table-column
                            align="center"
                            prop="index"
                            label="序号"
                            width="200%"
                            sortable>
                        </el-table-column>
                        <el-table-column
                            align="center"
                            prop="content"
                            mid-width="50%"
                            label="内容">
                        </el-table-column>
                      </el-table>
                    </el-col>
                  </el-row>
                </div>
<!--                评分-->
                <div v-else-if="item.type===3" style="margin-left: 5%;margin-right: 5%;text-align: center">
                  <el-row style="margin-top:1%">
                    <el-col :span="24" style="height: 100%;width: 100%;margin-top:2%">
                      <el-table
                          margin-left: fill
                          border
                          stripe
                          :data="item.option"
                          style="width: 100%"
                          :summary-method="getSummaries"
                          show-summary>
                        <el-table-column
                            align="center"
                            prop="content"
                            sortable
                            label="分数"
                        >
                        </el-table-column>
                        <el-table-column
                            align="center"
                            prop="count"
                            sortable
                            label="人数"
                            width="100">
                        </el-table-column>
                        <el-table-column
                            show-overflow-tooltip
                            prop="percentage"
                            align="center"
                            label="比例"
                            >
                          <template slot-scope="scope">
                            <el-progress :percentage="scope.row.percentage" :format="format" ></el-progress>
                          </template>
                        </el-table-column>
                      </el-table>
                    </el-col>
                  </el-row>
                </div>
              </div>
            </div>
          </el-card>
        </div>
      </el-col>
      <button
          type="button"
          class="button button--login button--round-s button--text-thick button--inverted button--size"
          style="position:absolute;left: 5%; top: 6%;width: 200px; height: 65px"
          @click="toHome"
      >返回列表
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Result",
  props: {
    msg: String
  },
  created() {
    this.fullscreenLoading=true;
    this.que.qid=this.$route.query.id
    this.$axios({
      method:"post",
      //todo: url
      url:"/getQn",
      data:{"QnId": this.que.qid}
    })
        .then(res => {
          this.que.title=res.data.que.title
          for (let i = 0; i < res.data.que.QList.length; i++) {
            if(res.data.que.QList[i].type===0||res.data.que.QList[i].type===1){
              this.que.QList.push({
                qid:res.data.que.QList[i].qid,
                total:0,
                type:res.data.que.QList[i].type,
                title:res.data.que.QList[i].title,
                option:res.data.que.QList[i].option
              })
            }else if(res.data.que.QList[i].type===2){
              this.que.QList.push({
                qid:res.data.que.QList[i].qid,
                type:res.data.que.QList[i].type,
                title:res.data.que.QList[i].title,
                Inputlist:[]
              })
            }else{
              this.que.QList.push({
                qid:res.data.que.QList[i].qid,
                total:0,
                type:res.data.que.QList[i].type,
                title:res.data.que.QList[i].title,
                option:[]
              })
              for (let j = 0; j < 6; j++) {
                this.que.QList[i].option.push({content:j+1,count:0,percentage:0})
              }
            }
          }
          this.fullscreenLoading=false
        })
        .catch(() => {
          this.fullscreenLoading=false
        })


    this.$axios({
          method:"post",
          //todo: url
          url:"/quiz/result",
          data:{"ID": this.que.qid}
    })
      .then(res => {
        this.AnswerList=JSON.parse(JSON.stringify(res.data.AnswerList))
        for (let i = 0; i < this.AnswerList.length; i++) {
          if (this.AnswerList[i].type === 0 || this.AnswerList[i].type === 1 || this.AnswerList[i].type === 3) {
            for (let j = 0; j < this.AnswerList[i].selection.length; j++) {

              this.que.QList[i].option[j].count = this.AnswerList[i].selection[j];
              this.que.QList[i].total += this.AnswerList[i].selection[j]
            }
          } else if (this.AnswerList[i].type === 2) {
            for (let j = 0; j < this.AnswerList[i].input.length; j++)
              this.que.QList[i].Inputlist.push({index:j+1,content:this.AnswerList[i].input[j]})
          }
        }

        console.log(this.AnswerList)
        console.log(this.que.QList)
        for (let i = 0; i < this.AnswerList.length; i++) {
          if(this.AnswerList[i].type===0||this.AnswerList[i].type===1||this.AnswerList[i].type===3){
            for (let j = 0; j <this.que.QList[i].option.length; j++) {
              this.que.QList[i].option[j].percentage=this.que.QList[i].option[j].count*100.0/this.que.QList[i].total
            }
          }
        }

        this.fullscreenLoading=false
      })
      .catch(() => {
        this.fullscreenLoading=false
      })



  },
  data() {
    return {
      que: {
        qid: '',
        title: "",
        QList: []
      },
      fullscreenLoading: false,
      AnswerList: [

      ],
    }
  },
  methods: {
    getSummaries(param) {
      const { columns, data } = param;
      const sums = [];
      columns.forEach((column, index) => {
        if (index === 0) {
          sums[index] = '总计 ';
          return;
        }else if(index === 2){
          sums[index] = '';
          return;
        }
        const values = data.map(item => Number(item[column.property]));
        if (!values.every(value => isNaN(value))) {
          sums[index] = values.reduce((prev, curr) => {
            const value = Number(curr);
            if (!isNaN(value)) {
              return prev + curr;
            } else {
              return prev;
            }
          }, 0);
          sums[index] += ' ';
        } else {
          sums[index] = 'N/A';
        }
      });
      return sums;
    },
    format(percentage) {
      return parseFloat(percentage).toFixed(2)+"%";
    }
    ,
    toHome: function () {
      this.$router.push("/home");
    },
    ExportData() {
      //TODO:导出数据
      this.$notify({
        title: '导出成功',
        message: null,
        position: 'bottom-left',
        type: "success"
      })
    }
  }
}
</script>

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

.queLabel {
  margin-left: 5%;
  margin-bottom: 8px;
  margin-right: 5%;
  text-align: start;
}

.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}
</style>