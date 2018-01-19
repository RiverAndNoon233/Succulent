<template>
    <div class="my-publish style-box">
         <div class="head">
            <i class="yo-ico" @click="tologinon">&#xe605;</i><span>我的发表</span>       
        </div>
        <div class="Publish">
            <Publish v-for="(data,i) in datas" :key="i" :publi="data"></Publish>
        </div>
    </div>
</template>
<script>
import Publish from "./Publish.vue"
import axios from "axios"
    export default {
        name:"my-publish",
        data(){
            return{
                user_data:'',
                datas:'',
                user_id:''
            }
        },
        methods:{
            tologinon(){
                this.$router.replace({name:'mineloginon'})  
            },
        },
        components:{
            Publish
        },
        created(){
            let that=this
            that.user_data = localStorage.getItem("user_info")
            that.user_data = JSON.parse(that.user_data)
            that.user_id = that.user_data.user_id
            axios.get("/static/api/publishon.json",{user_id:that.user_id}).then((res)=>{
                console.log(res.data.data)
                that.datas=res.data.data
                console.log(that.datas)
            })
            
        }
    }
</script>
<style lang="scss" scoped>
    .my-publish{
        z-index:1;
        .Publish{
            flex:1;
            overflow-y:auto;
        }
    }
</style>