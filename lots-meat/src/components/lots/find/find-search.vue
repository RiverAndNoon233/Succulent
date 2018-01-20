<template>
    <div class="find-search">
       <div class="find-head">
          <router-link :to="'/find-fo'" tag="b" class="yo-ico">&#xe605;</router-link>
          <span>帖子</span>
          <b></b>
      </div>
      <div class="search-box">
        <div class="input-search">
          <input type="text" placeholder="请输入搜索关键字" v-model="searchkey"></input>
          <i class="yo-ico" @click="search">&#xe60b;</i>
        </div>
        <lots-box-item :hotartical = "hotartical" v-for="hotartical in data" :key="hotartical.id"></lots-box-item>
      </div>
    </div>
</template>

<script> 
import axios from 'axios'
import LotsBoxItem from "../modules/lots-vue/lots-boxItem"
export default {  
  name:"find-search",
  components:{
        LotsBoxItem
  },
  data(){
    return{
      searchkey:'',
      data:''
    }
  },
    methods:{
      search(){
        let that = this
        let url = '/static/api/hotartical.json'
        let params = {page:1,words:that.searchkey}
          axios.get(url,{params}).then(res=>{
            that.data=res.data
            console.log(that.data)
          })
      }
    }
}  
</script>         


<style lang="scss" scoped>
 .find-search{
    width:100%;
    height:100%;
    position:absolute;
    z-index:1000;
    background:#fff;
 }
</style>