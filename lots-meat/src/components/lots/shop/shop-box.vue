<template>
    <div class="shop-box">
       <ul class="shops"
		  v-infinite-scroll="loadMore"
		  infinite-scroll-disabled="loading"
		  infinite-scroll-distance="8">
          <ShopBoxItem  v-for="shop in shops" :info='shop' :key='shop.gid'></ShopBoxItem>
        </ul>
    </div>
</template>

<script>
import bus from '../../../modules/bus'
import ShopBoxItem from './shop-boxItem'
import axios from 'axios'
import { Indicator } from 'mint-ui';
import { Toast } from 'mint-ui';
    export default {
        name:"shop-box",
        components:{ShopBoxItem},
        data(){
        	return {
        		type:1,
        		page:1,
        		shops:[],
        		loading:false,
        		isOver:false
        	}
        },
        methods:{
        	getShops(){
                let that = this
                let url = '/static/api/shops.json'
                //let url = '/api/v1/shop/showgoods'
        		//let params = {type:that.type,page:that.page}
        		//axios.get(url,{params}).then(res=>{
        		Indicator.open({
				  text: '客官请稍等...',
				  spinnerType: 'triple-bounce'
				});
        		axios.get(url).then(res=>{
        			
        			Indicator.close();
        			//console.log(res.data)
        			that.shops=that.shops.concat(res.data.data)
        			that.loading = false
        			if(that.page==res.data.pages){
        				that.isOver = true
        				Toast({
						  message: '没有更多数据',
						  position:'bottom'
						});
        				return false
        			}
                    that.page++
                    //console.log(that.shops)
        		})
        	},
        	loadMore() {
        	  if(this.isOver){
        	  	return false;
        	  }
			  this.loading = true;
			  this.getShops()
			},
			changeType(){
				this.page = 1
				this.shops = []
				this.isLoading = false
				this.isOver = false
				this.getShops()
			}
        },
        mounted(){
        	let that = this
        	bus.$on("change-type",(type)=>{
                that.type = type
        		that.changeType()
        	})
        }
    }       
</script>

<style>
    
</style>