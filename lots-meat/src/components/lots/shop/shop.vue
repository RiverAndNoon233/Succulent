<template>
    <div class="shop">
        <div class="shophead">
            <shop-head></shop-head>
        </div>
        <shop-list></shop-list>
        <shop-box></shop-box>
    </div>
</template>

<script>
import ShopHead from './shop-head.vue'
import ShopList from './shop-list.vue'
import ShopBox from './shop-box.vue'
    export default {
        name:"shop",
         components:{
           ShopHead,ShopList,ShopBox
        }
    }        
</script>

<style lang="scss" scoped>
    .shopheade{
        height:44px;
    }
</style>