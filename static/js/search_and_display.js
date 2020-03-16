// J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
//
// This file takes data from the browser and passes it back and forth to our .py scripts.
// It also fills in the autocomplete form.

// Autocomplete
$(function() {
    var availableTags = [
        "ActionScript", "AppleScript", "Asp", "BASIC", "C", "C++",
        "Clojure", "COBOL", "ColdFusion", "Erlang", "Fortran",
        "Groovy", "Haskell", "Java", "JavaScript", "Lisp", "Perl",
        "PHP", "Python", "Ruby", "Scala", "Scheme"
    ];

    $(".autocomplete").autocomplete({
        source: availableTags
    });
});

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