<template>
    <div class="shop-boxItem">
        <li>
            <img :src="info.image"/>
            <p>
                <h4>{{info.goods_name}}</h4>
                <h5><b>￥{{info.price}}</b><i>{{info.count}}人付款</i></h5>
            </p>
        </li>
    </div>
</template>

<script>
    export default {
        name:"shop-boxItem",
        props:['info'],
    }        
</script>

<style>
    
</style>