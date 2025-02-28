import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ServiceView from '../views/ServiceView.vue';
import DownloadReadyView from '../views/DownloadReadyView.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/service',
    name: 'service',
    component: ServiceView
  },
  {
    path: '/download-ready',
    name: 'DownloadReady',
    component: DownloadReadyView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
