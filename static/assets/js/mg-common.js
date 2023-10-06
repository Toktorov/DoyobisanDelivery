$(document).ready(function () {
    /*
     * Discount Slider
     */
    $('.mg-discount-slider-main').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        dots: false,
        arrows: false,
        responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 1,
            infinite: false,
            dots: false
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: true,
            dots: false
          }
        },
        {
          breakpoint: 575,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            infinite: true,
            dots: false
          }
        },
        {
          breakpoint: 372,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            infinite: true,
            dots: false
          }
        }
    ]
    });
    /*
     * background image with text overlay slider
     */
    $('.mg-slider-section').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        initialSlide: 1,
        arrows: false,
        customPaging: function(slick,index) {
        return '<a>' + (index + 1) + '</a>';
    }
        
    });
    /*
     * Quick view modal
     */
    $(".mg-quick-view-modal-btn").click(function (event) {
        event.preventDefault();
        $("#mg-quick-view-modal").modal("show");
        setTimeout(function () {
            $('.mg-quick-view-slider').slick('slickSetOption', {}, true);
        }, 300);
    });
    /*
     * product grid carousel
     */
    $('.mg-product-grid-main-inner').slick({
        slidesToShow: 4,
        slidesToScroll: 4,
        dots: true,
        infinite: true,
        arrows: false,
        customPaging: function(slick,index) {
            return '<a></a>';
        },
        responsive: [
        {
          breakpoint: 1199,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: false,
            dots: true
        }
          },
          {
          breakpoint: 991,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            infinite: false,
            dots: true
          }
        },
          {
          breakpoint: 511,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            infinite: false,
            dots: true
          }
        }
    ]
    });
    /*
     *testimonial section slider
     */
    $('.mg-testimonial-main').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        dots: false,
        arrows: true,
        appendArrows:$('.mg-testimonial-btn'),
        prevArrow: '<button type="button" class="slick-prev"><img src="assets/images/icons/Testimonial-left-arrow.svg"></button>',
        nextArrow: '<button type="button" class="slick-next"><img src="assets/images/icons/Testimonial-right-arrowd.svg"></button>',
        customPaging: function(slick,index) {
            return '<a></a>';
        },
        responsive: [
        {
          breakpoint: 991,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            infinite: false,
            dots: true
        },
          }
          ,
          {
          breakpoint: 575,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            infinite: false,
            dots: true
          }
        }
        ]
    });
    /*
     * scroll down btn
     */
    /*
     *add coupon code 
     */
    $(".mg-scroll-down-link").click(function (e) {
        e.preventDefault();
        $("html, body").animate({
            scrollTop: $(".mg-feature-section").offset().top
        }, 100);
    });
     
});

