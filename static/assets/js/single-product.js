$(document).ready(function () {
    /*
     * Single product silder
     */
    $('.mg-single-product-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots:true,
        fade: true
    });
    
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
 });

