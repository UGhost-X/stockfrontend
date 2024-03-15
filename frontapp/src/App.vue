<template>
  <nav-header/>
  <router-view/>
</template>

<script setup lang="ts">
import NavHeader from './components/NavHeader.vue';
</script>

<style lang="less">

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
  height: 100%;
}

</style>
