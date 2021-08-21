<template>
  <div class="home">
    <div v-if="$store.state.isLogin">已经登录!</div>
    <div v-else>尚未登录,请前往登陆<router-link to="/login">Login</router-link></div>
    <img alt="Vue logo" src="../assets/logo.png">

  </div>
</template>

<script>

export default {

}
</script>
