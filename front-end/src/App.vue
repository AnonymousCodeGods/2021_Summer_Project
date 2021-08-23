<template>
  <div id="app" :style="heightAndWidth">
      <el-col >
        <router-view></router-view>
      </el-col>
  </div>
</template>

<script>
export default{
  data: function () {
    return{
      heightAndWidth: 'margin:0; height:'+
          (window.innerHeight).toString()+
          'px; width:'+
          (window.innerWidth).toString()+
          'px;',
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin: 0px;
  color: #2c3e50;
}
</style>
