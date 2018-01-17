<template>
    <div class="publish">
        <div class="pub-top">
            <div><img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516104053064&di=7fa58b5cda205b45f5856f2373592521&imgtype=0&src=http%3A%2F%2Fyouimg1.c-ctrip.com%2Ftarget%2Ffd%2Ftg%2Fg4%2FM08%2FEB%2FBA%2FCggYHVaW-cKARMOTADESWSID6vo582.jpg"/></div>
            <div>
                <p>Madobba</p>
                <p><span>肉肉爱好者</span><span>2015年9月17日发布</span></p>    
            </div>    
        </div>
        <div class="pub-but">
            <h2>新鲜的肉来啦</h2>
            <p>最美的风景,总是在路上,走走停停,边看边拍,拥抱美丽的大自然</p>
            <ul>
                <li><img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516104053064&di=7fa58b5cda205b45f5856f2373592521&imgtype=0&src=http%3A%2F%2Fyouimg1.c-ctrip.com%2Ftarget%2Ffd%2Ftg%2Fg4%2FM08%2FEB%2FBA%2FCggYHVaW-cKARMOTADESWSID6vo582.jpg"/></li>
                <li><img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516104053064&di=7fa58b5cda205b45f5856f2373592521&imgtype=0&src=http%3A%2F%2Fyouimg1.c-ctrip.com%2Ftarget%2Ffd%2Ftg%2Fg4%2FM08%2FEB%2FBA%2FCggYHVaW-cKARMOTADESWSID6vo582.jpg"/></li>
                <li><img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516104053064&di=7fa58b5cda205b45f5856f2373592521&imgtype=0&src=http%3A%2F%2Fyouimg1.c-ctrip.com%2Ftarget%2Ffd%2Ftg%2Fg4%2FM08%2FEB%2FBA%2FCggYHVaW-cKARMOTADESWSID6vo582.jpg"/></li>                    
            </ul>
            <h3><span><i class="yo-ico">&#xe611;</i>拍摄于 西藏自治区 · 纳木错</span><b><span><i class="yo-ico">&#xe602;</i>3333</span><span><i class="yo-ico">&#xe62c;</i>333</span></b></h3>
        </div>
    </div>
</template>
<script>
    export default {
        name:"publish",

    }
</script>
<style lang="scss" scoped>
    .publish{
        width:100%;
        min-height:1.5rem;
        padding:.2rem;
        background:#fff;
        border-bottom:.16rem solid #E0E0E0;
        .pub-top{
            display:flex;
            justify-content:space-between;
            div{
                padding:0;
                img{
                    width:.5rem;
                    height:.5rem;
                    border-radius:.25rem;
                    
                }
                padding:0 .1rem;
            }
            
            p:nth-of-type(2){   
                display:flex;
                justify-content:space-between;
            }
        }
        .pub-but{
            h2{
                line-height:.5rem;
                font-size:.2rem;
                color:#BBFFBB;
            }
            p{
                text-indent:.3rem;
            }
            ul{
                display:flex;
                overflow-x:auto;
                padding:.2rem 0;
                li{
                   img{
                        width:1.3rem;
                        height:1rem;
                        display:inline-block;
                        margin-right:.16rem;
                    }
                    
                }
                li:nth-last-of-type(1){
                    img:nth-last-of-type(1){
                        margin:0;
                    }
                }
            }
            h3{
                display:flex;
                justify-content:space-between;
                b{
                    span{
                        padding-right:.1rem;
                    }
                }
            }
            
        }
    }
</style>