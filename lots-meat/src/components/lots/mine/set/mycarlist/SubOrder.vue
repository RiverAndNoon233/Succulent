<template>
    <div class="sub-order style-box">
        <div class="head">
        <i class="yo-ico" @click="tocar">&#xe605;</i><span></span>       
        </div>
        <div class="content-box">
            <div class="content">
                <div class="cont-top">
                    <img src="/static/images/图层1.png"/>
                    <div>
                        <p><span>收货人:二哈先生</span><span>17611112548</span></p>
                        <p>收货地址:河南省大兴市哒哒区哒哒街道三公路康泰路景秀花园北门东100米</p>
                    </div>
                </div>
            </div>
            <MyOrderList/>
            <div class="leave">
                <p><span>购买数量</span><b><b>+</b><span>1</span><b>-</b></b></p>
                <p><span>不支持七天无理由退款</span></p>
                <p><span>配送方式</span><span>快递 免邮</span></p>
                <p><span>配送时间</span><span>23.00前付款,承诺2月21日送达</span></p>
                <p><span>买家留言</span><input type="text" placeholder="选填：填写内容已和卖家协商确认"/></p>            
            </div>
        </div>
        <div class="footer">
            <div>
                <span>合计:9.9</span>
                <span>提交订单</span>
            </div>
        </div>
    </div>
</template>
<script>
import MyOrderList from "./MyOrderList"
export default {
    name:"sub-order",
    components:{
        MyOrderList
    },
    methods:{
        tocar(){
            this.$router.replace({name:'mycar'}) 
        }
    }
}
</script>
<style lang="scss" scoped>
    .sub-order{
        z-index:1;
        .content-box{
            overflow:auto;
            padding-bottom:.5rem;
            .content{
                
                .cont-top{
                    height:1rem;
                    width:100%;
                    border-top:.05rem solid #ccc;
                    border-bottom:.05rem solid #ccc;
                    display:flex;
                    justify-content:space-between;
                    padding:.14rem .2rem;
                    img{
                        display:block;
                        width:.6rem;
                        height:.6rem;
                    }
                    div{
                        padding:.05rem 0 0 .1rem;
                        p{
                            font-size:.1rem;
                        }
                        p:nth-of-type(1){
                            display:flex;
                            justify-content:space-between;
                            padding-right:.1rem;
                        }
                        p:nth-of-type(2){
                            color:#999999;
                        }
                    }
                }
            }
            .leave{
                
                p{
                    padding:0 .2rem;
                    height:.6rem;  
                    width:100%;
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                    border-top:.02rem solid #ccc;
                    span:nth-of-type(1){
                        color:#999999;
                    }
                }
                p:nth-of-type(1){
                    b{
                        b{
                            display:inline-block;
                            width:.2rem;
                            height:.2rem;
                            border:1px solid #000;
                            border-radius:.1rem;
                            line-height:.16rem;
                            text-align:center;
                        }
                        b:nth-of-type(1){
                            margin-right:.1rem;
                        }   
                        b:nth-of-type(2){
                            margin-left:.1rem;
                        }
                    }
                }
                p:nth-of-type(5){
                    display:flex;
                    justify-content:flex-start;
                    input{
                        border:none;
                        margin-left:.1rem;
                        flex:1;
                    }
                }
                
            }
        }
        .footer{
            width:100%;
            display:flex;
            justify-content:flex-end;
            position:fixed;
            bottom:0;
            background:#fff;
            div{
                span:nth-of-type(1){
                    color:red;
                }
                span:nth-of-type(2){
                    display:inline-block;
                    width:1.5rem;
                    height:.5rem;
                    line-height:.5rem;
                    text-align:center;
                    background:#04b10a;
                    color:#fff;
                }
            }
        }
    }
</style>