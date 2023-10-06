$(document).ready(function () {
    
    /*
     * product remove btn
     */
    $('.mg-remove-btn').click(function (e) {
        e.preventDefault();
        $(this).parents(".mg-ma-address-deatils").fadeOut('slow', function () {
            $(this).parents(".mg-ma-address-deatils").remove();
        });
    });
 });


