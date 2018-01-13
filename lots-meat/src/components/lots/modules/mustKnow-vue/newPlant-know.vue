<template>
    <div class="newPlant-know">
       <new-head></new-head> 
       newPlant-know
    </div>
</template>

<script>
 import NewHead from "./newHead-know"
    export default {
        name:"newPlant-know",
        components:{
           NewHead
        }
    }        
</script>

<style lang="scss" scoped>
    .newPlant-know{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#ccc;
    }
</style>