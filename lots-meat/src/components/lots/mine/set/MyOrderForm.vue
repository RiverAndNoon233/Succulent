<template>
    <!--订单组件-->
    <div class="my-order-from style-box">
        <div class="head">
            <i class="yo-ico" @click="tologinon">&#xe605;</i><span>买家中心</span>       
        </div>
        <div class="user">
            <img src="/static/images/10.jpg"/>
            <p>用户名:{{nick}}</p>
        </div>
        <ul class="nav-top">
            <li v-for="nav in navs" :key="nav.id"><i class="yo-ico" v-html="nav.icon">{{nav.icon}}</i><span>{{nav.content}}</span></li>
        </ul>
        <ul>
            <router-link :to="set.name" v-for="set in sets" :key="set.id" tag="li"><i class="yo-ico" v-html="set.icon">{{set.icon}}</i><span>{{set.content}}</span><span class="yo-ico">&#xe503;</span></router-link>
        </ul>
    </div>
</template>
<script>
    export default{
        name:"my-order-from",
        data(){
            return {
                navs:[
                    {id:1,content:"待付款",icon:'&#xe610;'},          
                    {id:2,content:"待发货",icon:"&#xe640;"},          
                    {id:3,content:"待签收",icon:"&#xe610;"},           
                    {id:4,content:"待评价",icon:"&#xe611;"},           
                ],
                sets:[
                    {id:1,content:"购物车",name:"/mine-fo/mycar",icon:'&#xe618;'},          
                    {id:2,content:"我的钱包",name:"/mine-fo/mywallet",icon:"&#xe502;"},          
                    {id:3,content:"收货地址",name:"",icon:"&#xe64e;"},                                        
                ],
                nick:'',
            }
        },
        mounted(){
            this.nick = JSON.parse(localStorage.user_info).username
        },
        methods:{
            tologinon(){
                this.$router.replace({name:'mineloginon'})  
            }
        }
    }    
</script>
<style lang="scss" scoped>
    .my-order-from{
        z-index:1;
        .user{
            width:100%;
            height:.9rem;
            display:flex;
            justify-content:space-between;
            padding:.1rem .2rem;
            border-bottom:.1rem solid #ccc;
            img{
                width:.6rem;
                height:.6rem;
                border-radius:.3rem;
            }
            p{
                flex:1;
                line-height:.6rem;
                padding-left:.2rem;
            }
        }
        ul:nth-of-type(1){
            display:flex;
            height:1rem;
            li{
                flex:1;
                text-align:center;
                i{
                    display:block;
                    font-size:.4rem;
                    color:#04b10a;
                    padding-top:.05rem;
                }
                span{
                    display:inline-block;
                    padding-top:.05rem;
                    font-size:.16rem;
                    color:#04b10a;
                }
            }
        }
        ul:nth-of-type(2){
            width:100%;
            border-top:.2rem solid #ccc;
            li{
                height:.5rem;
                display:flex;
                justify-content:space-between;
                padding:0 .1rem;
                line-height:.5rem;
                span:nth-of-type(2){
                    display:inline-block;
                    width:.2rem;
                }
                i{
                    font-size:.2rem;
                    height:.25rem;
                    width:.25rem;
                    margin-top:.1rem;
                    line-height:.26rem;
                    background:#03ab1a;
                    border-radius:.03rem;
                    text-align:center;
                    color:#fff;
                }
                span:nth-of-type(1){
                    flex:1;
                    padding-left:.2rem;
                }
            }
        }
    }
</style>