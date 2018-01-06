<template>
    <div class="artical-box">
        
        <artical-box-item :hotartical = "hotartical" v-for="hotartical in hotarticals" :key="hotartical.id"></artical-box-item>
    </div>
</template>

<script>
import axios from 'axios'
import ArticalBoxItem from "./artical-boxItem"
export default {
    name:"artical-box",
    components:{
        ArticalBoxItem
    },
    data(){
      return {
          hotarticals:[]
      }
    },
    methods:{
     gethotartical(){
         let that = this
         axios.get('/static/api/hotartical.json').then((res)=>{
             that.hotarticals = res.data
         })
     }  
  },
  created(){
      this. gethotartical()
  }
}        
</script>

<style lang="scss" scoped>
    
</style>

