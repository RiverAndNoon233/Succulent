<template>
    <div class="mine-login-on">
        <div class="loginonhead"><span>我</span></div>
        <div class="personage">
            <div class="personage-top">
                <div>
                    <img src="https://pic.maizuo.com/usr/default/maizuomoren66.jpg" />
                </div>
                <div>
                    <p>用户名:<span>xxx</span></p>
                    <p>积分 : <span>999</span>肉币 : <span>999</span></p>
                    <p>新手上路</p>
                    <!--<p>判断逻辑 当时间一定时显示这条数据</p>-->
                </div>
            </div>
            <div class="personage-bot">
                <ul>
                    <router-link v-for="nav_top in nav_tops" :key="nav_top.id" :to="nav_top.name" tag="li">{{nav_top.content}}</router-link>
                </ul>
            </div>
        </div>
        <div class="settingnape">
             <ul>
                <li><i class="fa fa-user-circle-o"></i><span></span><span>1</span></li>
            </ul>
        </div>
    </div>
</template>

<script>
    import bus from '../../../modules/bus.js'
    export default {
        name:"mine-login-on",
        
        data(){
            return{
                data:'',
                nav_tops:[
                    {id:1,content:"我的收藏",name:"/mine-fo/mycollect"},
                    {id:2,content:"我的好友",name:"/mine-fo/myfriends"},
                    {id:3,content:"我的发表",name:"/mine-fo/mypublish"},                
                ],
                // sets:[
                //     {id:1,content:"我的草稿",name:"/mine-fo/mydraft"},
                //     {id:2,content:"购物车",name:""},
                //     {id:3,content:"买家中心",name:""},
                //     {id:4,content:"卖家中心",name:""},
                //     {id:5,content:"商户管理",name:""},
                //     {id:6,content:"账号设置",name:""},
                //     {id:7,content:"个人设置",name:""},                  
                // ]
            }
        },
        components:{

        },
        created(){
            var that =this
            bus.$on("loginondata",(val)=>{
                that.data=val
                console.log(that.data)
            })
        },
    }        
</script>

<style lang="scss" scoped>
    .mine-login-on{
        width:100%;
        height:100%;
        .loginonhead{
            height:.44rem;
            background:#04b10a;
            display:flex;
            justify-content:center; 
            align-items: center;
            span{
                color:#fff;
            }
        }
        .personage{
            width:100%;
            height:1.9rem;
            background:pink;
            .personage-top{
                height:1.4rem;
                display:flex;
                justify-content:space-between; 
                padding:.25rem 0;
                border-bottom:1px solid #ccc;
                div:nth-of-type(1){
                    width:1.35rem;
                    text-align:center;
                    img{
                        width:1rem;
                        height:.9rem;
                    }
                }
                div:nth-of-type(2){
                    flex:1;
                    line-height:.3rem;
                    span{
                        padding-right:.06rem;
                    }
                }
            }
            .personage-bot{
                height:.5rem;
                ul{
                    height:100%;
                    display:flex;
                    li{
                        flex:1;
                        line-height:.5rem;
                        text-align:center;
                    }
                }
            }
        }
        .settingnape{
            ul{
                li{
                    width:100%;
                    height:.35rem;
                }
            }
        }
    }
</style>