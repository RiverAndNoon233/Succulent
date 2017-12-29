<template>
    <!--所有页面底部-->
    <div class="AppFooter">
       <div class="index-footer">
            <ul>
                <router-link v-for="foo in foos" :key="foo.id" :to="foo.name" tag="li" replace>{{foo.content}}</router-link>
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
                foos:[
                    {id:1,content:"多多",name:"/lotindex"},
                    {id:2,content:"发现",name:"/find-fo"},
                    {id:3,content:"商城",name:"/shop-fo"},
                    {id:4,content:"我的",name:"/mine-fo"},                
                ]
            }
        }
    }        
</script>

<style>
    
</style>