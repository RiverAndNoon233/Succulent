<template>
    <div class="my-publish style-box">
         <div class="head">
            <i class="yo-ico" @click="tologinon">&#xe605;</i><span>我的发表</span>       
        </div>
        <div class="Publish">
            <Publish></Publish>
            <Publish></Publish>
            <Publish></Publish>
            <Publish></Publish>
            <Publish></Publish>
            <Publish></Publish>
        </div>
    </div>
</template>
<script>
import Publish from "./Publish.vue"
    export default {
        name:"my-publish",
        methods:{
            tologinon(){
                this.$router.replace({name:'mineloginon'})  
            },
        },
        components:{
            Publish
        },

    }
</script>
<style lang="scss" scoped>
    .my-publish{
        z-index:1;
        .Publish{
            flex:1;
            overflow-y:auto;
        }
    }
</style>