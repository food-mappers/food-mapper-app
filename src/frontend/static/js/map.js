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

var community = {
	"name": "Public",
	"namespace": "public",
	"pk": 1
}

var map = L.map("map", {
	zoom: 15,
	center: gaTech,
	layers: [mapquestOSM]
});

function makePopup(val) {
	var popup = "<strong>" + val.name + "</strong><br>" + val.description + "<br>"
	return popup
}

// Layer group to hold all markers shown on map
var allMarkers = new L.layerGroup();

// Get food sources and parse them to markers in layer group

function getSources() {
	$.getJSON('/api/communities?namespace=' + community.namespace, function(data) {
		$.each(data[0].sources, function(i, val) {
			allMarkers.addLayer(L.marker([val.latitude, val.longitude]).bindPopup(makePopup(val)))
		})
		allMarkers.addTo(map)
	})
}

getSources();

//post new food source on success clear markers and get all markers... need to modify to get ?Created > initial pageload date/time

function addSource() {
	var latlng = map.getCenter()
	$.post('/api/sources/', {
		latitude: latlng.lat,
		longitude: latlng.lng,
		name: 'test1',
		description: 'this is a test',
		community: 1
	}, function(data, status) {
		if (status === 'success') {
			allMarkers.clearLayers();
			getSources();
		}
	})
}