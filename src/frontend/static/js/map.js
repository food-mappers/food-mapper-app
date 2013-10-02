var mapquestOSM = L.tileLayer("http://{s}.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png", {
	maxZoom: 19,
	subdomains: ["otile1", "otile2", "otile3", "otile4"],
	attribution: 'Tiles courtesy of <a href="http://www.mapquest.com/" target="_blank">MapQuest</a> <img src="http://developer.mapquest.com/content/osm/mq_logo.png">. Map data (c) <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> contributors, CC-BY-SA.'
});

var sampleData = {
	"type": "FeatureCollection",
	"features": [{
		"type": "Feature",
		"properties": {
			"name": "GaTech Hotdog Stand",
			"description": "Hotdogs at the football game"
		},
		"geometry": {
			"type": "Point",
			"coordinates": [-84.39348578453064,
				33.772369635684605
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "Food Court - Student Center",
			"description": "Indian, Mediterranean, Sushi"
		},
		"geometry": {
			"type": "Point",
			"coordinates": [-84.3987375497818,
				33.77406856895522
			]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "Apple Tree",
			"description": "Best apples in the world!"
		},
		"geometry": {
			"type": "Point",
			"coordinates": [-84.39829230308533,
				33.776133106558646
			]
		}
	}]
}

var gaTech = [33.77764915000493, -84.39986944198608]

var map = L.map("map", {
	zoom: 15,
	center: gaTech,
	layers: [mapquestOSM]
});

$.getJSON('/api/communities', function(data) {
	console.log(data)
})

function onEachFeature(feature, layer) {
	var popup = "<strong>" + feature.properties.name + "</strong><br>" + feature.properties.description + "<br>"
	layer.bindPopup(popup)
}

var dataLayer = L.geoJson(sampleData, {
	onEachFeature: onEachFeature
}).addTo(map);

// function addFeature() {
// 	map.removeLayer(dataLayer)
// 	var latlng = map.getCenter()
// 	console.log(latlng)
// 	sampleData.features.push({
// 		"type": "Feature",
// 		"properties": {
// 			"name": "new point",
// 			"description": "new point description"
// 		},
// 		"geometry": {
// 			"type": "Point",
// 			"coordinates": [latlng.lat,
// 				latlng.lng
// 			]
// 		}
// 	})
// 	console.log(sampleData)
// 	dataLayer = L.geoJson(sampleData, {
// 		onEachFeature: onEachFeature
// 	}).addTo(map);
// }