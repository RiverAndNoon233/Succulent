<template>
    <div class="lot-head">
    <!--首页头部-->
        <div class="lot-header">
            <p>多多</p>
        </div>
         <div class="lot-nav">
            <ul>
                <router-link  v-for="nav in navs" :key="nav.id" :to="nav.name" tag="li" class="rout">{{nav.content}}</router-link>
            </ul>
        </div>
    </div>
    
</template>
<script>

export default {
    name:"lot-head",
    //头部循环 路由
    data:function(){
        return {
            navs:[
                {id:1,content:"多多",name:"/lotindex/lots"},
                {id:2,content:"最新文章",name:"/lotindex/article"},
                {id:3,content:"新闻资讯",name:"/lotindex/news"},
                {id:4,content:"晒美图",name:"/lotindex/picture"},                
            ],
        }
    },
    methods:{
        
    }
}
</script>
<style lang="scss" scoped>
   
</style>

