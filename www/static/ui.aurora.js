/*!
 * jQuery UI Aurora 0.8
 *
 * Copyright 2012
 * Licensed under the GPL Version 2 license.
 *
 * http://киноархив.com/ru/разное/jqueryui-aurora-ru.html
 * http://киноархив.com/en/others/jqueryui-aurora-en.html
 */
;(function($, window, document, undefined){
	var methods = {
		init: function(options){
			options = $.extend({}, $.fn.aurora.settings, options);

			var elem = $(this),
				hidden = false,
				close_btn = '',
				hide_btn = '';

			if (options.show_close_btn) {
				close_btn = ' <a href="javascript:void(0);" class="close_msg">'+options.close_btn_text+'</a>';
			}

			if (options.show_hide_btn) {
				hide_btn = ' <a href="javascript:void(0);" class="hide_msg">'+options.hide_btn_text+'</a>';
			}

			if (options.leave_only_first === true && $('.ui-message').length != 0) {
				var ui_msg = $('.ui-message');

				if (options.msg_type_global_container != '') {
					ui_msg.eq(0).find(' > div > div').removeProp('class').prop('class', 'ui-corner-all ui-state-'+options.msg_type_global_container);
				}
				if (options.msg_type_global_icon != '') {
					ui_msg.eq(0).find('span:first').removeProp('class').prop('class', 'ui-icon ui-icon-'+options.msg_type_global_icon);
				}
				if (options.text != '') {
					ui_msg.eq(0).find('span:last').html(options.text+hide_btn+close_btn);
				}
				$('.ui-message:hidden').eq(0).animate({
					opacity: 'toggle'
				}, options.speed, options.effect, options.onComplete);
			} else {
				// Prepare parameters
				if (options.msg_type_custom === true) {
					container_class = options.msg_type_custom_container;
					icon_class = options.msg_type_custom_icon;
				} else {
					container_class = options.msg_type_global_container;
					icon_class = options.msg_type_global_icon;
				}

				if (options.font_override === true) {
					if (options.font_style.style != undefined) {
						span_text_style = options.font_style.style;
						span_text_selector = '';
					} else {
						span_text_style = '';
						span_text_selector = ' class="'+options.font_style.selector+'"';
					}
				} else {
					span_text_style = 'overflow: hidden; display: block; padding-left: 5px;';
					span_text_selector = '';
				}

				var html = '<div class="ui-message" style="display: none; margin: '+options.message_margin+';"><div class="ui-widget"><div style="padding: '+options.div_padding+';" class="ui-state-'+container_class+' ui-corner-all"><div style="margin: '+options.div_margin+'"><span style="float: left; margin-right: '+options.span_margin+';" class="ui-icon ui-icon-'+icon_class+'"></span><span style="'+span_text_style+'"'+span_text_selector+'>'+options.text+hide_btn+close_btn+'</span></div></div></div></div>';

				if (options.create_before && options.create_before != '') {
					var div = $(html).insertBefore(options.create_before).animate({
						opacity: 'toggle'
					}, options.speed, options.effect, options.onComplete);
				} else if (options.prepend && options.prepend != '') {
					var div = $(html).prependTo(options.prepend).animate({
						opacity: 'toggle'
					}, options.speed, options.effect, options.onComplete);
				} else if (options.append && options.append != '') {
					var div = $(html).appendTo(options.append).animate({
						opacity: 'toggle'
					}, options.speed, options.effect, options.onComplete);
				} else if (options.create_after && options.create_after != '') {
					var div = $(html).insertAfter(options.create_after).animate({
						opacity: 'toggle'
					}, options.speed, options.effect, options.onComplete);
				} else {
					var _elem = elem.length > 0 ? elem : 'body';

					var div = $(html).appendTo(_elem).animate({
						opacity: 'toggle'
					}, options.speed, options.effect, options.onComplete);
				}

				$('.hide_msg').live('click', function(e){
					options.onHide();
					var parent = $(this).closest('.ui-message');

					parent.find('.ui-corner-all').css('height', '26');
					parent.css({
						'width': '46',
						'height': '34'
					});
					parent.find('.ui-icon').prop('title', options.hidden_tooltip).css('cursor', 'pointer');
					$(this).parent('span').hide();
					hidden = true;
				});

				$('span.ui-icon').live('click', function(e){
					if (hidden === true) {
						var parent = $(this).closest('.ui-message');
						parent.css({
							'width': '100%',
							'height': 'auto'
						});
						parent.find('span:last').show();
						parent.find('.ui-corner-all').css('height', 'auto');
						$(this).css('cursor', 'default').prop('title', '');
					}
				});

				$('.close_msg').live('click', function(e){
					options.onClose();
					$(this).closest('.ui-message').remove();
				});
			}

			if (options.auto_hide || options.auto_remove) {
				if (elem.length > 0) {
					setTimeout(function(){
						if (options.auto_hide) {
							elem.children('.ui-message').hide();
						} else if (options.auto_remove) {
							elem.children('.ui-message').remove();
						}
					}, options.auto_hide_timeout);
				} else {
					setTimeout(function(){
						if (options.auto_hide) {
							$(div).hide();
						} else if (options.auto_remove) {
							$(div).remove();
						}
					}, options.auto_hide_timeout);
				}
			}

			return this;
		},
		toggleVis: function(options){
			options = $.extend({}, $.fn.aurora.toggleVisSettings, options);

			if (options.action == 'hide') {
				if (options.elems_indexes.length == 0) {
					$('.ui-message').animate({
						opacity: 'hide'
					}, options.speed, options.effect);
				} else {
					for (var i=0; i < options.elems_indexes.length; i++) {
						$('.ui-message').eq(options.elems_indexes[i]).animate({
							opacity: 'hide'
						}, options.speed, options.effect);
					}
				}
			} else if (options.action == 'show') {
				if (options.elems_indexes.length == 0) {
					$('.ui-message').animate({
							opacity: 'show'
						}, options.speed, options.effect);
				} else {
					for (var i=0; i < options.elems_indexes.length; i++) {
						$('.ui-message').eq(options.elems_indexes[i]).animate({
							opacity: 'show'
						}, options.speed, options.effect);
					}
				}
			} else {
				if (options.elems_indexes != '') {
					for (var i=0; i < options.elems_indexes.length; i++) {
						$('.ui-message').eq(options.elems_indexes[i]).animate({
							opacity: 'toggle'
						}, options.speed, options.effect);
					}
				} else {
					$('.ui-message').animate({
						opacity: 'toggle'
					}, options.speed, options.effect);
				}
			}

			return this;
		},
		toggleType: function(options){
			options = $.extend({}, $.fn.aurora.toggleTypeSettings, options);

			if (typeof options.elems_indexes[0] === 'number' || options.elems_indexes == 'all') {
				if (options.msg_type_container != '') {
					if (options.elems_indexes == 'all') {
						$('.ui-message').find(' > div > div').removeProp('class').prop('class', 'ui-corner-all ui-state-'+options.msg_type_container);
					} else {
						for (var i=0; i < options.elems_indexes.length; i++) {
							$('.ui-message').eq(options.elems_indexes[i]).find(' > div > div').removeProp('class').prop('class', 'ui-corner-all ui-state-'+options.msg_type_container);
						}
					}
				}

				if (options.msg_type_icon != '') {
					if (options.elems_indexes == 'all') {
						$('.ui-message').find('span:first').removeProp('class').prop('class', 'ui-icon ui-icon-'+options.msg_type_icon);
					} else {
						for (var i=0; i < options.elems_indexes.length; i++) {
							$('.ui-message').eq(options.elems_indexes[i]).find('span:first').removeProp('class').prop('class', 'ui-icon ui-icon-'+options.msg_type_icon);
						}
					}
				}

				if (options.text != '') {
					if (options.elems_indexes == 'all') {
						$('.ui-message').find('span:last').html(options.text);
					} else {
						for (var i=0; i < options.elems_indexes.length; i++) {
							$('.ui-message').eq(options.elems_indexes[i]).find('span:last').html(options.text);
						}
					}
				}
			}

			return this;
		},
		destroy: function(options){
			options = $.extend({}, $.fn.aurora.destroySettings, options);

			if (typeof options.elems_indexes[0] === 'number' || options.elems_indexes == 'all') {
				if (options.elems_indexes == 'all') {
					$('body').find('.ui-message').remove();
				} else {
					$('.ui-message').filter(function(i){
						return options.elems_indexes.indexOf(i) != -1;
					}).remove();
				}
			}

			return this;
		}
	}

	$.fn.aurora = function(method){
		if (methods[method]) {
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if (typeof method === 'object' || !method) {
			return methods.init.apply(this, arguments);
		} else {
			$.error('Method "' +  method + '" does not exist!');
		}
	}

	$.aurora = function(method){
		return $.fn.aurora(method);
	}

	$.fn.aurora.settings = {
		text: '',
		msg_type_global_container: 'highlight',
		msg_type_global_icon: 'info',
		msg_type_custom: false,
		msg_type_custom_container: 'highlight',
		msg_type_custom_icon: 'info',
		font_override: false,
		font_style: {
			style: '', // By default this is "font-size: 0.8em; font-weight: normal;"
			selector: '' // Only class name
		},
		message_margin: '0.4em 0 0 0',
		div_padding: '0 0.5em',
		div_margin: '5px !important',
		span_margin: '0 0.3em 0 0',
		create_before: '',
		create_after: '',
		prepend: '',
		append: '',
		effect: 'swing',
		speed: 400,
		onComplete: function(){},
		onClose: function(){},
		onHide: function(){},
		leave_only_first: false,
		show_close_btn: false,
		close_btn_text: '[Close]',
		show_hide_btn: false,
		hide_btn_text: '[Hide]',
		hidden_tooltip: 'Click for show',
		auto_hide: false,
		auto_remove: false,
		auto_hide_timeout: 2000
	}
	$.fn.aurora.toggleVisSettings = {
		action: 'toggle',
		elems_indexes: [],
		effect: 'swing',
		speed: 400
	}
	$.fn.aurora.toggleTypeSettings = {
		msg_type_container: '',
		msg_type_icon: '',
		elems_indexes: [],
		text: ''
	}
	$.fn.aurora.destroySettings = {
		elems_indexes: []
	}
})(jQuery, window, document);