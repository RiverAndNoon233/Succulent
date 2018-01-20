<template>
    <div class="shopdetails">
        <div class="details-con">
            <div class="lunbo">
                <mt-swipe class="box" :auto="3000">
                    <mt-swipe-item v-for="(img,i) in imgUrl" :key="i"><img :src="img"></mt-swipe-item>
                    
                </mt-swipe>
                <div class="rou"><i class="yo-ico" @click="toshop">&#xe605;</i></div>
            </div>
            <div class="content">
                <div class="con-top">
                    <h1>{{datas.goods_name}}</h1>

                    <p><i>￥</i>{{datas.price}}</p>
                    <p>原价:￥{{datas.price+10}}</p>
                    <p><span>快递:免运费</span><b>月销：700笔</b><span>上海</span></p>
                </div>
                <div class="intro">
                    <h2>宝贝简介</h2>
                    <p>{{datas.introduction}}</p>
                </div>
            </div>
            <ul class="but-bottom">
                <li><button @click="addgood(detail_id)">加入购物车</button></li>
                <li><button @click="tosubo">立即购买</button></li>
            </ul>
        </div>
    </div>
</template>
<script>
import axios from "axios"
import {mapActions} from "vuex"
import {Toast} from 'mint-ui'

    export default {
        name:"shopdetails",
        data(){
            return{
                detail_id:'',
                imgUrl:[],
                datas:'',
            }
        },
        created(){
            this.detail_id = this.$route.params._id
            this.getData()
        },
        methods:{
            getData(){
                axios.get("/static/api/details.json",{params:{gid:this.detail_id}}).then((res)=>{
                    this.imgUrl =  res.data.image
                    this.datas = res.data
                })
            },
            // submitForm (gid) {
            //     //  this.$store.commit("addGid",gid)
            //      this.$store.dispatch('addGood')
            // }
            addgood(id){
                console.log(id)
                axios.get("/static/api/addcar.json",{params:{gid:id,ad:1}}).then((res)=>{
                    console.log(res)
                    if(res.data == 0){
                        Toast({
                            message: '用户未登陆',
                            position: 'bottom',
                            duration: 1000
                        })
                    }else if(res.data == 1){
                        Toast({
                            message: '加入成功',
                            position: 'bottom',
                            duration: 1000
                        })
                    }
                })
            },
            toshop(){
                this.$router.replace({name:'shop-fo'})  
            },
            tosubo(){
                this.$router.replace({name:'suborder'})  
            },
        }
        
    }    
</script>
<style lang="scss" scoped>
     .shopdetails{
         z-index:1;
         width:100%;
         height:100%;
         position:absolute;
         background:#fff;
         overflow-y:auto;
         padding-bottom:.5rem;
         .details-con{
            .lunbo{
                position:relative;
                .box{ 
                    width:100%;
                    height:3.67rem;
                    img{
                        width:100%;
                        height:3.67rem;
                    }
                }
                .rou{
                    position:absolute;
                    top:.1rem;
                    left:.1rem;
                    i{
                        display:inline-block;
                        width:.3rem;
                        height:.3rem;
                        border-radius:.15rem;
                        border:.02rem solid #fff;
                        text-align:center;
                        line-height:.25rem;
                        color:#fff;
                    }
                }
            }
            
            .content{
                .con-top{
                    padding:.1rem .15rem;
                    border-bottom:.1rem solid #d8d8d8;
                    h1{
                        font-size:.16rem;
                        padding-bottom:.26rem;
                    }
                    p{
                        color:#999999;
                    }
                    p:nth-of-type(1){
                        font-size:.13rem;
                        color:red;
                        font-weight:1000;
                        i{
                            font-size:.06rem;
                        }
                    }
                    p:nth-of-type(2){
                        text-decoration:line-through;
                        line-height:.3rem;
                    }
                    p:nth-of-type(3){
                        display:flex;
                        justify-content:space-between;
                        b{
                            font-weight:normal;
                        }
                    }
                }
                .intro{
                    min-height:.5rem;
                    padding:.1rem .2rem;
                    color:#999999;
                    h2{
                        color:#666666;
                    }
                    p{
                        padding:.1rem .05rem 0 .25rem;
                        line-height:.25rem;
                    }
                }
            }
            .but-bottom{
                display:flex;
                justify-content:space-between;
                position:fixed;
                bottom:0;
                width:100%;
                li{
                    flex:1;
                    height:.5rem;
                    button{
                        width:100%;
                        height:100%;
                        border:none;
                        background:#fff;
                        color:#04b10a;
                        font-size:.15rem;
                        font-weight:bold;
                    }
                }
                li:nth-of-type(2){
                    button{
                        background:#04b10a;
                        color:#fff;
                    }
                }
                li{
                    button:active{
                        color:#fff;
                        background:#04b10a;
                    }
                }
            }
         }
    }
</style>