<template>
  <div>
    <el-container>
      <el-dialog :visible="titleEditDialog" :show-close="false">
        <div slot="title">编辑题目</div>
        <el-input type="textarea" v-model="editingTitle" style="margin-bottom: 30px;width: 80%"/>
        <el-button v-on:click="doneTitleEdit" style="width: 60%" type="success" icon="el-icon-check"></el-button>
      </el-dialog>
      <el-container style="width: 30%; margin-top: 5%">
        <el-aside width="200px" style="background-color: rgb(238, 241, 246);margin:auto">
        <el-menu :default-openeds="['1','2', '3']">
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-s-tools"></i></template>
          <el-menu-item index="1-1">返回首页</el-menu-item>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-edit"></i>添加题目</template>
          <el-menu-item-group>
            <el-menu-item index="2-1" v-on:click="addSingleChoice"><i class="el-icon-circle-plus"></i>单选题</el-menu-item>
            <el-menu-item index="2-2" v-on:click="addMultiChoice"><i class="el-icon-circle-plus"></i>多选题</el-menu-item>
          </el-menu-item-group>
          <el-menu-item index="2-3" v-on:click="addSpaceFilling"><i class="el-icon-circle-plus"></i>填空题</el-menu-item>
          <el-menu-item index="2-4" v-on:click="addRating"><i class="el-icon-circle-plus"></i>评分题</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-setting"></i>问卷操作</template>
          <el-menu-item index="3-1" v-on:click="beforeUpload(true)"><i class="el-icon-upload"></i>保存并发布</el-menu-item>
          <el-menu-item index="3-2" v-on:click="beforeUpload(false)"><i class="el-icon-turn-off"></i>保存暂不发布</el-menu-item>
        </el-submenu>
      </el-menu>
      </el-aside>
      </el-container>
      <el-container style="width: 70%;">
        <div id="Qn" style="position:fixed;overflow:scroll;height: 100%;">
      <el-card style="width:800px;" v-loading.fullscreen.lock="fullscreenLoading">
        <div slot="header" class="clearfix">
          <el-input style="font-size: larger" v-model="que.title"></el-input>
        </div>
        <vuedraggable v-model="que.QList" chosenClass="ghost" handle=".drag" :scroll-sensitivity="150" force-fallback="true" animation="400" @start="onStart" @end="onEnd" style="display:table;width:100%">
          <tbody is="transition-group">
            <div v-for="item in que.QList"
                 :key="item.qid" class="move">
              <el-card style="margin: 15px;cursor: move"
                       shadow="hover">
                <el-button type="text" icon="el-icon-rank" class="drag"></el-button>
                <div style="float: right;margin-right: 12px">
                  <el-button type="text" icon="el-icon-document-copy" v-on:click="copyQuestion(item)">复制</el-button>
                  <el-button type="text" icon="el-icon-delete" v-on:click="deleteQuestion(item)">删除</el-button>
                  <el-checkbox v-if="item.type===0||item.type===1" v-model="item.necessary">必选</el-checkbox>
                  <el-checkbox v-if="item.type===2||item.type===3" v-model="item.necessary">必填</el-checkbox>
                </div>
                <div v-if="item.type===0" class="queLabel" id="singleChoice">
                  <div>
                    <span style="line-height: 30px;">
                    <el-tag size="small">单选</el-tag>
                    {{item.qid+1}}.{{item.title}}
                    <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                      <el-switch
                        v-model="item.isSumLimit"
                        active-color="#3292ff"
                        inactive-color="#99a9bf"
                        style="margin-left: 5%"
                        active-text="人数限制"
                        v-if="que.type ==='2' "
                        inactive-text="无" />
                    </span>

                    <div style="margin-left: 5%;margin-right: 5%;margin-top:15px">
                      <div v-for="subItem in item.option" :key="subItem.oid" >
                        <el-input v-if="item.isSumLimit"
                                  v-model="subItem.content"
                                  maxlength="28"
                                  style="width: 78%;margin-bottom: 10px;">
                          <el-button slot="append" icon="el-icon-close" v-on:click="deleteOption(item,subItem)"></el-button>
                        </el-input>
                        <el-input v-else
                                  v-model="subItem.content"
                                  maxlength="28"
                                  style="width: 100%;margin-bottom: 10px;">
                          <el-button slot="append" icon="el-icon-close" v-on:click="deleteOption(item,subItem)"></el-button>
                        </el-input>
                        <el-input
                            v-if="item.isSumLimit"
                            v-model="subItem.num"
                            style="width: 17%;margin-bottom: 10px;margin-left: 5%"
                            placeholder="limit:">
                        </el-input>
                      </div>
                      <el-button style="width: 100%" icon="el-icon-plus" v-on:click="addOption(item)"></el-button>
                    </div>
                  </div>
                </div>
                <div v-if="item.type===1" class="queLabel"  id="multiChoice">
                  <div>
                    <span style="line-height: 30px;">
                        <el-tag size="small" type="success">多选</el-tag>
                        {{item.qid+1}}.{{item.title}}
                        <el-link icon="el-icon-edit" :underline="false"  v-on:click="initialTitleEdit(item)"></el-link>
                    </span>
                    <div style="margin-left: 5%;margin-right: 5%;margin-top:15px">
                      <el-input v-for="subItem in item.option"
                                :key="subItem.oid"
                                v-model="subItem.content"
                                maxlength="28"
                                style="width: 100%;margin-bottom: 10px">
                        <el-button slot="append" icon="el-icon-close" v-on:click="deleteOption(item,subItem)"></el-button>
                      </el-input>
                      <el-button style="width: 100%" icon="el-icon-plus" v-on:click="addOption(item)"></el-button>
                    </div>
                  </div>
                </div>
                <div v-if="item.type===2" class="queLabel"  id="fillInBlank">
                  <div style="margin-top: 10px">
                    <el-tag size="small" type="info">填空</el-tag>
                    {{item.qid+1}}.{{item.title}}
                    <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                  </div>
                </div>
                <div v-if="item.type===3" class="queLabel"  id="rating">
                  <div style="margin-top: 10px">
                    <el-tag size="small" type="warning">评分</el-tag>
                    {{item.qid+1}}.{{item.title}}
                    <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                  </div>
                </div>
              </el-card>
            </div>
          </tbody>
        </vuedraggable>
      </el-card>
    </div>
      </el-container>
      <el-dialog title="创建问卷" :visible.sync="dialogvis" width="45%" :before-close="handleClose" center style="margin-top: 4%">
        <el-form :model="que" style="" :label-position=" 'left' " >
          <el-form-item required label="问卷标题" :label-width="queLabelWidth" style="text-align: left">
            <el-input v-model="que.title" autocomplete="off" placeholder="请输入标题" maxlength="15" show-word-limit style="width: 65%"></el-input>
          </el-form-item>
          <el-form-item required label="问卷类型" :label-width="queLabelWidth" style="text-align: left">
            <el-radio-group v-model="que.Qntype" style="width: 100%">
              <el-radio :label=0>普通问卷</el-radio>
              <el-radio :label=1>投票问卷</el-radio>
              <el-radio :label=2>报名问卷</el-radio>
              <el-radio :label=3>考试问卷</el-radio>
              <el-radio :label=4>疫情打卡问卷</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item v-if="share" required label="问卷截至时间" :label-width="queLabelWidth" style="text-align: left">
            <el-date-picker
                v-model="que.endTime"
                type="datetime"
                placeholder="选择日期时间">
            </el-date-picker>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="handleClose(done)">取 消</el-button>
          <el-button type="primary" @click="handleConfirm(done)">确 定</el-button>
        </div>
      </el-dialog>
    </el-container>
  </div>
</template>

<script>
import vuedraggable from 'vuedraggable';
export default {
  components: {
    vuedraggable,
  },
  created() {
    this.que.title= this.$route.query.title
    this.que.type= this.$route.query.type
    if(this.que.type==='2'){
      this.que.QList=[]
      this.que.QList.push(
          {
            qid:0,
            type:2,
            title: "姓名:" },
          {
            qid:1,
            type:2,
            title: "手机号:" },
          {
            qid:2,
            type:0,
            title: "请选择你的报名项",
            isSumLimit:true,
            sum: 0,
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
            }] },
      )
    }
    if(this.$route.query.id!=='0') {
      this.getQn(this.$route.query.id)
    }
  },
  name: 'NewQue',
  data: function(){
    return {
      que: {
        qnid: '0',
        Qntype:0,
        endTime:'',
        title: "holo",
        type: 0,
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
      titleEditDialog: false,
      editingTitleQuestion:null,
      editingTitle:'',
      addQuestionVisible: false,
      drag: false,
      dialogvis:false,
      queLabelWidth: '20%',
      share:false
    }
  },
  methods: {
    getQn(qnid) {
      this.fullscreenLoading=true
      this.$axios({method:"post", url:"/getQn", data:{"QnId": qnid}})
          .then(res => {
            this.que.QList=[];
            this.que.Qntype=res.data.que.Qntype;
            this.que.endTime=res.data.que.endTime;
            this.que.qnid = res.data.que.qnid;
            this.que.title = res.data.que.title;
            for(let i=0;i<res.data.que.QList.length;i++){
              let temp1=res.data.que.QList[i];
              if(temp1.type === 0){
                let optionTemp=[];
                for(let j=0;j<temp1.option.length;j++){
                  let temp2=temp1.option[j];
                  optionTemp.push({
                    oid:j,
                    content:temp2.content
                  })
                }
                this.que.QList.push({
                  qid:i,
                  type:temp1.type,
                  title: temp1.title,
                  necessary: temp1.necessary,
                  option:optionTemp
                })
              }
              else if(temp1.type === 1){
                let optionTemp=[];
                for(let j=0;j<temp1.option.length;j++){
                  let temp2=temp1.option[j];
                  optionTemp.push({
                    oid:j,
                    content:temp2.content
                  })
                }
                this.que.QList.push({
                  qid:i,
                  type:temp1.type,
                  title: temp1.title,
                  necessary: temp1.necessary,
                  option:optionTemp
                })
              }
              else if(temp1.type === 2){
                this.que.QList.push({
                  qid:i,
                  type:temp1.type,
                  title: temp1.title
                })
              }
              else{
                this.que.QList.push({
                  qid:i,
                  type:temp1.type,
                  title: temp1.title
                })
              }
            }
            for(let i = 0; i < this.que.QList.length; i++) {
        this.que.QList[i].qid=i;
      }
            this.fullscreenLoading=false
          })
          .catch(() => {
            this.$notify({
              title: '失败',
              message: '连接失败',
              type: 'error',
              position: 'bottom-left'
            });
            this.fullscreenLoading=false
          })
    },
    initialTitleEdit(question){
      this.editingTitle=question.title
      this.editingTitleQuestion=question
      this.titleEditDialog=true
    },
    doneTitleEdit(){
      this.editingTitleQuestion.title=this.editingTitle
      this.titleEditDialog=false
    },
    deleteOption(question,option){
      let num = question.option.indexOf(option)
      question.option.splice(num,1)
      for(let i = num; i < question.option.length; i++) {
        question.option[i].oid--
      }
    },
    addOption(question){
      question.option.push({
        oid: question.option.length,
        content: ""
      })
    },
    addSingleChoice() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 0,
        title: "请输入题干",
        option: []
      })
      this.roll("singleChoice");
    },
    addMultiChoice() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 1,
        title: "请输入题干",
        option: []
      })
      this.roll("multiChoice");
    },
    addSpaceFilling() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 2,
        title: "请输入题干",
      })
      this.roll("fillInBlank");
    },
    addRating() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 3,
        title: "请输入题干",
      })
      this.roll("rating");
    },
    deleteQuestion(question) {
      let num = this.que.QList.indexOf(question)
      this.que.QList.splice(num,1)
      for(let i = num; i < this.que.QList.length; i++) {
        this.que.QList[i].qid--
      }
    },
    copyQuestion(question) {
      let num = this.que.QList.indexOf(question)
      if(question.type === 0 || question.type === 1) {
        this.que.QList.splice(num+1,0,{
          qid: num+1,
          type: question.type,
          title: question.title+"（副本）",
          option: []
        })
        for(let i = 0; i < question.option.length; i++) {
          this.que.QList[num+1].option.push({
            oid:question.option[i].oid,
            content:question.option[i].content
          })
        }
      } else if(question.type === 2 || question.type === 3) {
        this.que.QList.splice(num+1,0,{
          qid: num+1,
          type: question.type,
          title: question.title+"（副本）",
        })
      }
      for(let i = num+2; i < this.que.QList.length; i++) {
        this.que.QList[i].qid++
      }
    },
    beforeUpload(flag){
      this.share=flag;
      this.dialogvis = true;
    },
    uploadQn(flag){
      this.fullscreenLoading = true;
      console.log(this.que.endTime);
      this.$axios({method:"post",url:"/createQn/saveQn", data:{
          "qnid":(this.que.qnid==='0')?0:this.que.qnid,
          "userName": this.$cookies.isKey("username")?this.$cookies.get("username"):"unLogin",
          "que":{
            "Qntype":this.que.Qntype,
            "title":this.que.title,
            "endTime":flag?this.que.endTime:null,
            "state":flag,
            "QList":this.que.QList
          }}})
          .then(res => {
            this.$notify({
              title: '成功',
              message: flag?'创建问卷成功':'保存问卷成功',
              type: 'success',
              position: 'bottom-left'
            });
            this.fullscreenLoading = false
            if(flag) {
              this.$router.push("/home")
            } else {
              this.getQn(res.data.qnid)
            }
          })
          .catch(() => {
            this.$notify({
              title: '失败',
              message: '连接失败',
              type: 'error',
              position: 'bottom-left'
            });
            this.fullscreenLoading=false
            //this.$router.push('/');
          })
    },
    onStart() {
      this.drag = true;
    },
    onEnd() {
      for(let i = 0; i < this.que.QList.length; i++) {
        this.que.QList[i].qid=i;
      }
      this.drag = false;
    },
    roll(str){
      let temp=document.getElementById("Qn");
      temp.scrollTop= temp.scrollHeight+1000;
    },
    handleClose() {
      this.$confirm('确认取消创建问卷？')
          .then(_ => {
            this.dialogvis=false
          })
          .catch(_ => {});
    },
    handleConfirm() {
      if (this.que.title === '') {
        this.$notify({
          title: '创建失败',
          message: '标题不能为空',
          position: 'bottom-left',
          type: "error"
        });
      } else {
        this.uploadQn(this.share)
        if(this.share === true){
          this.$router.push('/');
        }
        this.dialogvis=false
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
  float:left;
  margin-left: 12px;
  cursor: move;
}

.ghost {
  opacity: 1;
}
</style>