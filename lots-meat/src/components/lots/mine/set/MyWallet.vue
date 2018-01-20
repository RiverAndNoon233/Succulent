<template>
    <!--钱包组件-->
    <div class="my-wallet">
        <div class="wallet-top">
            <p><i class="yo-ico" @click="tologinon">&#xe605;</i><span>我的钱包</span><i></i></p>
            <p>账户可用余额</p>
            <p>￥<span>0.00</span></p>
            <div><button @click="torecharge">提现</button><button @click="towithdraw">充值</button></div>
        </div>
        <div class="wallet-bot">
            <p><span>冻结金额</span><span>￥0.00</span></p>
        </div>
            <p class="wallet-det"><span>账户明细</span></p>
    </div>
</template>
<script>
export default{
    name:"my-wallet",
    methods:{
        tologinon(){
            this.$router.replace({name:'mineloginon'})  
        },
        torecharge(){
            this.$router.replace({name:'recharge'})  
        },
        towithdraw(){
            this.$router.replace({name:'withdraw'})  
        }
    }
}    
</script>
<style lang="scss" scoped>
    .my-wallet{
        position:absolute;
        width:100%;
        height:100%;
        background:#fff;
        z-index:1;
        background:#d8d8d8;
        .wallet-top{
            width:100%;
            height:2.5rem;
            background:#04b10a;
            color:#fff;
            padding:.1rem;
            p{
                display:flex;
                justify-content:center;
            }
            p:nth-of-type(1){
                display:flex;
                justify-content:space-between;

                span{
                    line-height:.26rem;
                }
            }
            p:nth-of-type(2){
                padding-top:.5rem;
                font-size:.16rem;
            }
            p:nth-of-type(3){
                padding-top:.25rem;
                font-size:.14rem;
            }
            div{
                display:flex;
                justify-content:space-between;
                padding:.2rem .8rem;
                button{
                    width:.55rem;
                    height:.25rem;
                    border-radius:.03rem;
                    border:1px solid #fff;
                    background:#04b10a;
                    
                }
            }
        }
        .wallet-bot{
            width:100%;
            height:.6rem;
            border-top:.1rem solid #d8d8d8;
            border-bottom:.1rem solid #d8d8d8;
            line-height:.4rem;
            padding:0 .1rem;
            background:#fff;
            p{
                display:flex;
                justify-content:space-between;
                span:nth-of-type(2){
                    color:red;
                }
            }
        }
        .wallet-det{
            width:100%;
            height:.6rem;
            border-top:.1rem solid #d8d8d8;
            border-bottom:.1rem solid #d8d8d8;
            line-height:.4rem;
            padding:0 .1rem;
            background:#fff;
        }
    }
</style>