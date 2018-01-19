<template>
    <div class="my-order-list">
            <img src="/static/images/图层3.png"/>
            <div>
                <p>黄丽</p>
                <p><span>￥</span><span>9.9</span></p>
            </div>
    </div>
</template>
<script>
    export default {
        name:"my-order-list",
    }
</script>
<style lang="scss" scoped>
    .my-order-list{
        height:.9rem;
        display:flex;
        justify-content:flex-start;
        padding: .1rem .2rem;
        img{
            display:block;
            width:.6rem;
            height:.6rem;
        }
        div{
            display:flex;
            flex-direction:column;
            justify-content:space-between; 
            padding:.05rem;
            p:nth-of-type(2){
                color:red;
                span:nth-of-type(2){
                    font-size:.2rem;
                }
            }
        }
    }
</style>