<template>
    <div class="newShop-know">
       <new-head></new-head> 
       newShop-know
    </div>
</template>

<script>
 import NewHead from "./newHead-know"
    export default {
        name:"newShop-know",
        components:{
           NewHead
        }
    }        
</script>

<style lang="scss" scoped>
    .newShop-know{
        width:100%;
        height:100%;
        position:absolute;
        z-index:1000;
        background:#ccc;
    }
</style>