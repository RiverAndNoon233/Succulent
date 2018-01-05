<template>
    <div class="mine-login">
        <div class="head">
            <i class="fa fa-chevron-left"></i><span>登录</span>       
        </div>
        <h1>肉多多</h1>
        <form @submit.prevent = 'login(username,password)'>
            <div><input v-model = "username" type="text" placeholder="请输入您的账号"><i class="fa fa-user-o"></i></div>
            <div><input v-model = "password" type="password" placeholder="请输入您的密码"><i class="fa fa-unlock-alt"></i></div>  
            <a>找回密码</a>         
            <div class="sub"><input type="submit" value="登录" /></div>
        </form>
        <div class="register"><button>注册</button></div>
    </div>
</template>

<script>
    import bus from '../../../modules/bus.js'
    import axios from 'axios'
    import {Toast} from 'mint-ui'
    export default {
        name:"mine-login",
        props:['LoginShow'],
        data(){
            return {
                username:'',
                password:'',
                LoginOnData:''
            }
        },
        methods:{
            login(user,pass){
                let that =this
                if(user==''||pass==''){
                    return false
                }
                axios.get('/static/api/login.json',{params:{user:that.username,pass:that.password}}).then((res)=>{
                    if(res.data.msg!=0) {
                        Toast('登陆失败')
                        return false;
                    }
                    Toast('登陆成功')
                    let data = {user_id:that.username,username:that.username}
                    that.LoginOnData = res.data.data
                    console.log(that.LoginOnData)
                    //调用vuex方法 创建本地存储
                    that.$store.commit('change_type',data)    
                    that.$router.replace({name:'mineloginon'})       
                })
                 bus.$emit("loginondata",this.LoginOnData)
            },
        },
    }
</script>

<style lang="scss" scopde>
    .mine-login{
        width:100%;
        height:100%;
        position:absolute;
        z-index:1000;
        background:#fff;
        .head{
            height:.44rem;
            background:#04b10a;
            text-align:center;
            line-height:.44rem;
            color:#fff;
            padding:0 .1rem;
            i{
                float:left;
                line-height:.44rem;
                
            }
            span{
                text-align:center;
            }
        }
        h1{
            text-align:center;
            font-size:.6rem;
            font-weight:normal;
            color:#03a81b;
            margin:.37rem 0 .48rem 0;
        }
        form{
            div{
                width:100%;
                height:.74rem;
                position:relative;
                padding:0 .7rem;
                input{
                    display:block;
                    border:none;
                    width:100%;
                    height:100%;
                    border-bottom:1px solid #03ab1a;
                    padding:0;
                    font-size:.15rem;
                    padding-left:.5rem;
                }
                ::-webkit-input-placeholder { /* WebKit browsers */
                    color:    #03a81b;
                }
                :-moz-placeholder { /* Mozilla Firefox 4 to 18 */
                    color:    #03a81b;
                }
                ::-moz-placeholder { /* Mozilla Firefox 19+ */
                    color:    #03a81b;
                }
                :-ms-input-placeholder { /* Internet Explorer 10+ */
                    color:    #03a81b;
                }
                i{
                   color:#03a81b;
                   position:absolute;
                   top:.3rem;
                }
            }
            a{
                display:block;
                padding:.2rem .7rem 0;
                color:#03a81b;
                text-align:right;
            }
            .sub{
                width:100%;
                padding:0 .7rem;
                height:.32rem;
                input{
                    width:100%;
                    height:.32rem;
                    padding:0;
                    border-radius:.32rem;
                    background:#03a81b;
                    border:none;
                    margin-top:.36rem;
                    color:#fff;
                }
            }
        }
    .register{ 
        display:flex;
        justify-content:center;
        button{
            width:.8rem;
            height:.32rem;
            border-radius:.32rem;
            background:#03a81b;
            border:none;
            margin-top:.36rem;
            color:#fff;
        }
    }
    }
    

</style>