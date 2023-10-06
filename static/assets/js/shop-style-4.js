$(document).ready(function(){
    /*
     * Shop page price range
     */
    $(".mg-price-filter-range").slider({
        range: true,
        min: 0,
        max: 500,
        values: [75, 300],
        slide: function (event, ui) {
            $(".mg-min-price").html("$" + ui.values[ 0 ]);
            $(".mg-max-price").html("$" + ui.values[ 1 ]);
        }
    });
    $(".mg-min-price").html("$" + $(".mg-price-filter-range").slider("values", 0));
    $(".mg-max-price").html("$" + $(".mg-price-filter-range").slider("values", 1));
    
    /*
     * show hide btn
     */
    $(".mg-hf-category-btn").click(function () {
        $(this).next().toggle("slidedown");
        $(this).toggleClass("mg-bottom-radius");
    });
    
    
    $(".mg-hf-main-filter-btn").click(function () {
        $(".mg-hf-filter-toggle").toggle("fade");
    });
});



