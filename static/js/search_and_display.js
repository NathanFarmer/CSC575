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
            $.each(data.result, function(index, value) {
                $("#result").append(`<tr><th scope='row'>${index}</th><td><a href='${value}'>${value}</td><td></td><td></td><td></td></tr>`);
              });
        });
        return false;
    });
});