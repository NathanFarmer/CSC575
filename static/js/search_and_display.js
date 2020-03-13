// J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
//
// Takes search query as input and feeds it to ir_project.py. Retrieived documents are then
// returned to this file for display in the browser.

$(function() {
    $('a#process_input').bind('click', function() {
        $.getJSON('/get_query', {
            query: $('input[name="query"]').val(),
        }, function(data) {
            $("#result").text(data.query);
        });
        return false;
    });
});