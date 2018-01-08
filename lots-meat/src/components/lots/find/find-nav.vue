<template>
    <div class="find-nav">
        <ul>
            <li @click="turntype(1)">
                <img src="/static/images/find1.jpg"/>
                <b>景天科</b>
            </li>
             <li @click="turntype(2)">
                 <img src="/static/images/find2.jpg"/>
                 <b>仙人掌科</b>
             </li>
            <li @click="turntype(3)">
                 <img src="/static/images/find3.jpg"/>
                 <b>番杏科</b>
             </li>
             <li @click="turntype(4)">
                 <img src="/static/images/find4.jpg"/>
                 <b>百合科</b>
             </li>
        </ul>
        
    </div>
    
</template>

<script>
    export default {
        name:"find-nav",
        methods:{
            turntype(num){
                this.$router.push({path:'/find-fo/FindBoxDetail',query:{"num":num}});
            }
        }
    }        
</script>

<style lang="scss" scoped>

    
</style>