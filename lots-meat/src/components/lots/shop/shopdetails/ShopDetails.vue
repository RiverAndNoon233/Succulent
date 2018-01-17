<template>
    <div class="shopdetails style-box">
        <div class="head">
            <i class="yo-ico" @click="toshop">&#xe605;</i><span>商品详情</span>       
        </div>
        <div class="details-con">
            <mt-swipe class="box" :auto="3000">
                <mt-swipe-item v-for="(img,i) in imgUrl" :key="i"><img :src="img"></mt-swipe-item>
            </mt-swipe>
            <div class="content">
                <h1>{{datas.goods_name}}</h1>
                <p>￥{{datas.price}}</p>
                <p><span>快递:免运费</span><span><b>月销：700笔</b>上海</span></p>
                <div class="intro">
                    <h2>宝贝简介</h2>
                    <p>{{datas.introduction}}</p>
                </div>
            </div>
            <ul class="but-bottom">
                <li><button @click="addgood(detail_id)">加入购物车</button></li>
                <li><button>立即购买</button></li>
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
        }
        
    }    
</script>
<style lang="scss" scoped>
     .shopdetails{
         z-index:1;
         width:100%;
         height:100%;
         position:absolute;
         .details-con{
             overflow-y:auto;
            .box{ 
                width:100%;
                height:2.3rem;
                img{
                    width:100%;
                    height:2.3rem;
                }
            }
            .content{
                padding:.1rem .15rem;
                h1{
                    font-size:.2rem;
                }
                p:nth-of-type(2){
                    display:flex;
                    justify-content:space-between;
                }
                .intro{
                    min-height:.5rem;
                    padding:.1rem;
                    background:#04b10a;
                    color:#fff;
                    border-radius:.1rem;
                }
            }
            .but-bottom{
                display:flex;
                justify-content:space-between;
                padding:0 .15rem;
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
                        background:#04b10a;
                        color:#fff;
                        border-radius:.1rem;
                    }
                }
            }
         }
    }
</style>