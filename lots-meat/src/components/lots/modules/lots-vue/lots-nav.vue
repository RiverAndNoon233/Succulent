<template>
    <div class="lots-nav">
       <ul>
           <router-link :to="'/lotindex/newPersonKnow'" tag="li" replace>
                <p><img src="/static/images/5.png"></p>
                <i>新人须知</i>
           </router-link>
            <router-link :to="'/lotindex/newShopKnow'" tag="li" replace>
                <p><img src="/static/images/6.png"></p>
                <i>交易须知</i>
           </router-link>
            <router-link :to="'/lotindex/newPlantKnow'" tag="li" replace>
                <p><img src="/static/images/7.png"></p>
                <i>种植知识</i>
           </router-link>
            <router-link :to="'/lotindex/newDayKnow'" tag="li" replace>
                <p><img src="/static/images/8.png"></p>
                <i>小助手</i>
           </router-link>
       </ul>
    </div>
</template>

<script>
    export default {
        name:"lots-nav",
    }        
</script>


<style lang="scss" scoped>
    
</style>