<template>
    <div class="find-box">
       <find-nav></find-nav>
       <find-news-box></find-news-box>
    </div>
</template>

<script>
import FindNav from './find-nav.vue'
import FindNewsBox from './find-newsbox.vue'
    export default {
        name:"find-box",
        components:{
           FindNav,FindNewsBox
        }
    }        
</script>

<style lang="scss" scoped>
    .find-box{
      overflow-y: scroll;
    }
    
</style>