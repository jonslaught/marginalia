function NTile (array, n) {
  var self = this;
  this.boundaries = [];
  
  // "constructor" -- TODO: clean up, since it's by no means foolproof
  var numbers = [];
  for (var key in array) {
    numbers.push(array[key]);
  }
    
  // sort numerically
  numbers.sort(function(a,b){return a - b});
  var count = numbers.length;
  
  if (n > 0 && n <= count) {
    for (var i = 0; i < n; i++) {
      self.boundaries.push(numbers[Math.floor(i * count / n)]);
    }
  }

  this.assignColor = function (frequency) {
    var className = "freq";
    for (var i = 0; i < self.boundaries.length; i++) {
      if (frequency <= self.boundaries[i]) {
        return className + i;
      }
    }
    
    return className + self.boundaries.length;
  };

}


SOURCE = $.url().param('source');
VERSION = '5-16'

$(document).ready(function() {
  // Load the HTML file
  $.get('../data/' + VERSION + '_' + SOURCE + '_marked.html',function(html){
    $('.article .text').html(html);
    $('#articleTitle').html($('#textTitle').html());

    // Load the counts data
    $.getJSON('../data/' + VERSION + '_' + SOURCE + '_counts.js',function(metadata) {

      // Calculate n-tile (5 for now)
      nTile = new NTile(metadata, 5);

      // Do the marking
      $(".marker").each(function(index) {
        var id = $(this).attr("id");
        var frequency = metadata[id];
        if (frequency) {
          $(this).addClass(nTile.assignColor(frequency));
          $(this).attr('title',frequency)
        }
      });
    });
  });
});