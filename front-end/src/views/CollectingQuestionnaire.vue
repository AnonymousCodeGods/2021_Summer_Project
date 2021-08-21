<template>
  <div>
    <el-card style="width: 800px; margin: auto"  v-loading.fullscreen.lock="fullscreenLoading">
      <div slot="header" class="clearfix">
        <span style="font-size: larger">{{que.title}}</span>
      </div>
      <div v-for="item in que.QList"
           :key="item.id" style="margin: 15px">
        <div v-if="item.type===0">
          <div class="queLabel">
            {{item.qid+1}}.{{item.title}}
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
            {{item.qid+1}}.{{item.title}}
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
            {{item.qid+1}}.{{item.title}}
          </div>
          <div style="margin: 7px 10%;">
            <el-input v-model="item.input"/>
          </div>
        </div>
        <div v-if="item.type===3">
          <div style="margin-left: 10%;margin-bottom:8px;text-align: start;">
            {{item.qid+1}}.{{item.title}}
          </div>
          <div class="queLabel">
            <el-rate
                v-model="item.rating"
                :colors="colors">
            </el-rate>
          </div>
        </div>
      </div>
      <div style="margin-top: 30px">
        <el-button type="primary" style="width: 15%">提交</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CQue',
  created() {
    this.$axios({method:"post",url:"/questionnaire/getQn", data:{"QnId": this.$route.query.id}})
        .then(res => {
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
                option:optionTemp,
                selection:-1
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
                selections: []
              })
            }
            else if(temp1.type === 2){
              this.que.QList.push({
                qid:i,
                type:temp1.type,
                title: temp1.title,
                input : ""
              })
            }
            else{
              this.que.QList.push({
                qid:i,
                type:temp1.type,
                title: temp1.title,
                rating : 0
              })
            }
          }
        })
        // eslint-disable-next-line no-unused-vars
        .catch(() => {
          this.$notify({
            title: '失败',
            message: '连接失败',
            type: 'error',
            position: 'bottom-left'
          });
          //this.$router.push('/');
        })
  },
  data: function(){
    return {
      que: {
        qnid: '123123',
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
          selection: -1
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
          selections: []
        }, {
          qid: 2,
          type: 2,
          title: "到底到底什么是hello",
          input: ""
        }, {
          qid: 3,
          type: 3,
          title: "到底到底到底什么是hello",
          rating: 0
        }]
      },
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      fullscreenLoading: false
    }
  },
  methods: {

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