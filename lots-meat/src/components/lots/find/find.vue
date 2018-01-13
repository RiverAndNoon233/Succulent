<template>
    <div class="find-to">
        <router-view></router-view>
        <div class="header">
             <find-head></find-head>
        </div>
        <find-box></find-box>
        <!-- <router-view></router-view> -->
    </div>
</template>

<script>
import FindHead from './find-head.vue'
import FindBox from './find-box.vue'
    export default {
        name:"find-fo",
        components:{
           FindHead,FindBox 
        }
    }        
</script>

<style lang="scss" scoped>
    .header{
        height:44px;
    }
</style>