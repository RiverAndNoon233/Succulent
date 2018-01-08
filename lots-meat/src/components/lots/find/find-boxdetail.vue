<template>
    <div class="find-boxdetail">
      <detail-head></detail-head>
       boxdetail--{{$route.query.num}}
    </div>
</template>

<script>
import DetailHead from './find-detailhead.vue'
    export default {
        name:"find-boxdetail",
        components:{
           DetailHead
        },
       
    }        
</script>

<style lang="scss" scoped>
       .find-boxdetail{
            width:100%;
            height:100%;
            position:absolute;
            z-index:1000;
            background:#ccc;
        }
</style>