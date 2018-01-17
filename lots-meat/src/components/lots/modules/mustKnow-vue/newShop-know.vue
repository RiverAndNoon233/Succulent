<template>
    <div class="newShop-know">
       <new-head></new-head> 
       <div class="newShop-box">
            <h1>肉多多交易购买须知</h1>
            <h2><span>2017-10-13</span><i>肉多多网</i></h2>
            <div class="imgbox">
                <img src="/static/images/shop1.jpg"/>
                <h3>购买须知</h3>
            </div>
            <div class="newShop-font">
                声明在肉多多平台购买的商品植物的相关产品。肉多多都将严格监督管理。买家收到货后发现与描述不相符如植物坏死发病的情况可以卖家取得联系。如果无法达成和解，可在二十四小时内及时与我们取得联系。肉多多会将配合买卖双方协调做出合理的处理。凡是发现任何假货商品，一律关店处理。
            </div>
            <div class="question">
                1.肉多多不支持以下交易方式
            </div>
            <p class="answer">
                在线一元拍 在线起拍价
            </p>
            <div class="question">
                2.肉多多支持以下交易方式
            </div>
            <p class="answer">
                一口价在线购买
            </p>
            <div class="question">
                3.什么是一口价商品
            </div>
            <p class="answer">
                一口价商品就是卖家明码标价,买家根据所需数量付款,卖家发货,收货确认则成交,确认收货后可以卖家评价
            </p>
       </div>
    </div>
</template>

<script>
 import NewHead from "./newHead-know"
    export default {
        name:"newShop-know",
        components:{
           NewHead
        }
    }        
</script>

<style lang="scss" scoped>
    .newShop-know{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#fff;
        .newShop-box{
            padding:0 0.1rem;
            h1{
                width:100%;
                margin-top:0.1rem;
                color:#333333;
                font-size:20px;
                font-weight: 500;
            }
            h2{
                color:#999999;
                font-size:14px;
                font-weight: normal;
                i{
                    margin-left:0.1rem;
                }
            }
            .imgbox{
                width:100%;
                height: 2.31rem;
                background:#03ab1a;
                text-align: center;
                margin-top:0.08rem;
                img{
                    width:0.81rem;
                    height:1rem;
                    margin-top:0.4rem;
                }
                h3{
                    color:#fff;
                    margin-top:0.2rem;
                    font-size:16px;
                    font-weight: 500;
                }
            }
            .newShop-font{
                line-height: 0.25rem;
                color:#007e10;
                font-size:14px;
            }
            .question{
                margin-top:0.08rem;
                font-size:14px;
                color:#333333;
            }
            .answer{
                font-size:14px;
                color:#666;
            }
        }
    }
</style>