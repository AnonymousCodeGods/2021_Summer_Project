<template>
  <div style="justify-content: center;margin-top: 200px">
    <el-card style="width: 800px; margin: auto;height: 200px"  v-loading.fullscreen.lock="fullscreenLoading">
      <div slot="header" class="clearfix">
        <span style="font-size: larger">抱歉！您已经填写过此问卷</span>
      </div>
      <div style="margin-top: 30px">
        <el-button type="primary" style="width: 30%" plain icon="el-icon-circle-check" v-on:click="quit">返回首页</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CQue',
  data: function(){
    return {
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