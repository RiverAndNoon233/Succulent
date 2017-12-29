import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
//一下四个是二级路由组件
import news from "@/components/lots/modules/news"
import lots from "@/components/lots/modules/lots"
import article from "@/components/lots/modules/article"
import picture from "@/components/lots/modules/picture"

//以下四个分别是 多多 商城 我的 。。
import lotTwo from '@/components/lots/lotTwo'
import Find from "@/components/lots/find"
import Shop from "@/components/lots/shop"
import Mine from "@/components/lots/mine"

Vue.use(Router)

const routes = [
    {path:'/',redirect:'/lotindex'},
    
    {path:"/find-fo",name:'find-fo',component:Find},
    {path:"/shop-fo",name:'shop-fo',component:Shop},
    {path:"/mine-fo",name:'mine-fo',component:Mine},
    //二级路由
    {path: '/lotindex',component:lotTwo,children:[
      {path: '',redirect:'lots',component:lots},
      {path: 'lots',name: 'lots',component:lots},
      {path: 'article',name: 'article',component:article},
      {path: 'picture',name: 'picture',component:picture},
      {path: 'news',name: 'news',component:news},    
    ]
    },    
    {path:'/**',redirect:'/lotindex'}
  ]
//去掉路由前面#号
const router = new Router({
  routes,
  mode:'history'
})
//暴露路由模块
export default router