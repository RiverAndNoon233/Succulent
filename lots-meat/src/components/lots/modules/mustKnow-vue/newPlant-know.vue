<template>
    <div class="newPlant-know">
         <router-view></router-view> 
       <new-head></new-head> 
       <div class="classify">
           <img src="/static/images/plant1.jpg"/>
           <div class="classify-zhe">
               <p>养护知识</p>
               <a @click="turntype(1)">点击查看</a>
           </div>
       </div>
       <div class="classify">
           <img src="/static/images/plant2.jpg"/>
           <div class="classify-zhe">
               <p>播种叶插繁殖</p>
               <a @click="turntype(2)">点击查看</a>
           </div>
       </div>
       <div class="classify">
           <img src="/static/images/plant3.jpg"/>
           <div class="classify-zhe">
               <p>修根移栽上盆</p>
               <a @click="turntype(3)">点击查看</a>
           </div>
       </div>
       <div class="classify">
           <img src="/static/images/plant4.jpg"/>
           <div class="classify-zhe">
               <p>病虫害防治</p>
               <a @click="turntype(4)">点击查看</a>
           </div>
       </div>
    </div>
</template>

<script>
 import NewHead from "./newHead-know"
    export default {
        name:"newPlant-know",
        components:{
           NewHead
        },
        methods:{
            turntype(plantnum){
                this.$router.push({path:'/lotindex/newPlantKnow/newPlantDetail',query:{"class":plantnum}});
            }
        }
    }        
</script>

<style lang="scss" scoped>
    .newPlant-know{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#ccc;
        .classify{
            width:100%;
            height:144px;
            margin-top:0.09rem;
            position: relative;
            img{
                width:100%;
                height:100%;
            }
            .classify-zhe{
                width:150px;
                height: 100%;
                position: absolute;
                top:0;
                right:0;
                background-color:rgba(0,0,0,0.3);
                text-align: center;
                p{
                    color:#fff;
                    font-size:16px;
                    margin-top:0.43rem;
                }
                a{
                    color:#fff;
                    font-size:14px;
                    margin-top:0.17rem;
                }
            }
        }
    }
</style>