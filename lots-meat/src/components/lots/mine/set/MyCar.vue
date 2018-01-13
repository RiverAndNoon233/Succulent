<template>
    <!--购物车组件-->
    <div class="my-car style-box">
        <div class="head">
        <i class="yo-ico" @click="tologinon">&#xe605;</i><span>购物车</span>       
        </div>
        <div class="car-none">
            <p>购物车空空哒，快去逛逛吧</p>
            <button>随便看看></button>
        </div>
    </div>
</template>
<script>
export default{
    name:"my-car",
    methods:{
        tologinon(){
            this.$router.replace({name:'mineloginon'})  
        }
    }
}    
</script>
<style lang="scss" scoped>
    .my-car{
        .car-none{
            text-align:center;
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
    }
</style>