<template>
        <li class="find-detail-li" @click="detail">
            <div class="newsbox-top">
                <img src="/static/images/find5.jpg">
                <p class="newsbox-p">
                    <b>{{newItem.user_name}}</b>
                    <i>{{newItem.essay_time}}分钟</i>
                </p>
            </div>
            <div class="newsbox-font">
                {{newItem.essay_title}}
            </div>
            <div class="newsbox-image">
                <img v-for="(ImageUrl,i) in ImageUrls" :key="i" v-preview="ImageUrl" :src="ImageUrl">
            </div>
            <div class="newsbox-foot">
                <span>评论</span><span class="fa fa-commenting-o"></span>
                <span>{{newItem.essay_views_num}}</span><span class="fa fa-eye"></span>
            </div>
        </li>
</template>

<script>
    export default {
        name:"find-newsboxItem",
        data(){
            return {
                ImageUrls:[]
            }
        },
        props:['newItem'],
        methods:{
            detail(){
                this.$router.push({path:'/lotindex/lotBoxDetail'});
            } 
        },
        mounted(){
            this.ImageUrls = this.newItem.essay_image;
            //console.log(this.newItem.essay_image)
        }
    }        
</script>

<style lang="scss" scoped>
 
</style>