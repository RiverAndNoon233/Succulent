<template>
    <div class="find-head">
        <router-link :to="'/find-fo/FindSearch'" tag="b" class="yo-ico">&#xe60b;</router-link>
        <span>发现</span>
        <router-link :to="'/find-fo/FindWritePublish'" tag="b" class="yo-ico">&#xe71f;</router-link>
    </div>
</template>

<script>
    export default {
        name:"find-head"
    }        
</script>

<style lang="scss" scoped>
    .find-head{
       
    }
    
</style>