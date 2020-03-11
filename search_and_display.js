// J. Nathan Farmer, Rohit Kothari, Sachinder Katoch
//
// Takes search query as input and feeds it to retrieive_documents.py. Retrieived documents are then
// returned to this file for display in the browser.


// Pass the query that was entered to retrieve_documents.py
function searchQuery(ev) {

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


// Wait for a keypress in the search box
const el1 = document.getElementById('search');
el1.addEventListener('keydown', enterSubmit);


// COPIED FROM STACK OVERFLOW FOR PASSING DATA TO PYTHON
function on_request_success(response) {
    console.debug('response', response);
} 

function on_request_error(r, text_status, error_thrown) {
    console.debug('error', text_status + ", " + error_thrown + ":\n" + r.responseText);
}

var request = { ... };
jQuery.ajax({
    url: 'http://host/whatever.cgi',
    type: 'POST',
    cache: false,
    data: JSON.stringify(request),
    contentType: 'application/json',
    processData: false,
    success: on_request_success,
    error: on_request_error
});