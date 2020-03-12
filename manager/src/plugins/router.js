import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter);

const announcement = () => import('@/components/Announcement');
const dormitoryManagement = () => import('@/components/DormitoryManagement');
const health = () => import('@/components/Health');
const maintenance = () => import('@/components/Maintenance');
const login = () => import('@/components/login');
const passwordChange = () => import('@/components/PasswordChange');
const studentMangement = () => import('@/components/StudentMangement');
const waterElectricity = () => import('@/components/WaterElectricity');
const routes = [
  {
    path: '/login',
    component: login
  },
  {
    path: '/announcement',
    component: announcement
  },
  {
    path: '/dormitoryManagement',
    component: dormitoryManagement
  },
  {
    path: '/health',
    component: health
  },
  {
    path: '/maintenance',
    component: maintenance
  },
  {
    path: '/passwordChange',
    component: passwordChange
  },
  {
    path: '/studentMangement',
    component: studentMangement
  },
  {
    path: '/waterElectricity',
    component: waterElectricity
  },
];

const router = new VueRouter({
  routes: routes
});

export default router;
