<template>
    <div class="lots-box">
       <p class="kong"></p>
       <h3>
           <span></span>
           最新热帖
        </h3>
        <lots-box-item></lots-box-item>
        <lots-box-item></lots-box-item>
        <lots-box-item></lots-box-item>
        <lots-box-item></lots-box-item>
        <lots-box-item></lots-box-item>
        <lots-box-item></lots-box-item>
        <lots-box-item></lots-box-item>
        <lots-box-item></lots-box-item>
    </div>
</template>

<script>
import LotsBoxItem from "./lots-boxItem"
export default {
    name:"lots-box",
    components:{
        LotsBoxItem
    }
}        
</script>

<style lang="scss" scoped>
    
</style>

