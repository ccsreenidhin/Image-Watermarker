$(document).ready(function() {
    $('#login-register-form').modal('show');
});

$('#login-register-form').on('shown.bs.modal', function(){
  $("#signup").trigger("click");
});
