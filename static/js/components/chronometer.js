//Javascript
let currentInterval;
let currentTime = new Date(0);

$(function(){
  displayTime();
  $('.chronometer .start').on('click', function(){
    if (!currentInterval) {
      currentInterval = setInterval(function () {
        currentTime = new Date(currentTime.getTime() + 1000);
        displayTime();
      }, 1000);
    }
  });
  $('.chronometer .pause').on('click', function(){
    stopCurrentInterval();
  });
  $('.chronometer .reset').on('click', function(){
    resetTime();
    displayTime();
  });
});

function stopCurrentInterval() {
  if (currentInterval) {
    clearInterval(currentInterval);
    currentInterval = null;
  }
}

function resetTime() {
  currentTime = new Date(0);
}

function displayTime(){
  $('.chronometer .elapsed').text(fillZeroes(
    currentTime.getMinutes()) + ':' + fillZeroes(currentTime.getSeconds()));
}

function fillZeroes(text){
  text = text + '';
  if(text.length === 1) {
    return '0' + text;
  }
  else {
    return text;
  }
}
