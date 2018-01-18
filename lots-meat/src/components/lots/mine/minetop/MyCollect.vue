<template>
<!-- -->
    <div class="my-collect style-box">
        <div class="head">
            <i class="yo-ico" @click="tologinon">&#xe605;</i><span>收藏</span>       
        </div>
        <div class="collect-con">
            <ul>
                <li v-for="(data,i) in datas" :key="i">
                    <div><h3>{{data.headline}}</h3><p><span>{{data.time}}</span><span>{{data.username}}</span><span><i class="yo-ico">&#xe639;</i>{{data.reader}}</span></p></div>
                    <div><img :src="data.imurl"/></div>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        name:"my-collect",
        data(){
            return {
                user_data:'',
                datas:'',
                user_id:''
            }
        },
        methods:{
            tologinon(){
                this.$router.replace({name:'mineloginon'})  
            }    
        },
        created(){
            let that=this
            axios.get("/static/api/collect.json",{user_id:that.user_id}).then((res)=>{
                console.log(res.data.data)
                that.datas=res.data.data
                console.log(that.datas.headline)
            })
            that.user_data = localStorage.getItem("user_info")
            that.user_data = JSON.parse(that.user_data)
            that.user_id = that.user_data.user_id
        }
    }
</script>
<style lang="scss" scoped>
        .my-collect{
       
        .collect-con{
            flex:1;
            overflow-y:auto;
            padding-bottom:.34rem;
            ul{
                li{
                    width:100%;
                    height:1.05rem;
                    display:flex;
                    justify-content:space-between;
                    padding:.1rem .2rem;
                    border-bottom:.01rem solid #d8d8d8;
                    div:nth-of-type(1){
                        width:2rem;
                        line-height:.3rem;
                        display:flex;
                        flex-direction:column;
                        justify-content:space-between;
                        h3{
                            overflow: hidden;
                            text-overflow:ellipsis;
                            white-space: nowrap;
                        }
                        p{
                            width:1.8rem;
                            display:flex;
                            justify-content:space-between;
                        }
                    }
                    div:nth-of-type(2){
                        img{
                            width:.85rem;
                            height:.85rem;
                        }
                    }
                }
            }
        }
    }
</style>