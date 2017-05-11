$(document).ready(function(){
    $('#dropdown-cluster li').first().toggleClass("dropdown-select");
 $('#dropdown-cluster li').click(function(e)
    {
    $(this).toggleClass("dropdown-select");
    $(this).siblings().removeClass("dropdown-select");
    selected_cluster=$(this).index()+1
        if(hasSelected){
            onUserChange();
        }
    });
});
var hasSelected=false;
var selectedUser=0
var selected_cluster=1

var card_counter=0;
var cards=[];

function loadUsersId(usersID){
var selectElem=$('<select id="user-select">');
var defaultOption=$('<option value="" class="grey_color center-align" disabled selected >'+"Select User"+'</option>')
selectElem.append(defaultOption)
  usersID.forEach(function(user){
    var option=$('<option data-icon="/static/images/users-icon.png" class="left circle"  value='+user.userId+'>'+user.userId+'</option>')

    selectElem.append(option)
  });
   selectElem.change(onUserChange);
    $("#users-list").append(selectElem);
}


function onUserChange(){
   hasSelected=true;
    value=$("#user-select").val();
    loadPreloader(true);
    selectedUser=value;
        $.ajax({
            url: '/getUser',
            data:  JSON.stringify({
                        "value":selectedUser,
                        "selected_cluster":selected_cluster
                    }),
            type: 'POST',
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            success: function(response) {
               loadPreloader(false);
                $('#movies-rated').empty();
                loadContentForUserMovies(JSON.parse(response.defaultMovies));
                $('#movies-recommended').empty();
                loadContentForRecommendedMovies(JSON.parse(response.recommended))
            },
            error: function(error) {
                loadPreloader(false);
            }
        });
}

function loadPreloader(val){
    loader=$("#preloaderDiv");
    if(val){
    loader.removeClass("defaultloader");
    loader.addClass("prav-pre-con");
    $(".se-pre-con").fadeIn("slow");
    }else{
    $(".se-pre-con").fadeOut("slow");
    loader.removeClass("prav-pre-con");
    loader.addClass("defaultloader");

}
}
function loadContentForUserMovies(movies){
var cards=[];
movies.forEach(function(movie){
        var card_col=$('<div class="col s6 l3 style_prav_card">');
        var card=$('<div class="card black">');
        var imgCard=$('<div class="card-image">');
        var title=''
        if(movie.image_url=='NoImg'){
            src="/static/images/not_found.png"
        }
        else{
            src=movie.image_url
        }
         var img=$('<img src='+src+' alt="Still Loading....">');
         imgCard.append(img);
         if(movie.image_url=='NoImg'){
             title=$(' <span class="card-title">'+movie.title+'</span>');
            imgCard.append(title);
         }

        var card_row=$('<div class="row transparent">');
        var card_content=$('<div class="card-content white-text">');
        var genre=$('<p>'+movie.genres+'</p>');
        card_content.append(genre);
        card.append(imgCard);
        card.append(card_content)
        card_col.append(card);
        card_counter++;
        cards.push(card_col);
        if(card_counter==4){
                card_counter=0;
                cards.forEach(function(card){
                 card_row.append(card);
                          });
                          cards=[];
                }
        var ratingsDiv=$('<div class="chip">');
        var span=$('<span class="center-align">'+"Rated: "+movie.ratings+'</span>');
       imgCard.append(ratingsDiv);
        ratingsDiv.append(span);
        card_row.append(card_col)
        $('#movies-rated').append(card_row);
    });
}
function loadContentForRecommendedMovies(movies){
var cards=[];
movies.forEach(function(movie){
        var card_col=$('<div class="col s6 l3 style_prav_card">');
        var card=$('<div class="card black">');
        var imgCard=$('<div class="card-image">');
        var title=''

        if(movie.image_url=='NoImg'){
            src="/static/images/not_found.png"
        }
        else{
            src=movie.image_url
        }
         var img=$('<img src='+src+' alt="Still Loading....">');
         imgCard.append(img);
         if(movie.image_url=='NoImg'){
             title=$(' <span class="card-title">'+movie.title+'</span>');
            imgCard.append(title);
         }

        var card_row=$('<div class="row transparent">');
        var card_content=$('<div class="card-content white-text">');
        var genre=$('<p>'+movie.genres+'</p>');
        card_content.append(genre);
        card.append(imgCard);
        card.append(card_content)
        card_col.append(card);
        card_counter++;
        cards.push(card_col);
        if(card_counter==4){
                card_counter=0;
                cards.forEach(function(card){
                 card_row.append(card);
                          });
                          cards=[];
                }

        card_row.append(card_col)
        $('#movies-recommended').append(card_row);
    });
}