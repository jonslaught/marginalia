function assignColor (frequency) {
  var className = "noFreq";
  
  // TODO: replace with generic algorithm
  if (frequency > 300) {
    className = "highFreq"; 
  } else if (frequency > 100) {
    className = "highMidFreq";
  } else if (frequency > 50) {
    className = "midFreq";
  } else if (frequency > 10) {
    className = "lowMidFreq";
  } else if (frequency > 1) {
    className = "lowFreq";
  }

  return className;
}


$(document).ready(function() {
// grab all the sentences in the DOM
$("mark").each(function(index) {
  var id = $(this).attr("id");
  var frequency = METADATA[id];
  if (frequency) {
    $(this).addClass(assignColor(frequency));
  }
});


});