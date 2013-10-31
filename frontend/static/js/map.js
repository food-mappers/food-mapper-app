// Javascript required for the /map/ page.
var temp;
var activeSource;
// Getting CSRF token to allow post requests

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');

// Sets up AJAX requests to use CSRF Token
$(function() {
	$.ajaxSetup({
		headers: {
			"X-CSRFToken": getCookie("csrftoken")
		}
	});
});

// Define basemap layer
var mapquestOSM = L.tileLayer("http://{s}.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png", {
	maxZoom: 19,
	subdomains: ["otile1", "otile2", "otile3", "otile4"],
	attribution: 'Tiles courtesy of <a href="http://www.mapquest.com/" target="_blank">MapQuest</a> <img src="http://developer.mapquest.com/content/osm/mq_logo.png">. Map data (c) <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> contributors, CC-BY-SA.'
});

var gaTech = [33.77764915000493, -84.39986944198608];

var map_detail = L.map("map", {
	zoom: 15,
	// center: gaTech,
	layers: [mapquestOSM]
});

map_detail.fitBounds(bbox);

//Add geolocation

L.control.locate({
	follow: true,
	stopFollowingOnDrag: true
}).addTo(map_detail);


function getComments(val) {
	console.log(val)
	$.getJSON('/api/comments/?source=' + val.id, function(data) {
		console.log(data)
		var html = "";
		if (data.length == 0) {
			html += "<span style='color: light-gray;'>Be the first to comment on " + val.name + "</span>"
		}
		$.each(data, function(i, comment) {
			var user = ''
			if (comment.user == null) {
				user = 'Anonymous'
			} else {
				user = comment.user
			}
			html += "Posted by: " + user + " <span class='pull-right'>" + moment(comment.created).fromNow() + "</span><br><small>" + comment.content + "</small><hr>"
		})
		html += "<button id='show-add-comment-block' class='btn btn-info btn-xs pull-right'>add a comment</button><br>";
		$('#comment-block').html(html);

		$('#add-comment-block').hide();
		$('#show-add-comment-block').click(function() {
			$('#add-comment-block').toggle();
		});
	});
}

// ITF: the selection and completion of the point modal from callbacks to API

function setupViewModal(val) {
	// console.log(val)
	activeSource = val;
	$('#source-name').text(val.name);
	$('#source-description').text(val.description);
	$('#source-creation-time').text(moment(val.created).fromNow());
	$('#view-source-modal').modal('show');
	$('#tags-block').html( function() {
		var tags = val.tags;
		var text = '';
		if (val.tags.length == 0) { 
			return '';
		}
		for (i in tags) {
			text += "<span class='badge badge-default'>" + tags[i] + "</span>"
			if (i != tags.length) {
				text += ' '
			}
		}
		text += '<hr>';
		return text;
	});
	getComments(val)


	// extract this into a function
	getComments(val);
}

function getComments(val) {
	var html = "";
	$.getJSON('/api/comments/?source=' + val.id, function(data){
		if (data.length == 0) {
			html += "<span style='color: light-gray;'>Be the first to comment on " + val.name + "</span>"
		}
		$.each(data, function(i,comment){
			// console.log(comment);
			var user = ''
			if (comment.user == null){
				user = 'Anonymous'
			}else{
				user = comment.user
			}
			html += "<div class='comment-element'>"
			html += comment.content + "<br><small>Posted by: " + user + " <span class='pull-right'>" + moment(comment.created).fromNow() + "</span></small><hr>"
			html += "</div>"
		})
		$('#comment-block').html(html);
	});
}

// Layer group to hold all markers shown on map
var allMarkers = new L.layerGroup();

// Get food sources and parse them to markers in layer group

function getSources() {
	$.getJSON('/api/sources/?map=' + map.pk, function(data) {
		$.each(data, function(i, val) {
			allMarkers.addLayer(L.marker([val.latitude, val.longitude]).on('click', function(e) {
				setupViewModal(val)
			}))
		})
		allMarkers.addTo(map_detail)
	})
}

getSources();

//post new food source on success clear markers and get all markers... need to modify to get ?Created > initial pageload date/time

function addSource() {
	$('#add-source-modal').modal('hide')
	var latlng = map_detail.getCenter()
	var name = $('#sourceName').val()
	var desc = $('#sourceDesc').val()
	var tags = $('#sourceTags').val();
	// console.log(tags);
	$('#sourceName').val('');
	$('#sourceDesc').val('');
	$('#sourceTags').val('');
	$.post('/api/sources/', {
		latitude: latlng.lat,
		longitude: latlng.lng,
		name: name,
		description: desc,
		tags: tags,
		map: map.pk
	}, function(data, status) {
		if (status === 'success') {
			allMarkers.clearLayers();
			getSources();
		}
	})
}

function addComment(e) {
	var comment = $('#commentText').val();
	$('#commentText').val('');
	$.post('/api/comments/', {
		source: activeSource.id,
		content: comment,
	}, function(data, status) {
		if (status === 'success') {
			getComments(activeSource)
			// console.log('ok');
		}
	})
	
}