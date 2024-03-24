<template>
  <a-row>
    <a-col :span="6">
      <div style="background-color: black">1233</div>
    </a-col>
    <a-col :span="18" class="logstyle">
      <div class="logbackground">
        <div class="loginfo">
          12222223 52333333 2223544 11132131 11313dddddddddddddddddddddddddddd
          11313dddddddddddddddddddddddddddd 11313dddddddddddddddddddddddddddd
          11313dddddddddddddddddddddddddddd
        </div>
      </div>
    </a-col>
  </a-row>
</template>

<script setup lang="ts">
import { ref } from "vue";
</script>

<style scoped>
.logstyle {
  background-image: url("@/assets/pictures/logtelevison3.png");
  background-repeat: no-repeat;
  background-position: right;
  background-size: 100% 100%;
  height: calc(100vh - 83px);
  width: 100%;
  /* margin: 50px 50px 0 0; */
  /* padding: 50px 50px 0 0; */
  border-width: 50px 50px 0 0;
  border-style: solid;
  border-color: transparent;
  position: relative;
}
.logbackground{
  background: linear-gradient(31deg,#65799ba3,#5e2563);
  z-index:-999;
}
.loginfo {
  position: absolute;
  font-size: 102px;
  /* height: 100%; */
  left: calc(100vw - 94vw);
  top: 90px;
  bottom: 200px;
  padding: 0 0 0 0;
  max-height: calc(100vh);
  max-width: calc(100vw - 53vw);
  overflow-y: scroll;
  overflow-wrap: break-word;
}
::-webkit-scrollbar-thumb {
  background-color: transparent;
}
</style>
