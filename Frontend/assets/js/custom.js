(function($) {
	'use strict';
	jQuery(document).on('ready', function(){
        // START MENU JS
        $(window).on('scroll', function() {
            if ($(this).scrollTop() > 10) {
                $('.navbar-light').addClass('menu-shrink');
            } else {
                $('.navbar-light').removeClass('menu-shrink');
            }
        });	

        $('.navbar-nav li a').on('click', function(e){
            var anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $(anchor.attr('href')).offset().top - 50
            }, 1500);
            e.preventDefault();
        });

        $(document).on('click','.navbar-collapse.show',function(e) {
            if( $(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle' ) {
                $(this).collapse('hide');
            }
        });		

        // Home Slider JS
        $('.home-slider').owlCarousel({
            items:1,
            loop:true,
            dots: false,
            nav:true,
            navText: [
                "<i class='icofont-thin-left'></i>",
                "<i class='icofont-thin-right'></i>"
            ]
        })

        // PROJECTS PORTFOLIO
        $('#Container').mixItUp();

        // Feedback slider
        $('.feedback-slider').owlCarousel({
            items: 1,
            loop: true,
            nav: false,
        })

        // Logo Slider JS
        $('.logo-slider').owlCarousel({
            loop:true,
            dots: false,
            nav:false,
            margin: 30,
            autoplay: true,
            responsive:{
                0:{
                    items:1
                },
                576:{
                    items:3
                },
                768:{
                    items:4
                },
                1000:{
                    items:5
                }
            }
        })

        // Wow JS
        new WOW().init();

        // Back top top btn JS
        $('body').append('<div id="toTop" class="top-btn"><i class="icofont-swoosh-up"></i></div>');
            $(window).scroll(function () {
                if ($(this).scrollTop() != 0) {
                    $('#toTop').fadeIn();
                } else {
                    $('#toTop').fadeOut();
                }
        }); 
        $('#toTop').click(function(){
            $("html, body").animate({ scrollTop: 0 }, 600);
            return false;
        });
    }); 	
    // PRELOADER
    jQuery(window).on('load',function(){
        jQuery(".loader-content").fadeOut(500);
    });
})(jQuery);

