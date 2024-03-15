<template>
  <a-layout class="layout" style="height: 100%;">
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
</script>
<style scoped>
.layout {
  margin: 0; /* 居中布局 */
}
</style>
