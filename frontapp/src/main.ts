import { createApp, onBeforeMount, onMounted } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Antd from "ant-design-vue";
//@ts-ignore
import VuewechatTitle from "vue-wechat-title";
import "@/assets/style/index.less";


const app = createApp(App);
app.use(VuewechatTitle);
app.use(store);
app.use(router);
app.use(Antd);
app.mount("#app");
