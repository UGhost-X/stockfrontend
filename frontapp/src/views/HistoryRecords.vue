<template>
  <!-- (index:number) => (index%2===1?'ant-table-row':null) -->
  <a-layout class="layout">
    <a-layout-content>
      <a-table
        class="ant-table-striped"
        :columns="columns"
        :data-source="tabledata"
        :row-class-name="(_record:any,index:number) => (index%2===0?'oddsrowcolor':'evenrowcolor')">
        <template #emptyText>
          <a-empty description="暂无数据" />
        </template>
        <template #bodyCell="{ column, record }">
          <template v-if="column.dataIndex === 'operation'">
            <a-popconfirm
              v-if="tabledata.length"
              title="确认删除"
              ok-text="是"
              cancel-text="否"
              @confirm="onDeleteRecord(record.key)">
              <a><DeleteIcon /></a>
            </a-popconfirm>
          </template>
        </template>
      </a-table>
    </a-layout-content>
  </a-layout>
</template>
<script setup lang="ts">
import { ref, Ref } from "vue";
// 表格控制区
const columns = [
  {
    title: "选中日期",
    dataIndex: "pickdate",
    key: "pickdate",
    align: "center",
    width: 100,
  },
  {
    title: "代码",
    dataIndex: "code",
    key: "code",
    align: "center",
  },
  {
    title: "名称",
    dataIndex: "name",
    key: "code",
    align: "center",
  },
  {
    title: "当前涨幅",
    dataIndex: "currentlyshave",
    key: "currentlyshave",
    align: "center",
  },
  {
    title: "三日涨幅",
    dataIndex: "thirdday",
    key: "thirdday",
    align: "center",
  },
  {
    title: "七日涨幅",
    dataIndex: "thirdday",
    key: "seventhday",
    align: "center",
  },
  {
    title: "双周涨幅",
    dataIndex: "dualweeks",
    key: "dualweeks",
    align: "center",
  },
  {
    title: "10%达到日期",
    dataIndex: "10%arrivedate",
    key: "arrivedate",
    align: "center",
  },
  {
    title: "耗费天数",
    dataIndex: "consumedays",
    key: "consumedays",
    align: "center",
  },
  {
    title: "操作",
    dataIndex: "operation",
    key: "operation",
    align: "center",
  },
];

interface DataItem {
  key: string;
  code: string;
  name: string;
}

const tabledata: Ref<DataItem[]> = ref([
  {
    key: "1",
    code: "6020000",
    name: "xxxxxxx",
  },
  {
    key: "2",
    code: "6020000",
    name: "xxxxxxx",
  },
  {
    key: "3",
    code: "6020000",
    name: "xxxxxxx",
  },
]);
const onDeleteRecord = (key: string) => {
  tabledata.value = tabledata.value.filter((item) => item.key !== key);
};
</script>
<style scoped>
.oddsrowcolor {
  background-color: #1abc9c;
}
.evensrowcolor {
  background-color: #ff4757;
}


</style>
