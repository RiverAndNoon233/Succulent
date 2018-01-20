<template>
    <div class="newPlantDetail">
         <div class="find-head">
            <router-link :to="'/lotindex/newPlantKnow'"  tag="b"  class="yo-ico">&#xe605;</router-link>
            <span>养护知识</span>
            <i></i>
        </div>
        <ul>
             <lots-box-item :hotartical = "hotartical" v-for="hotartical in hotarticals" :key="hotartical.id"></lots-box-item>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
import LotsBoxItem from "../lots-vue/lots-boxItem"
    export default {
        name:"newPlantDetail",
        components:{
            LotsBoxItem
        },
         data(){
            return {
                hotarticals:[]
            }
        },
        methods:{
            getPlant(){
                let that = this
                axios.get('/static/api/hotartical.json').then((res)=>{
                    that.hotarticals = res.data
                })
            }
        },
        created(){
            this. getPlant()
        }
    }       
</script>

<style lang="scss" scoped>
    .newPlantDetail{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#fff;
        
    }
</style>