<template>
    <!--钱包组件-->
    <div class="my-wallet">
        <div class="wallet-top">
            <p><i class="yo-ico" @click="tologinon">&#xe605;</i></p>
            <p>账户可用余额</p>
            <p>￥<span>0.00</span></p>
            <div><button>提现</button><button>充值</button></div>
        </div>
        <div class="wallet-bot">
            <p>冻结金额</p>
        </div>
    </div>
</template>
<script>
export default{
    name:"my-wallet",
    methods:{
        tologinon(){
            this.$router.replace({name:'mineloginon'})  
        },
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
        .wallet-top{
            width:100%;
            height:2.2rem;
            background:#04b10a;
            color:#fff;
            padding:.1rem;
            p{
                display:flex;
                justify-content:center;
            }
            p:nth-of-type(1){
                display:flex;
                justify-content:left;
            }
            p:nth-of-type(2){
                padding-top:.3rem;
                font-size:.2rem;
            }
            p:nth-of-type(3){
                padding:0;
                font-size:.3rem;
            }
            div{
                display:flex;
                justify-content:center;
                padding:.2rem 0;
                button{
                    width:.9rem;
                    height:.45rem;
                    border-radius:.1rem;
                    border:1px solid #fff;
                    background:#04b10a;
                    margin-left:.2rem;
                }
            }
        }
        .wallet-bot{
            width:100%;
            height:.6rem;
            border-top:.1rem solid #ccc;
            border-bottom:.1rem solid #ccc;
            line-height:.4rem;
            padding:0 .1rem;
        }
    }
</style>