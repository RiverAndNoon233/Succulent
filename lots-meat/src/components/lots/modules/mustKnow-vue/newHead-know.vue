<template>
    <div class="newhead">
         <router-link :to="'/lotindex'"  tag="span" class="fa fa-chevron-left"> </router-link>
        <div class="newhead"><span>{{title_know}}</span></div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
    export default {
        name:"newhead",
        data(){
            return{

            }
        },
        computed:{
        	...mapState(['title_know'])
        },
    }       
</script>

<style lang="scss" scoped>
    .newhead{
        padding-left:0.01rem;
        width:100%;
        height:.44rem;
        background:#04b10a;
        display:flex;
        justify-content:center; 
        align-items: center;
        span{
            color:#fff;
        }
    }

</style>