var hideHelp=true;
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

$(document).ready(function() {
$("#searchbtn").click(function(){

});
$('#menu').on('click',function(e){
    displayHelp(hideHelp)

});
$("input[placeholder]").each(function () {
        $(this).attr('size', $(this).attr('placeholder').length);
    });
loadDefaultData();
});
function loadSpinner(val){
loader=$("#loaderDiv");
if(val){
loader.removeClass("defaultloaderDiv");
loader.addClass("se-pre-con");
$(".se-pre-con").fadeIn("slow");
}else{
$(".se-pre-con").fadeOut("slow");
loader.removeClass("se-pre-con");
loader.addClass("defaultloaderDiv");

}

}
//function storeResponse(output){
//$.ajax({
//        url:'../getcategories/',
//        type:'POST',
//        data:JSON.stringify(output),
//        success: function(response){
//          jsonObj=JSON.parse(response);
//          populateContents(jsonObj);
//        }
//});
function loadDefaultData(){
$.ajax({
        url:'../loadDefaultQuestions/',
        type:'GET',

        success: function(response){
          jsonObj=JSON.parse(response);

//          populateContents(jsonObj);
          constructDefaultquestions(jsonObj)
        }
});
}

function constructDefaultquestions(jsonQuestions){
  var datalist=$('<datalist id="questionsTxt"  class="dropdown-content"></datalist>');
   for (var i in jsonQuestions) {
            var option=$("<option id="+i+">"+ jsonQuestions[i] +"</option>");
            datalist.append(option)
        }
  datalist.appendTo("[name='searchtxt']");
   $("input[name='searchtxt']").on('input', function(e){
    var selected = $(this).val();
    onOptionSelect(selected)
});
}
function onOptionSelect(selected){
    $.ajax({
        url:'../onSelectOfList/',
        type:'POST',
        data:selected,
         beforeSend: function(){
        loadSpinner(true);

   },
        success: function(response){
        try{
        loadSpinner(false);
          jsonObj=JSON.parse(response);

           $('#resultview').empty()
          if(jsonObj.res_type==0){

          generateColorfulCardsForTopics(jsonObj)
          }
          if(jsonObj.res_type==1){

          generateColorfulCardsForRecentGroups(jsonObj)
          }
          if((jsonObj.res_type==2)){

          generateColorfulCardsForRecentGroups(jsonObj)
          }

        }
        catch(err){
        loadSpinner(false);
        }
        }
});

}
function generateColorfulCardsForTopics(jsonObj){
    var containerRow=$('<div class="row">');
jsonObj.contents.forEach(function(item){
    var colsDiv=$('<div class="col s12 m3">');
           var div= $('<div class="card-panel teal hoverable">');
            var span=$('<span class="white-text">'+item+'</span>');
            div.append(span);
            colsDiv.append(div);
            containerRow.append(colsDiv);
   });
$('#resultview').append(containerRow);
}

function generateColorfulCardsForRecentGroups(jsonObj){
    jsonObj.contents.forEach(function(item){
    var containerDiv=$('<div class="card small col s12 m4 l2 hoverable">')
           var div= $('<div class="card-content">');
            var span=$('<span class="card-title activator grey-text text-darken-4">'+item.name+'</span>');
            div.append(span);
            containerDiv.append(div)
            var contentReveal=$('<div class="card-reveal">');
            var revealSpan=$('<span class="card-title grey-text text-darken-4">'+item.name+'</span>');
            var rating=$('<p>'+"Rating: "+item.rating+"</p>");
            var i=$('<i class="material-icons right">close</i>')
            var date=new Date(item.created)
            var created=$('<p>'+"Created: "+date.toLocaleDateString()+"</p>")
            revealSpan.append(i)
            contentReveal.append(revealSpan);
            contentReveal.append(rating);
            contentReveal.append(created);
            containerDiv.append(contentReveal);
            $('#resultview').append(containerDiv);
   });

}
var safeColors = ['00','33','66','99','cc','ff'];
var rand = function() {
    return Math.floor(Math.random()*6);
};
var randomColor = function() {
    var r = safeColors[rand()];
    var g = safeColors[rand()];
    var b = safeColors[rand()];
    return "#"+r+g+b;
};
function displayHelp(val){
    if(val){
        $('.tap-target').tapTarget('open');
        hideHelp=false;
    }else{
        $('.tap-target').tapTarget('close');
        hideHelp=true;
    }
}
