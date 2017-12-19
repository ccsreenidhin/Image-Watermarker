var current = 0;
var li = document.getElementsByClassName("song");
$(document).ready(function() {
    current = 0;
    var x = $(li[current]).attr("data-m")
    $("#mplay").attr("src", x);
    $("#mplay")[0].play();
});

$("#mplay").on('ended', function(){
  if (li[current+1]){
    current+=1;
    var x = $(li[current]).attr("data-m")
    $("#mplay").attr("src", x);
    $("#mplay")[0].play();
  }
  else{
    current=0;
    var x = $(li[current]).attr("data-m")
    $("#mplay").attr("src", x);
    $("#mplay")[0].play();
  }
});

$(".rew").on('click', function(){
  if (li[current-1]){
    current-=1;
    var x = $(li[current]).attr("data-m")
    $("#mplay").attr("src", x);
    $("#mplay")[0].play();
  }
  else{
    current=li.length-1;
    var x = $(li[current]).attr("data-m")
    $("#mplay").attr("src", x);
    $("#mplay")[0].play();
  }
});

$(".fwd").on('click', function(){
  if (li[current+1]){
    current+=1;
    var x = $(li[current]).attr("data-m")
    $("#mplay").attr("src", x);
    $("#mplay")[0].play();
  }
  else{
    current=0;
    var x = $(li[current]).attr("data-m")
    $("#mplay").attr("src", x);
    $("#mplay")[0].play();
  }
});

$("#plist button").on('click', function(){
    var x = $(this).attr("data-m")
    $("#mplay").attr("src", x);
    $("#mplay")[0].play();
    for(i=0;i<li.length;i++){
    if (this==li[i]){
      current = i;
    }
    }

});
