$('#metric').submit( function (e) {
    e.preventDefault();
    //var serializedData = $(this).serialize();
    //var user = $('input[name="user"]').val();
    //var weight = $('input[name="weight"]').val();
    //var height = $('input[name="height"]').val();
    //var bmi = $('input[name="bmi"]').val();
    //console.log(weight)

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: 'POST',
        url: "{% url 'bmi:metric' %}",
        data: {
            "user": $('input[name="user"]').val(), 
            "weight": $('input[name="weight"]').val(),
            'height': $('input[name="height"]').val(),
            'bmi': $('input[name="bmi"]').val(),
            //'csrfmiddlewaretoken': csrfmiddlewaretoken
        },         
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function(response){
            //reset form on success
            $('#metric').trigger('reset');
            $('#id_weight').focus();

            var result = JSON.parse(response['bmi']);
            alert('the data has been posted...' + result)
        },
        error: function(xhr, errmsg, err) {
          console.log(xhr.status + ":" + xhr.responseText)
        }
    });

});