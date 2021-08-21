<template>
  <div class="QueList">
    <div class="title">
      {{title}}
    </div>
    <el-divider></el-divider>
    <span></span>
  </div>
</template>

<script>
export default {
  name: "QueList",
  data: function () {
    return {
        title: '时间统计',
        qid: 1,
        status: false,
        date: '2021/05/01',
        count: 0
    }
  }
}
</script>

<style scoped>

.QueList {
  width:900px;
  margin: auto;
  border: 1px solid #eee;
  border-radius: 2px;
  height: 150px;
  padding: 24px;
}

.title{
  text-align: left;
}

</style>