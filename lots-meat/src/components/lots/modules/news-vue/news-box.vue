<template>
    <div class="news-box">
        <news-box-item :newartical = "newartical" v-for="newartical in newarticals" :key="newartical.id"></news-box-item>
    </div>
</template>

<script>
import axios from 'axios'
import newsBoxItem from "./news-boxItem"
export default {
    name:"news-box",
    components:{
        newsBoxItem
    },
    data(){
      return {
          newarticals:[]
      }
    },
    methods:{
     getnews(){
         let that = this
         axios.get('/static/api/news.json').then((res)=>{
             that.newarticals = res.data
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

