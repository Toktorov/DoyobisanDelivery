$(document).ready(function(){
    /*
     * show hide
     */
    $(".mg-forget-password").click(function(){
        $(".mg-login-form").hide();
        $(".mg-forget-password-form").show();
      });

      $(".mg-redirect-login-form").click(function(){
        $(".mg-login-form").show();
        $(".mg-forget-password-form").hide();
      });
});



