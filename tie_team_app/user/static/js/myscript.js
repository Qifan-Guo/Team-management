$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })


  $(document).ready(function(){
    $('[data-toggle="popover"]').popover({
        html: true,
        trigger: 'hover',
        placement: 'right',
        content: function(){return '<ul class="container"><li class="row"><img class= "icon" src="'+$('.tie1_icon').data('img') + '" /><p class="icontext">TIE I</p></li>'+
        '<li class="row"><img class= "icon" src="'+$('.tie2_icon').data('img') + '" /><p class="icontext">TIE II</p></li>'+
        '<li class="row"><img class= "icon" src="'+$('.tieLead_icon').data('img') + '" /><p class="icontext">TIE Lead</p></li>'+
        '<li class="row"><img class= "icon" src="'+$('.tieSuper_icon').data('img') + '" /><p class="icontext">Supervisor</p></li>'+
        '</ul>';}
      });   
});

