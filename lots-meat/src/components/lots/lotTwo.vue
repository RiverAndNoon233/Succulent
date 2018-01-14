<template>
  <div class="lot-two">
    <lotHead></lotHead> 
     <router-view></router-view>
      <!-- <lotHeadTwo></lotHeadTwo> -->
  </div>
</template>

<script>  
import lotHead from "./head/lotHead.vue"
// import lotHeadTwo from "./head/lotHeadTwo.vue"
export default {
    name:"lot-two",
    components: { 
      lotHead
    }
}
</script>

<style>

</style>
