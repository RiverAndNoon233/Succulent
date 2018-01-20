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
import newPlantDetail from "@/components/lots/modules/mustKnow-vue/newPlantDetail"


import lotBoxDetail from "@/components/lots/modules/lots-vue/lots-boxDetail"
import lotPingjia from "@/components/lots/modules/lots-vue/lots-pingjia"

//以下一级路由。。
import lotTwo from '@/components/lots/lotTwo'
import Find from "@/components/lots/find/find"
import Shop from "@/components/lots/shop/shop"
import Mine from "@/components/lots/mine/Mine"
import ShopDetails from "@/components/lots/shop/shopdetails/ShopDetails.vue"
import SubOrder from "@/components/lots/mine/set/mycarlist/SubOrder.vue"

//未登陆和注册时路由
import MineLogin from "@/components/lots/mine/MineLogin"
import MineRegister from "@/components/lots/mine/MineRegister"
import MineLoginOn from "@/components/lots/mine/MineLoginOn"

//我的组件路由
import MyPublish from "@/components/lots/mine/minetop/MyPublish"
import MyCollect from "@/components/lots/mine/minetop/MyCollect"
import MyCar from "@/components/lots/mine/set/MyCar"
import MyModifyEmail from "@/components/lots/mine/set/MyModifyEmail"
import MyOrderForm from "@/components/lots/mine/set/MyOrderForm"
import MyResetpass from "@/components/lots/mine/set/MyResetpass"
import MyWallet from "@/components/lots/mine/set/MyWallet"
//发现里面的二级路由
import FindBoxDetail from "@/components/lots/find/Find-boxdetail"
import FindWritePublish from "@/components/lots/find/find-writepublish"
import FindSearch from "@/components/lots/find/find-search"


//以下钱包路由
import ReCharge from "@/components/lots/mine/set/wallet/ReCharge"
import WithDraw from "@/components/lots/mine/set/wallet/WithDraw"

Vue.use(Router)

import store from '../vuex/store'

const routes = [
    {path:'/',redirect:'/lotindex'},
    
    {path:"/find-fo",name:'find-fo',component:Find,children:[
      {path:"FindBoxDetail",name:"FindBoxDetail",component:FindBoxDetail},
      {path:"FindWritePublish",name:"FindWritePublish",component:FindWritePublish},
      {path:"FindSearch",name:"FindSearch",component:FindSearch}
    ]},
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
      {path: 'mineregister',name: 'mineregister',component:MineRegister},      
      {path:'mycollect',name:"mycollect",component:MyCollect},
      {path:'mypublish',name:"mypublish",component:MyPublish},
      {path: 'minelogin',name: 'minelogin',component:MineLogin},
      {path: 'mycar',name: 'mycar',component:MyCar},
      {path: 'mymodifyemail',name: 'mymodifyemail',component:MyModifyEmail},
      {path: 'myorderfrom',name: 'myorderfrom',component:MyOrderForm},
      {path: 'myresetpass',name: 'myresetpass',component:MyResetpass},
      {path: 'mywallet',name: 'mywallet',component:MyWallet},
      {path: 'recharge',name: 'recharge',component:ReCharge},
      {path: 'withdraw',name: 'withdraw',component:WithDraw},      
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
      {path: 'newPlantKnow',name: 'newPlantKnow',component:newPlantKnow,children:[
           {path: 'newPlantDetail',name: 'newPlantDetail',component:newPlantDetail}
      ]},
      {path: 'newDayKnow',name: 'newDayKnow',component:newDayKnow},
      {path: 'lotBoxDetail',name: 'lotBoxDetail',component:lotBoxDetail,children:[
           {path: 'lotPingjia',name: 'lotPingjia',component:lotPingjia}
      ]},
    ]
    },
    {path:"/shopdetails:_id",name:"shopdetails",component:ShopDetails},
    {path:"/suborder",name:"suborder",component:SubOrder},
    {path:'/**',redirect:'/lotindex'}
  ]
//去掉路由前面#号
const router = new Router({
  routes,
  mode:'history'
})

//change title_know
router.beforeEach(function(to,from,next){
  let num = to.query.num;
	let {name} = to
	let title = ''
  let type=""
  
	switch(name){
		case 'newPersonKnow':title='新人须知';break;
		case 'newShopKnow':title='肉多多交易购买';break;
    case 'newPlantKnow':title='种植知识';break;
    case 'newDayKnow':title='多多小助手';break;
		default :title = '多多';break;
  }
  switch(num){
    case 1:type='景天科';break;
    case 2:type='仙人掌科';break;
    case 3:type='番杏科';break;
    case 4:type='百合科';break;
    default :type = '多多';break;
  }
  store.commit('changeTitle_know',title)
  store.commit('changeType',type)
	next()
})

router.beforeEach(function(to,from,next){
  
  if(!localStorage.user_info){
    if(to.name=="mineloginon"){
        location.href="/mine-fo/minelogin"
    }
  }
	next()
})
//暴露路由模块
export default router