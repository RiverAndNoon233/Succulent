<template>
    <div class="lots-boxdetail">
         <router-view></router-view>
        <div class="head-height">
            <lots-box-detail-head></lots-box-detail-head>
       </div>
       <div class="lots-articaldetail">
            <div class="lots-articaldetailtop">
                <h1>夏天入了多肉坑，开始了勇敢尝试之旅</h1>
                <h2>
                    <span class="spanone">
                        <i>
                            <b class="fa fa-commenting-o"></b>
                            <strong>13</strong>
                        </i>
                        <i class="itwo">
                            <b class="fa fa-eye"></b>
                            <strong>256</strong>
                        </i>
                    </span>
                    <span class="spantwo">
                        <b>2017-10-21</b>
                        <b>14:18</b>
                    </span>
                </h2>
            </div>
            <p></p>
            <div class="lots-articaldetailcenter">
                <div class="font">
                    好久没有晒肉啦～这是我的小棚子第一个冬天，大棚威力无穷
                    都来发你们的广寒宫看看啊，来啊，互相伤害啊，来个广寒宫大赛
                    度夏我一度想要放弃它们了，扔在角落当个死肉，结果最近发现它们又有了生气！！
                    本帖做个记录，看看它们之后的情况
                </div>
                <img src="/static/images/new1.jpg">
                <div class="font">
                    好久没有晒肉啦～这是我的小棚子第一个冬天，大棚威力无穷
                    都来发你们的广寒宫看看啊，来啊，互相伤害啊，来个广寒宫大赛
                    度夏我一度想要放弃它们了，扔在角落当个死肉，结果最近发现它们又有了生气！！
                    本帖做个记录，看看它们之后的情况
                </div>
                <img src="/static/images/new2.jpg">
            </div>
       </div>
    </div>
</template>

<script>
import LotsBoxDetailHead from './lots-boxdetailhead'
export default {
    name:"lots-boxdetail",
    components:{
        LotsBoxDetailHead
    },
}
</script>

<style lang="scss" scoped>
.lots-boxdetail{
    width:100%;
    height:100%;
    position: fixed;
    top:0;
    z-index:1000;
    background:#fff;
    .head-height{
        width:100%;
        height:44px;
    }
}
</style>

