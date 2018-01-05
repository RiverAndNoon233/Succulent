<template>
  <div id="app">
    <div class="exothecium">
      <headers></headers>
      
      <router-view></router-view>

      <Footers></Footers>
    </div>
  </div>
</template>

<script>
import Headers from "./components/lots/head/lotHead"
import Footers from "./components/lots/AppFooter/AppFooter"
export default {
  name: 'app',
  components:{
    Footers,Headers
  }
}
</script>

<style>

</style>
