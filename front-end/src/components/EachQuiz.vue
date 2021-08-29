<template>
  <div class="quiz">
    <a style="float: left;padding-left: 45px;padding-top: 20px;width: 400px;text-align:left;">{{ name }}</a>
    <!--    <a class="bas" style="float: left;padding-left: 50px;padding-top: 20px">ID：{{ id }}</a>-->
    <a class="bas" style="float: left;padding-left: 40px;padding-top: 20px;">状态：{{
        state === true ? '已发布' : '未发布'
      }}</a>
    <a class="bas" style="float: left;padding-left: 30px;padding-top: 20px">创建日期：{{ date.substring(0, 10) }}</a>
    <a class="bas" style="float: left;padding-left: 30px;padding-top: 20px">回收量：{{ num }}</a>
    <!--分割线-->
    <div class="midText"></div>
    <a class="on" style="float:right;padding-right: 70px;padding-top: 52px;height: 20px;cursor:pointer;" @click="del"
       @mouseover="Over($event)"
       @mouseleave="Leave($event)">删除</a>
    <img src="../assets/del.png" style="float:right;padding-right: 10px;padding-top: 52px;height: 20px;cursor:pointer;">

    <a class="on" style="float:right;padding-right: 30px;padding-top: 52px;height: 20px;width: 60px;cursor:pointer;"
       @click="dialogFormVisible = true"
       v-if="state===false"
       @mouseover="Over($event)"
       @mouseleave="Leave($event)">发布</a>
    <a class="on" style="float:right;padding-right: 30px;padding-top: 52px;height: 20px;width: 60px;cursor:pointer;"
       @click="suspend"
       v-else
       @mouseover="Over($event)"
       @mouseleave="Leave($event)"
    >暂停</a>
    <img src="../assets/suspend.png" v-if="state===true"
         style="float:right;padding-right: 0;padding-top: 53px;height: 20px;cursor:pointer;">
    <img src="../assets/open.png" v-else
         style="float:right;padding-right: 0;padding-top: 53px;height: 20px;cursor:pointer;">

    <a class="on" style="float:right;padding-right: 30px;padding-top: 52px;height: 20px;width: 60px;cursor:pointer;"
       @click="copy"
       @mouseover="Over($event)"
       @mouseleave="Leave($event)"
    >拷贝</a>
    <img src="../assets/copy.png"
         style="float:right;padding-right: 0px;padding-top: 53px;height: 20px;cursor:pointer;">

    <el-dialog title="问卷截止日期" :visible.sync="dialogFormVisible">
      <el-date-picker
          v-model="value"
          type="datetime"
          placeholder="选择日期时间"
          default-time="12:00:00">
      </el-date-picker>
      <div slot="footer" class="dialog-footer">
        <el-button @click="pub">不 限</el-button>
        <el-button v-if="this.value !== ''" type="primary" @click="pub">提 交</el-button>
        <el-button v-else type="primary" disabled>提 交</el-button>
      </div>
    </el-dialog>


    <a class="fun" style="float: right;padding-right: 130px;padding-top: 50px" @click="edit"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">编辑问卷</a>
    <!--    暂时先写成导出结果-->

    <download-excel
        :data="json_data"
        :fields="json_fields"
        worksheet="My Worksheet"
        type="excel"
        name="filename.xls">
      <a class="fun" style="float: right;padding-right: 30px;padding-top: 50px"
         @mouseover="mouseOver($event)"
         @mouseleave="mouseLeave($event)"
         @click="exported">导出数据</a>
    </download-excel>

    <a class="fun" style="float: right;padding-right: 30px;padding-top: 50px" @click="toResult"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">查看结果</a>
    <a class="fun" style="float: right;padding-right: 30px;padding-top: 50px" @click="links"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">发送链接</a>


  </div>
</template>

<script>
export default {
  name: "EachQuiz",
  props: {
    name: String,
    type: String,
    id: String,
    state: Boolean,
    date: String,
    num: String,
    Qsum: String
  },
  data() {
    return {
      json_fields: {},
      letter: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
      json_data: [],
      dialogTableVisible: false,
      dialogFormVisible: false,
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      value: '',
      formLabelWidth: '120px'
    }

  },
  methods: {
    mouseOver($event) {
      $event.currentTarget.className = 'active';
    },
    mouseLeave($event) {
      $event.currentTarget.className = 'fun';
    },
    Over($event) {
      $event.currentTarget.className = 'off';
    },
    Leave($event) {
      $event.currentTarget.className = 'on';
    },
    del() {
      const formData = new FormData();
      formData.append("ID", this.id)
      this.$axios.post('/quiz/recycle', {"ID": this.id})
          .then(result => {
            console.log(result)
            this.$router.go(0);
          })
    },
    deadline() {


    },
    pub() {
      this.dialogFormVisible = false
      this.$axios.post('/user/set_end', {"qnid": this.id, "endTime": this.value})
          .then(result => {
            console.log(result)
          })
      this.$axios.post('/quiz/publish', {"ID": this.id})
          .then(result => {
            console.log(result)
            this.state = true;
            this.$router.go(0);
          })
    },
    suspend() {
      const formData = new FormData();
      formData.append("ID", this.id)
      this.$axios.post('/quiz/suspend', {"ID": this.id})
          .then(result => {
            console.log(result)
            this.state = false;
            this.$router.go(0);
          })
    },
    edit() {
      this.$router.push({
        path: "/creatingQuestionnaire",
        query: {
          isEdit: true,
          id: this.id,
        }
      });
    },
    toResult() {
      if (this.num !== '0') {
        this.$router.push({
          path: "/result",
          query: {
            id: this.id
          }
        });
      } else {
        this.$notify({
          title: '抱歉',
          message: '暂时没有答卷',
          position: 'bottom-left',
          type: "warning"
        });
      }

    },
    copy() {
      this.$axios.post('/createQn/copy', {"qnid": this.id})
          .then(result => {
            console.log(result)
            this.$router.go(0);
          })
    },
    exported() {
      if (this.num !== '0') {
        this.json_fields = {
          '编号': 'Qnum',
          '用户名': 'username',
        };
        for (let i = 0; i < this.Qsum; i++) {
          let x = (i + 1).toString();
          this.json_fields[x] = 'num' + i;
        }
        this.$axios.post('/quiz/idp_result', {"qnid": this.id})
            .then(result => {
              this.json_data = [];
              for (let i = 0; i < result.data.resultList.length; i++) {
                let line = {'Qnum': i + 1};
                line['username'] = result.data.resultList[i].userName;
                for (let k = 0; k < this.Qsum; k++) {
                  if (result.data.resultList[i].AnswerList[k].answer !== null) {
                    if (result.data.resultList[i].AnswerList[k].type === 0) {
                      line['num' + k] = this.letter[result.data.resultList[i].AnswerList[k].answer];
                    } else if (result.data.resultList[i].AnswerList[k].type === 1) {
                      let ans = '';
                      for (let j = 0; j < result.data.resultList[i].AnswerList[k].answer.length; j++)
                        ans += this.letter[result.data.resultList[i].AnswerList[k].answer]
                      line['num' + k] = ans;
                    } else if (result.data.resultList[i].AnswerList[k].type === 2) {
                      line['num' + k] = result.data.resultList[i].AnswerList[k].answer;
                    } else if (result.data.resultList[i].AnswerList[k].type === 3) {
                      line['num' + k] = result.data.resultList[i].AnswerList[k].answer;
                    } else {
                      line['num' + k] = result.data.resultList[i].AnswerList[k].answer;
                    }
                  } else
                    line['num' + k] = '未填'
                }
                this.json_data.push(line)
              }
              console.log('x')
              console.log(this.json_data)
            });
      } else {
        this.$notify({
          title: '抱歉',
          message: '暂时没有答卷',
          position: 'bottom-left',
          type: "warning"
        });
      }
    },

    links() {
      this.$router.push({
        path: "/sentout",
        query: {
          id: this.id,
          type: this.type}}
      );
    }
  }
}
</script>

<style scoped>
.quiz {
  min-width: 855px;
  max-width: 855px;
  padding-left: 0;
  width: 100%;
  height: 130px;
  background-color: white;
  border: #e5e5e5 solid 1px;
  border-radius: 10px;
  box-shadow: 0px 0px 2px 1px #e5e5e5;
}

.midText {
  position: absolute;
  margin-top: 60px;
  left: 22%;
  width: 850px;
  height: 2px;
  max-width: 800px;
  background-color: #e5e4e4;
}

.bas {
  font-size: 5px;
}

.fun {
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  height: 50px;
}

.active {
  color: #0b92e8;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  height: 50px;
}

.on {
  font-size: 15px;
  cursor: pointer;
  height: 50px;
}

.off {
  color: #0b92e8;
  font-size: 15px;
  cursor: pointer;
  height: 50px;
}
</style>