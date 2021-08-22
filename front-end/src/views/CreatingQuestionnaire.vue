<template>
  <div>
    <el-dialog :visible="titleEditDialog" :show-close="false">
      <div slot="title">编辑题目</div>
      <el-input type="textarea" v-model="editingTitle" style="margin-bottom: 30px;width: 80%"/>
      <el-button v-on:click="doneTitleEdit" style="width: 60%" type="success" icon="el-icon-check"></el-button>
    </el-dialog>
    <el-card style="width: 800px; margin: auto"  v-loading.fullscreen.lock="fullscreenLoading">
      <div slot="header" class="clearfix">
        <span style="font-size: larger">{{que.title}}</span>
      </div>
      <vuedraggable v-model="que.QList" chosen-class="choose" force-fallback="true" animation="400" @start="onStart" @end="onEnd">
        <tbody is="transition-group">
          <div v-for="item in que.QList"
               :key="item.qid" class="move">
            <el-card style="margin: 15px;cursor: move"
                     shadow="hover">
              <div style="float: right;margin-right: 12px">
                <el-button type="text" icon="el-icon-document-copy" v-on:click="copyQuestion(item)"></el-button>
                <el-button type="text" icon="el-icon-delete" v-on:click="deleteQuestion(item)"></el-button>
              </div>
              <div v-if="item.type===0" class="queLabel">
                <div>
                  <span style="line-height: 30px;">
                  <el-tag size="small">单选</el-tag>
                  {{item.qid+1}}.{{item.title}}
                  <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
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
              <div v-if="item.type===1" class="queLabel">
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
              <div v-if="item.type===2" class="queLabel">
                <div style="margin-top: 10px">
                  <el-tag size="small" type="info">填空</el-tag>
                  {{item.qid+1}}.{{item.title}}
                  <el-link icon="el-icon-edit" :underline="false" v-on:click="initialTitleEdit(item)"></el-link>
                </div>
              </div>
              <div v-if="item.type===3" class="queLabel">
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
      <div style="margin-top: 30px">
        <el-button plain type="primary" style="width: 15%" icon="el-icon-download" v-on:click="uploadQn(false)"></el-button>
        <el-popover
            style="margin: 20px"
            placement="top"
            width="150"
            v-model="addQuestionVisible">
          <div >
            <el-button plain type="primary" v-on:click="addSingleChoice">单选</el-button>
            <el-button plain type="success" style="margin-left: 10px" v-on:click="addMultiChoice">多选</el-button>
          </div>
          <div style="margin-top: 10px">
            <el-button plain type="info" v-on:click="addSpaceFilling">填空</el-button>
            <el-button plain type="warning" style="margin-left: 10px" v-on:click="addRating">评分</el-button>
          </div>
          <el-button plain type="success" style="width: 15%" icon="el-icon-plus" v-on:click="addQuestionDialog=true" slot="reference"></el-button>
        </el-popover>
        <el-button plain type="danger" style="width: 15%" icon="el-icon-upload2" v-on:click="uploadQn(true)"></el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
import vuedraggable from 'vuedraggable';
export default {
  components: {
    vuedraggable,
  },
  name: 'NewQue',
  data: function(){
    return {
      que: {
        title: "holo",
        QList: [{
          qid: 0,
          type: 0,
          title: "主要用于课堂测试等场景，发布者应该可以设置每道题目的评分和答案，也可以设置问" +
              "卷整体的限时时间，超时将自动回收。针对填写者，问卷题目应该可以乱序展示，在填写者" +
              "提交后，问卷应该可以对客观题目进行自动评分，并使填写者可以查看答案。",
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
          qid: 1,
          type: 1,
          title: "到底什么是hello",
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
          title: "到底到底什么是hello",
        }, {
          qid: 3,
          type: 3,
          title: "到底到底到底什么是hello",
        }]
      },
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      fullscreenLoading: false,
      titleEditDialog: false,
      editingTitleQuestion:null,
      editingTitle:'',
      addQuestionVisible: false,
      drag: false
    }
  },
  methods: {
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
    },
    addSpaceFilling() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 2,
        title: "请输入题干",
      })
    },
    addRating() {
      this.addQuestionVisible = false;
      let i = this.que.QList.length
      this.que.QList.push({
        qid: i,
        type: 3,
        title: "请输入题干",
      })
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
    uploadQn(flag){
      this.$axios({method:"post",url:"/questionnaire/saveQn", data:{
        "share": flag,
          "que":{
            "title":this.que.title,
            "QList":this.que.QList
          }}})
          .then(res => {
            if(res.data.success === true){
              this.$notify({
                title: '成功',
                message: flag?'分享':'保存'+'问卷成功',
                type: 'success',
                position: 'bottom-left'
              });
            }
            else {
              this.$notify({
                title: '失败',
                message: flag?'分享':'保存'+'问卷失败',
                type: 'error',
                position: 'bottom-left'
              });
            }
            //这里要加一个弹出分享窗口的语句
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
        this.que.QList[i].qid=i
      }
      this.drag = false;
    },
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

.choose {
  opacity: 0;
}
</style>