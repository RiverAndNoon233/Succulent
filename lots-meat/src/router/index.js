import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

//一下四个是二级路由组件
import news from "@/components/lots/modules/news"
import lots from "@/components/lots/modules/lots"
import article from "@/components/lots/modules/article"
import picture from "@/components/lots/modules/picture"

import newPersonKnow from "@/components/lots/modules/mustKnow-vue/newPerson-know"
import newShopKnow from "@/components/lots/modules/mustKnow-vue/newShop-know"
import newPlantKnow from "@/components/lots/modules/mustKnow-vue/newPlant-know"
import newDayKnow from "@/components/lots/modules/mustKnow-vue/newDay-know"

//以下四个分别是 多多 商城 我的 。。
import lotTwo from '@/components/lots/lotTwo'
import Find from "@/components/lots/find/find"
import Shop from "@/components/lots/shop"
import Mine from "@/components/lots/mine/Mine"

//未登陆和注册时路由
import MineLogin from "@/components/lots/mine/MineLogin"
import MineLoginOn from "@/components/lots/mine/MineLoginOn"

//我的组件路由
import MyPublish from "@/components/lots/mine/minetop/MyPublish"
import MyCollect from "@/components/lots/mine/minetop/MyCollect"
import MyFriends from "@/components/lots/mine/minetop/MyFriends"

Vue.use(Router)

import store from '../vuex/store'

const routes = [
    {path:'/',redirect:'/lotindex'},
    
    {path:"/find-fo",name:'find-fo',component:Find},
    {path:"/shop-fo",name:'shop-fo',component:Shop},
    {path:"/mine-fo",name:'',component:Mine,children:[
      {path:'',redirect:to=>{ 			
  			//判断是否登陆
  		
  			if(!localStorage.user_info){
  				return {name:'minelogin'}
  			}else{
  			
  				//vuex里的同步
  				store.commit("change_type",JSON.parse(localStorage.user_info))
  				return {name:'mineloginon'}
  			}
  			
       }},  	
      {path: 'mineloginon',name: 'mineloginon',component:MineLoginOn},
      {path:'mycollect',name:"mycollect",component:MyCollect},
      {path:'myfriends',name:"myfriends",component:MyFriends},
      {path:'mypublish',name:"mypublish",component:MyPublish},
      {path: 'minelogin',name: 'minelogin',component:MineLogin},
    ]},
    //二级路由
    {path: '/lotindex',component:lotTwo,children:[
      {path: '',redirect:'lots',component:lots},
      {path: 'lots',name: 'lots',component:lots},
      {path: 'article',name: 'article',component:article},
      {path: 'picture',name: 'picture',component:picture},
      {path: 'news',name: 'news',component:news},
      {path: 'newPersonKnow',name: 'newPersonKnow',component:newPersonKnow},
      {path: 'newShopKnow',name: 'newShopKnow',component:newShopKnow},
      {path: 'newPlantKnow',name: 'newPlantKnow',component:newPlantKnow},
      {path: 'newDayKnow',name: 'newDayKnow',component:newDayKnow}
    ]
    },    
    {path:'/**',redirect:'/lotindex'}
  ]
//去掉路由前面#号
const router = new Router({
  routes,
  mode:'history'
})

//change title_know
router.beforeEach(function(to,from,next){
	
	let {name} = to
	let title = ''
	
	switch(name){
		case 'newPersonKnow':title='新人须知';break;
		case 'newShopKnow':title='交易须知';break;
    case 'newPlantKnow':title='种植知识';break;
    case 'newDayKnow':title='每日签到';break;
		default :title = '卖座电影';break;
	}
	store.commit('changeTitle_know',title)
	next()
})
//暴露路由模块
export default router