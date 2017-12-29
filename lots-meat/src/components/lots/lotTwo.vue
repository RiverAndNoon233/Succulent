<template>
  <div class="lot-two">
      <lotHead></lotHead>
      <router-view></router-view><!--二级路由显示-->
  </div>
</template>

<script>  
import lotHead from "./head/lotHead.vue"
export default {
    name:"lot-two",
    components: { 
      lotHead,
    }
}
</script>

<style>

</style>
