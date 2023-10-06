$(document).ready(function () {
    
    /*
     * Quantity counter
     */

    $('.mg-qty-plus-btn').click(function (e) {
        e.preventDefault();
        var quantity = parseInt($(this).parents(".mg-quanitity-option-section").find('.mg-qty-number').val());
        $(this).parents(".mg-quanitity-option-section").find('.mg-qty-number').val(quantity + 1);
    });

    $('.mg-qty-minus-btn').click(function (e) {
        e.preventDefault();
        var quantity = parseInt($(this).parents(".mg-quanitity-option-section").find('.mg-qty-number').val());
        if (quantity > 1) {
            $(this).parents(".mg-quanitity-option-section").find('.mg-qty-number').val(quantity - 1);
        }
    });
    /*
     * product remove btn
     */
    $('.mg-product-remove-btn').click(function (e) {
        e.preventDefault();
        $(this).parents("tr").fadeOut('slow', function () {
            $(this).parents("tr").remove();
        });
    });
 });