<template>
    <div class="find-detailhead">
        <router-link :to="'/find-fo'"  tag="span" class="yo-ico">&#xe605;</router-link>
        <div class="find-detailhead"><span>{{detail_type}}</span></div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
    export default {
        name:"find-detailhead",
        computed:{
        	...mapState(['detail_type'])
        },
    }        
</script>

<style lang="scss" scoped>
    .find-detailhead{
       
    }
    
</style>