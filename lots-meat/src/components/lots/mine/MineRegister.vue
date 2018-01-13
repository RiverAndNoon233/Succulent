<template>
    <div class="mine-register style-box">
        <div class="head">
            <i class="yo-ico" @click="tologin">&#xe605;</i><span>注册</span>       
        </div>
        <div class="register-con">
            <p>肉多多</p>
            <p>欢迎你的到来</p>      
            <form @submit.prevent = 'register(username,email,password)'>
                <div><label for="username">用户名</label><input v-model="username" @blur.prevent="table_judge(username)" type="text" id="username" placeholder="请输入用户名"/></div>
                <div><label for="email">邮箱地址</label><input v-model="email" @blur.prevent="table_judge1(email)" type="text" id="email" placeholder="请输入邮箱"/></div>
                <div><label for="password">密码</label><input v-model="password" @blur.prevent="table_judge2(password)" type="password" id="password" placeholder="请输入密码"/></div>
                <div><label for="passto">确认密码</label><input v-model="password1" @blur.prevent="table_judge3(password1)" type="password" id="passto" placeholder="确认密码"/> </div>           
                <h3><span v-show="isShow">{{errormessage}}</span></h3>
                <div class="sub"><input type="submit" value="注册" /></div>
            </form>   
        </div>
    </div>
</template>
<script>
     import axios from 'axios'
     import {Toast} from 'mint-ui'
     export  default {
        name:"mine-register",
        data:function(){
            return {
                username:'',
                email:'',
                password:'',
                password1:'',
                isShow:false,
                errormessage:'',
            }
        },
        methods:{
            table_judge(data){
                let reg = /[a-z]/
                if(reg.test(data)){
                    this.isShow=true
                    this.errormessage='用户名格式有误'
                }else{
                    this.isShow=false
                }
            },
            table_judge1(data){
                let reg = /[a-z]/
                if(reg.test(data)){
                    this.isShow=true
                    this.errormessage='邮箱格式有误'
                }else{
                    this.isShow=false
                }
            },
             table_judge2(data){
                let reg = /[a-z]/
                if(reg.test(data)){
                    this.isShow=true
                    this.errormessage='i密码格式有误'
                }else{
                    this.isShow=false
                }
            },
             table_judge3(data){
                if(data != this.password){
                    this.isShow=true
                    this.errormessage='请输入一致的密码'
                }else{
                    this.isShow=false
                }
            },
            register(username,email,password){
                let that =this
                if(username==''||password==''||email==''){
                    return false
                }
                axios.get('/static/api/register.json',{params:{username:that.username,password:that.password,email:that.email}}).then((res)=>{
                    console.log(res.data.msg)
                    if(res.data.code==0){
                        //跳转
                        Toast('注册成功')
                        that.$router.replace({name:'minelogin'}) 
                    }else if(res.data.code==1){
                        Toast('账号已存在')
                    }else if(res.data.code==2){
                        Toast('')
                    }else if(res.data.code==3){
                        Toast('邮箱已注册')
                    }
                })
                
            },
            tologin(){
                this.$router.replace({name:'minelogin'})  
            }
        }
    }
</script>
<style lang="scss" scoped>
    .mine-register{
        z-index:1;
        .register-con{
            flex:1;
            background:#fff;
            p{
                text-align:center;
                font-size:.35rem;
                color:#04b10a;
                line-height:.7rem;
            }
            p:nth-of-type(2){
                padding-bottom:.2rem;
            }
            form{
                div{
                    width:100%;
                    display:flex;
                    justify-content:flex-end;
                    padding:.1rem .45rem;
                    label{
                        display:block;
                        font-size:.16rem;
                        padding-right:.1rem;
                    }
                    input{
                        border:1px solid #04b10a;
                        width:2.1rem;
                        height:.24rem;
                    } 
                }
                .sub{
                    width:100%;
                    display:flex;
                    justify-content:center;
                    padding-top:.4rem;
                    input{
                        border:none;
                        background:#04b10a;
                        width:100%;
                        height:.4rem;
                        border-radius:.1rem;
                        font-size:.2rem;
                        color:#fff;
                    }
                }
                h3{
                    width:100%;
                    height:.1rem;
                    color:red;
                    font-size:.2rem;
                    text-align:center;
                }
            }
        }
    }
</style>