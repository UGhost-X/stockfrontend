<template>
  <a-layout class="layout">
    <a-layout-content style="margin: 10px 10px 3px 10px">
      <a-row>
        <a-col :span="6">
          <div class="functionalarea" style="padding-top: 5px;">
            <a-switch v-model:checked="checked" />
          </div>
        </a-col>
        <a-col :span="12">
          <div class="functionalarea">
            <a-select
              v-model:value="value"
              style="width: 100%;"
              placeholder="6022222 xxxxxx"
              :options="options"
              :show-arrow="false"
              @change="handleChange"></a-select>
          </div>
        </a-col>
        <a-col :span="6">
          <div class="functionalarea">
            <!-- <a-switch v-model:checked="checked" /> -->
          </div>
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="24">
          <div class="cardscontent">
            <a-skeleton active :paragraph="{ rows: 15 }" />
          </div>
        </a-col>
      </a-row>
    </a-layout-content>

    <a-float-button-group
      trigger="click"
      type="primary"
      :style="{ right: '24px' ,bottom:'15px'}">
      <template #icon>
        <CustomerServiceOutlined />
      </template>

      <a-float-button />

      <a-float-button>
        <template #icon>
          <CommentOutlined />
        </template>
      </a-float-button>
    </a-float-button-group>
  </a-layout>
</template>
<script setup lang="ts">
import {
  CustomerServiceOutlined,
  CommentOutlined,
} from "@ant-design/icons-vue";
import { ref } from "vue";
const checked = ref<boolean>(false);
const handleChange = (value: string) => {
  console.log(`selected ${value}`);
};
const value = ref([]);
const options = [...Array(25)].map((_, i) => ({
  value: (i + 10).toString(36) + (i + 1),
}));
</script>
<style scoped>
.layout {
  margin: 0; /* 居中布局 */
  height: 100%;
}
.functionalarea {
  margin-bottom: 10px;
  /* background: #fff; */
}
.cardscontent {
  border-radius: 0 0 10px 10px;
  background: #fff;
  padding: 12px;
}
</style>
