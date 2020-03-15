// J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
//
// Takes search query as input and feeds it to ir_project.py. Retrieived documents are then
// returned to this file for display in the browser.

// AJAX sends query and waits for response
$(function() {
    $('a#process_input').bind('click', function() {
        $("#result").empty();
        $("#topic").html('<b>Selected Topic:</b>');
        $.getJSON('/get_query', {
            query: $('input[name="query"]').val(),
        }, function(data) {
            $("#topic").html('<b>Selected Topic:</b> ' + data.result.topic);
            $.each(data.result.docs, function(rank, info) {
                $("#result").append(`<tr><th scope='row'>${rank}</th><td><a href='${info.link}'>${info.document_id}</td><td>${info.relevance}</td><td>${info.precision}</td><td>${info.recall}</td></tr>`);
              });
        });
        return false;
    });
});