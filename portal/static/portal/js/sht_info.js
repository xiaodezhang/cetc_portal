var preventIndex = 1;

var commonEvent = function(){
	initFullPageConfig();
	firstPageAnimate();
	clickEventListener();
}

var initFullPageConfig = function(){
	$('#fullpage').fullpage({
	    //verticalCentered: true,
	    anchors: ['anchor1', 'anchor2', 'anchor3', 'anchor4', 'anchor5', 'anchor6', 'anchor7', 'footer'],
	    menu: '#menu',
	    css3: true,
	    scrollingSpeed: 700,
	    afterLoad: function(anchorLink, index){
	    },
	    onLeave: function(index, nextIndex, direction){
	    	if(index == 1 && direction == 'down'){
					preventIndex = 1;
					$('.main_page').addClass('notFirstPage');
	    	}
	    	if(index == 2 && nextIndex == 1){
	    		$('.main_page').removeClass('notFirstPage');
	    	}
	    	if(nextIndex == 2){
	    		//离开其他页面，进入section1页面，就是第二屏页面，开始渲染动画
	    		initParamAnimation();
	    	}
	    	if(nextIndex == 8){
	    		//应该是进入倒数第二屏的时候，不要取消效果，应该就是 section + index，应该是id数目加2
	    		$('.main_page #section6').addClass('pre_active');
	    	}
	    	if(index == 8){
	    		//离开倒数第二屏的时候，取消辅助辅助效果，这个方法和上面协助使用
	    		$('.main_page #section6').removeClass('pre_active');	
	    	}
	    },
	    afterRender: function(){
	    	//初始化渲染完成之后
	    	//initParamAnimation();
	    }
	});
}

var firstPageAnimate = function(duration){
	//setTimeout($('.wave_4').animate({'background-size': '160%'}, 3000), 1200);
}

var clickEventListener = function(){
	$('.modal_menu_nav .close_btn').on('click', function(e){
		$('.modal_menu_nav').fadeOut(600);
	});

	$('.page_navigater .menu_icon').on('click', function(){
		$('.modal_menu_nav').fadeIn(600);
	});

	$('.page_navigater .page_link_list').on('click', function(){
		return;
		var page_link = $(this);
		if(page_link.hasClass('active')){
			return;
		} else {
			$('.page_navigater .page_link_list.active').removeClass('active');
			page_link.addClass('active');
		}
	});
}

var initParamAnimation = function(){
 var delay = 0.245;
 var step = 0.045;
 var fontItemList = $('#section1').find('.ani_font');
 for(var k = 0;k < fontItemList.length;k++){
 	var item = $(fontItemList[k]);
 	delay = delay + step;
 	item.css({
 		'transition-delay': delay + 's',
 		'opacity': 1,
 		'transform': 'translateY(0)'
 	})
 }
 fontItemList.css({
 	'opacity': 1,
 	'transform': 'translateY(0)'
 });
}
