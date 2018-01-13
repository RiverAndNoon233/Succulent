<template>
    <div class="newPerson-know">
         <new-head></new-head> 
           newPerson-know
    </div>
</template>

<script>
    import NewHead from "./newHead-know"
    export default {
        name:"newPerson-know",
         components:{
          NewHead
        }
    }        
</script>

<style lang="scss" scoped>
    .newPerson-know{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#ccc;
    }
</style>