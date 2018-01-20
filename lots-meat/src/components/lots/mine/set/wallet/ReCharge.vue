<template>
    <div class="recharge style-box">
        <div class="head">
            <i class="yo-ico" @click="tomywallet">&#xe605;</i><span>充值</span>       
        </div>
        <div class="content">
            <p><span>充值金额</span><input type="text" placeholder="请输入充值金额，最少10元"/></p>
            <p>支付方式</p>
            <div><img src="/static/images/wx.jpg"/><span>微信</span></div>           
            <div><img src="/static/images/zfb.jpg"/><span>支付宝</span></div>           
            <div><button>确认</button></div>
        </div>
    </div>
</template>
<script>
//充值

    export default{
        name:"recharge",
        methods:{
            tomywallet(){
                this.$router.replace({name:'mywallet'})  
            }
        }
    }
</script>
<style lang="scss" scoped>
    .recharge{
        z-index:1;
        background:#ccc;
        .content{
            p{
                padding-left:.1rem;
            }
            
            p:nth-of-type(1){
                height:.45rem;
                background:#fff;
                margin:.1rem 0;
                line-height:.45rem;
                input{
                    margin-left:.1rem;
                    border:none;
                }
            }
            p:nth-of-type(2){
                height:.35rem;
                background:#fff;        
                line-height:.35rem;        
            }
            div{
                height:.27rem;
                background:#fff; 
                margin-top:1px;  
                line-height:.27rem;    
                padding-left:.1rem;                         
                img{
                    width:.2rem;
                    height:.2rem;
                    
                }          
                span{
                    margin-left:.1rem;
                }      
            }
            div:nth-of-type(3){
                width:100%;
                padding:.2rem .1rem 0 .1rem;
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