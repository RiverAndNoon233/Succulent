<template>
    <div class="newDay-know">
        <new-head></new-head> 
        newDay-know
    </div>
</template>

<script>
 import NewHead from "./newHead-know"
    export default {
        name:"newDay-know",
        components:{
            NewHead
        }
    }        
</script>

<style lang="scss" scoped>
    .newDay-know{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#ccc;
    }
</style>