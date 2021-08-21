<template>
  <div class="hello">
    <div class="head" style="color: black">
      <img alt="Vue logo" src="../assets/logo.png" class="logo">
    </div>
    <div class="body">

    </div>


  </div>


</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.logo{
  position:absolute;
  left: 10%;
  bottom: 100%;
  transform:translate(-50%);
  height: 30%;
}
.head{
  position: absolute;
  height: 20%;
  width: 100%;
  background-color:#ffffff46;
}
.body{
  position: absolute;
  height: 80%;
  width: 100%;
  background-color:#ffffff46;
}
</style>
