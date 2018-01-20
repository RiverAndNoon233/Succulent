<template>
    <div class="mine-login style-box">
        <div class="head">
            <i class="yo-ico">&#xe605;</i><span>登录</span>       
        </div>
        <div class="cen">
            <h1>肉多多</h1>
            <form @submit.prevent = 'login(username,password)'>
                <div><input v-model = "username" id="user" type="text" placeholder="请输入您的账号"><i class="yo-ico">&#xe6e6;</i></div>
                <div><input v-model = "password" id="pass" type="password" placeholder="请输入您的密码"><i class="yo-ico">&#xe610;</i></div>  
                <a>找回密码</a>         
                <div class="sub"><input type="submit" value="登录" /></div>
                
            </form>
            <div class="register">
                <button @click="toRegister">注册</button>
            </div>
        </div>
    </div>
</template>

<script>
    import bus from '../../../modules/bus.js'
    import axios from 'axios'
    import {Toast} from 'mint-ui'
    import {mapActions} from "vuex"
    export default {
        name:"mine-login",
        props:['LoginShow'],
        data(){
            return {
                username:'',
                password:'',
                LoginOnData:'',
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
                    let data = {user_id:that.username,username:that.username,LoginOnData:res.data.data}
                    that.LoginOnData = res.data.data
                    //调用vuex方法 创建本地存储
                    that.$store.commit('change_type',data)    
                    that.$router.replace({name:'mineloginon'}) 

                })
                this.submitForm()
            },
            toRegister(){
                this.$router.replace({name:'mineregister'})  
            },
            submitForm () {
                //  this.$store.commit("addGid",gid)
                this.$store.dispatch('addGood')
            }
        },

    }
</script>

<style lang="scss" scopde>
    .mine-login{
        z-index:1;
        .cen{
        flex:1;
        overflow-y:auto;
        h1{
            text-align:center;
            font-size:.6rem;
            font-weight:normal;
            color:#03a81b;
            padding:.37rem 0 .48rem 0;
        }
        form{
            div{
                width:100%;
                height:.74rem;
                position:relative;
                padding:0 .7rem;
                background:#fff;
                input{
                    display:block;
                    border:none;
                    width:100%;
                    height:100%;
                    border-bottom:1px solid #03ab1a;
                    font-size:.15rem;
                    padding-left:.5rem;
                }
                #user,#pass{
                    -webkit-box-shadow: 0 0 0 1000px white inset;
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
                padding:.36rem .7rem 0;
                height:.32rem;
                input{
                    width:100%;
                    height:.32rem;
                    padding:0;
                    border-radius:.32rem;
                    background:#03a81b;
                    border:none;
                    
                    color:#fff;
                }
            }
        }
    .register{ 
        display:flex;
        justify-content:center;
        padding-top:.66rem;
        button{
            width:.8rem;
            height:.32rem;
            border-radius:.32rem;
            background:#03a81b;
            border:none;
            color:#fff;
        }
    }
    }
    }
    

</style>