<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--     <link rel="stylesheet" href="css/01.css"> -->
    <title>王者荣耀官网</title>
    <!-- <meta name="keyword"> 搜索关键字 -->
    <style>
        body {
    font-size: 16px;
    font-family: Arial, "Microsoft YaHei";
    background-image: url("../img/bg.jpg");
    /* background-size: 100% auto; */
    background-position: center;
    /* 鑳屾櫙鍥剧墖y杞村亸绉� */
    background-position-y: 60px;
    /* 鑳屾櫙鍥剧墖浠呮樉绀轰竴娆� */
    background-repeat: no-repeat;
}

.container {
    width: 1200px;
    /* 椤甸潰灞呬腑 */
    margin: 0 auto;
    /* 琛岄珮 */
    line-height: 60px;
    /* 鑷�傚簲鍐呭 */
    /* overflow: hidden; */
}

#header {
    /* 寮规�у竷灞�鐨勪袱绔榻� */
    height: 60px;
    display: flex;
    justify-content: space-between;
}

#header .left {
    text-align: center;
}

#header .left div {
    float: left;
}

#header .right {
    text-align: center;
}

#header .right div {
    float: right;
    line-height: 60px;
    margin-right: 30px;
}

.shouhu {
    width: 30px;
    height: 30px;
    display: inline-block;
    /*鍨傜洿灞呬腑*/
    vertical-align: middle;
    background-image: url("../img/title_sprite.png");
    /* 鍥剧墖鍋忕Щ */
    background-position: -30px 0px;
}

#level1 {
    width: 100%;
    margin-top: -10px;
    background: rgba(0, 0, 0, 0.8);
    color: white;
}

#level1 .container2 {
    width: 1200px;
    height: 100px;
    display: flex;
    justify-content: space-between;
}

#level1 .logo {
    margin-top: 20px;
    margin-left: 60px;
    width: 100px;
}

#level1 .nav1 {
    width: 1050px;
    margin-top: 0px;
    margin-left: 80px;
    display: flex;
    justify-content: space-between;
}

#level1 .nav1 li {
    list-style: none;
    width: 150px;
    text-align: center;
}

.nav1 li:hover {
    background: linear-gradient(rgba(0, 0, 0, 0), rgba(255, 220, 0, 0.3));
    border-bottom: 3px solid gold;
    cursor: pointer;
    color: gold;
}



#level1 .nav1 .big {
    font-size: 20px;
}

#level1 .nav1 .small {
    color: grey;
    font-size: 13px;
}

#level1 .nav1 li:hover .small {
    color: gold;
}


#level1 .login {
    width: 180px;
    line-height: 42px;
    margin-right: -300px;
    text-align: right;
    vertical-align: middle;
}

#level1 .login .left {
    width: 42px;
    height: 42px;
    border-radius: 42px;
    border: 1px solid gold;
    float: left;
    margin-top: 30px;
}

#level1 .login .right {
    float: left;
    text-align: left;
    margin-left: 10px;
    vertical-align: middle;
    /* display: inline-block; */
}

#level1 .login .right .text {
    font-size: 15px;
    margin-top: 20px;
}

#level1 .login .right .sub {
    font-size: 12px;
    color: grey;
    margin-top: -30px;
}

#level2 {
    width: 100%;
    overflow: hidden;
    background: rgba(0, 0, 0, 0.5);
    display: none;
}

#level2>ul {
    width: 1000px;
    display: flex;
    list-style: none;
    justify-content: space-between;
    margin-left: 220px;
}

#level2>ul>li {
    width: 100px;
    text-align: center;
}

#level2>ul>li>ul>li {
    width: 110px;
    color: white;
    list-style: none;
    clear: both;
    line-height: 30px;
    font-size: 12px;
}

#level2>ul>li>ul>li a {
    text-decoration: none;
    color: white;
}

#level2>ul>li>ul>li a:hover {
    text-decoration: underline;
    color: gold;
}


#level2 .hot,
#level2 .new {
    width: 25px;
    height: 25px;
    display: inline-block;
    vertical-align: middle;
    background-image: url(../img/sprite.png);
}

#level2 .hot {
    background-position: -160px -65px;
}

#level2 .new {
    background-position: -140px -65px;
}

#core {
    width: 1170px;
    display: flex;
    justify-content: space-between;
    /* background-image: url(../img/); */
    /* background-repeat: no-repeat; */
    margin-top: 200px;
    margin-left: 200px;
}

#core .banner {
    width: 605px;
    height: 342px;
    display: flex;
    justify-content: space-between;
}

#core .banner .img {
    width: 605px;
    height: 298px;
    margin-left: -40px;
}

#core .banner .img li {
    list-style: none;
}

#core .banner .title {
    width: 605px;
    height: 44px;
    background-color: black;
    color: gray;
    margin-top: -16px;
}

#core .banner .title ul {
    display: flex;
    /* justify-content: space-between; */
    margin-left: -40px;
}

#core .banner .title ul li {
    /* 涓変釜flex鐨勫睘鎬х畝鍐� */
    flex: 1;
    text-align: center;
    line-height: 44px;
    list-style: none;
}

#core .banner .title ul li:hover {
    background-color: gray;
    color: gold;
}

/* #core .banner .title .on {
    background-color: gray;
    color: gold;
} */

#core .infos {
    width: 325px;
    height: 342px;
    background: rgba(0, 0, 0, 0.7);
    margin-top: 15px;
}

#core .infos .titles ul {
    display: flex;
    border-bottom: 1px solid black;
    color: gray;
    /* margin-left: -10px; */
}

#core .infos .titles ul li {
    flex: 1;
    width: auto;
    text-align: center;
    list-style: none;
    line-height: 50px;
    margin-top: -10px;
    /* border-bottom: 1px solid black; */
    /* margin-left: -30px; */
}

#core .infos .titles ul li:hover {
    /* background-color: gray; */
    color: gold;
    border-bottom: 1px solid gold;
}


#core .infos .list {
    width: 325px;
}

#core .infos .list .bd {
    list-style: none;
    display: flex;
    justify-content: space-between;
    margin-left: -30px;
    overflow: hidden;
}

#core .infos .list .bd .ul01 {
    list-style: none;
    margin-left: -30px;
}

#core .infos .list .title {
    width: 280px;
    height: 30px;
    color: gold;
    font-size: 16px;
    background-color: gray;
    text-align: left;
    margin-top: 1px;
    /* margin-left: -15px; */
}

#core .infos .list .ul01 li {
    display: inline-block;
    width: 250px;
    height: 30px;
    /* 鍐呭寮哄埗鍦ㄤ竴琛� */
    white-space: nowrap;
    /* 瓒呭嚭閮ㄥ垎闅愯棌 */
    overflow: hidden;
    /* 闅愯棌閮ㄥ垎鐢ㄧ渷鐣ュ彿琛ㄧず */
    text-overflow: ellipsis;
    margin-right: 45px;
}

#core .infos .list .date {
    float: right;
    margin-top: -30px;
}

#core .infos .list .remen,
#core .infos .list .gonggao,
#core .infos .list .xinwen,
#core .infos .list .huodong,
#core .infos .list .saishi {
    border-width: 1px;
    border-style: solid;
    border-radius: 5px;
}

#core .infos .list .remen {
    border-color: red;
    color: red;
}

#core .infos .list .gonggao {
    border-color: gold;
    color: gold;
}
#core .infos .list .xinwen {
    border-color: blue;
    color: blue;
}
#core .infos .list .huodong {
    border-color: pink;
    color: pink;
}
#core .infos .list .saishi {
    border-color: wheat;
    color: wheat;
}


#core .downlond {
    width: 240px;
    height: 342px;
    float: left;
    margin-left: 1px;
    margin-top: 15px;
}

#core .downlond .xiazai {
    width: 240px;
    height: 130px;
    background: url(../img/sprite.png);
    background-position: 0 -218px;
    background-repeat: no-repeat;
}

#core .downlond .duiju {
    width: 240px;
    height: 107px;
    background: url(../img/sprite.png);
    background-position: 0 -351px;
    background-repeat: no-repeat;
}

#core .downlond .tiyan {
    width: 240px;
    height: 105px;
    background: url(../img/sprite.png);
    background-position: 0 -463px;
    background-repeat: no-repeat;
}

#core .nianling {
    float: left;
    margin-left: -5px;
}

#core .nianling img {
    width: 100%;
    height: 100%;
}

#core .nianling .shiling {
    width: 53px;
    height: 68px;
}

#core .nianling .fangchenmi {
    width: 53px;
    height: 53px;
}


#zone .container3 {
    margin-top: 40px;
    margin-left: 160px;
    /* display: flex;
    justify-content: space-between; */
}

#zone .container3 ul li {
    width: 292px;
    height: 134px;
    display: block;
    float: left;
    list-style: none;
    overflow: hidden;
    cursor: pointer;
}

#zone .container3 img {
    width: 291px;
    height: 134px;
    transform: scale(1, 1);
    transition: all 0.5sxx;
}

#zone .container3 img:hover {
    width: 100%;
    height: 100%;
    transform: scale(1.1, 1.1);
}

/* #denglu {
    width: 100%;
    height: 100%; */
/* 鐩稿瀹氫綅 */
/* position: fixed;
    left: 0;
    top: 0; */
/* 灞傚彔鏍峰紡锛堟鏁颁紭鍏堢骇楂樺湪涓婏紝璐熸暟浼樺厛绾т綆鍦ㄤ笅锛� */
/* z-index: 1;
    display: flex;
    justify-content: center;
    align-items: center;
} */

#aside .da {
    z-index: 1;
    position: fixed;
    top: 300px;
    right: 150px;
}

#aside .da .daji {
    width: 165px;
    height: 145px;
    /* z-index: 1;
    position: fixed;
    top: 450px;
    right: 150px; */
}

#aside .da .aside {
    margin-top: -16px;
    margin-left: 16px;
}

#aside .da .aside ul li {
    list-style: none;
}

#aside .da .aside .tu1 {
    width: 120px;
    height: 134px;
    background-image: url(../img/r_all2022.png);
    background-position: -240px 0;
}

#aside .da .aside .tu2 {
    width: 120px;
    height: 38px;
    background-image: url(../img/r_all2022.png);
    background-position: -240px -133px;
}

#aside .da .aside .tu3 {
    width: 120px;
    height: 38px;
    background-image: url(../img/r_all2022.png);
    background-position: -120px -120px;
}

#aside .da .aside .tu4 {
    width: 120px;
    height: 38px;
    background-image: url(../img/r_all2022.png);
    background-position: -120px -159px;
}

#aside .da .aside .tu5 {
    width: 120px;
    height: 38px;
    background-image: url(../img/r_all2022.png);
    background-position: -120px 0;
}

#content .container4 {
    display: flex;
    justify-content: space-between;
    width: 1170px;
    margin-left: 200px;
}

#content .container4 .left {
    width: 800px;
    margin-right: 30px;
}

#content .container4 .left .nr1 {
    display: flex;
    justify-content: space-between;
}

#content .container4 .left .img1 {
    width: 200px;
    height: 27px;
    float: left;
}

#content .container4 .left .img2 {
    color: gray;
    cursor: pointer;
}

#content .container4 .left .img2:hover {
    color: gold;
}

#content .container4 .left .nr2 ul {
    display: flex;
    margin-left: -35px;
}

#content .container4 .left .nr2 li {
    list-style: none;
    clear: both;
    text-align: center;
}

#content .container4 .left .nr2 .ul1 li {
    background-color: antiquewhite;
    border-bottom: 3px solid antiquewhite;
    flex: 1;
}

#content .container4 .left .nr2 .ul1 li:hover {
    border-bottom: 3px solid gold;
}

#content .container4 .left .nr2 .ul2 ul {
    text-align: left;
}

#content .container4 .left .nr2 .ul2 li {
    background-color: white;
    border-radius: 20px;
    margin-left: 20px;
}

#content .container4 .left .nr2 .ul2 li:hover {
    background-color: gold;
    color: white;
}

#content .container4 .left .nr2 .ul3 {
    display: flex;
    justify-content: space-between;
}

#content .container4 .left .nr2 .div3 {
    width: 800px;
    height: 200px;
}


#content .container4 .left .nr2 .ul3 li {
    text-align: left;
    margin-left: 15px;
}

#content .container4 .left .nr2 .ul3 li img {
    width: 100%;
    height: 100%;
}

#content .container4 .right {
    width: 300px;
}

#content .container4 .right .nr1 {
    display: flex;
    justify-content: space-between;
}

#content .container4 .right .img1 {
    width: 200px;
    height: 27px;
    float: left;
}

#content .container4 .right .img2 {
    color: gray;
    cursor: pointer;
}

#content .container4 .right .img2:hover {
    color: gold;
}

#content .container4 .right .nr2 ul {
    display: flex;
    margin-left: -35px;
}

#content .container4 .right .nr2 li {
    list-style: none;
    clear: both;
    text-align: center;
}


#content .container4 .right .nr2 .ul1 li {
    background-color: antiquewhite;
    border-bottom: 3px solid antiquewhite;
    flex: 1;
}

#content .container4 .right .nr2 .ul1 li:hover {
    border-bottom: 3px solid gold;
}

#content .container4 .right .nr2 .ul2 ul {
    text-align: left;
}

#content .container4 .right .nr2 .ul2 li {
    background-color: white;
    border-radius: 20px;
    margin-left: 20px;
}

#content .container4 .right .nr2 .ul2 li:hover {
    background-color: gold;
    color: white;
}

#content .container4 .right .img3 img {
    width: 300px;
    height: auto;
}

#content .container4 .right .img3 span {
    font-size: 20px;
}

#content .container4 .right .h3 {
    width: 300px;
    height: 80px;
    border: 1px solid black;
    border-top: 1px solid white;
}

#content .container4 .right .h3 p {
    margin-top: -10px;
}

#content .container4 .right .ul3 {
    display: flex;
    justify-content: space-between;
}

#content .container4 .right .ul3 li {
    list-style: none;
}

#content .container4 .right .ul4 {
    display: flex;
    justify-content: space-between;
}

#content .container4 .right .ul4 li {
    list-style: none;
    margin-left: -38px;
}

#dibu {
    width: 1300px;
    /* height: 500px; */
    float: left;
    margin-left: 200px;
}

#dibu .zb {
    width: 550px;
    float: left;
}

#dibu .zb ul {
    margin-left: -40px;
}

#dibu .zb li {
    list-style: none;
    float: left;
    margin-right: 10px;
    font-size: 12px;
}

#dibu .yb {
    width: 700px;
    float: right;
}

#dibu .yb ul {
    margin-left: -41px;
}

#dibu .yb ul li {
    list-style: none;
    float: left;
    text-align: left;
    margin-right: 20px;
    /* font-size: 12px; */
}

#dibu .yb .yb1 {
    font-size: 10px;
}

#dibu .yb .yb2 {
    font-size: 12px;
}
    </style>
</head>

<body>
    <form action="" method="post"></form>
    <!-- 页眉 -->
    <header id="header" class="container">
        <!-- 页眉左区域 -->
        <div class="left">
            <div>
                <img src="img/tg-logo.png" alt="">
            </div>
            <div class="bigimg">
                <img src="img/nizhan.jpg" alt="">
            </div>
        </div>
        <!-- 页眉右区域 -->
        <div class="right">
            <div>
                <span>腾讯游戏排行榜</span>
            </div>
            <div>
                <span class="shouhu"></span>成长守护平台
            </div>
        </div>
    </header>
    <!-- 一级导航 -->
    <!-- nav定义导航容器 -->
    <nav id="level1">
        <div class="container2">
            <div class="logo">
                <img src="img/logo.png" alt="">
            </div>
            <ul class="nav1">
                <li>
                    <p class="big">游戏资料</p>
                    <p class="small">DATE</p>
                </li>
                <li>
                    <p class="big">内容中心</p>
                    <p class="small">CONTENTS</p>
                </li>
                <li>
                    <p class="big">赛事中心</p>
                    <p class="small">MATCH</p>
                </li>
                <li>
                    <p class="big">百态王者</p>
                    <p class="small">SULTUER</p>
                </li>
                <li>
                    <p class="big">社区互动</p>
                    <p class="small">COMMUNITY</p>
                </li>
                <li>
                    <p class="big">玩家支持</p>
                    <p class="small">PLAYER</p>
                </li>
                <li>
                    <p class="big">IP新游</p>
                    <p class="small">NEM&nbsp;GAMES</p>
                </li>
            </ul>

            <div class="login">
                <div class="left">
                    <img src="img/login.png" alt="">
                </div>
                <div class="right">
                    <p class="text">欢迎登录</p>
                    <p class="sub">登陆后查看战绩</p>
                </div>
            </div>
        </div>
    </nav>
    <!-- 二级导航 -->
    <nav id="level2">
        <ul>
            <li>
                <ul>
                    <li> <a href="">版本介绍</a> </li>
                    <li> <a href="">游戏介绍</a> </li>
                    <li> <a href="">英雄资料</a> </li>
                    <li><span class="hot"></span> <a href="">爆料站</a> </li>
                    <li><span class="new"></span> <a href="">世界观体验站</a> </li>
                    <li> <a href="">游戏壁纸</a> </li>
                </ul>
            </li>


            <li>
                <ul>
                    <li> <a href="">攻略中心</a> </li>
                    <li> <a href="">开放素材库</a> </li>
                    <li><span class="new"></span> <a href="">内容共创平台</a> </li>
                    <li><span class="new"></span> <a href="">手语打法参考</a> </li>
                </ul>
            </li>


            <li>
                <ul>
                    <li><span class="hot"></span> <a href="">挑战者杯</a> </li>
                    <li> <a href="">kpl</a> </li>
                    <li> <a href="">世界冠军杯</a> </li>
                    <li><span class="hot"></span> <a href="">全国大赛</a> </li>
                    <li> <a href="">女子公开赛</a> </li>
                    <li> <a href="">k甲联赛</a> </li>
                    <li><span class="new"></span> <a href="">王者赛宝</a> </li>
                    <li> <a href="">赛事数据</a> </li>
                </ul>
            </li>


            <li>
                <ul>
                    <li> <a href="">荣耀传承</a> </li>
                    <li> <a href="">王者文化站</a> </li>
                    <li> <a href="">万千世界</a> </li>
                    <li> <a href="">星光殿堂</a> </li>
                    <li><span class="new"></span> <a href="">IP共创计划</a> </li>
                    <li> <a href="">商户特权</a> </li>
                    <li><span class="new"></span> <a href="">龙翼王者卡</a> </li>
                </ul>
            </li>


            <li>
                <ul>
                    <li><span class="hot"></span> <a href="">创意互动营</a> </li>
                    <li><span class="hot"></span> <a href="">王者营地</a> </li>
                    <li> <a href="">微信圈子</a> </li>
                    <li> <a href="">官方微博</a> </li>
                    <li> <a href="">微信公众号</a> </li>
                    <li> <a href="">手Q订阅号</a> </li>
                </ul>
            </li>


            <li>
                <ul>
                    <li> <a href="">腾讯游戏防沉迷</a> </li>
                    <li><span class="shouhu"></span> <a href="">成长守护平台</a> </li>
                    <li> <a href="">对局环境情报站</a> </li>
                    <li> <a href="">客服专区</a> </li>
                    <li> <a href="">礼包兑换</a> </li>
                    <li> <a href="">自助服务</a> </li>
                </ul>
            </li>


            <li>
                <ul>
                    <li><span class="new"></span> <a href="">王者荣耀世界</a> </li>
                    <li><span class="new"></span> <a href="">代号破晓</a> </li>
                    <li><span class="new"></span> <a href="">代号启程</a> </li>
                </ul>
            </li>
        </ul>
    </nav>
    <!-- 核心区域 section定义文档的节 -->
    <section id="core">
        <div class="banner slidebox">
            <div>
                <div class="img">
                    <ul class="bd">
                        <li><img src="img/banner/banner1.jpg" alt=""></li>
                        <li><img src="img/banner/banner2.jpg" alt=""></li>
                        <li><img src="img/banner/banner3.jpg" alt=""></li>
                        <li><img src="img/banner/banner4.jpg" alt=""></li>
                        <li><img src="img/banner/banner5.jpg" alt=""></li>
                    </ul>

                </div>
                <div class="title hd">
                    <ul>
                        <li class="on">S29全新赛季 </li>
                        <li>品质升级共创</li>
                        <li>上营地开顺风局</li>
                        <li>春季选秀招募</li>
                        <li>大神教你玩</li>
                    </ul>
                </div>
            </div>
            <!-- 公告区 -->
            <div class="infos">
                <div class="titles hd">
                    <ul>
                        <li>热门</li>
                        <li>新闻</li>
                        <li>公告</li>
                        <li>活动</li>
                        <li>赛事</li>
                        <li>···</li>
                    </ul>
                </div>
                <div class="list">
                    <ul class="bd">
                        <li>
                            <ul class="ul01">
                                <li class="title">9月22日正式版本更新公告</li>
                                <li> <span class="remen">热门</span> 互动小任务第18期-金秋主题头相框</li> <span class="date">
                                    09/26</span>
                                <li> <span class="remen">热门</span> 姜子牙英雄品质升级共享-技能特效展示</li> <span class="date">
                                    09/23</span>
                                <li> <span class="remen">热门</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date"> 09/16</span>
                                <li> <span class="remen">热门</span> 蔡小姬探班手记|百里守约·碎云皮肤特效展示</li> <span class="date">
                                    09/15</span>
                                <li> <span class="gonggao">公告</span> 9月14日全服不停服更新公告</li> <span class="date">09/13</span>
                                <li> <span class="remen">热门</span> 姜子牙英雄品质升级共享-技能</li> <span class="date">09/13</span>
                                <li> <span class="remen">热门</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date">09/09</span>
                            </ul>
                        </li>
                        <li>
                            <ul class="ul01">
                                <li class="title">9月22日正式版本更新公告2</li>
                                <li> <span class="xinwen">新闻</span> 互动小任务第18期-金秋主题头相框</li> <span class="date">
                                    09/26</span>
                                <li> <span class="xinwen">新闻</span> 姜子牙英雄品质升级共享-技能特效展示</li> <span class="date">
                                    09/23</span>
                                <li> <span class="xinwen">新闻</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date"> 09/16</span>
                                <li> <span class="xinwen">新闻</span> 蔡小姬探班手记|百里守约·碎云皮肤特效展示</li> <span class="date">
                                    09/15</span>
                                <li> <span class="xinwen">新闻</span> 9月14日全服不停服更新公告</li> <span class="date">09/13</span>
                                <li> <span class="xinwen">新闻</span> 姜子牙英雄品质升级共享-技能</li> <span class="date">09/13</span>
                                <li> <span class="xinwen">新闻</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date">09/09</span>
                            </ul>
                        </li>
                        <li>
                            <ul class="ul01">
                                <li class="title">9月22日正式版本更新公告4</li>
                                <li> <span class="gonggao">公告</span> 互动小任务第18期-金秋主题头相框</li> <span class="date">
                                    09/26</span>
                                <li> <span class="gonggao">公告</span> 姜子牙英雄品质升级共享-技能特效展示</li> <span class="date">
                                    09/23</span>
                                <li> <span class="gonggao">公告</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date"> 09/16</span>
                                <li> <span class="gonggao">公告</span> 蔡小姬探班手记|百里守约·碎云皮肤特效展示</li> <span class="date">
                                    09/15</span>
                                <li> <span class="gonggao">公告</span> 9月14日全服不停服更新公告</li> <span class="date">09/13</span>
                                <li> <span class="gonggao">公告</span> 姜子牙英雄品质升级共享-技能</li> <span class="date">09/13</span>
                                <li> <span class="gonggao">公告</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date">09/09</span>
                            </ul>
                        </li>
                        <li>
                            <ul class="ul01">
                                <li class="title">9月22日正式版本更新公告3</li>
                                <li> <span class="huodong">活动</span> 互动小任务第18期-金秋主题头相框</li> <span class="date">
                                    09/26</span>
                                <li> <span class="huodong">活动</span> 姜子牙英雄品质升级共享-技能特效展示</li> <span class="date">
                                    09/23</span>
                                <li> <span class="huodong">活动</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date"> 09/16</span>
                                <li> <span class="huodong">活动</span> 蔡小姬探班手记|百里守约·碎云皮肤特效展示</li> <span class="date">
                                    09/15</span>
                                <li> <span class="huodong">活动</span> 9月14日全服不停服更新公告</li> <span class="date">09/13</span>
                                <li> <span class="huodong">活动</span> 姜子牙英雄品质升级共享-技能</li> <span class="date">09/13</span>
                                <li> <span class="huodong">活动</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date">09/09</span>
                            </ul>
                        </li>
                        <li>
                            <ul class="ul01">
                                <li class="title">9月22日正式版本更新公告5</li>
                                <li> <span class="saishi">赛事</span> 互动小任务第18期-金秋主题头相框</li> <span class="date">
                                    09/26</span>
                                <li> <span class="saishi">赛事</span> 姜子牙英雄品质升级共享-技能特效展示</li> <span class="date">
                                    09/23</span>
                                <li> <span class="saishi">赛事</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date"> 09/16</span>
                                <li> <span class="saishi">赛事</span> 蔡小姬探班手记|百里守约·碎云皮肤特效展示</li> <span class="date">
                                    09/15</span>
                                <li> <span class="saishi">赛事</span> 9月14日全服不停服更新公告</li> <span class="date">09/13</span>
                                <li> <span class="saishi">赛事</span> 姜子牙英雄品质升级共享-技能</li> <span class="date">09/13</span>
                                <li> <span class="saishi">赛事</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date">09/09</span>
                            </ul>
                        </li>
                        <li>
                            <ul class="ul01">
                                <li class="title">9月22日正式版本更新公告6</li>
                                <li> <span class="remen">热门</span> 互动小任务第18期-金秋主题头相框</li> <span class="date">
                                    09/26</span>
                                <li> <span class="remen">热门</span> 姜子牙英雄品质升级共享-技能特效展示</li> <span class="date">
                                    09/23</span>
                                <li> <span class="remen">热门</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date"> 09/16</span>
                                <li> <span class="remen">热门</span> 蔡小姬探班手记|百里守约·碎云皮肤特效展示</li> <span class="date">
                                    09/15</span>
                                <li> <span class="gonggao">公告</span> 9月14日全服不停服更新公告</li> <span class="date">09/13</span>
                                <li> <span class="remen">热门</span> 姜子牙英雄品质升级共享-技能</li> <span class="date">09/13</span>
                                <li> <span class="remen">热门</span> 峡谷夏日特别行动之狄某有话说</li> <span class="date">09/09</span>
                            </ul>
                        </li>
                    </ul>

                </div>
            </div>
            <!-- 下载专区 -->
            <div class="downlond">
                <div class="xiazai"></div>
                <div class="duiju"></div>
                <div class="tiyan"></div>
            </div>
            <div class="nianling">
                <div class="shiling"><img src="img/shiling.png" alt=""></div>
                <div class="fangchenmi"><img src="img/fangchenmi.png " alt=""></div>
            </div>
        </div>
    </section>
    <!-- 专区 -->
    <section id="zone">
        <div class="container3">
            <ul>
                <li><img src="img/zhuanqu/gfblz.jpg" alt=""></li>
                <li><img src="img/zhuanqu/rycc.png" alt=""></li>
                <li><img src="img/zhuanqu/sszq.jpg" alt=""></li>
                <li><img src="img/zhuanqu/wzyd.jpg" alt=""></li>
            </ul>
            <br><br><br><br><br><br><br><br>
        </div>
    </section>
    <!-- 登录 -->
    <section id="denglu">
        <div class="box"></div>
    </section>
    <!-- 悬浮 -->
    <section>

    </section>
    <!-- 侧边栏 -->
    <aside id="aside">


        <!-- <a href="http://www.baidu.com" target="_blank">百度</a>
    <input type="hidden" name="隐藏域"> -->
        <div class="da">
            <div class="daji">
                <span><img src="img/r_dj.png" alt=""></span>
            </div>
            <div class="aside">
                <div>
                    <ul>
                        <li class="tu1"></li>
                        <li class="tu2"></li>
                        <li class="tu3"></li>
                        <li class="tu4"></li>
                        <li class="tu5"></li>
                    </ul>
                </div>
            </div>
        </div>
    </aside>

    <section id="content">
        <div class="container4">
            <div class="left">
                <div class="nr1">
                    <div class="img1">
                        <span><img src="img/nrzx/neirong.png" alt=""> <strong>内容中心</strong> </span>
                    </div>
                    <div class="img2">
                        <span>+更多</span>
                    </div>
                </div>
                <div class="nr2">
                    <ul class="ul1">
                        <li>精品栏目</li>
                        <li>赛事精品</li>
                        <li>英雄攻略</li>
                    </ul>
                    <ul class="ul2">
                        <li>最新</li>
                        <li>峡谷大气层</li>
                        <li>狄仁杰封神录</li>
                        <li>游走基本法</li>
                        <li>野王修炼手册</li>
                    </ul>
                    <div>
                        <div class="div3">
                            <ul class="ul3">
                                <li><img src="img/nrzx/01.jpg" alt=""> <br> <span>峡谷大气层</span> </li>
                                <li><img src="img/nrzx/02.png" alt=""> <br> <span>峡谷大气层</span> </li>
                                <li><img src="img/nrzx/03.png" alt=""> <br> <span>峡谷大气层</span> </li>
                                <li><img src="img/nrzx/04.png" alt=""> <br> <span>峡谷大气层</span> </li>
                            </ul>
                        </div>
                        <div class="div3">
                            <ul class="ul3">
                                <li><img src="img/nrzx/05.png" alt=""> <br> <span>峡谷大气层</span></li>
                                <li><img src="img/nrzx/05.png" alt=""> <br> <span>峡谷大气层</span></li>
                                <li><img src="img/nrzx/05.png" alt=""> <br> <span>峡谷大气层</span></li>
                                <li><img src="img/nrzx/05.png" alt=""> <br> <span>峡谷大气层</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="right">
                <div class="nr1">
                    <div class="img1">
                        <span><img src="img/nrzx/neirong.png" alt=""> <strong>英雄/皮肤</strong> </span>
                    </div>
                    <div class="img2">
                        <span>+更多</span>
                    </div>
                </div>
                <div class="nr2">
                    <ul class="ul1">
                        <li>最新英雄</li>
                        <li>最新皮肤</li>
                        <li>周免英雄</li>
                    </ul>
                </div>
                <div class="img3">
                    <img src="img/nrzx/laixiao.png" alt="">
                    <div class="h3">
                        <h3>新英雄：莱西奥</h3>
                        <p>上线时间2023.01.03</p>
                    </div>
                </div>
                <div>
                    <ul class="ul4">
                        <li><img src="img/nrzx/zhaohuaizhen.png" alt=""></li>
                        <li><img src="img/nrzx/zhaohuaizhen.png" alt=""></li>
                        <li><img src="img/nrzx/zhaohuaizhen.png" alt=""></li>
                        <li><img src="img/nrzx/zhaohuaizhen.png" alt=""></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    <div id="dibu">
        <img src="" alt="">
        <hr>
        <div class="zb">
            <ul>
                <li>抵制不良游戏</li>
                <li>抵制不良游戏</li>
                <li>抵制不良游戏</li>
                <li>抵制不良游戏</li>
                <li>抵制不良游戏</li>
                <li>抵制不良游戏</li>
            </ul>
            <ul>
                <li>抵制不良游戏</li>
                <li>抵制不良游戏</li>
            </ul>
            <br> <br>
            <p>《王者荣耀》全部背景故事发生于架空世界“王者大陆”中。相关人物、地理、事件均为艺术创作，并非正史。若因观看王者故事对相关历史人物产生兴趣，建议查阅正史记载。</p>
        </div>
        <div class="yb">
            <p>
                腾讯互动娱乐|服务条款|王者荣耀隐私保护指引|儿童隐私保护指引|腾讯游戏招聘|腾讯游戏客服|游戏列表|广告服务及商务合作</p>
            <br>
            <ul>
                <li class="yb1">COPYRIGHT © 1998 - 2023 TENCENT. ALL RIGHTS RESERVED.</li>
                <li class="yb2">腾讯公司版权所有 &nbsp;网络游戏行业防沉迷自律公约</li>
            </ul>
        </div>
    </div>
    <script src="js/jquery.min.js"></script>
    <script src="js/jquery.SuperSlide.2.1.js"></script>
    <script src="js/01.js"></script>
</body>
</html>
