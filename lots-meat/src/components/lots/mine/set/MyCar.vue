<template>
    <!--购物车组件-->
    <div class="my-car style-box">
        <div class="head">
        <i class="yo-ico" @click="tologinon">&#xe605;</i><span>购物车</span>       
        </div>
        <div class="car-none">
            <div v-if="!car.length">
                <p>购物车空空哒，快去逛逛吧</p>
                <button>随便看看></button>
            </div>
            <MyCarList v-for="(data,i) in car" :key="data.gid" :info = "data" :changeprice="price"></MyCarList>
        </div>
        
        
        <div class="car-bot" v-if="car.length"> 
            <div></div>
            <div>
                <span>总计:<b>￥{{prices}}</b></span>
                <button @click="toorder">去结算</button>
            </div>
        </div>
    </div>
</template>
<script>
import MyCarList from "./mycarlist/MyCarList.vue"
import {mapState} from 'vuex'
export default{
    name:"my-car",
    data(){
        return{
            ischeck:false,
            prices:'',
            car_leng:''
        }
    },
    methods:{
        tologinon(){
            this.$router.replace({name:'mineloginon'})  
        },
        toorder(){
            this.$router.replace({name:'suborder'})  
        },
        checked(){
            this.ischeck = !this.ischeck
        },
        price(){
            let datas = JSON.parse(localStorage.car?localStorage.car:'')
            let num=0
            for(let i = 0; i<datas.length;i++){
                num+=(datas[i].price*datas[i].num)
            }
            this.$store.commit('changepri',num.toFixed(2))
            this.prices = this.$store.state.carprice
        }
    },
    components:{
        MyCarList
    },
    mounted(){
       this.price()
        //使用接口时 不注释
        //this.$store.dispatch('addGood')
    },
    computed:{
        ...mapState(['car'])
    },
    updated(){
        if(this.prices==0){
            // location=location
        }
    }
}    
</script>
<style lang="scss" scoped>
    .my-car{
        z-index:1;
        
        .car-none{
            text-align:center;
            overflow-y:auto;
            padding-bottom:.5rem;
            p{
                font-size:.2rem;
                padding:1rem 0 .6rem 0;
            }
            button{
                width:.9rem;
                height:.2rem;
                border:none;
                border-radius:.05rem;
                background:#04b10a;
                color:#fff;
                font-size:.1rem;
            }
        }
        .car-bot{
            width:100%;
            height:.5rem;
            display:flex;
            justify-content:space-between;
            position:fixed;
            bottom:0;
            align-items:center;
            padding-left:.1rem;
            background:#fff;
            span{
                b{
                    color:red;
                }
            }
            button{
                width:.8rem;
                height:.5rem;
                background:#e4393c;
                border:none;
                margin-lift:.1rem;
                color:#fff;
            }
            div:nth-of-type(1){
                span{
                    color:red;
                    padding-left:.1rem;
                }
            }
        }
    }
</style>