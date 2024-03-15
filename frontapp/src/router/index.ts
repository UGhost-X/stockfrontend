import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import StockStatus from '@/views/StockStatus.vue'
import StockAnalysis from '@/views/StockAnalysis.vue'
import HistoryForce from '@/views/HistoryForce.vue'
import HistoryRecords from '@/views/HistoryRecords.vue'
import LogManagement from '@/views/LogManagement.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect:'/stockstatus'
  },
  {
    path: '/stockstatus',
    name: 'stockstatus',
    component: StockStatus
  },
  {
    path: '/stockanalysis',
    name: 'stockanalysis',
    component: StockAnalysis
  },
  {
    path: '/historyforce',
    name: 'historyforce',
    component: HistoryForce
  },
  {
    path: '/historyrecords',
    name: 'historyrecords',
    component: HistoryRecords
  },
  {
    path: '/logmanagement',
    name: 'logmanagement',
    component: LogManagement
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
