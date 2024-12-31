$(document).ready(function() {
  
  $('.btn').addClass("click");
  $('.sidebar').addClass("show");


  $('.btn').click(function(){
    $(this).toggleClass("click");
    $('.sidebar').toggleClass("show");
  });

  $('.feat-btn').click(function(){
    $('nav ul .feat-show').toggleClass("show");
    $('nav ul .first').toggleClass("rotate");
  });

  $('.serv-btn').click(function(){
    $('nav ul .serv-show').toggleClass("show1");
    $('nav ul .second').toggleClass("rotate");
  });

  $('.sale-btn').click(function(){
    $('nav ul .sale-show').toggleClass("show2");
    $('nav ul .third').toggleClass("rotate");
  });

  $('.rep-btn').click(function(){
    $('nav ul .rep-show').toggleClass("show3");
    $('nav ul .forth').toggleClass("rotate");
  });

  $('nav ul li').click(function(){
    $(this).addClass("active").siblings().removeClass("active");
  });
});
