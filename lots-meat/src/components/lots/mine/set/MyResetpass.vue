<template>
    <!--修改密码组件-->
    <div class="my-resetpass style-box">
        <div class="head">
            <i class="yo-ico" @click="tologinon">&#xe605;</i><span>修改密码</span>       
        </div>
        <div class="con">
            <form @submit.prevent = 'changepas()'>
                <div>
                    <p>原密码</p>
                    <input type="password" v-model="oldpassword" placeholder="请输入原密码">
                    <p>新密码</p>
                    <input type="password" v-model="newpassword" placeholder="请输入新密码">
                </div>
                <div class="sub"><input type="submit" id="" value="保存"></div>
            </form>
        </div>
    </div>
</template>
<script>
    
    import axios from 'axios'
    import {Toast} from 'mint-ui'
    export default {
        name:"my-resetpass",
        data(){
            return {
                u_id:'',
                oldpassword:'',
                newpassword:''
            }
        },
            methods:{
                changepas(){
                let that =this
                if(that.oldpassword==''||that.newpassword==''){
                    return false
                }
                axios.get('/static/api/changepd.json',{params:{id:that.u_id,old_password:that.oldpassword,new_password:that.newpassword}}).then((res)=>{
                    console.log(res.data.data)
                    if(res.data.data==1) {
                        Toast('原密码输入错误')
                        return false;
                    }else if(res.data.data==0){
                        Toast('修改成功')
                        return true;
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
    .my-resetpass{
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