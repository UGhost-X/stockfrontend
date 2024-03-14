<template>
  <a-layout class="layout" style="height: 100%;">
    <a-layout-header style="height: 48px">
      <div class="logo">
        <img src="@/assets/logo.svg" style="width: 42px;height: 42px;margin-top: 4px; "/>
      </div>
      <a-menu
        v-model:selectedKeys="selectedKeys"
        theme="dark"
        mode="horizontal"
        :style="{ lineHeight: '48px',padding: '0'}"
      >
        <a-menu-item key="1">大盘晴雨</a-menu-item>
        <a-menu-item key="2">候选分析</a-menu-item>
        <a-menu-item key="3">历史跟踪</a-menu-item>
        <a-menu-item key="4">历史记录</a-menu-item>
        <a-menu-item key="5">日志管理</a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="margin:10px 10px 10px 10px;">
      <div :style="{ background: '#fff', padding: '12px', minHeight: '100%' }">
        <a-skeleton  active :paragraph="{ rows: 7 }"/>
      </div>
    </a-layout-content>
    <!-- <a-layout-footer style="text-align: center">
      Ant Design ©2018 Created by Ant UED
    </a-layout-footer> -->
  </a-layout>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
const selectedKeys = ref<string[]>(['1']);
</script>
<style scoped>
.layout {
  margin: 0; /* 居中布局 */
}
.logo {
  float: left;
  width: 120px;
  height: 31px;
  /* margin: 16px 24px 16px 0; */
}
</style>
