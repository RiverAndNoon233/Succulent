<template>
    <div class="lots-boxItem" @click="detail">
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
    name:"lots-boxItem",
    props:['hotartical'],
    methods:{
     detail(){
        this.$router.push({path:'/lotindex/lotBoxDetail'});
     } 
    }
}        
</script>

<style lang="scss" scoped>
    
</style>

