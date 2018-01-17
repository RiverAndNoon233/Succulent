<template>
    <div class="my-car-list"> 
        <input type="checkbox" v-model="ischeck">
        <img :src = "info.image">
        <div>
            <h1><span>{{info.goods_name}}</span><span @click="del_good(info.gid)">删除</span></h1>
            <p><span><b>￥{{info.price}}</b>&nbsp;&nbsp;&nbsp;26人付款</span><span>X{{info.num}}</span></p>
        </div>
        
    </div>
</template>
<script>
    import axios from "axios"
    import {Toast} from 'mint-ui'
    export default{
        name:"my-car-list",
        props:['info','changeprice'],
        data(){
            return {
                ischeck:false
            }
        },
        
        methods:{
            del_good(id){
                console.log(id)
                
                axios.get("/static/api/addcar.json",{params:{gid:id,ad:0}}).then((res)=>{
                    console.log(res)
                    if(res.data == 0){
                        Toast({
                            message: '用户未登陆',
                            position: 'bottom',
                            duration: 1000
                        })
                    }else if(res.data == 1){
                        
                        Toast({
                            message: '删除成功',
                            position: 'bottom',
                            duration: 1000
                        })
                        this.$store.commit('removeGood',{id})
                        this.changeprice()
                    }
                })
                
            },  
        },
    }
</script>
<style lang="scss" scoped>
    .my-car-list{
        display:flex;
        justify-content:space-between;
        border-top:1px solid #ccc;
        border-bottom:1px solid #ccc;        
        align-items:center;
        margin-top:.1rem;
        padding:.1rem;
        position:relative;
        img{
            width:.85rem;
            height:.85rem;
        }
        div{
            width:2.3rem;
            height:.85rem;
            display:flex;
            flex-direction:column;
            justify-content:space-between;
            h1{
                font-size:.2rem;
                color:#04b10a;
                font-weight:normal;
                text-align:left;
                display:flex;
                justify-content:space-between;
                span:nth-of-type(2){
                    font-size:.06rem;
                    color:red;
                }
            }
            p{
                display:flex;
                justify-content:space-between;
            }
        }
        
    }
</style>