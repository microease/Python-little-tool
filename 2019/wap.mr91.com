<!DOCTYPE HTML>
<html>
<head>
<meta charset="gb2312">
<base href="http://wap.mr91.com/zhuanti/jgquban/">
    <title>Ƥ�뼤�����-���ڷǷ�ҽ������ҽԺ</title>
    <meta name="keywords" content="������ߣ�Ƥ�뼤��" />
    <meta name="description" content="�Ƿ�Ƥ�뼤����߲��÷䳲FOCUS����ʹ�����۽����ܹ���ɫ������ɼ�ΪϸС�Ŀ���������ٶȿ죬ʱ��̣������˶�Ƥ�������˼����ڼ��ʡ��������ߣ�0755-82281088" />
	<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0" />
<meta name="format-detection" content="telephone=no"/>
<meta content="yes" name="apple-mobile-web-app-capable"/>
<meta content="black" name="apple-mobile-web-app-status-bar-style"/>
    <script type="text/javascript" src="dist/swiper-4.1.0.min.js"></script>
    <link rel="stylesheet" type="text/css" href="dist/swiper-4.1.0.min.css" />
    <link rel="stylesheet" type="text/css" href="css/index.css" />
</head>
<body>
    <script type="text/javascript">
        (function (doc, win) {
            var docEl = doc.documentElement,
                resizeEvt =
                "orientationchange" in window ? "orientationchange" : "resize",
                recalc = function () {
                    var clientWidth = docEl.clientWidth;
                    if (!clientWidth) return;
                    if (clientWidth >= 640) {
                        docEl.style.fontSize = "100px";
                    } else {
                        docEl.style.fontSize = 100 * (clientWidth / 640) + "px";
                    }
                };
            if (!doc.addEventListener) return;
            win.addEventListener(resizeEvt, recalc, false);
            doc.addEventListener("DOMContentLoaded", recalc, false);
        })(document, window);

        function swip(obj) {
            var mySwiper = new Swiper(obj, {
                effect: "fade",
                direction: "horizontal",
                loop: true,
                speed: 200,
                // �����Ҫ��ҳ��
                pagination: {
                    el: ".swiper-pagination"
                },
                autoplay: {
                    delay: 1700, //1���л�һ��
                    disableOnInteraction: false
                }
            });
        }
    </script>
    <div class="box">
        <img src="./images/ban_01.jpg" alt="" />
        <a class="fo_28 fo_we co_blue" href="http://wap.mr91.com/onlinecall.html" target="_blank">
            <img src="./images/ban_02.jpg" alt="" />
        </a>
        <div class="tit1">�١��ߡ����� �򡰰ߡ�����</div>
        <div class="tit2"><img src="./images/tit2_01.jpg" alt="" /></div>
        <img class="p1_img" src="./images/p1_01.jpg" alt="" />
        <div class="tit1">������ߣ����Ĳȡ��ӡ�</div>
        <div class="tit2"><img src="./images/tit2_02.jpg" alt="" /></div>
        <div class="part2">
            <img src="./images/p2_01.jpg" alt="" /><br>
            <img class="pa2_img2" src="./images/p2_02.jpg" alt="" /><br>
            <img src="./images/p2_03.jpg" alt="" />
            <div class="btn">
                <a class="fo_28 fo_we co_blue" href="http://wap.mr91.com/onlinecall.html" target="_blank">���ϰߵ���ô���</a>
            </div>
        </div>
        <div class="tit1 p3_tit">�����䳲Ƥ�뼤��</div>
        <div class="tit2">�������������ʱ��</div>
        <img src="./images/p3_01.jpg" alt="" />
        <div class="tit1 p4_tit">Ƥ�뼤��Ϊ�����򡰰ߡ�����</div>
        <div class="tit2 p4_tit4"><img src="./images/tit2_03.jpg" alt="" /></div>
        <img src="./images/p4_01.jpg" alt="" />
        <div class="part4">
            <img src="./images/p4_02.jpg" alt="" /><br>
            <img src="./images/p4_03.jpg" alt="" /><br>
            <img src="./images/p4_04.jpg" alt="" />
            <div class="btn">
                <a class="fo_28 fo_we co_blue" href="http://wap.mr91.com/onlinecall.html" target="_blank">����ԤԼ���</a>
            </div>
        </div>
        <img src="./images/p5_01.jpg" alt="" />
        <div class="tit1">���������еġ���������</div>
        <div class="tit2 p4_tit4">Ƥ����� �죡�ݣ��ȣ�׼��</div>
        <div class="part5">
            <div class="swiper-container1">
                <ul class="swiper-wrapper">
                    <li class="swiper-slide">
                        <img src="./images/p5_02.jpg" alt="" />
                    </li>
                    <li class="swiper-slide">
                        <img src="./images/p5_03.jpg" alt="" />
                    </li>
                    <li class="swiper-slide">
                        <img src="./images/p5_04.jpg" alt="" />
                    </li>
                    <li class="swiper-slide">
                        <img src="./images/p5_05.jpg" alt="" />
                    </li>
                </ul>
                <div class="swiper-pagination"></div>
            </div>
            <div class="btn">
                <a class="fo_28 fo_we co_blue" href="http://wap.mr91.com/onlinecall.html" target="_blank">��ѯ�۸�</a>
            </div>
        </div>
        <script>
            swip(".swiper-container1");
        </script>
        <div class="part6">
            <img src="./images/p6_01.jpg" alt="" />
            <div class="tit1 p3_tit">���ߡ��߷��գ���ʰ���Ǽ�</div>
            <div class="tit2">�Ƿ�Ƥ�뼤����߹��̼�����</div>
            <div class="pa6">
                <img src="./images/p6_02.jpg" alt="" /><br>
                <img src="./images/p6_03.jpg" alt="" /><br>
                <img src="./images/p6_04.jpg" alt="" /><br>
                <img src="./images/p6_05.jpg" alt="" />
            </div>
            <div class="btn">
                <a class="fo_28 fo_we co_blue" href="http://wap.mr91.com/onlinecall.html" target="_blank">��Ҫ���</a>
            </div>
        </div>
        <img src="./images/p5_01.jpg" alt="" />
        <div class="tit1 p3_tit">���ˡ��ߡ� ����ǰ׷���</div>
        <div class="tit2 p7_tit"><img src="./images/tit2_04.jpg" alt="" /></div>
        <img src="./images/p7_02.jpg" alt="" />
        <div class="btn pa7_btn">
            <a class="fo_28 fo_we co_blue" href="http://wap.mr91.com/onlinecall.html" target="_blank">��Ҫ�¡��ߡ� ����ԤԼ</a>
        </div>
        <img src="./images/p8_01.jpg" alt="" />
        <div class="part8">
            <div class="tit1">�Ƿ����ҽʦ</div>
            <div class="tit2 p7_tit">Ҫ�¡��ߡ�������</div>
            <div class="swiper-container">
                <ul class="swiper-wrapper">
                    <li class="swiper-slide">
                        <img src="./images/p8_02.jpg" alt="" />
                    </li>
                    <!--li class="swiper-slide">
                        <img src="./images/p8_03.jpg" alt="" />
                    </li-->
                </ul>
                <div class="swiper-pagination"></div>
            </div>
        </div>
        <script>
            swip(".swiper-container");
        </script>
    </div>
		<script src="http://wap.mr91.com/newjs/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="http://wap.mr91.com/newjs/kf.js"></script>
</body>
</html>