$(document).ready(function () {
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