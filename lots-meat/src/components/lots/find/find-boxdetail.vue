<template>
    <div class="find-boxdetail">
       <div class="detail-head">
        <detail-head></detail-head>
      </div>
      <div class="find-detailbox">
        <div class="find-top">
             {{detail_type}}

        </div>
        <div class="find-Item">
            <find-news-box-item :newItem = "newItem" v-for="newItem in news" :key="newItem.id"></find-news-box-item>
        </div>
     </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import DetailHead from './find-detailhead.vue'
import FindNewsBoxItem from "./find-newsboxItem"
import axios from 'axios'
    export default {
        name:"find-boxdetail",
        components:{
           DetailHead,FindNewsBoxItem
        },
        data(){
            return {
                news:[]
            }
        },
        computed:{
        	...mapState(['detail_type'])
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
      .detail-head{
          height:44px;
      }
</style>