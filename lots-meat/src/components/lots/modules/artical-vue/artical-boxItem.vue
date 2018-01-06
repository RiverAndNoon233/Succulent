<template>
    <div class="lots-boxItem">
      <div class="lots-boxItemLeft">
          <img :src="hotartical.urlimage">
      </div>
      <div class="lots-boxItemRight">
          <h4>{{hotartical.title}}</h4>
          <p><i>{{hotartical.timestamp}}分钟前</i><b>{{hotartical.count}}</b></p>
      </div>
    </div>
</template>

<script>
export default {
    name:"artical-boxItem",
    props:['hotartical']
}        
</script>

<style lang="scss" scoped>
    
</style>

