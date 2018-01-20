<template>
    <!--修改邮箱组件-->
    <div class="my-modify-email style-box">
        <div class="head">
        <i class="yo-ico" @click="tologinon">&#xe605;</i><span>修改邮箱</span>       
        </div>
        <div class="con">
            <form @submit.prevent = 'changepas()'>
                <div>
                    <p>原邮箱</p>
                    <input type="text" v-model="email" placeholder="请输入原邮箱">
                    <p>新邮箱</p>
                    <input type="text" v-model="newemail" placeholder="请输入新邮箱">
                </div>
                <div class="sub"><input type="submit" value="保存"></div>
            </form>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import {Toast} from 'mint-ui'
    export default {
        name:"my-modify-email",
        data(){
            return {
                u_id:'',
                email:'',
                newemail:''
            }
        },
            methods:{
                changepas(){
                let that =this
                if(that.email==''||that.newemail==''){
                    return false
                }
                axios.get('/static/api/changeEm.json',{params:{id:that.u_id,email:that.email,new_email:that.newemail}}).then((res)=>{
                    console.log(res.data.msg)
                    if(res.data.msg='succes') {
                        Toast('修改成功')
                        return
                    }else{
                        Toast('邮箱验证失败')
                        return false;
                    }
                })
                
            },
            tologinon(){
                this.$router.replace({name:'mineloginon'})  
            }
        },
        mounted(){  
            let that=this
            that.data = localStorage.getItem("user_info")
            that.data = JSON.parse(that.data)
            that.u_id = that.data.user_id
        },
    }       
</script>
<style lang="scss" scoped>
     .my-modify-email{
        z-index:1;
        background:#ccc;
        .con{
            form{
                div{
                    padding:.5rem .6rem 0;
                    p{
                        font-size:.13rem;
                        line-height:.3rem;
                    }
                    input{
                        width:2.5rem;
                        height:.4rem;
                        border:none;
                        border-radius:.06rem;
                        padding-left:.1rem;
                    }
                }
                .sub{
                    width:100%;
                    padding:.25rem .1rem 0 .1rem;
                    display:flex;
                    justify-content:center;
                    input{
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
    }
</style>