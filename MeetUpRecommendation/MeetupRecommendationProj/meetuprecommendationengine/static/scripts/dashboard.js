$(document).ready(function() {
$("#searchbtn").click(function(){
$.ajax({
        url:"https://api.meetup.com/2/categories?offset=0&format=json&photo-host=public&page=20&order=shortname&desc=false&sig_id=225559964&sig=1efa3f6254d446aa80e717d413db9ad50916e9cb",
         crossDomain: true,
            dataType: 'jsonp',
        success: function(response){
           output = response;
            storeResponse(output);
        }
});
});
});
function storeResponse(output){
$.ajax({
        url:'../getcategories/',
        type:'POST',
        data:JSON.stringify(output),
        success: function(response){
          alert(response);

        }
});

}
function getCookie(name) {
    var cookieValue = null;
    if(document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for(var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if(cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    global: true,
    beforeSend: function(xhr, settings) {
        if(!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xhr.setRequestHeader("Content-Type", 'application/x-www-form-urlencoded; charset=UTF-8');
        }
    }
});