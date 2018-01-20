<template>
    <div class="shop-list">
       <div class="shop-input">
           <input type="text" placeholder="搜索商品"/>
       </div>
       <ul class="shop-type">
           <li @click='type = 1' :class="[type==1 ? 'active' : '']">景天科</li>
           <li @click='type = 2' :class="[type==2 ? 'active' : '']">番杏科</li>
           <li @click='type = 3' :class="[type==3 ? 'active' : '']">仙人掌科</li>
           <li @click='type = 4' :class="[type==4 ? 'active' : '']">其他科目</li>           
       </ul>
    </div>
</template>

<script>
import bus from '../../../modules/bus'
    export default {
        name:"shop-list",
         data(){
        	return {
        		type:1,
        	}
        },
        watch:{
        	type(){
        		bus.$emit('change-type',this.type)
        	}
        }
    }        
</script>

<style lang="scss" scoped>
    .active{
        color:#04b10a;
        border-bottom:1px solid #04b10a;
    }
    .active1{
        color:#000;
        border-bottom:none;
    }
</style>