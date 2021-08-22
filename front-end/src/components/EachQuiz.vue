<template>
  <div class="quiz">
    <a style="float: left;padding-left: 40px;padding-top: 20px;width: 300px">{{ type }}</a>
    <a class="bas" style="float: left;padding-left: 50px;padding-top: 20px">ID：{{ id }}</a>
    <a class="bas" style="float: left;padding-left: 30px;padding-top: 20px;">状态：{{ state==='1'?'已发布':'未发布' }}</a>
    <a class="bas" style="float: left;padding-left: 30px;padding-top: 20px">创建日期：{{ date }}</a>
    <a class="bas" style="float: left;padding-left: 30px;padding-top: 20px">回收量：{{ num }}</a>
    <!--分割线-->
    <div class="midText"></div>
    <a style="float:right;padding-right: 70px;padding-top: 60px;height: 20px;cursor:pointer;" @click="del">删除</a>
    <img src="../assets/del.png" style="float:right;padding-right: 10px;padding-top: 60px;height: 20px;cursor:pointer;">
    <a style="float:right;padding-right: 70px;padding-top: 60px;height: 20px;width: 60px;cursor:pointer;" @click="pub" v-if="state==='0'">发布</a>
    <a style="float:right;padding-right: 70px;padding-top: 60px;height: 20px;width: 60px;cursor:pointer;" @click="start" v-else>暂停</a>
    <img src="../assets/open.png"
         style="float:right;padding-right: 10px;padding-top: 60px;height: 20px;cursor:pointer;">
    <a class="fun" style="float: right;padding-right: 190px;padding-top: 58px" @click="edit"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">编辑问卷</a>
    <a class="fun" style="float: right;padding-right: 30px;padding-top: 58px" @click="toResult"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">查看结果</a>
    <a class="fun" style="float: right;padding-right: 30px;padding-top: 58px" @click="exported"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">导出问卷</a>
    <a class="fun" style="float: right;padding-right: 30px;padding-top: 58px" @click="links"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">发送链接</a>


  </div>
</template>

<script>
export default {
  name: "EachQuiz",
  props: {
    type: String,
    id: String,
    state: String,
    date: String,
    num: String,
  },
  methods: {
    mouseOver($event) {
      $event.currentTarget.className = 'active';
    },
    mouseLeave($event) {
      $event.currentTarget.className = 'fun';
    },
    del() {

    },
    pub() {
      this.state='1';
    },
    start(){
      this.state='0';
    },
    edit() {

    },
    toResult() {

    },
    exported() {

    },
    links() {

    },
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
  border: #d5d5d5 solid 1px;
}

.midText {
  position: absolute;
  margin-top: 60px;
  left: 31%;
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
</style>