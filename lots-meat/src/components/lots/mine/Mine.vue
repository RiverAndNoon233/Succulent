<template>
    <div class="mine">
       <!-- <transition leave-active-class="animated slideOutRight">
            <MineLogin :LoginShow = "LoginShow" v-if="isLoginShow"></MineLogin>
        </transition>-->
        <router-view></router-view>
    </div>
</template>

<script>
//mport MineLogin from './MineLogin.vue'
    export default {
        name:"mine",
        components:{
           // MineLogin
        },
        data(){
            return {
                isLoginShow:true
            }
        },
        methods:{
            LoginShow(){
                this.isLoginShow=false
            }
        }
    }        
</script>

<style>
    
</style>