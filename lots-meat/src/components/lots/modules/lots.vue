<template>
    <div class="router-items">
        <!-- <router-view></router-view> -->
        <LotsBanner></LotsBanner>
        <lots-nav></lots-nav>
        <lot-box></lot-box>
    </div>
</template>

<script>
import LotsBanner from "./lots-vue/lots-banner"
import LotsNav from "./lots-vue/lots-nav"
import LotBox from "./lots-vue/lots-box"
    export default {
        name:"router-items",
         components:{
           LotsBanner,LotsNav,LotBox
        }
    }        
</script>

<style>
    
</style>