<template>
  <div class="lot-two">
      <!-- <lotHead></lotHead> -->
      <lotHeadTwo></lotHeadTwo>
      <router-view></router-view><!--二级路由显示-->
  </div>
</template>

<script>  
import lotHead from "./head/lotHead.vue"
import lotHeadTwo from "./head/lotHeadTwo.vue"
export default {
    name:"lot-two",
    components: { 
      lotHead,lotHeadTwo
    }
}
</script>

<style>

</style>
