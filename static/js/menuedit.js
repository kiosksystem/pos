 window.addEventListener("DOMContentLoaded", function(){
     var menuid = document.getElementById("menu_inform");
     delete_btn = document.getElementById("delete_btn");

     delete_btn.addEventListener("click", function(){
         console.log(menuid);
     });

 });