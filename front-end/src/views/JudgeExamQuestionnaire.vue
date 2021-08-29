<template>
  <div :style="heightAndWidth">
    <el-card style="width: 800px; margin: auto" v-loading.fullscreen.lock="fullscreenLoading">
      <div id="pdfDom">
        <div slot="header" class="clearfix">
          <span style="font-size: larger">考试答案</span>
        </div>


        <el-table
            :data="tableData"
            style="width: 100%">
          <el-table-column
              prop="no"
              label="题号"
              width="340">
          </el-table-column>
          <el-table-column
              prop="user"
              label="您的答案"
              width="340">
          </el-table-column>
          <el-table-column
              prop="cor"
              label="标准答案">
          </el-table-column>
        </el-table>


        <div v-for="item in que.QList"
             :key="item.qid"
             style="margin: 15px;margin-top: 5%">
          <div v-if="item.type===0">
            <div class="queLabel">
              <span v-if="que.showNumbers">
                {{ item.qid + 1 }}.
              </span>
              <span>
                {{ item.title }}
              </span>
            </div>
            <div v-if="item.hasAnswer" style="margin-left: 10%;margin-right: 10%">
              <el-radio-group
                  v-model="item.selection" style="width: 100%">
                <el-radio
                    disabled
                    v-for="(subItem,index) in item.option"
                    :key="subItem.oid"
                    :label="subItem.oid"
                    style="width: 100%;margin: 10px;display: flex;align-items: flex-start;">
                  <span style="font-size: medium;color: black">
                    {{ subItem.content }}
                    <el-tag type="info" v-if="index===item.answer"
                            style="margin-left: 20%;color: #ff7500;background-color: #f3f9f1">
                    答案{{ subItem.limit }}
                  </el-tag>
                  </span>
                </el-radio>
              </el-radio-group>
            </div>
          </div>


          <div v-if="item.type===1">
            <div class="queLabel">
              <span v-if="que.showNumbers">
                {{ item.qid + 1 }}.
              </span>
              <span>
                {{ item.title }}
              </span>
            </div>
            <div v-if="item.hasAnswer" style="margin-left: 10%;margin-right: 10%">
              <el-checkbox-group
                  v-model="item.selections" style="width: 100%">
                <el-checkbox
                    disabled
                    v-for="(subItem,index) in item.option"
                    :key="subItem.oid"
                    :label="subItem.oid"
                    style="width: 100%;margin: 10px;display: flex;align-items: flex-start;">
                  <span style="font-size: medium;color: black">
                    {{ subItem.content }}
                    <el-tag type="info" v-if="item.answer.includes(index)"
                            style="margin-left: 20%;color: #ff7500;background-color: #f3f9f1">
                    答案{{ subItem.limit }}
                    </el-tag>
                  </span>
                </el-checkbox>
              </el-checkbox-group>
            </div>
          </div>
          <div v-if="item.type===2">
            <div class="queLabel">
              <span v-if="que.showNumbers">
                {{ item.qid + 1 }}.
              </span>
              <span>
                {{ item.title }}
              </span>
            </div>
            <div v-if="item.hasAnswer" style="margin: 7px 10%;text-align: left">
              <span style="font-size: medium;display: block">{{ item.input }}</span>
              <span style="font-size: medium;color: orange;display: block">答案：{{ item.answer }}</span>
            </div>
          </div>
          <div v-if="item.type===3">
            <div class="queLabel">
              <span v-if="que.showNumbers">
                {{ item.qid + 1 }}.
              </span>
              <span>
                {{ item.title }}
              </span>
            </div>
            <div v-if="false" class="queLabel">
              <el-rate
                  v-model="item.rating"
                  :colors="colors">
              </el-rate>
            </div>
          </div>
          <div v-if="item.type===4">
            <div class="queLabel">
              <span v-if="que.showNumbers">
                {{ item.qid + 1 }}.
              </span>
              <span>
                {{ item.title }}
              </span>
            </div>
            <div v-if="false" class="queLabel">
              <el-input v-model="item.location" disabled style="width: 75%">

              </el-input>
              <el-popover placement="top"
                          title="确定要获取您的当前位置吗"
                          v-model="item.dialogVisible">
                <el-button plain type="warning" icon="el-icon-map-location" slot="reference"
                           style="margin-left: 5%;width: 20%">
                  定位
                </el-button>
                <el-button plain type="warning" icon="el-icon-check" size="mini" style="margin-left:15%;width: 30%"
                           v-on:click="getMapLocation(item)"/>
                <el-button plain type="" icon="el-icon-close" size="mini" style="margin-left:10%;width: 30%"
                           v-on:click="item.dialogVisible=false"/>
              </el-popover>
            </div>
          </div>
        </div>
      </div>
      <div style="margin-top: 30px">
        <el-button type="primary" style="width: 30%" plain icon="el-icon-circle-check" v-on:click="quit">返回首页
        </el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CQue',
  created() {
    // this.fullscreenLoading = true;
    this.que.qnId = this.$route.query.id;
    console.log(this.$route.query.id)
    this.$axios.post('/quiz/score_stat', {"userName": this.$cookies.get('username'), "qnid": this.que.qnId})
        .then(result => {
          console.log(result)
          this.correct = result.data.correctAnswer;
          this.userAnswer = this.$route.query.AnswerList;
          for (let i = 0; i <= this.correct.length; i++) {
            let line = {};
            if (this.correct[i].type === 0) {
              let chars = 'ABCDEFGHIJKLMNOPQRSTUVWSYZ'
              line['no'] = i;
              line['user'] = this.userAnswer[i].answer === null ? '无' : chars[this.userAnswer[i].answer];
              line['cor'] = this.correct[i].answer === null ? '无' : chars[this.correct[i].answer];
            } else if (this.correct[i].type === 1) {
              let chars = 'ABCDEFGHIJKLMNOPQRSTUVWSYZ'
              line['no'] = i;
              let us='';
              for(let k=0;k<this.userAnswer[i].answer.length;k++)
                us+=this.userAnswer[i].answer[k] === null ? '无' : chars[this.userAnswer[i].answer[k]];
              line['user']=us;

              let co='';
              for(let k=0;k<this.correct[i].answer.length;k++)
                co+=this.correct[i].answer[k] === null ? '无' : chars[this.correct[i].answer[k]];
              line['cor']=co;
            } else {
              line['no'] = i;
              line['user'] = this.userAnswer[i].answer === null ? '无' : this.userAnswer[i].answer;
              line['cor'] = this.correct[i].answer === null ? '无' : this.correct[i].answer;
            }
            this.tableData.push(line)
          }
        })
  },
  data: function () {
    return {
      tableData: [],
      heightAndWidth: 'margin:0; height:' +
          (window.innerHeight).toString() +
          'px; width:' +
          (window.innerWidth).toString() +
          'px;' +
          'background-color: #fafafa;' +
          'position:fixed;overflow:scroll',
      que: {
        qnId: '0',
        showNumbers: true,
        qnType: '3',
        title: "考试问卷",
        QList: []
      },
      correct: [],
      userAnswer: [],
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      fullscreenLoading: false,
    }
  },

  methods: {
    quit() {
      this.$router.push("/")
    }
  },
}
</script>

<style>
.queLabel {
  margin-left: 10%;
  margin-bottom: 8px;
  margin-right: 10%;
  text-align: start;
}

.row {
  margin-top: 50px
}
</style>
