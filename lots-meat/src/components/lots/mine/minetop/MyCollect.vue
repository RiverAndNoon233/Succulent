<template>
<!-- -->
    <div class="my-collect style-box">
        <div class="head">
            <i class="fa fa-chevron-left" @click="tologinon"></i><span>收藏</span>       
        </div>
        <div class="collect-con">
            <ul>
                <li v-for="(data,i) in datas" :key="i">
                    <div><h3>[交流]{{data.data.headline}}</h3><p><span>{{data.data.time}}</span><span>{{data.data.username}}</span><span>{{data.data.reader}}阅读</span></p></div>
                    <div><img :src="data.data.imurl"/></div>
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
                console.log(res)
                that.datas=res.data
                console.log(that.datas[1].data)
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
            ul{
                li{
                    width:100%;
                    height:.8rem;
                    display:flex;
                    justify-content:space-between;
                    padding:.1rem .2rem;
                    div:nth-of-type(1){
                        width:2rem;
                        line-height:.3rem;
                        h3{
                            overflow: hidden;
                            text-overflow:ellipsis;
                            white-space: nowrap;
                        }
                        p{
                            display:flex;
                            justify-content:space-between;
                        }
                    }
                    div:nth-of-type(2){
                        img{
                            width:.9rem;
                            height:.6rem;
                        }
                    }
                }
            }
        }
    }
</style>