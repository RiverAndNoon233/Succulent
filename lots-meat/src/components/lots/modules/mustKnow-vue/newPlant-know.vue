<template>
    <div class="newPlant-know">
       <new-head></new-head> 
       <div class="classify">
           <img src=""/>
           <div class="classify-zhe">
               <p>养护知识</p>
               <a href="">点击查看</a>
           </div>
       </div>
       <div class="classify">
           <img src=""/>
           <div class="classify-zhe">
               <p>养护知识</p>
               <a href="">点击查看</a>
           </div>
       </div>
       <div class="classify">
           <img src=""/>
           <div class="classify-zhe">
               <p>养护知识</p>
               <a href="">点击查看</a>
           </div>
       </div>
       <div class="classify">
           <img src=""/>
           <div class="classify-zhe">
               <p>养护知识</p>
               <a href="">点击查看</a>
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
            margin-top:0.05rem;
            background:red;
            position: relative;
            .classify-zhe{
                width:150px;
                height: 100%;
                position: absolute;
                top:0;
                right:0;
                background:#333;
                transform: 0.5;
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