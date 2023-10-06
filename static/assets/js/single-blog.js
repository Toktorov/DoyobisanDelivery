$(document).ready(function(){
    /*
     *add coupon code 
     */
    $(".mg-comment-reply").click(function (e) {
        e.preventDefault();
        $(".mg-comment-form form input.mg-commnet-field").focus();
        $("html, body").animate({
            scrollTop: $(".mg-comment-form").offset().top
        }, 100);
    });
});




