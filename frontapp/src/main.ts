import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Button,Flex,Radio,RadioButton,RadioGroup,Layout,Menu,MenuItem,LayoutContent,LayoutHeader
    ,LayoutFooter,Breadcrumb,BreadcrumbItem,Skeleton
} from 'ant-design-vue'

const app = createApp(App)

app.use(store)
app.use(router)

// 将Ant Design Vue组件安装到Vue实例上
app.component(Button.name, Button)
app.component(Flex.name, Flex)
app.component(Radio.name,Radio)
app.component(RadioButton.name, RadioButton)
app.component(RadioGroup.name, RadioGroup)
app.component(Layout.name, Layout)
app.component(Menu.name, Menu)
app.component(MenuItem.name, MenuItem)
app.component(LayoutContent.name, LayoutContent)
app.component(LayoutHeader.name, LayoutHeader)
app.component(LayoutFooter.name, LayoutFooter)
app.component(Breadcrumb.name, Breadcrumb)
app.component(BreadcrumbItem.name, BreadcrumbItem)
app.component(Skeleton.name, Skeleton)

app.mount('#app')
