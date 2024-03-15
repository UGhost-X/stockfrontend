<template>
  <a-layout class="layout">
    <a-layout-content style="margin: 10px 10px 5px 10px">
      <a-row :gutter="[16, 24]">
        <a-col :span="24">
          <div class="cardscontent">
            <a-skeleton active :paragraph="{ rows: 8 }" />
          </div>
        </a-col>
        <a-col :span="16">
          <div class="cardscontent">
            <a-skeleton active :paragraph="{ rows: 5 }" />
          </div>
        </a-col>
        <a-col :span="8">
          <div class="cardscontent">
            <a-skeleton active :paragraph="{ rows: 5 }" />
          </div>
        </a-col>
      </a-row>
    </a-layout-content>
  </a-layout>
</template>
<script lang="ts" setup></script>
<style scoped>
.layout {
  margin: 0; /* 居中布局 */
  height: 100%;
}
.cardscontent{
  border-radius: 10px;
  background: #fff;
  padding: 12px;
}
</style>
