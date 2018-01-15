<template>
    <div class="newPerson-know">
         <new-head></new-head> 
         <div class="newPerson-box">
           <div class="newPerson-box1">
               <p class="box1-p">新人帮助</p>
               <p class="box1-p1">APP使用常见问题详解</p>
           </div>
            <div class="newPerson-box2">
               Q1:怎么注册，登录肉多多
           </div>
            <div class="newPerson-box3">
              1.点击最下方我的
              <img class="img1" src="/static/images/know3.png"/>
              2.根据提示完成登录或注册
              <img class="img2" src="/static/images/know4.png"/>
           </div>
           <div class="newPerson-box2">
               Q2:为什么我被禁言了
           </div>
           <p class="box1-p2">
               对于多次不在规定板块发布交易帖的卖家,管理将根据具体情况做出1-3天的禁言警告, 情节严重的直接关进小黑屋哦。具体禁言时长可在消息页面查看
           </p>
           <div class="newPerson-box2">
               Q3:如何删帖
           </div>
           <p class="box1-p2">
               暂时不支持用户自己删帖，可自行编辑内容，若特殊情况删帖，请联系在线客服
           </p>
           <div class="newPerson-box2">
               Q4:我想在肉多读做广告怎么做
           </div>
           <p class="box1-p2">
              肉多多 还有很多功能等您发掘，如果您感觉哪里操作让你感到非常不爽，请联系客服，以便我们尽快改进，如果您觉得肉多多为您带来了方便，您在应用商城为我们的付出做个好评哦
           </p>
        </div>
    </div>
</template>

<script>
    import NewHead from "./newHead-know"
    export default {
        name:"newPerson-know",
         components:{
          NewHead
        }
    }        
</script>

<style lang="scss" scoped>
    .newPerson-know{
        width:100%;
        height:100%;
        position: fixed;
        top:0;
        z-index:1000;
        background:#fff;
    }
</style>