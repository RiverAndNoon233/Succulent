<template>
    <div class="withdraw style-box">
        <div class="head">
            <i class="yo-ico" @click="tomywallet">&#xe605;</i><span>购物车</span>       
        </div>
        <div class="content">
            <p>当前账户可提现金额<span>0.00</span></p>
            <p><span>提现金额</span><input type="text" placeholder="请输入提现金额，最少10元"/></p>
            <p>暂时仅支持提现至账号绑定的支付宝账号，手续费1%，提现处理将在3日内完成，遇节假日顺延</p>
            <div><button>确认</button></div>
        </div>
    </div>
</template>
<script>
    export default{
        name:"withdraw",
        methods:{
            tomywallet(){
                this.$router.replace({name:'mywallet'})  
            }
        }
    }
</script>
<style lang="scss" scoped>
    .withdraw{
        z-index:1;background:#ccc;
        .content{
            p{
                padding:0 .2rem;
            }
            p:nth-of-type(1){
                height:.55rem;
                line-height:.55rem;
            }
            p:nth-of-type(2){
                height:.45rem;
                background:#fff;
                line-height:.45rem;
                input{
                    margin-left:.1rem;
                    border:none;
                }
            }
            p:nth-of-type(3){
                font-size:.1rem;
                padding:.1rem .2rem;
            }
            div{
                width:100%;
                padding:0 .1rem 0 .1rem;
                background:#ccc; 
                button{
                    width:100%;
                    height:.4rem;
                    background:#03ab1a;
                    color:#fff;
                    border-radius:.06rem;
                    border:none;
                } 
            }
        }
    }
</style>