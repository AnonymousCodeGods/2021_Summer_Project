<template>
  <div :style="heightAndWidth">

    <el-button circle plain type="primary" class="hoverB" style="top:50px" icon="el-icon-back" v-on:click="$router.push('/home')"></el-button>
    <el-popover
        placement="right"
        width="390"
        v-model="addQuestionVisible">
      <div style="text-align: right; margin: 0">
        <el-button plain type="primary" size="mini"  @click="addSingleChoice">单选</el-button>
        <el-button plain type="success" size="mini" @click="addMultiChoice">多选</el-button>
        <el-button plain type="info" size="mini"  @click="addSpaceFilling">填空</el-button>
        <el-button plain type="warning" size="mini" @click="addRating">评分</el-button>
        <el-button plain type="danger" size="mini" @click="addLocating">定位</el-button>
        <el-button :disabled="this.que.qnType==='2'||this.que.qnType==='3'" plain type="danger" size="mini" @click="addBranch">分支</el-button>
      </div>
      <el-button circle plain type="success" class="hoverB" style="top:100px" icon="el-icon-plus" slot="reference"></el-button>
    </el-popover>
    <el-popover
        placement="right"
        width="200"
        v-model="moreFunctionVisible">
      <div style="text-align: center; margin: 0">
        <el-switch
            active-text="显示题号"
            inactive-text="隐藏题号"
            v-model="que.showNumbers">
        </el-switch>
        <el-switch
            v-if="que.qnType==='2'"
            style="margin: 10px"
            active-text="限制人数"
            inactive-text="自由填写"
            v-model="que.isSumLimit">
        </el-switch>
        <el-input style="width: 80%" v-if="que.qnType==='2'" v-model="que.limit" :disabled="!que.isSumLimit"/>
      </div>
      <el-button circle plain type="info" class="hoverB" style="top:150px" icon="el-icon-s-tools" slot="reference"></el-button>
    </el-popover>
    <el-button circle plain type="warning" class="hoverB" style="top:200px;margin-left: 0" icon="el-icon-check" @click="uploadQn"></el-button>


    <el-dialog :visible="titleEditDialog" :show-close="false">
      <div slot="title">编辑题目</div>
      <el-input v-model="editingTitle" style="margin-bottom: 30px;width: 80%"/>
      <el-button v-on:click="doneTitleEdit" style="width: 60%" type="success" icon="el-icon-check"></el-button>
    </el-dialog>


    <el-dialog :visible="singleAnswerEditDialog" :show-close="false">
      <div slot="title">编辑答案</div>
      <el-select
          v-model="editingAnswer"
          style="margin-right: 20px;width: 80%"
          placeholder="请选择">
        <el-option
            v-for="item in editingAnswerOption"
            :key="item.oid"
            :label="'选项'+(item.oid+1)"
            :value="item.oid">
        </el-option>
      </el-select>
      <el-button circle plain v-on:click="doneAnswerEdit" type="success" icon="el-icon-check"></el-button>
    </el-dialog>

    <el-dialog :visible="multiAnswerEditDialog" :show-close="false">
      <div slot="title">编辑答案</div>
      <el-select
          multiple
          collapse-tags
          v-model="editingAnswers"
          style="margin-right: 20px;width: 80%"
          placeholder="请选择">
        <el-option
            v-for="item in editingAnswerOption"
            :key="item.oid"
            :label="'选项'+(item.oid+1)"
            :value="item.oid">
        </el-option>
      </el-select>
      <el-button circle plain v-on:click="doneAnswerEdit" type="success" icon="el-icon-check"></el-button>
    </el-dialog>


    <div id="Qn" style="height: 100%;width: 100%;overflow-y:scroll;margin: auto">
      <el-card style="margin: 20px 20% ;" v-loading.fullscreen.lock="fullscreenLoading">
        <div slot="header" class="clearfix">
          <el-input style="font-size: larger" v-model="que.title"></el-input>
        </div>
        <vuedraggable group='001'
                      v-model="que.QList"
                      chosenClass="ghost"
                      handle=".drag"
                      :scroll-sensitivity="150"
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


              <div style="float: right;margin-right: 0;width: 180px">
                <el-button :disabled="item.type===5"
                           type="text"
                           icon="el-icon-document-copy"
                           v-on:click="copyQuestion(item)">复制
                </el-button>
                <el-button type="text"
                           icon="el-icon-delete"
                           style="color: #F56C6C;"
                           v-on:click="deleteQuestion(item)">删除
                </el-button>
                <el-popover placement="bottom" width="200">
                  <el-button circle
                             plain
                             icon="el-icon-more"
                             type=""
                             style="margin-left: 18px"
                             slot="reference">
                  </el-button>
                  <div style="width:100%;margin: 5px;">
                    <el-checkbox v-model="item.necessary">必填</el-checkbox>
                  </div>
                  <div style="width:100%;margin: 5px;" v-if="que.qnType ==='2'&&(item.type===0||item.type===1)">
                    <el-checkbox v-model="item.isSumLimit">限制人数</el-checkbox>
                  </div>
                  <div style="width:100%;margin: 5px;" v-if="que.qnType ==='3'&&(item.type===0||item.type===1)">
                    <el-checkbox v-model="item.hasAnswer">正确答案</el-checkbox>
                    <el-link style="margin-left: 10px" icon="el-icon-edit" :underline="false" :disabled="!item.hasAnswer" v-on:click="initialAnswerEdit(item)"></el-link>
                  </div>
                </el-popover>
              </div>


              <div v-if="item.type===0" class="queLabel" id="singleChoice">
                <div>
                    <span style="line-height: 30px;">
                      <el-tag size="small">单选</el-tag>
                      {{ item.qid + 1 }}.{{ item.title }}
                      <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
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
                          style="width: 19%;margin-bottom: 10px;margin-left: 3%"
                          placeholder="" suffix-icon="el-icon-s-custom">
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
                          style="width: 19%;margin-bottom: 10px;margin-left: 3%"
                          placeholder=""  suffix-icon="el-icon-s-custom">
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

              <div v-if="item.type===5" class="queLabel" id="branch">
                <div style="margin-top: 10px">
                  <el-tag size="small" type="danger">分支</el-tag>
                  {{ item.qid + 1 }}.{{ item.title }}
                  <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                  <div v-for="subItem in item.option" :key="subItem.oid" style="margin: 20px 0 0 0 ">
                    <div style="width: 100%;border-radius: 0;padding: 0">
                      <el-tag style="margin-left: 5px;" size="small" type="info">分支{{subItem.oid+1}}</el-tag>
                      <el-input v-model="subItem.content"
                                maxlength="28"
                                style="margin-left:10px;width: 90%">
                        <el-button slot="append" icon="el-icon-close"
                                   v-on:click="deleteOption(item,subItem)"></el-button>
                      </el-input>
                      <vuedraggable v-model="subItem.question"
                                    group='001'
                                    style="margin:0;min-height: 100px"
                                    animation="300"
                                    @start="onStart"
                                    @end="onEnd">
                        <span slot="header" style="max-height: 100px">

                        </span>
                        <div v-for="subQuestion in subItem.question" :key="subQuestion.qid" class="unDrag">
                          <el-card style="margin: 10px"  class="unDrag" shadow="hover">
                            <el-tag v-if="subQuestion.type===0" size="small" type="primary">单选</el-tag>
                            <el-tag v-if="subQuestion.type===1" size="small" type="success">多选</el-tag>
                            <el-tag v-if="subQuestion.type===2" size="small" type="info">填空</el-tag>
                            <el-tag v-if="subQuestion.type===3" size="small" type="warning">评分</el-tag>
                            <el-tag v-if="subQuestion.type===4" size="small" type="danger">定位</el-tag>
                            <el-tag v-if="subQuestion.type===5" size="small" type="danger">分支</el-tag>
                            <span style="margin-left: 20px">{{subQuestion.qid+1}}.{{subQuestion.title}}</span>
                          </el-card>
                        </div>
                      </vuedraggable>
                    </div>
                  </div>
                  <el-button style="width: 100%;margin-top:20px" icon="el-icon-plus" v-on:click="addABranch(item)"></el-button>
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
    this.que.qnType = this.$route.query.type;
    if (this.$route.query.id !== '0') {
      this.getQn(this.$route.query.id)
    } else if(this.$route.query.type === '1') {
      this.que = {
        qnId: '0',
        showNumbers: true,
        isSumLimit: false,
        limit: 0,
        qnType: '1',
        title: "投票问卷",
        QList: [
          {
            qid: 0,
            type: 0,
            title: "请编辑投票题目",
            hasAnswer: false,
            necessary: true,
            belongTo: {qid:-1,option:-1},
            isSumLimit: false,
            answer:[],
            option:[
              {
                oid:0,
                content:'请输入选项内容',
                limit:0
              }
            ]
          }
        ]
      }
    } else if(this.$route.query.type === '2') {
      this.que = {
        qnId: '0',
        showNumbers: true,
        isSumLimit: false,
        limit: 0,
        qnType: '2',
        title: "报名问卷",
        QList: [
          {
            qid: 0,
            type: 2,
            title: "请输入姓名",
            necessary: true,
            belongTo: {qid:-1,option:-1},
          }, {
            qid: 1,
            type: 2,
            title: "请输入手机号",
            necessary:  true,
            belongTo: {qid:-1,option:-1},
          }, {
            qid: 2,
            type: 0,
            title: "请编辑报名题目",
            hasAnswer: false,
            necessary: true,
            belongTo: {qid:-1,option:-1},
            isSumLimit:true,
            answer:[],
            option:[
              {
                oid:0,
                content:'请输入选项内容',
                limit:10
              }
            ]
          }
        ]
      }
    } else if(this.$route.query.type === '3') {
      this.que = {
        qnId: '0',
        showNumbers: true,
        isSumLimit:false,
        limit: 0,
        qnType: '3',
        title: "考试问卷",
        QList: [
          {
            qid: 0,
            type: 2,
            title: "请输入姓名",
            necessary: true,
            belongTo: {qid:-1,option:-1},
          }, {
            qid: 1,
            type: 2,
            title: "请输入学号",
            necessary: true,
            belongTo: {qid:-1,option:-1},
          }
        ]
      }
    } else if(this.$route.query.type === '4') {
      this.que = {
        qnId: '0',
        showNumbers: true,
        isSumLimit:false,
        limit: 0,
        qnType: '4',
        title: "疫情上报问卷",
        QList: [
          {
            qid: 0,
            type: 2,
            title: "请输入姓名",
            necessary: true,
            belongTo: {qid:-1,option:-1},
          }, {
            qid: 1,
            type: 2,
            title: "请输入学号",
            necessary: true,
            belongTo: {qid:-1,option:-1},
          }, {
            qid: 2,
            type: 0,
            title: "请选择体温",
            necessary: true,
            belongTo: {qid:-1,option:-1},
            isSumLimit: false,
            hasAnswer: false,
            option:[
              {
                oid:0,
                content: "36°以下"
              },
              {
                oid:1,
                content: "36°~37.3°"
              },
              {
                oid:2,
                content: "37.3°以上"
              }
            ]
          }, {
            qid: 3,
            type: 0,
            title: "是否去过高风险地区",
            necessary: true,
            belongTo: {qid:-1,option:-1},
            isSumLimit: false,
            hasAnswer: false,
            option:[
              {
                oid:0,
                content: "否"
              },
              {
                oid:1,
                content: "是"
              }
            ]
          },{
            qid: 4,
            type: 4,
            title: "请点击定位",
            necessary: true,
            belongTo: {qid:-1,option:-1},
          }
        ]
      }
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
        isSumLimit:false,
        limit: 0,
        qnType: '0',
        title: "普通问卷",
        hasBranch:false,
        QList: [{
          qid: 0,
          type: 0,
          title: "这是一道单选题，点击右边的按钮可以更改题目",
          hasAnswer: false,
          answer:0,
          necessary: true,
          belongTo: {qid:-1,option:-1},
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
          hasAnswer: false,
          answer: [],
          necessary: false,
          belongTo: {qid:-1,option:-1},
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
          belongTo: {qid:-1,option:-1},
        }, {
          qid: 3,
          type: 3,
          title: "我是一道评分题",
          necessary: true,
          belongTo: {qid:-1,option:-1},
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
      moreFunctionVisible: false,
      singleAnswerEditDialog:false,
      multiAnswerEditDialog:false,
      editingAnswerOption:0,
      editingAnswers:[],
      editingAnswer:-1,
      editingAnswerQuestion:null,
    }
  },
  methods: {
    getQn(qnId) {
      this.fullscreenLoading = true
      this.$axios({method: "post", url: "/getQn", data: {"QnId": qnId}})
          .then(res => {
            this.que.QList = [];
            this.que.qnType = res.data.que.qnType+'';
            this.que.showNumbers = res.data.que.showNumbers;
            this.que.qnId = res.data.que.qnid;
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
                    limit: 0,
                  })
                }
                this.que.QList.push({
                  qid: i,
                  type: temp1.type,
                  title: temp1.title,
                  necessary: temp1.necessary,
                  belongTo: {qid:-1,option:-1},
                  hasAnswer: false,
                  answer: 0,
                  option: optionTemp
                })
              } else if (temp1.type === 1) {
                let optionTemp = [];
                for (let j = 0; j < temp1.option.length; j++) {
                  let temp2 = temp1.option[j];
                  optionTemp.push({
                    oid: j,
                    content: temp2.content,
                    limit: 0,
                  })
                }
                this.que.QList.push({
                  qid: i,
                  type: temp1.type,
                  title: temp1.title,
                  necessary: temp1.necessary,
                  belongTo: {qid:-1,option:-1},
                  hasAnswer: false,
                  answer: [],
                  option: optionTemp
                })
              } else if (temp1.type === 2) {
                this.que.QList.push({
                  qid: i,
                  type: temp1.type,
                  belongTo: {qid:-1,option:-1},
                  title: temp1.title,
                  necessary: temp1.necessary,
                })
              } else {
                this.que.QList.push({
                  qid: i,
                  type: temp1.type,
                  belongTo: {qid:-1,option:-1},
                  title: temp1.title,
                  necessary: temp1.necessary,
                })
              }
            }
            this.reorder(this.que.QList,0)
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
    initialAnswerEdit(question) {
      this.editingAnswerQuestion = question
      this.editingAnswerOption = question.option
      if(question.type === 0){
        this.editingAnswer = question.answer
        this.singleAnswerEditDialog = true
      }
      else if(question.type === 1){
        this.editingAnswers = question.answer
        this.multiAnswerEditDialog = true
      }
    },
    doneAnswerEdit() {
      if(this.editingAnswerQuestion.type === 0){
        this.editingAnswerQuestion.answer = this.editingAnswer
        this.singleAnswerEditDialog = false
      }
      else if(this.editingAnswerQuestion.type === 1){
        this.editingAnswerQuestion.answer = this.editingAnswers
        this.multiAnswerEditDialog = false
      }
      this.singleAnswerEditDialog = false
      this.multiAnswerEditDialog = false
      this.editingAnswer = 0
      this.editingAnswers = []
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
        limit: 0
      })
    },
    addABranch(question) {
      question.option.push({
        oid: question.option.length,
        content: "",
        question:[]
      })
    },
    addSingleChoice() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 0,
        necessary: false,
        belongTo: {qid:-1,option:-1},
        isSumLimit: false,
        hasAnswer: false,
        answer: 0,
        title: "请输入题干",
        option: []
      })
      this.reorder(this.que.QList,0)
      this.roll();
    },
    addMultiChoice() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 1,
        necessary: false,
        belongTo: {qid:-1,option:-1},
        isSumLimit: false,
        hasAnswer: false,
        answer: [],
        title: "请输入题干",
        option: []
      })
      this.reorder(this.que.QList,0)
      this.roll();
    },
    addSpaceFilling() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 2,
        necessary: false,
        belongTo: {qid:-1,option:-1},
        title: "请输入题干",
      })
      this.reorder(this.que.QList,0)
      this.roll();
    },
    addRating() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 3,
        necessary: false,
        belongTo: {qid:-1,option:-1},
        title: "请输入题干",
      })
      this.reorder(this.que.QList,0)
      this.roll();
    },
    addLocating() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 4,
        necessary: false,
        belongTo: {qid:-1,option:-1},
        title: "点击获取地理位置",
      })
      this.reorder(this.que.QList,0)
      this.roll();
    },
    addBranch() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 5,
        necessary: false,
        title: "分支名称",
        belongTo: {qid:-1,option:-1},
        option:[]
      })
      this.reorder(this.que.QList,0)
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
          isSumLimit: question.isSumLimit,
          hasAnswer: question.hasAnswer,
          answer: question.type===0?question.answer:[],
          necessary: question.necessary,
          belongTo: {qid:-1,option:-1},
          option: []
        })
        for (let i = 0; i < question.option.length; i++) {
          this.que.QList[num + 1].option.push({
            oid: question.option[i].oid,
            content: question.option[i].content,
            limit: question.option[i].limit
          })
        }
        if (question.type===1) {
          for (let i = 0; i < question.option.length; i++) {
            this.que.QList[num + 1].answer.push(question.answer[i])
          }
        }
      } else if (question.type === 2 || question.type === 3 || question.type === 4) {
        this.que.QList.splice(num + 1, 0, {
          qid: num + 1,
          type: question.type,
          title: question.title + "（副本）",
          isSumLimit: question.isSumLimit,
          belongTo: {qid:-1,option:-1},
          necessary: question.necessary
        })
      }
      for (let i = num + 2; i < this.que.QList.length; i++) {
        this.que.QList[i].qid++
      }
    },
    uploadQn() {
      for(let i=0;i<this.que.QList.length;i++){
        console.log(this.que.QList[i].type)
        if(this.que.QList[i].type === 5){
          this.que.hasBranch = true;
          break;
        }
      }
      this.fullscreenLoading = true;
      this.connectQuestion(this.que.QList)
      this.$axios({
        method: "post", url: "/createQn/saveQn", data: {
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
            this.$router.push('/home');
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
    onStart() {
      this.drag = true;
    },
    onEnd() {
      this.reorder(this.que.QList,0)
      this.drag = false;
    },
    roll() {
      let temp = document.getElementById("Qn");
      temp.scrollTop = temp.scrollHeight + 1000;
    },
    reorder(QList,num) {
      for (let i = 0; i < QList.length; i++) {
        QList[i].qid = num;
        num++;
        if(QList[i].type === 5) {
          for(let j = 0; j < QList[i].option.length; j++) {
            num = this.reorder(QList[i].option[j].question,num)
          }
        }
      }
      return num
    },
    connectQuestion(QList){
      for (let i = 0; i < QList.length; i++) {
        if(QList[i].type === 5) {
          let optionTemp = []
          for(let j = QList[i].option.length-1; j >= 0 ; j--) {
            let ql = QList[i].option[j].question
            this.connectQuestion(ql)
            for(let k = 0; k< ql.length;k++) {
              QList.splice(i+k+1,0,ql[k])
              QList[i+k+1].belongTo={
                qid:i,
                option:j
              }
            }
            optionTemp.push({
              oid: j,
              content: QList[i].option[j].content,
              limit: 0
            })
          }
          optionTemp.reverse()
          QList[i]={
            qid: QList[i].qid,
            type: 0,
            belongTo: {qid:-1,option:-1},
            necessary: QList[i].necessary,
            title: QList[i].title,
            isSumLimit: false,
            hasAnswer: false,
            answer: 0,
            option: optionTemp
          }
        }
      }
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

@keyframes inputScale{
  0%{width: 100%}
  100%{width: 78%}
}
.inputOptionPlay{
  animation-name: inputScale;
  animation-duration: 0.3s;
  animation-iteration-count: 1;
  animation-fill-mode: forwards;
  animation-play-state: paused;
}

.unDrag {

}
</style>