<template>
  <div :style="heightAndWidth">
    <el-card style="width: 800px; margin: auto"  v-loading.fullscreen.lock="fullscreenLoading">
    <div class="row" id="pdfDom">
      <div slot="header" class="clearfix">
        <span style="font-size: larger">{{que.title}}</span>
      </div>
      <div v-for="item in que.QList"
           :key="item.qid" style="margin: 15px">
        <div v-if="item.belongTo.qid===-1||que.QList[item.belongTo.qid].selection===item.belongTo.option">
          <div style="float: left;margin-left: 12px">
            <el-tag type="warning" size="small" v-if="(item.type===0||item.type===1)&&(item.necessary === true)">必选</el-tag>
            <el-tag type="warning" size="small" v-if="(item.type === 2||item.type === 3)&&(item.necessary === true)">必填</el-tag>
          </div>
          <div v-if="item.type===0">
            <div class="queLabel">
            <span v-if="que.showNumbers">
              {{item.qid+1}}.
            </span>
              <span>
              {{item.title}}
            </span>
            </div>
            <div style="margin-left: 10%;margin-right: 10%">
              <el-radio-group
                  v-model="item.selection" style="width: 100%">
                <el-radio
                    v-for="subItem in item.option"
                    :key="subItem.oid"
                    :label="subItem.oid"
                    style="width: 100%;margin: 10px;display: flex;align-items: flex-start;">
                  <span style="font-size: medium;">{{subItem.content}}</span>
                </el-radio>
              </el-radio-group>
            </div>
          </div>
          <div v-if="item.type===1">
            <div class="queLabel">
            <span v-if="que.showNumbers">
              {{item.qid+1}}.
            </span>
              <span>
              {{item.title}}
            </span>
            </div>
            <div style="margin-left: 10%;margin-right: 10%">
              <el-checkbox-group
                  v-model="item.selections" style="width: 100%">
                <el-checkbox
                    v-for="subItem in item.option"
                    :key="subItem.oid"
                    :label="subItem.oid"
                    style="width: 100%;margin: 10px;display: flex;align-items: flex-start;">
                  <span style="font-size: medium;">{{subItem.content}}</span>
                </el-checkbox>
              </el-checkbox-group>
            </div>
          </div>
          <div v-if="item.type===2">
            <div class="queLabel">
            <span v-if="que.showNumbers">
              {{item.qid+1}}.
            </span>
              <span>
              {{item.title}}
            </span>
            </div>
            <div style="margin: 7px 10%;">
              <el-input v-model="item.input"/>
            </div>
          </div>
          <div v-if="item.type===3">
            <div class="queLabel">
            <span v-if="que.showNumbers">
              {{item.qid+1}}.
            </span>
              <span>
              {{item.title}}
            </span>
            </div>
            <div class="queLabel">
              <el-rate
                  v-model="item.rating"
                  :colors="colors">
              </el-rate>
            </div>
          </div>
          <div v-if="item.type===4">
            <div class="queLabel">
            <span v-if="que.showNumbers">
              {{item.qid+1}}.
            </span>
              <span>
              {{item.title}}
            </span>
            </div>
            <div class="queLabel">
              <el-input v-model="item.location" disabled style="width: 75%">

              </el-input>
              <el-popover placement="top"
                          title="确定要获取您的当前位置吗"
                          v-model="item.dialogVisible">
                <el-button plain type="warning" icon="el-icon-map-location" slot="reference" style="margin-left: 5%;width: 20%">
                  定位
                </el-button>
                <el-button plain type="warning" icon="el-icon-check"  size="mini" style="margin-left:15%;width: 30%" v-on:click="getMapLocation(item)"/>
                <el-button plain type="" icon="el-icon-close"  size="mini" style="margin-left:10%;width: 30%" v-on:click="item.dialogVisible=false"/>
              </el-popover>
            </div>
          </div>
        </div>
      </div>
      </div>
      <div style="margin-top: 30px">
        <el-button type="primary" style="width: 15%" plain icon="el-icon-circle-check" v-on:click="submitQn">提交</el-button>
        <el-button type="primary" style="width: 15%" plain icon="el-icon-circle-check" v-on:click="getPdf('问卷')">导出pdf</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
import AMap from 'AMap'
export default {
  name: 'CQue',
  created() {
    this.fullscreenLoading=true;
    this.$axios({method:"post",url:"/getQn", data:{"QnId": this.$route.query.id}})
        .then(res => {
          if(res.data.que.state === false){
            this.$router.push('/failedResult');
          }
          console.log(res)
          this.que.QList=[]
          this.que.qnType = res.data.que.qnType
          this.que.qnId = res.data.que.qnid;
          this.que.showNumbers = res.data.que.showNumbers;
          this.que.title = res.data.que.title;
          for(let i=0;i<res.data.que.QList.length;i++){
            let temp1=res.data.que.QList[i];
            if(temp1.type === 0){
              let optionTemp=[];
              console.log(temp1.option.length)
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
                option:optionTemp,
                necessary: temp1.necessary,
                selection:-1,
                belongTo:temp1.belongTo
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
                option:optionTemp,
                necessary: temp1.necessary,
                selections: [],
                belongTo:temp1.belongTo
              })

            }
            else if(temp1.type === 2){
              this.que.QList.push({
                qid:i,
                type:temp1.type,
                title: temp1.title,
                input : "",
                belongTo:temp1.belongTo,
                necessary: temp1.necessary,
              })

            }
            else if(temp1.type === 3){
              this.que.QList.push({
                qid:i,
                type:temp1.type,
                title: temp1.title,
                rating : 0,
                belongTo:temp1.belongTo,
                necessary: temp1.necessary,
              })


            } else {
              this.que.QList.push({
                qid:i,
                type:temp1.type,
                title: temp1.title,
                location : '',
                dialogVisible: false,
                belongTo:temp1.belongTo,
                necessary: temp1.necessary,
              })

            }
          }
          console.log(this.que)
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
          this.$router.push('/');
        })
  },
  data: function(){
    return {
      heightAndWidth: 'margin:0; height:'+
          (window.innerHeight).toString()+
          'px; width:'+
          (window.innerWidth).toString()+
          'px;'+
          'background-color: #fafafa;'+
          'position:fixed;overflow:scroll',
      que: {
        qnId: '0',
        qnType: 0,
        showNumbers: true,
        title: "测试问卷",
        QList: [{
          qid: 0,
          type: 0,
          title: "这是一道单选题，点击右边的按钮可以更改题目",
          hasAnswer: false,
          answer:0,
          necessary: true,
          selection: -1,
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
          selections: [],
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
          input:''
        }, {
          qid: 3,
          type: 3,
          title: "我是一道评分题",
          necessary: true,
          rating:0
        }, {
          qid: 4,
          type: 4,
          title: "我是一道定位题",
          necessary: false,
          location:'',
          dialogVisible: false
        }]
      },
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      fullscreenLoading: false
    }
  },
  methods: {
    getMapLocation(item) {
      let temp = this
      AMap.plugin('AMap.Geolocation', function() {
        let geolocation = new AMap.Geolocation({
          // 是否使用高精度定位，默认：true
          enableHighAccuracy: true,
          // 设置定位超时时间，默认：无穷大
          timeout: 10000,

        })

        geolocation.getCurrentPosition()
        AMap.event.addListener(geolocation, 'complete', onComplete)
        AMap.event.addListener(geolocation, 'error', onError)

        function onComplete (data) {
          temp.$notify({
            title: '成功',
            message: '定位成功',
            type: 'success',
            position: 'bottom-left'
          });
          item.location = data.formattedAddress
        }

        function onError () {
          temp.$notify({
            title: '失败',
            message: '定位失败',
            type: 'error',
            position: 'bottom-left'
          });
        }
      })
      item.dialogVisible =false
    },
    submitQn(){
      this.fullscreenLoading = true
      for(let i=0;i<this.que.QList.length;i++){
        if(this.que.QList[i].necessary) {
          if(this.que.QList[i].belongTo.qid===-1||this.que.QList[this.que.QList[i].belongTo.qid].selection===this.que.QList[i].belongTo.option){
            if((this.que.QList[i].type === 0 && this.que.QList[i].selection===-1)
                ||(this.que.QList[i].type === 1 && this.que.QList[i].selections.length===0)
                ||(this.que.QList[i].type===2&&this.que.QList[i].input==='')
                ||(this.que.QList[i].type===3&&this.que.QList[i].rating===0)
                ||(this.que.QList[i].type===4&&this.que.QList[i].location==='')) {
              this.$message({
                message: '请填写所有必填项',
                type: 'warning'
              });
              this.fullscreenLoading = false
              return
            }
          }

        }
      }
      let AnswerListTemp = [];
      for(let i=0;i<this.que.QList.length;i++){
        let temp1=this.que.QList[i];
        if(temp1.type === 0){
          AnswerListTemp.push({
            type: temp1.type,
            answer:temp1.selection
          })
        }
        else if(temp1.type === 1){
          AnswerListTemp.push({
            type: temp1.type,
            answer: temp1.selections
          })
        }
        else if(temp1.type === 2){
          AnswerListTemp.push({
            type: temp1.type,
            answer : temp1.input
          })
        }
        else if(temp1.type ===3) {
          AnswerListTemp.push({
            type: temp1.type,
            answer : temp1.rating
          })
        }else {
          AnswerListTemp.push({
            type: temp1.type,
            answer : temp1.location
          })
        }
      }
      this.$axios({method:"post",url:"/quiz/submitQn", data:{
          "qnId": this.que.qnId,
          "qnType": this.que.qnType,
          "userName": this.$cookies.isKey("username") ? this.$cookies.get("username") : "unLogin",
          "AnswerList":AnswerListTemp
      }})
          .then(res => {
            this.fullscreenLoading = false
            if(res.data.success === true){
              this.$notify({
                title: '成功',
                message: '提交问卷成功',
                type: 'success',
                position: 'bottom-left'
              });
              if(this.que.qnType === 1) {
                this.$router.push({
                  path:'/showVoteResult',
                  query:{
                    id:this.que.qnId
                  }
                });
              } else {
                this.$router.push('/successResult');
              }
            }
            else {
              this.$notify({
                title: '失败',
                message: '提交问卷失败',
                type: 'error',
                position: 'bottom-left'
              });
              this.fullscreenLoading=false
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
          })
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
</style>
