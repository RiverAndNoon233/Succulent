<template>
    <li class="pingjiaItem">
        <div class="pingjia-top">
            <img :src="pingjia.user_icon"/>
            <span>{{pingjia.user_name}}</span>
        </div>
        <div class="pingjia-content">
            {{pingjia.comment}}
        </div>
        <div class="pingjia-time">
            <i>{{pingjia.comment_time}}</i>
            <b>08:23</b>
        </div>
    </li>
</template>

<script>
export default {
    name:"pingjiaItem",
    props:["pingjia"]
}
</script>

<style lang="scss" scoped>
   
</style>

