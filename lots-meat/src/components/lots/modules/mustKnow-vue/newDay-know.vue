<template>
    <div class="newDay-know">
        <div class="robot-head">
            <new-head></new-head> 
        </div>
        <div class="talk">
            <div class="talk_left">
                <ul>
                    <li v-for="(robot_talk,i) in robot_talk" :key="i">
                        <img src="/static/images/robot.jpg"/>
                        <span>{{robot_talk}}</span>
                    </li>
                </ul>
            </div>
            <div class="talk_right">
                <ul>
                    <li v-for="(pushcontent,i) in pushcontent" :key="i">
                        <img src="/static/images/find5.jpg"/>
                        <span>{{pushcontent}}</span>   
                    </li>
                </ul>
            </div>
        </div>
         <div class="pingjia-bottom">
            <input type="text" v-model="pushitem"></input>
            <i @click="pushing()">发送</i>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
 import NewHead from "./newHead-know"
    export default {
        name:"newDay-know",
        components:{
            NewHead
        },
     data(){
      return{
         pushitem:"",
         pushcontent:[],
         robot_item:"",
         robot_talk:[],  
      }
    },
    methods:{   
     pushing(){
         let that = this
         let params = this.pushcontent
         that.pushcontent.push(that.pushitem)
         that.pushitem = ''
         axios.get('/static/api/pushcontent.json',params).then((res)=>{
             if(res.data.code == 200){
                 that.robot_item = res.data.data[0].robot_talk
                 that.robot_talk.push(that.robot_item)
             } 
        })
     }
  }
}        
</script>


<style lang="scss" scoped>
    .newDay-know{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#fff;
         display: flex;
         flex-direction: column;
         .robot-head{
             height:44px;
         }
        .talk{
            width:100%;
            overflow-y: scroll;
            display: flex;
            justify-content: space-between;
            padding:5px 10px 0 10px;
            .talk_left{
                width:48%;
               // background:red;
                margin-top:30px;
                li{
                    vertical-align: middle;
                     margin-bottom:50px;
                    img{
                        width:30px;
                        height:30px;  
                    }
                    span{
                        background:#ccc;
                        display:inline-block;
                        border-radius: 5px;
                    }
                 }
                
            }
            .talk_right{
                width:48%;
                position: relative;
                 li{
                    vertical-align: middle;
                     margin-bottom:50px;
                     display: flex;
                     flex-direction: row-reverse;
                     img{
                        width:30px;
                        height:30px;
                    }
                    span{
                        background:#ccc;
                        border-radius: 5px;
                        display:inline-block;
                        margin-right:5px;
                    }
                 }
                 
            }
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