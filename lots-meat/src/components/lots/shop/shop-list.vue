<template>
    <div class="shop-list">
       <div class="shop-input">
           <input type="text" placeholder="搜索商品"/>
       </div>
       <ul class="shop-type">
           <li @click='type = 1'>景天科</li>
           <li @click='type = 2'>番杏科</li>
           <li @click='type = 3'>仙人掌科</li>
           <li @click='type = 4'>其他科目</li>           
       </ul>
    </div>
</template>

<script>
import bus from '../../../modules/bus'
    export default {
        name:"shop-list",
         data(){
        	return {
        		type:1
        	}
        },
        watch:{
        	type(){
        		bus.$emit('change-type',this.type)
        	}
        }
    }        
</script>

<style>
    
</style>