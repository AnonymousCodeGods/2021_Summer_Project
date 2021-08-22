<template>
  <div>
    <el-card style="width: 800px; margin: auto"  v-loading.fullscreen.lock="fullscreenLoading">
      <div slot="header" class="clearfix">
        <span style="font-size: larger">{{que.title}}的结果</span>
      </div>
      <div v-for="item in que.QList"
           :key="item.id" style="margin: 15px">
        <div class="queLabel" style="line-height: 30px;">
          <el-tag v-if="item.type===0" size="small" type="success">单选</el-tag>
          <el-tag v-else size="small" type="primary">多选</el-tag>
          {{item.qid+1}}.{{item.title}}
        </div>
        <div style="margin-left: 10%;margin-right: 10%">
            <div
                v-for="subItem in item.option"
                :key="subItem.oid"
                style="width: 100%;margin: 10px;">
              <div style="font-size: medium;text-align: left;margin-left: 1%">{{subItem.content}}</div>
              <el-progress :percentage="subItem.percentage" ></el-progress>
            </div>
        </div>
      </div>
      <div style="margin-top: 30px">
        <el-button type="primary" style="width: 15%" plain icon="el-icon-circle-check" v-on:click="quit">确认</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CQue',
  created() {
  },
  data: function(){
    return {
      que: {
        qnid: 0,
        title: "测试问卷",
        QList: [{
          qid: 0,
          type: 0,
          title: "主要用于课堂测试等场景，发布者应该可以设置每道题目的评分和答案，也可以设置问" +
              "卷整体的限时时间，超时将自动回收。针对填写者，问卷题目应该可以乱序展示，在填写者" +
              "提交后，问卷应该可以对客观题目进行自动评分，并使填写者可以查看答案。",
          option: [{
            oid: 0,
            content: "你好",
            percentage: 10
          }, {
            oid: 1,
            content: "hello",
            percentage: 80
          }, {
            oid: 2,
            content: "hi",
            percentage: 10
          }],
        }, {
          qid: 1,
          type: 1,
          title: "到底什么是hello",
          option: [{
            oid: 0,
            content: "你好",
            percentage: 60
          }, {
            oid: 1,
            content: "hello",
            percentage: 20
          }, {
            oid: 2,
            content: "hi",
            percentage: 80
          }]
        }]
      },
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      fullscreenLoading: false
    }
  },
  methods: {
    quit(){
      this.$router.push("/")
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