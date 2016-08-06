function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$('#upload-trigger').click(function() {
    $("#id_image").click();
    return false;
});

$("#id_image").change(function() {
    var file = document.getElementById('id_image').files[0];
    var validTypes = ["image/png", "image/jpg", "image/jpeg", "image/gif"];

    if (typeof file == "undefined") {
        return false;
    }

    if (validTypes.indexOf(file.type) === -1) {
        $('#modal-title').text('Error!');
        $('#modal-message').text("Only jpeg/jpg, png, and gif are supported.");
        $('#modal').openModal();
    } else {
        var formData = new FormData();
        formData.append("csrfmiddlewaretoken", csrftoken);
        formData.append("image", file);
        $.ajax({
            url: '/user/settings/imageupload',
            type: 'post',
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            enctype: 'multipart/form-data',
            success: function(response) {
                var image = document.getElementById("user_image");
                if (response) {
                    image.src = response;
                }
            }
        });
    }
    return false;
});