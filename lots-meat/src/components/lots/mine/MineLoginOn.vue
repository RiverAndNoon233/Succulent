<template>
    <div class="mine-login-on style-box">
        
        <div class="loginonhead"><span>我</span></div>
        <div class="mark">
        <div class="personage" >
            <div class="personage-top">
                <div >
                    <img src="/static/images/10.jpg" />
                </div>
                <div>
                    <div><div><span>积分 : {{data_nickname}}</span><span>新手上路</span></div></div>
                    <p>{{data_nickname}}</p>
                    <!--<p>判断逻辑 当时间一定时显示这条数据</p>-->
                </div>
            </div>
            <div style="width:100%;height:100%;background:url(/static/images/10.jpg) no-repeat;background-size:100% 100%; -webkit-filter: blur(10px) brightness(1); /* Chrome, Opera */
            -moz-filter: blur(10px) brightness(1); 
            -ms-filter: blur(10px) brightness(1);    
            filter: blur(10px) brightness(1);position:absolute;top:0;z-index:-1;"></div>
           </div>
        
        <div class="gray"></div>
         <div class="personage-bot">
                <ul>
                    <router-link v-for="nav_top in nav_tops" :key="nav_top.id" :to="nav_top.name" tag="li">{{nav_top.content}}</router-link>
                </ul>
            </div>
        <div class="settingnape">
             <ul>
                <router-link v-for="set in sets" :key="set.id" :to="set.name" tag="li"><i class="yo-ico" v-html="set.icon">{{set.icon}}</i><span>{{set.content}}</span><span class="yo-ico">&#xe503;</span></router-link>
                <div class="logout" @click="delateItem()">退出登录</div>
            </ul>
            
        </div>
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
                data_nickname:'',
                nav_tops:[
                    {id:1,content:"我的收藏",name:"/mine-fo/mycollect"},
                    {id:2,content:"我的发表",name:"/mine-fo/mypublish"},              
                ],
                sets:[
                    {id:1,content:"购物车",name:"/mine-fo/mycar",icon:'&#xe618;'},          
                    {id:2,content:"我的钱包",name:"/mine-fo/mywallet",icon:"&#xe502;"},          
                    {id:3,content:"修改密码",name:"/mine-fo/myresetpass",icon:"&#xe610;"},           
                    {id:4,content:"修改邮箱",name:"/mine-fo/mymodifyemail",icon:"&#xe90a;"},           
                    {id:5,content:"我的订单",name:"/mine-fo/myorderfrom",icon:"&#xe504;"},                               
                ]
            }
        },
        mounted(){  
            let that=this
            that.data = localStorage.getItem("user_info")
            that.data = JSON.parse(that.data)
            that.data_nickname = that.data.user_id
        },
        methods:{
            delateItem(){
                let that = this
                localStorage.removeItem("user_info")
                location.href="/mine-fo/minelogin"
            }
        }
    }
</script>

<style lang="scss" scoped>
    .mine-login-on{
        width:100%;
        height:100%;
        
            overflow-y:auto;
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
        .mark{
        flex:1;
        overflow-y:auto;
        .personage{
            width:100%;
            height:1.9rem;  
            position:relative;
            .personage-top{
                padding-top:.2rem;
                z-index:1111;
                
                
                div:nth-of-type(1){
                    display:flex;
                    text-align:center;                
                    justify-content:center; 
                    img{
                        width:.8rem;
                        height:.8rem;
                        border-radius:.4rem;
                    }
                }
                div:nth-of-type(2){
                    position:relative;
                    div{
                        width:100%;
                        position:absolute;
                        padding:.1rem .8rem 0;
                        div{
                            width:100%;
                            display:flex;
                            justify-content:space-between; 
                            color:#fff;                            
                        }
                        
                    }
                    p:nth-of-type(1){
                        text-align:center;
                        font-size:.2rem;
                        padding-top:.1rem;
                        color:#fff;
                    }
                }
            }
            
        }
        .gray{
            height:.07rem;
            background:#ccc;
        }
        .personage-bot{
                height:.5rem;
                background:#fff;
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
        .settingnape{
            background:#fff;
            ul{
                height:3.72rem;
                
                background:#fff;
                li{
                    width:100%;
                    height:.55rem;
                    display:flex;
                    justify-content:space-between; 
                    align-items:center;
                    padding:0 .1rem;
                    i{
                        display:inline-block;
                        width:.3rem;
                        font-size:.2rem;
                        background:#03ab1a;
                        text-align:center;
                        color:#fff;
                        border-radius:.06rem;
                    }
                    span:nth-of-type(1){
                        padding-right:1.8rem;
                    }
                }
            }
        }
        .logout{
            height:.4rem;
            display:flex;
            justify-content:center; 
            align-items:center;
            font-size:.2rem;
            color:#04b10a;
        }
        }
    }
</style>