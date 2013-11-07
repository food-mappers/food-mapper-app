// Javascript used in the navbar.

// Dynamically populate the Google Docs Feedback Form URL
var feedbackFormUrl = 'https://docs.google.com/forms/d/15LLhT_SJurl4qr_mpcjqhdw0UcfFTyOsYKowtdBv9PM/viewform';
$('#feedback-link').attr('href', function() { return feedbackFormUrl; });

// Alternate version doesn't work so hot... additional fields in the document URL break the google forms parse.
$('#feedback-link').attr('href', function() { return feedbackFormUrl + '?entry.1821625281=' + 'http://' + window.document.location.host + window.document.location.pathname;});

