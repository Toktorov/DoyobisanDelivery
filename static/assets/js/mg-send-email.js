$(document).ready(function () {
    $('.mg-contact-form-main').validate({
        rules: {
            Name: {
                required: true
            },
            Email: {
                required: true,
                email: true
            },
            Subject: {
                required: true,
            },
            Message: {
                required: true
            }
        },
        submitHandler: function (form) {
            $('.mg-contact-form-main').trigger('reset');
            $('.alert-msg').fadeIn();
            return false;
        }
    })
});