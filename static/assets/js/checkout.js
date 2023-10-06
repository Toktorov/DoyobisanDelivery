$(document).ready(function () {
    
    /*
     * Quantity counter
     */

    $('.mg-qty-plus-btn').click(function (e) {
        e.preventDefault();
        var quantity = parseInt($('.mg-qty-number').val());
        $('.mg-qty-number').val(quantity + 1);
    });

    $('.mg-qty-minus-btn').click(function (e) {
        e.preventDefault();
        var quantity = parseInt($('.mg-qty-number').val());
        if (quantity > 1) {
            $('.mg-qty-number').val(quantity - 1);
        }
    });
    /*
     *add coupon code 
     */
    $(".mg-coupon-link").click(function (e) {
        e.preventDefault();
        $(".mg-coupon-field form input").focus();
        $("html, body").animate({
            scrollTop: $(".mg-coupon-field").offset().top
        }, 100);
    });
 });



