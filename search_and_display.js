// J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
//
// Takes search query as input and feeds it to retrieive_documents.py. Retrieived documents are then
// returned to this file for display in the browser.


// Pass the query that was entered to retrieve_documents.py
function searchQuery(ev) {
    var request = document.getElementById('search').value;
    console.log(request)
    jQuery.ajax({
        url: '/launch_ui.py',
        type: 'POST',
        cache: false,
        data: {query: request},
        contentType: 'text/plain',
        processData: false,
        success: on_request_success,
        error: on_request_error
    });
};

// Prevent the press of enter in the search box from refreshing the page
function enterSubmit(ev) {
    if (ev.key === 'Enter') {
        // Don't refresh the page
        ev.preventDefault();
        // but search if enter is pressed
        searchQuery();
    };
};

// Error handling for AJAX request
function on_request_success(response) {
    console.debug('response', response);
};

function on_request_error(r, text_status, error_thrown) {
    console.debug('error', text_status + ", " + error_thrown + ":\n" + r.responseText);
};

// Wait for a keypress in the search box
const el1 = document.getElementById('search');
el1.addEventListener('keydown', enterSubmit);