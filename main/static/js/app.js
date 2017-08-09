(function (d, w, c) { (w[c] = w[c] || []).push(function() { try { w.yaCounter45100650 = new Ya.Metrika({ id:45100650, clickmap:true, trackLinks:true, accurateTrackBounce:true, webvisor:true }); } catch(e) { } }); var n = d.getElementsByTagName("script")[0], s = d.createElement("script"), f = function () { n.parentNode.insertBefore(s, n); }; s.type = "text/javascript"; s.async = true; s.src = "https://mc.yandex.ru/metrika/watch.js"; if (w.opera == "[object Opera]") { d.addEventListener("DOMContentLoaded", f, false); } else { f(); } })(document, window, "yandex_metrika_callbacks");

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-101618267-1', 'auto');
ga('require', 'displayfeatures');
ga('send', 'pageview');

<!-- Rating@Mail.ru counter -->
var _tmr = window._tmr || (window._tmr = []);
_tmr.push({id: "2914361", type: "pageView", start: (new Date()).getTime()});
(function (d, w, id) {
  if (d.getElementById(id)) return;
  var ts = d.createElement("script"); ts.type = "text/javascript"; ts.async = true; ts.id = id;
  ts.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//top-fwz1.mail.ru/js/code.js";
  var f = function () {var s = d.getElementsByTagName("script")[0]; s.parentNode.insertBefore(ts, s);};
  if (w.opera == "[object Opera]") { d.addEventListener("DOMContentLoaded", f, false); } else { f(); }
})(document, window, "topmailru-code");


$(function() {
    function onNavbar() {
        if (window.innerWidth >= 768) {
            $(".navbar-custom .dropdown").on("mouseover", function(){
                $(".dropdown-toggle", this).next(".dropdown-menu").show();
            }).on("mouseout", function(){
                $(".dropdown-toggle", this).next(".dropdown-menu").hide();
            });
            $(".dropdown-toggle").click(function() {
                if ($(this).next(".dropdown-menu").is(":visible")) {
                    window.location = $(this).attr("href");
                }
            });
        } else {
            $(".navbar-default .dropdown").off("mouseover").off("mouseout");
        }
    }
    $(window).resize(function() {
        onNavbar();
    });
    onNavbar();
});

function preventDoubleClick(form)
{
    form.submit.disabled = true;
    return true;
}

$(window).scroll(function() {
    if ($(this).scrollTop() >= 50) {
        $('#return-to-top').fadeIn(200);
    } else {
        $('#return-to-top').fadeOut(200);
    }
});
$('#return-to-top').click(function() {
    $('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
});