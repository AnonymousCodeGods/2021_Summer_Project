<template>
  <div>
    <span style="font-size: 20px;margin-left: 1100px;margin-top: 100px" class="box_fixed" id="boxFixed" :class="{'is_fixed' : isFixed}">考试结束倒计时:{{
        hour ? hourString + ':' + minuteString + ':' + secondString : minuteString + ':' + secondString
      }}</span>
    <el-card style="width: 800px; margin: auto" v-loading.fullscreen.lock="fullscreenLoading">
      <div class="row" id="pdfDom">
        <div slot="header" class="clearfix">
          <span style="font-size: larger">{{ que.title }}</span>
        </div>
        <div v-for="item in que.QList"
             :key="item.qid" style="margin: 15px">
          <div v-if="item.type===0">
            <div class="queLabel">
              {{ item.qid + 1 }}.{{ item.title }}
            </div>
            <div style="margin-left: 10%;margin-right: 10%">
              <el-radio-group
                  v-model="item.selection" style="width: 100%">
                <el-radio
                    v-for="subItem in item.option"
                    :key="subItem.oid"
                    :label="subItem.oid"
                    style="width: 100%;margin: 10px;display: flex;align-items: flex-start;">
                  <span style="font-size: medium;">{{ subItem.content }}</span>
                </el-radio>
              </el-radio-group>
            </div>
          </div>
          <div v-if="item.type===1">
            <div class="queLabel">
              {{ item.qid + 1 }}.{{ item.title }}
            </div>
            <div style="margin-left: 10%;margin-right: 10%">
              <el-checkbox-group
                  v-model="item.selections" style="width: 100%">
                <el-checkbox
                    v-for="subItem in item.option"
                    :key="subItem.oid"
                    :label="subItem.oid"
                    style="width: 100%;margin: 10px;display: flex;align-items: flex-start;">
                  <span style="font-size: medium;">{{ subItem.content }}</span>
                </el-checkbox>
              </el-checkbox-group>
            </div>
          </div>
          <div v-if="item.type===2">
            <div class="queLabel">
              {{ item.qid + 1 }}.{{ item.title }}
            </div>
            <div style="margin: 7px 10%;">
              <el-input v-model="item.input"/>
            </div>
          </div>
          <div v-if="item.type===3">
            <div style="margin-left: 10%;margin-bottom:8px;text-align: start;">
              {{ item.qid + 1 }}.{{ item.title }}
            </div>
            <div class="queLabel">
              <el-rate
                  v-model="item.rating"
                  :colors="colors">
              </el-rate>
            </div>
          </div>
        </div>
      </div>
      <div style="margin-top: 30px">
        <el-button type="primary" style="width: 15%" plain icon="el-icon-circle-check" v-on:click="submitQn">提交
        </el-button>
        <el-button type="primary" style="width: 15%" plain icon="el-icon-circle-check" v-on:click="getPdf('问卷')">导出pdf
        </el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CQue',
  created() {
    this.fullscreenLoading = true;
    this.$axios({method: "post", url: "/getQn", data: {"QnId": 87}})
        // data: {"QnId": this.$route.query.id}
        .then(res => {
          if (res.data.que.state === false) {
            this.$router.push('/failedResult');
          }
          this.que.QList = []
          this.que.qnid = res.data.que.qnid;
          this.que.title = res.data.que.title;
          for (let i = 0; i < res.data.que.QList.length; i++) {
            let temp1 = res.data.que.QList[i];
            if (temp1.type === 0) {
              let optionTemp = [];
              for (let j = 0; j < temp1.option.length; j++) {
                let temp2 = temp1.option[j];
                optionTemp.push({
                  oid: j,
                  content: temp2.content
                })
              }
              this.que.QList.push({
                qid: i,
                type: temp1.type,
                title: temp1.title,
                option: optionTemp,
                selection: -1
              })
            } else if (temp1.type === 1) {
              let optionTemp = [];
              for (let j = 0; j < temp1.option.length; j++) {
                let temp2 = temp1.option[j];
                optionTemp.push({
                  oid: j,
                  content: temp2.content
                })
              }
              this.que.QList.push({
                qid: i,
                type: temp1.type,
                title: temp1.title,
                option: optionTemp,
                selections: []
              })
            } else if (temp1.type === 2) {
              this.que.QList.push({
                qid: i,
                type: temp1.type,
                title: temp1.title,
                input: ""
              })
            } else {
              this.que.QList.push({
                qid: i,
                type: temp1.type,
                title: temp1.title,
                rating: 0
              })
            }
          }
          this.fullscreenLoading = false
        })
        .catch(() => {
          this.$notify({
            title: '失败',
            message: '连接失败',
            type: 'error',
            position: 'bottom-left'
          });
          this.fullscreenLoading = false
          this.$router.push('/');
        })
  },
  data: function () {
    return {
      que: {
        qnid: 0,
        title: "测试问卷",
        QList: []
      },
      hour: '',
      minute: '',
      second: '',
      timer: '',
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      fullscreenLoading: false,
      remainTime: '150',
      isFixed: false,
      offsetTop: 0
    }
  },
  mounted() {
    window.addEventListener('scroll', this.initHeight);
    this.$nextTick(() => {
      this.offsetTop = document.querySelector('#boxFixed').offsetTop;
    })
    if (this.remainTime > 0) {
      this.hour = Math.floor((this.remainTime / 3600) % 24)
      this.minute = Math.floor((this.remainTime / 60) % 60)
      this.second = Math.floor(this.remainTime % 60)
      this.countDowm()
    } else {
      this.$router.push('/failedResult');
    }
  },
  methods: {
    initHeight() {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      this.isFixed = scrollTop > this.offsetTop;
    },
    destroyed() {
      window.removeEventListener('scroll', this.handleScroll)
    },
    countDowm() {
      var self = this
      clearInterval(this.timer)
      this.timer = setInterval(function () {
        if (self.hour === 0) {
          if (self.minute !== 0 && self.second === 0) {
            self.second = 59
            self.minute -= 1
          } else if (self.minute === 0 && self.second === 0) {
            self.second = 0;
            self.$emit('countDowmEnd', true)
            clearInterval(self.timer)
            self.$router.push('/endResult');
          } else {
            self.second -= 1
          }
        } else {
          if (self.minute !== 0 && self.second === 0) {
            self.second = 59
            self.minute -= 1
          } else if (self.minute === 0 && self.second === 0) {
            self.hour -= 1
            self.minute = 59
            self.second = 59
          } else {
            self.second -= 1
          }
        }
      }, 1000)
    },
    formatNum(num) {
      return num < 10 ? '0' + num : '' + num
    },
    submitQn() {
      let AnswerListTemp = [];
      for (let i = 0; i < this.que.QList.length; i++) {
        let temp1 = this.que.QList[i];
        if (temp1.type === 0) {
          AnswerListTemp.push({
            type: temp1.type,
            answer: temp1.selection
          })
        } else if (temp1.type === 1) {
          AnswerListTemp.push({
            type: temp1.type,
            answer: temp1.selections
          })
        } else if (temp1.type === 2) {
          AnswerListTemp.push({
            type: temp1.type,
            answer: temp1.input
          })
        } else {
          AnswerListTemp.push({
            type: temp1.type,
            answer: temp1.rating
          })
        }
      }
      this.$axios({
        method: "post", url: "/quiz/submitQn", data: {
          "qnid": this.que.qnid,
          "AnswerList": AnswerListTemp
        }
      })
          .then(res => {
            if (res.data.success === true) {
              this.$notify({
                title: '成功',
                message: '提交问卷成功',
                type: 'success',
                position: 'bottom-left'
              });
            } else {
              this.$notify({
                title: '失败',
                message: '提交问卷失败',
                type: 'error',
                position: 'bottom-left'
              });
              this.$router.push('/');
            }
          })
          .catch(() => {
            this.$notify({
              title: '失败',
              message: '连接失败',
              type: 'error',
              position: 'bottom-left'
            });
            this.fullscreenLoading = false
            this.$router.push('/');
          })
      this.$router.push('/successResult');
    }
  }
  ,
  computed: {
    hourString() {
      return this.formatNum(this.hour)
    }
    ,
    minuteString() {
      return this.formatNum(this.minute)
    }
    ,
    secondString() {
      return this.formatNum(this.second)
    }
  }
}
</script>

<style>
.box_fixed {
  width: 500px;
  height: 40px;
  border: 2px solid #eee;
  border-radius: 10px;
  margin: 0 auto;
  line-height: 40px;
  background: #eee;
}

.is_fixed {
  position: fixed;
  top: 0;
  left: 50%;
  margin-left: -250px;
  z-index: 999;
}

.queLabel {
  margin-left: 10%;
  margin-bottom: 8px;
  margin-right: 10%;
  text-align: start;
}
</style>
