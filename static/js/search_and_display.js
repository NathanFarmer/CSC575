// J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
//
// Takes search query as input and feeds it to ir_project.py. Retrieived documents are then
// returned to this file for display in the browser.

// AJAX sends query and waits for response
$(function() {
    $('a#process_input').bind('click', function() {
        $("#result").empty();
        $.getJSON('/get_query', {
            query: $('input[name="query"]').val(),
        }, function(data) {
            var i = 1;
            $.each(data.result, function(document, link) {
                $("#result").append(`<tr><th scope='row'>` + i + `</th><td><a href='${link}'>${document}</td><td></td><td></td><td></td></tr>`);
                i++;
              });
        });
        return false;
    });
});