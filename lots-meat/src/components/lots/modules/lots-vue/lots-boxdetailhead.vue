<template>
    <div class="lots-boxdetailhead">
        <router-link :to="'/lotindex'"  tag="b" class="yo-ico">&#xe605;</router-link>
        <span>文章详情</span>
        <router-link :to="'/lotindex/lotBoxDetail/lotPingjia'"  tag="b">评价</router-link>
        <!-- <b>评价</b> -->
    </div>
</template>

<script>
export default {
    name:"lots-boxdetailhead"
}
</script>

<style lang="scss" scoped>
  
</style>

