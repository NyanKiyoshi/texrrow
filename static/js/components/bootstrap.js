import 'bootstrap/js/src/modal';

$(function () {
  // Enable Tooltips
  const tooltips = $('[data-toggle="tooltip"]');
  if (tooltips.length) {
    tooltips.tooltip();
  }

  // Enable Modals
  $('.popup').click(function() {
    $('#base-modal .modal-content').load($(this).data('href'), function() {
      $('#base-modal').modal('show');
    });
  });
});
