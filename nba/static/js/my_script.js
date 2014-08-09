$("button").click(function() {
    $.getJSON("http://notoriousbiginteger.pythonanywhere.com/cuisines/json", function(obj){
       $.each(obj, function(key, value) {
           $("ul").append("<li>"+value.name+"</li>");
       });
    });
});