<template>
    <div class="find-writepublish">
       <div class="find-writehead">
            <router-link :to="'/find-fo'"  tag="b" class="fa fa-chevron-left"> </router-link>
            <span>发帖</span>
            <!-- <router-link :to="'/find-fo'" tag="b">发布</router-link> -->
            <b @click="publish">发布</b>
       </div>
        <find-write-box></find-write-box>
    </div>
</template>

<script>
import { Toast } from 'mint-ui';
import FindWriteBox from './find-writebox.vue'
    export default {
        name:"find-writepublish",
        components:{
           FindWriteBox
        },
        methods:{
            publish(){
                
                Toast({
                    message: '发表成功',
                });
                let that = this;
                setTimeout(function(){
                     that.$router.push('/find-fo')
                },2000)
               
            }
        }
    }        
</script>

<style lang="scss" scoped>

</style>