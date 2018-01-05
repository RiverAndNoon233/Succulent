<template>
    <div class="lots-banner">
        <mt-swipe :auto="4000">
            <mt-swipe-item><img src="/static/images/1.jpg"></mt-swipe-item>
            <mt-swipe-item><img src="/static/images/2.jpg"></mt-swipe-item>
            <mt-swipe-item><img src="/static/images/3.jpg"></mt-swipe-item>
        </mt-swipe>
        <!-- <img src="http://www.duorou.com/data/afficheimg/20171212agvohe.jpg"> -->
    </div>
</template>

<script>
export default {
    name:"lots-banner"
}        
</script>

<style lang="scss" scoped>
    .lots-banner{
        width:100%;
        height:1.27rem;
        img{
            width:100%;
            height:1.27rem;
        }
    }
</style>

