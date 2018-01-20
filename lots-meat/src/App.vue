<template>
  <div id="app">
    <div class="exothecium">
      <router-view></router-view>
       <lg-preview></lg-preview>
      <Footers></Footers>
    </div>
  </div>
</template>

<script>
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
