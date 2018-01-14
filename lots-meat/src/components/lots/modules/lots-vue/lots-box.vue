<template>
    <div class="lots-box">
       <p class="kong"></p>
       <h3>
           <span></span>
           最新热帖
        </h3>
        <lots-box-item :hotartical = "hotartical" v-for="hotartical in hotarticals" :key="hotartical.id"></lots-box-item>
    </div>
</template>

<script>
import axios from 'axios'
import LotsBoxItem from "./lots-boxItem"
export default {
    name:"lots-box",
    components:{
        LotsBoxItem
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

