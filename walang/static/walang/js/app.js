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
