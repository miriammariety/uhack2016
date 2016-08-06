var Search = function() {
	var $serviceList = $('#mobile-nav .service a')
	var serviceList = $.map($serviceList, function(item, i) {
		return $(item).html();
	}),
	init = function() {
		$('#search').on('change', function() {
			var searchTerm = $(this).val().toLowerCase();
			if (searchTerm === '') {
				$serviceList.parent().show();
			} else {
				$.each(serviceList, function(i, service) {
					if (service.toLowerCase().includes(searchTerm)) {
						$serviceList.eq(i).parent().show();
					} else {
						$serviceList.eq(i).parent().hide();
					}
				});
			}
		}).on('keyup', function() {
			$(this).trigger('change');
		});
	}

	return {
		init: init
	}
}();

Search.init();

var Content = function() {
	var container = $('#content-container'),
		containerParent = container.parent(),
		replace = function(data) {
			container.detach().html(data);
			containerParent.append(container);
		}

	return {
		replace: replace
	}
}();

var Services = function() {
	var init = function() {
		$('#mobile-nav .service a').on('click', function(e) {
			var service = $(e.target).html();
			$.ajax({
				url: ROOT_URL + 'services/' + service,
				beforeSend: function() {
					$('.loading').addClass('active');
				},
				success: function(data) {
					Content.replace(data);
				},
				complete: function() {
					$('.loading').removeClass('active');
				}
			});
		});
	}

	return {
		init: init
	}
}();

Services.init();

var Settings = function() {
	var init = function() {
		$('#')
	}

	return {
		init: init
	}
}();
