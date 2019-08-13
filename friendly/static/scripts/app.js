// ------------------------- CSRF Token ------------------------- //

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
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
// ------------------------- end CSRF Token ------------------------- //

// ------------------------- Cached DOM Elements ------------------------- //

const connectBtn = $('.connect-btn')

// ------------------------- Event Listeners ------------------------- //

connectBtn.on('click', function(event){
    event.preventDefault();
    $.ajax({
        url: '/match/create/',
        method: 'POST',
        data: {
            'profile_id': connectBtn.attr('id')
        },
        success: function(response){
            $(`<h1 class="response">${response}</h1>`).insertBefore($('.button-container'))
            setTimeout(() => window.location.reload(), 2000)
        }
    });
});