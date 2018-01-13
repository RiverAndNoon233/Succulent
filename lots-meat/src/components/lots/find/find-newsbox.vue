<template>
    <div class="find-newsbox">
        <h3>
           <span></span>
           最新资讯
        </h3>
        <ul class="find-newsboxItem">
            <find-news-box-item :newItem = "newItem" v-for="newItem in news" :key="newItem.id"></find-news-box-item>
        </ul>
    </div>
</template>

<script>
import FindNewsBoxItem from "./find-newsboxItem"
import axios from 'axios'
    export default {
        name:"find-newsbox",
         components:{
            FindNewsBoxItem
        },
        data(){
            return {
                news:[]
            }
        },
         methods:{
            getnews(){
                let that = this
                axios.get('/static/api/find.json').then((res)=>{
                    that.news = res.data
                    //console.log(that.news);
                })
            }  
        },
        created(){
            this. getnews()
        }
    }        
</script>

<style lang="scss" scoped>
 
</style>