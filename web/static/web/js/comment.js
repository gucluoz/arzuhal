$(document).ready(function(){
  $("#postcomment").click(function(){
    if( !$(this).isValid() ) {
      $("#poststatus").html("Formu tam doldurun.").delay(1000).animate({'opacity':'0'},1500);
     } else {
      $.ajax({
        url : "/web/comment/",
        type : "POST",
        data : $("#comment").serialize(),
        success : function(data, textStatus, jqXHR)
        {
          $("#poststatus").html("Yorumunuz gönderildi.").delay(1000).animate({'opacity':'0'},1500);
          $("#commentrow").hide();
        },
        error : function(jqXHR, textStatus, errorThrown)
        {
          $("#poststatus").html("Hata oluştu").delay(1000).animate({'opacity':'0'},1500);
        }
      });
     }
  });
  $.validate({
    form : '#comment',
    onElementValidate : function(valid, $el, $form, errorMess) {
      if ($("#comment").isValid()) {
        $("#postcomment").show();
      }
      else {
        $("#postcomment").hide();
      }
    }
  });
  $("#postcomment").hide();
});
