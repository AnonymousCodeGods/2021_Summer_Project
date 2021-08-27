<template>
  <div :style="heightAndWidth">

    <el-button circle plain type="primary" class="hoverB" style="top:50px" icon="el-icon-back"></el-button>
    <el-popover
        placement="right"
        width="325"
        v-model="addQuestionVisible">
      <div style="text-align: right; margin: 0">
        <el-button plain type="primary" size="mini"  @click="addSingleChoice">单选</el-button>
        <el-button plain type="success" size="mini" @click="addMultiChoice">多选</el-button>
        <el-button plain type="info" size="mini"  @click="addSpaceFilling">填空</el-button>
        <el-button plain type="warning" size="mini" @click="addRating">评分</el-button>
        <el-button plain type="danger" size="mini" @click="addLocating">定位</el-button>
      </div>
      <el-button circle plain type="success" class="hoverB" style="top:100px" icon="el-icon-plus" slot="reference"></el-button>
    </el-popover>
    <el-popover
        placement="right"
        width="185"
        v-model="moreFunctionVisible">
      <div style="text-align: center; margin: 0">
        <el-switch
            active-text="显示题号"
            inactive-text="隐藏题号"
            v-model="que.showNumbers">
        </el-switch>
      </div>
      <el-button circle plain type="info" class="hoverB" style="top:150px" icon="el-icon-more" slot="reference"></el-button>
    </el-popover>
    <el-button circle plain type="warning" class="hoverB" style="top:200px;margin-left: 0" icon="el-icon-check" @click="uploadQn"></el-button>

    <el-dialog :visible="titleEditDialog" :show-close="false">
      <div slot="title">编辑题目</div>
      <el-input v-model="editingTitle" style="margin-bottom: 30px;width: 80%"/>
      <el-button v-on:click="doneTitleEdit" style="width: 60%" type="success" icon="el-icon-check"></el-button>
    </el-dialog>

    <div id="Qn" style="height: 100%;width: 100%;overflow-y:scroll;margin: auto">
      <el-card style="margin: 20px 20% ;" v-loading.fullscreen.lock="fullscreenLoading">
        <div slot="header" class="clearfix">
          <el-input style="font-size: larger" v-model="que.title"></el-input>
        </div>
        <vuedraggable v-model="que.QList"
                      chosenClass="ghost"
                      handle=".drag"
                      :scroll-sensitivity="150"
                      force-fallback="true"
                      animation="400"
                      @start="onStart"
                      @end="onEnd"
                      style="display:table;width:100%">
          <tbody is="transition-group">
          <div v-for="item in que.QList"
               :key="item.qid" class="move">
            <el-card style="margin: 15px;cursor: move"
                     shadow="hover">
              <el-button type="text" icon="el-icon-rank" class="drag"></el-button>
              <div style="float: right;margin-right: 5px;width: 200px  ">
                <el-button type="text"
                           icon="el-icon-document-copy"
                           v-on:click="copyQuestion(item)">复制
                </el-button>
                <el-button type="text"
                           icon="el-icon-delete"
                           style="color: #F56C6C;"
                           v-on:click="deleteQuestion(item)">删除
                </el-button>
                <el-checkbox
                             v-model="item.necessary"
                             style="margin-left: 3%">必填
                </el-checkbox>
              </div>
              <div v-if="item.type===0" class="queLabel" id="singleChoice">
                <div>
                    <span style="line-height: 30px;">
                    <el-tag size="small">单选</el-tag>
                      {{ item.qid + 1 }}.{{ item.title }}
                    <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                      <el-switch
                          v-model="item.isSumLimit"
                          active-color="#3292ff"
                          inactive-color="#99a9bf"
                          style="margin-left: 5%"
                          active-text="限制人数"
                          v-if="que.type ==='2'"
                          inactive-text="开放填写"/>
                    </span>

                  <div style="margin-left: 5%;margin-right: 5%;margin-top:15px">
                    <div v-for="subItem in item.option" :key="subItem.oid">
                      <el-input v-if="item.isSumLimit"
                                v-model="subItem.content"
                                maxlength="28"
                                style="width: 78%;margin-bottom: 10px;">
                        <el-button slot="append" icon="el-icon-close"
                                   v-on:click="deleteOption(item,subItem)"></el-button>
                      </el-input>
                      <el-input v-else
                                v-model="subItem.content"
                                maxlength="28"
                                style="width: 100%;margin-bottom: 10px;">
                        <el-button slot="append" icon="el-icon-close"
                                   v-on:click="deleteOption(item,subItem)"></el-button>
                      </el-input>
                      <el-input
                          v-if="item.isSumLimit"
                          v-model="subItem.limit"
                          style="width: 17%;margin-bottom: 10px;margin-left: 5%"
                          placeholder="Limit:">
                      </el-input>
                    </div>
                    <el-button style="width: 100%" icon="el-icon-plus" v-on:click="addOption(item)"></el-button>
                  </div>
                </div>
              </div>
              <div v-if="item.type===1" class="queLabel" id="multiChoice">
                <div>
                    <span style="line-height: 30px;">
                        <el-tag size="small" type="success">多选</el-tag>
                        {{ item.qid + 1 }}.{{ item.title }}
                        <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                      <el-switch
                          v-model="item.isSumLimit"
                          active-color="#3292ff"
                          inactive-color="#99a9bf"
                          style="margin-left: 5%"
                          active-text="限制人数"
                          v-if="que.type ==='2'"
                          inactive-text="开放填写"/>
                    </span>
                  <div style="margin-left: 5%;margin-right: 5%;margin-top:15px">

                    <div v-for="subItem in item.option" :key="subItem.oid">
                      <el-input v-if="item.isSumLimit"
                                v-model="subItem.content"
                                maxlength="28"
                                style="width: 78%;margin-bottom: 10px;">
                        <el-button slot="append" icon="el-icon-close"
                                   v-on:click="deleteOption(item,subItem)"></el-button>
                      </el-input>
                      <el-input v-else
                                v-model="subItem.content"
                                maxlength="28"
                                style="width: 100%;margin-bottom: 10px;">
                        <el-button slot="append" icon="el-icon-close"
                                   v-on:click="deleteOption(item,subItem)"></el-button>
                      </el-input>
                      <el-input
                          v-if="item.isSumLimit"
                          v-model="subItem.limit"
                          style="width: 17%;margin-bottom: 10px;margin-left: 5%"
                          placeholder="Limit:">
                      </el-input>
                    </div>
                    <el-button style="width: 100%" icon="el-icon-plus" v-on:click="addOption(item)"></el-button>
                  </div>
                </div>
              </div>
              <div v-if="item.type===2" class="queLabel" id="fillInBlank">
                <div style="margin-top: 10px">
                  <el-tag size="small" type="info">填空</el-tag>
                  {{ item.qid + 1 }}.{{ item.title }}
                  <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                </div>
              </div>
              <div v-if="item.type===3" class="queLabel" id="rating">
                <div style="margin-top: 10px">
                  <el-tag size="small" type="warning">评分</el-tag>
                  {{ item.qid + 1 }}.{{ item.title }}
                  <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                </div>
              </div>
              <div v-if="item.type===4" class="queLabel" id="locating">
                <div style="margin-top: 10px">
                  <el-tag size="small" type="danger">定位</el-tag>
                  {{ item.qid + 1 }}.{{ item.title }}
                  <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                </div>
              </div>
            </el-card>
          </div>
          </tbody>
        </vuedraggable>
      </el-card>
    </div>
  </div>
</template>

<script>
import vuedraggable from 'vuedraggable';

export default {
  components: {
    vuedraggable,
  },
  created() {
    this.que.type = this.$route.query.type
    if (this.$route.query.id !== '0') {
      this.getQn(this.$route.query.id)
    } else if(this.$route.query.type === '2') {
      this.que = {
        qnId: '0',
        showNumbers: true,
        qnType: 2,
        title: "报名问卷",
        QList: [

        ]
      }
      this.que.QList.push(
          {
            qid: 0,
            type: 2,
            title: "姓名:"
          },
          {
            qid: 1,
            type: 2,
            title: "手机号:"
          },
          {
            qid: 2,
            type: 0,
            title: "请选择你的报名项",
            isSumLimit: true,
            option: [{
              oid: 0,
              content: "A",
              num: ''
            }, {
              oid: 1,
              content: "B",
              num: ''
            }, {
              oid: 2,
              content: "C",
              num: ''
            }]
          },
      )
    }
  },
  name: 'NewQue',
  data: function () {
    return {
      heightAndWidth: 'margin:0; height:'+
          (window.innerHeight).toString()+
          'px; width:'+
          (window.innerWidth).toString()+
          'px;'+
          'background-color: #fafafa;',
      que: {
        qnId: '0',
        showNumbers: true,
        qnType: 0,
        title: "测试问卷",
        sum: '',
        isSumLimit:false,
        QList: [{
          qid: 0,
          type: 0,
          title: "这是一道单选题，点击右边的按钮可以更改题目",
          necessary: true,
          option: [{
            oid: 0,
            content: "你好"
          }, {
            oid: 1,
            content: "hello"
          }, {
            oid: 2,
            content: "这是一个选项，点击下方按钮可以增加新的选项"
          }],
        }, {
          qid: 1,
          type: 1,
          title: "这是一道多选题",
          necessary: false,
          option: [{
            oid: 0,
            content: "你好"
          }, {
            oid: 1,
            content: "hello"
          }, {
            oid: 2,
            content: "hi"
          }],
        }, {
          qid: 2,
          type: 2,
          title: "我是一道填空题",
          necessary: false,
        }, {
          qid: 3,
          type: 3,
          title: "我是一道评分题",
          necessary: true,
        }]
      },
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      fullscreenLoading: false,
      editingTitleQuestion: null,
      editingTitle: '',
      addQuestionVisible: false,
      uploadQnVisible:false,
      drag: false,
      titleEditDialog: false,
      queLabelWidth: '20%',
      moreFunctionVisible: false
    }
  },
  methods: {
    getQn(qnid) {
      this.fullscreenLoading = true
      this.$axios({method: "post", url: "/getQn", data: {"QnId": qnid}})
          .then(res => {
            this.que.QList = [];
            this.que.qnType = res.data.que.qnType;
            this.que.showNumbers = res.data.que.showNumbers;
            this.que.qnId = res.data.que.qnId;
            this.que.title = res.data.que.title;
            for (let i = 0; i < res.data.que.QList.length; i++) {
              let temp1 = res.data.que.QList[i];
              if (temp1.type === 0) {
                let optionTemp = [];
                for (let j = 0; j < temp1.option.length; j++) {
                  let temp2 = temp1.option[j];
                  optionTemp.push({
                    oid: j,
                    content: temp2.content,
                    limit: temp2.num,
                  })
                }
                this.que.QList.push({
                  qid: i,
                  type: temp1.type,
                  title: temp1.title,
                  necessary: temp1.necessary,
                  option: optionTemp
                })
              } else if (temp1.type === 1) {
                let optionTemp = [];
                for (let j = 0; j < temp1.option.length; j++) {
                  let temp2 = temp1.option[j];
                  optionTemp.push({
                    oid: j,
                    content: temp2.content,
                    limit: temp2.num,
                  })
                }
                this.que.QList.push({
                  qid: i,
                  type: temp1.type,
                  title: temp1.title,
                  necessary: temp1.necessary,
                  option: optionTemp
                })
              } else if (temp1.type === 2) {
                this.que.QList.push({
                  qid: i,
                  type: temp1.type,
                  title: temp1.title
                })
              } else {
                this.que.QList.push({
                  qid: i,
                  type: temp1.type,
                  title: temp1.title
                })
              }
            }
            for (let i = 0; i < this.que.QList.length; i++) {
              this.que.QList[i].qid = i;
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
          })
    },
    initialTitleEdit(question) {
      this.editingTitle = question.title
      this.editingTitleQuestion = question
      this.titleEditDialog = true
    },
    doneTitleEdit() {
      this.editingTitleQuestion.title = this.editingTitle
      this.titleEditDialog = false
    },
    deleteOption(question, option) {
      let num = question.option.indexOf(option)
      question.option.splice(num, 1)
      for (let i = num; i < question.option.length; i++) {
        question.option[i].oid--
      }
    },
    addOption(question) {
      question.option.push({
        oid: question.option.length,
        content: "",
        limit: ''
      })
    },
    addSingleChoice() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 0,
        isSumLimit: false,
        title: "请输入题干",
        option: []
      })
      this.roll();
    },
    addMultiChoice() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 1,
        isSumLimit: false,
        title: "请输入题干",
        option: []
      })
      this.roll();
    },
    addSpaceFilling() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 2,
        title: "请输入题干",
      })
      this.roll();
    },
    addRating() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 3,
        title: "请输入题干",
      })
      this.roll();
    },
    addLocating() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 4,
        title: "点击获取地理位置",
      })
      this.roll();
    },
    deleteQuestion(question) {
      let num = this.que.QList.indexOf(question)
      this.que.QList.splice(num, 1)
      for (let i = num; i < this.que.QList.length; i++) {
        this.que.QList[i].qid--
      }
    },
    copyQuestion(question) {
      let num = this.que.QList.indexOf(question)
      if (question.type === 0 || question.type === 1) {
        this.que.QList.splice(num + 1, 0, {
          qid: num + 1,
          type: question.type,
          title: question.title + "（副本）",
          option: []
        })
        for (let i = 0; i < question.option.length; i++) {
          this.que.QList[num + 1].option.push({
            oid: question.option[i].oid,
            content: question.option[i].content
          })
        }
      } else if (question.type === 2 || question.type === 3) {
        this.que.QList.splice(num + 1, 0, {
          qid: num + 1,
          type: question.type,
          title: question.title + "（副本）",
        })
      }
      for (let i = num + 2; i < this.que.QList.length; i++) {
        this.que.QList[i].qid++
      }
    },
    uploadQn() {
      this.fullscreenLoading = true;
      console.log(this.que.endTime);
      this.$axios({
        method: "post", url: "/createQn/saveQn", data: {
          "qnId": (this.que.qnId === '0') ? 0 : this.que.qnId,
          "userName": this.$cookies.isKey("username") ? this.$cookies.get("username") : "unLogin",
          "que": this.que
        }
      })
          .then(res => {
            this.$notify({
              title: '成功',
              message: '保存问卷成功',
              type: 'success',
              position: 'bottom-left'
            });
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
            //this.$router.push('/');
          })
    },
    onStart() {
      this.drag = true;
    },
    onEnd() {
      for (let i = 0; i < this.que.QList.length; i++) {
        this.que.QList[i].qid = i;
      }
      this.drag = false;
    },
    roll() {
      let temp = document.getElementById("Qn");
      temp.scrollTop = temp.scrollHeight + 1000;
    }
  }
}
</script>

<style>
.queLabel {
  margin-left: 10%;
  margin-bottom: 8px;
  margin-right: 10%;
  text-align: start;
}

.move {

}

.drag {
  float: left;
  margin-left: 12px;
  cursor: move;
}

.ghost {
  opacity: 1;
}
.hoverB {
  position: fixed;
  left:15%;
  margin-left:0;
}

@keyframes scale{
  0%{transform:scale(1)}
  100%{transform:scale(1.2)}
}

.hoverB:hover{
  animation-name:scale;
  animation-duration:0.3s;
  animation-iteration-count:1;
  animation-fill-mode: forwards;
}
</style>