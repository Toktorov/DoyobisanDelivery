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
     * mobile filter open
     */
     $(".mg-filter-btn").click(function (event) {
        event.preventDefault();
        $(".mg-sidebar-filters").addClass("mg-filter-open");
    });
    $(".mg-filter-close-btn").click(function (event) {
        event.preventDefault();
        $(".mg-sidebar-filters").removeClass("mg-filter-open");
    });
    $(".mg-sidenav-overlay").click(function (event) {
        event.preventDefault();
        $(".mg-sidebar-filters").removeClass("mg-filter-open");
    });
});



