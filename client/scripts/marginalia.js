function assignColor (frequency) {
  var className = "noFreq";
  
  // TODO: replace with generic algorithm
  if (frequency > 10000) {
    className = "highFreq"; 
  } else if (frequency > 7000) {
    className = "highMidFreq";
  } else if (frequency > 5000) {
    className = "midFreq";
  } else if (frequency > 3000) {
    className = "lowMidFreq";
  } else if (frequency > 1000) {
    className = "lowFreq";
  }

  return className;
}


SOURCE = $.url().param('source');
VERSION = 'shortones'

$(document).ready(function() {


  // Load the HTML file
  $.get('../data/' + VERSION + '_' + SOURCE + '_marked.html',function(html){
    $('.article .text').html(html);

    // Load the counts data
    $.getJSON('../data/' + VERSION + '_' + SOURCE + '_counts.js',function(metadata) {

    // Do the marking
      $(".marker").each(function(index) {
        var id = $(this).attr("id");
        var frequency = metadata[id];
        console.log([id,frequency]);
        if (frequency) {
          $(this).addClass(assignColor(frequency));
        }
      });

    });
  });
});