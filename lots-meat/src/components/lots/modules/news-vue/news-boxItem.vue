<template>
    <div class="lots-boxItem" @click="detail">
      <div class="lots-boxItemLeft">
          <img :src="newartical.urlimage">
      </div>
      <div class="lots-boxItemRight">
          <h4>{{newartical.title}}</h4>
          <p><i></i><b>{{newartical.count}}评</b></p>
      </div>
    </div>
</template>

<script>
export default {
    name:"news-boxItem",
    props:['newartical'],
    methods:{
     detail(){
        this.$router.push({path:'/lotindex/lotBoxDetail'});
     } 
    }
}        
</script>

<style lang="scss" scoped>
    
</style>

