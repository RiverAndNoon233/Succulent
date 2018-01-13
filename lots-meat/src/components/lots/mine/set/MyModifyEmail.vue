<template>
    <!--修改邮箱组件-->
    <div class="my-modify-email style-box">
        <div class="head">
        <i class="yo-ico" @click="tologinon">&#xe605;</i><span>修改邮箱</span>       
        </div>
        <div class="con">
            <form @submit.prevent = 'changepas()'>
                <p>原邮箱</p>
                <input type="text" v-model="email" placeholder="请输入原邮箱">
                <p>新邮箱</p>
                <input type="text" v-model="newemail" placeholder="请输入新邮箱">
                <input type="submit" value="保存">
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
        .con{
            padding:1rem  0 0 .7rem;
            p{
                line-height:.3rem;
            }
            input:nth-of-type(3){
                display:block;
                margin:.3rem 0 0 .5rem;
                border:none;
                background:#04b10a;
                width:.6rem;
                height:.23rem;
                border-radius:.1rem;
                font-size:.1rem;
                color:#fff;
            }
        }
    }
</style>