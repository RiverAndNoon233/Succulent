<template>
    <div class="shop-boxItem">
        <li @click="todetails">
            <img :src="info.image"/>
            <div class="shop-rig">
                <h4>{{info.goods_name}}</h4>
                <h5><b>￥{{info.price}}</b><i>{{info.count}}人付款</i></h5>
            </div>
        </li>
    </div>
</template>

<script>
    export default {
        name:"shop-boxItem",
        props:['info'],
        data(){
            return {
                params:''
            }
        },
        mounted(){
            this.params = this.info
        },
        methods:{
            todetails(){
                this.$router.push({name:'shopdetails',params:{_id:this.params.gid}})
            }
        }
    }        
</script>

<style lang="scss" scoped>
    .shop-boxItem{
        .shop-rig{
            display:flex;
            flex-direction:column;
            justify-content:space-between;
            flex:1;
            height:100%;
            padding:.1rem;
            h4{
                display:block;
                font-size:.2rem;
                color:#04b10a;
            }
            h5{
                display:flex;
                justify-content:space-between;
                b{
                    color:red;
                    font-weight:normal;
                }
            }
        }
    }
</style>