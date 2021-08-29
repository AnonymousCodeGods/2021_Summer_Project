<template>
<div class="box">
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <div class="box_fixed" id="boxFixed" :class="{'is_fixed' : isFixed}">
      我是来测试的、哇咔咔
    </div>
    <h3>快下来</h3>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
    <h4>吸顶测试</h4>
  </div>
</template>
<script>
 export default {
    data(){
      return {
        isFixed: false,
        offsetTop:0
      }
    },
    mounted(){
      window.addEventListener('scroll',this.initHeight);
      this.$nextTick( () => {
        this.offsetTop = document.querySelector('#boxFixed').offsetTop;
      })
    },
    methods:{
      initHeight () {
        var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
        this.isFixed = scrollTop > this.offsetTop ? true : false;
      },
    },
    destroyed () {
      window.removeEventListener('scroll', this.handleScroll)
    },
  }
</script>

<style>
  .box_fixed{
    width: 500px;
    height: 40px;
    border: 2px dashed pink;
    border-radius: 20px;
    margin: 0 auto;
    line-height: 40px;
    background: #eee;
  }
  .is_fixed{
    position: fixed;
    top: 0;
    left: 50%;
    margin-left: -250px;
    z-index: 999;
  }
</style>