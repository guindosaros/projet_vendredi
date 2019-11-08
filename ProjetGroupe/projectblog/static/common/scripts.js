
(function ($) {

    "use strict";
	
	
	// ISOTOPE
	
	$(window).on('load', function(){
		
		// ISOTOPE PORTFOLIO WITH FILTER
		if(isExists('.p-grid-isotope')){
			$('.p-grid-isotope').isotope({
				// set itemSelector so .grid-sizer is not used in layout
				itemSelector: '.p-item',
				percentPosition: true,
				masonry: {
					columnWidth: '.grid-sizer', 
					
				},
			})
		 
		}
	
	});
	
	// DROPDOWN MENU
	
	var winWidth = $(window).width();
	dropdownMenu(winWidth);
	
	$(window).on('resize', function(){
		winWidth = $(window).width();
		dropdownMenu(winWidth);
		
	});
	

				
	$('[data-menu]').on('click', function(){
		
		var mainMenu = $(this).data('menu');
		
		$(mainMenu).toggleClass('visible-menu');
		
	});
	
	
	enableSwiper();
	
})(jQuery);


function dropdownMenu(winWidth){
	
	if(winWidth > 767){
		
		$('.main-menu li.drop-down').on('mouseover', function(){
			var $this = $(this),
				menuAnchor = $this.children('a');
				
			menuAnchor.addClass('mouseover');
			
		}).on('mouseleave', function(){
			var $this = $(this),
				menuAnchor = $this.children('a');
				
			menuAnchor.removeClass('mouseover');
		});
		
	}else{
		
		$('.main-menu li.drop-down > a').on('click', function(){
			
			if($(this).attr('href') == '#') return false;
			if($(this).hasClass('mouseover')){ $(this).removeClass('mouseover'); }
			else{ $(this).addClass('mouseover'); }
			return false;
		});
	}
	
}

function enableSwiper(){
	
	if ( isExists('.swiper-container') ) {
		
		$('.swiper-container').each(function (index) {
			
			var swiperDirection 			= $(this).data('swiper-direction'),
				swiperSlidePerView			= $(this).data('swiper-slides-per-view'),
				swiperBreakpoints			= $(this).data('swiper-breakpoints'),
				swiperSpeed					= $(this).data('swiper-speed'),
				swiperCrossFade				= $(this).data('swiper-crossfade'),
				swiperLoop					= $(this).data('swiper-loop'),
				swiperAutoplay 				= $(this).data('swiper-autoplay'),
				swiperMousewheelControl 	= $(this).data('swiper-wheel-control'),
				swipeSlidesPerview 			= $(this).data('slides-perview'),
				swiperMargin 				= parseInt($(this).data('swiper-margin')),
				swiperSlideEffect 			= $(this).data('slide-effect'),
				swiperAutoHeight 			= $(this).data('autoheight'),
				swiperScrollbar 			= ($(this).data('scrollbar') ? $(this).parentsUntil('.swiper-area').find('.swiper-scrollbar') : null);
				//swiperScrollbar 			= ($(this).data('scrollbar') ? $(this).find('.swiper-scrollbar') : null);
				swiperScrollbar 			= (isExists(swiperScrollbar) ? swiperScrollbar : null),
				swprResponsive				= $(this).data('swpr-responsive'); 
		
	
			
			var swiper = new Swiper($(this)[0], {
				
				
				pagination			: $(this).find('.swiper-pagination'),
				
				slidesPerView		: ( swiperSlidePerView ? swiperSlidePerView : 1 ),
				direction			: ( swiperDirection ? swiperDirection : 'horizontal'),
				loop				: ( swiperLoop ? swiperLoop : false),
				nextButton			: '.swiper-button-next',
				prevButton			: '.swiper-button-prev',
				autoplay			: ( swiperAutoplay ? swiperAutoplay : false),
				paginationClickable	: true,
				spaceBetween		: ( swiperMargin ? swiperMargin : 0),
				mousewheelControl	: ( (swiperMousewheelControl) ? swiperMousewheelControl : false),
				mousewheelControl: true,
				scrollbar			: ( swiperScrollbar ? swiperScrollbar : null ),
				scrollbarHide		: false,
				speed				: ( swiperSpeed ? swiperSpeed : 1000 ),
				autoHeight			: ( (swiperAutoHeight == false) ? swiperAutoHeight : true ),
				effect				: ( swiperSlideEffect ? swiperSlideEffect : 'coverflow' ),
				fade				: { crossFade: swiperCrossFade ? swiperCrossFade : false },
				breakpoints			: {
											1200: 	{ slidesPerView: swprResponsive[3] ? swprResponsive[3] : 1, },
											992: 	{ slidesPerView: swprResponsive[2] ? swprResponsive[2] : 1, },
											768: 	{ slidesPerView: swprResponsive[1] ? swprResponsive[1] : 1, },
											576: 	{ slidesPerView: swprResponsive[0] ? swprResponsive[0] : 1, }
											
										},
			});
			
			$('.swiper-container').hover(function(){
				swiper.stopAutoplay();
			}, function(){
				swiper.startAutoplay();
			});
			
			
		});
		
		
	}
}

function isExists(elem){
	if ($(elem).length > 0) { 
		return true;
	}
	return false;
}
