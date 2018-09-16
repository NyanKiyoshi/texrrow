function toggleFullScreen() {
  if ((document.fullScreenElement && document.fullScreenElement !== null) ||
   (!document.mozFullScreen && !document.webkitIsFullScreen)) {
    if (document.documentElement.requestFullScreen) {
      document.documentElement.requestFullScreen();
    } else if (document.documentElement.mozRequestFullScreen) {
      document.documentElement.mozRequestFullScreen();
    } else if (document.documentElement.webkitRequestFullScreen) {
      document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
    }
  } else {
    if (document.cancelFullScreen) {
      document.cancelFullScreen();
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen();
    } else if (document.webkitCancelFullScreen) {
      document.webkitCancelFullScreen();
    }
  }
}

$(function () {
  const slideManager = $('.slide-manager');
  const nextSlideButton = $('.slide-manager .btn-next');
  const prevSlideButton = $('.slide-manager .btn-prev');

  const nextSlideUrl = slideManager.data('next-slide-url');
  const prevSlideUrl = slideManager.data('prev-slide-url');

  nextSlideButton.on('click', function () {
    $.ajax({url: nextSlideUrl, method: 'POST'});
  });
  prevSlideButton.on('click', function () {
    $.ajax({url: prevSlideUrl, method: 'POST'});
  });
});

window.toggleFullScreen = toggleFullScreen;
