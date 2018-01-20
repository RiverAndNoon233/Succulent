<template>
    <div class="lots-pingjia">
        <div class="find-head">
            <router-link :to="'/lotindex/lotBoxDetail'" tag="b" class="yo-ico">&#xe605;</router-link>
            <span>评价列表</span>
            <b></b>
        </div>
        <ul class="pingjia">
            <lots-pingjia-item :pingjia = "pingjia" v-for="pingjia in pingjias" :key="pingjia.comment_id"></lots-pingjia-item>
        </ul>
        <div class="pingjia-bottom">
          <input type="text" v-model="pushpingjia"></input>
          <i @click="pushing()">发送</i>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import LotsPingjiaItem from "./lots-pingjiaItem"
export default {
    name:"lots-pingjia",
     components:{
        LotsPingjiaItem
    },
     data(){
      return {
         pingjias:[],
         pushpingjia:"",
      }
    },
    methods:{
     getpingjia(){
         let that = this
         axios.get('/static/api/pingjia.json').then((res)=>{
             that.pingjias = res.data.data
         })

     },
     pushing(){
         console.log(this. pushpingjia)
         this.pingjias.push({
            "comment":this. pushpingjia,
            "user_name":"你好",
            "user_icon":"/static/images/find5.jpg",
            "comment_time":"2017-2-12",
            });
     }
  },
  created(){
      this. getpingjia()
  }
}        

</script>

<style lang="scss" scoped>
    .lots-pingjia{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#fff;
        display:flex;
        flex-direction: column;
        .find-head{
            width:100%;
            height:44px;
        }
        .pingjia{
            overflow-y: scroll;
        }
        .pingjia-bottom{
            position:fixed;
            width:350px;
            height:30px;
            bottom:0px;
            left:20px;
            display: flex;
            input{
                width:80%;
                height:100%;
            }
            i{
                width:18%;
                height:100%;
                display:inline-block;
                background:#ccc; 
                text-align:center;
                line-height: 30px;
            }
        }
    } 
</style>

