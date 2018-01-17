const mutations = {
    change_type(state,user_info){
        state.user_info = user_info
        localStorage.user_info = JSON.stringify(user_info)
    },
    initLogin(state,data){
        state.LoginOnData=data
    },
    changeTitle_know(state,title){
    	state.title_know = title
    },
    changeFind_type(state,type){
        state.find_type = type;
    },
    changeType(state,type){
        state.detail_type = type;
    },
    
    addGood(state,res){
        state.car = res
        localStorage.car = JSON.stringify(state.car)
        // let isHas = state.shopCars.some((item)=>{//判断购物车中是否含有当前的商品
		// 	if(item.goods_id == params.goods_id){	
		// 		item.num ++;		
		// 		return true;		
		// 	}else{		
		// 		return false;
		// 	}	
		// });
		// if(!isHas){	
		// 	params.num = 1;	
		// 	state.shopCars.push(params)
		// }
		// //与数据库数据同步一下
		// localStorage.shopCars = JSON.stringify(state.shopCars);
    },
    addGid(state,gid){
        state.gid = gid
    },
    removeGood(state,id){
        let leng = state.car.length
        console.log(id.id)
        for(var i=0;i<leng;i++){
            if(state.car[i].gid == id.id){
                state.car.splice(i,1)
                break;
            }
        }
        localStorage.car = JSON.stringify(state.car)
    },
    changepri(state,num){
        state.carprice = num
    }
}
export default mutations