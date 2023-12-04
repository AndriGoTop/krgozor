$(function(){
    $('.right-header-mob').click(function (e) { 
        e.preventDefault();
        $('#menu-mob').toggle();
    });
    $('.choose-city').click(function (e) {
        e.preventDefault();
        $('.cities').toggle();
    });
})
