<template>
    <!--所有页面底部-->
    <div class="AppFooter">
       <div class="index-footer">
            <ul>
                <router-link :to="'/lotindex'" tag="li" replace>
                    <span class="yo-ico">&#xe658;</span>
                    <i>多多</i>
                </router-link>
                <router-link :to="'/find-fo'" tag="li" replace>
                    <span class="yo-ico">&#xe607;</span>
                    <i>发现</i>
                </router-link>
                <router-link :to="'/shop-fo'" tag="li" replace>
                    <span class="yo-ico">&#xe600;</span>
                    <i>商城</i>
                </router-link>
                <router-link :to="'/mine-fo'" tag="li" replace>
                    <span class="yo-ico">&#xe6e6;</span>
                    <i>我的</i>
                </router-link>
            </ul>
       </div>
    </div>
</template>

<script>
    export default {
        name:"AppFooter",
        //底部循环 路由
        data:function(){
            return {
               
            }
        }
    }        
</script>

<style>
    
</style>