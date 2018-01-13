<template>
    <div class="find-writepublish">
       <div class="find-writehead">
            <router-link :to="'/find-fo'"  tag="b" class="fa fa-chevron-left"> </router-link>
            <span>发帖</span>
            <router-link :to="'/find-fo/FindWritePublish'" tag="b">发布</router-link>
       </div>
        <find-write-box></find-write-box>
    </div>
</template>

<script>
import FindWriteBox from './find-writebox.vue'
    export default {
        name:"find-writepublish",
        components:{
           FindWriteBox
        }
    }        
</script>

<style lang="scss" scoped>

</style>