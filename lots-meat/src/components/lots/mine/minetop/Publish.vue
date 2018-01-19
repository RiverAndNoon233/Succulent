<template>
    <div class="publish">
        <ul>
            <li>
                <div><img :src="publi.imurl"/></div>
                <div><h3>{{publi.headline}}</h3><p><span>{{publi.time}}</span><span><i class="yo-ico">&#xe639;</i>{{publi.reader}}</span></p></div>
            </li>
        </ul>
    </div>
</template>
<script>
    export default {
        name:"publish",
        props:['publi']
    }
</script>
<style lang="scss" scoped>
    .publish{
       ul{
            li{
                width:100%;
                height:1.05rem;
                display:flex;
                justify-content:space-between;
                padding:.1rem .2rem;
                border-bottom:.01rem solid #d8d8d8;
                div:nth-of-type(2){
                    width:2rem;
                    line-height:.3rem;
                    display:flex;
                    flex-direction:column;
                    justify-content:space-between;
                    flex:1;
                    padding-left:.15rem;
                    h3{
                        overflow: hidden;
                        text-overflow:ellipsis;
                        white-space: nowrap;
                    }
                    p{
                        display:flex;
                        justify-content:space-between;
                    }
                }
                div:nth-of-type(1){
                    img{
                        width:.85rem;
                        height:.85rem;
                    }
                }
            }
        }
    }
</style>