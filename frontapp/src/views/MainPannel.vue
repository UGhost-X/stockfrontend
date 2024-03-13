<template>
  <a-layout class="layout" style="top: 0%; padding: auto;">
    <a-layout-header>
      <div class="logo" />
      <a-menu
        v-model:selectedKeys="selectedKeys"
        theme="dark"
        mode="horizontal"
        :style="{ lineHeight: '48px' }"
      >
        <a-menu-item key="1">大盘晴雨</a-menu-item>
        <a-menu-item key="2">候选分析</a-menu-item>
        <a-menu-item key="3">历史跟踪</a-menu-item>
        <a-menu-item key="4">历史记录</a-menu-item>
        <a-menu-item key="5">日志管理</a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>Home</a-breadcrumb-item>
        <a-breadcrumb-item>List</a-breadcrumb-item>
        <a-breadcrumb-item>App</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">Content</div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      Ant Design ©2018 Created by Ant UED
    </a-layout-footer>
  </a-layout>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
const selectedKeys = ref<string[]>(['1']);
</script>
<style scoped>
.layout {
  width: 100%;
  max-width: 1200px; /* 设置最大宽度，根据需要调整 */
  margin: 0 auto; /* 居中布局 */
}
</style>
