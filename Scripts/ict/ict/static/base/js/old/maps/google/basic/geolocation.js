$(function() {
	'use strict';
    var map;
    // Initialize
    function initialize() {
        // Optinos
        var mapOptions = {
            zoom: 9
        };
        // Apply options
        map = new google.maps.Map($('.map-geolocation')[0], mapOptions);
        // Try HTML5 geolocation
        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                // Info window
                var infowindow = new google.maps.InfoWindow({
                    map: map,
                    position: pos,
                    content: 'Location found using HTML5'
                });
                map.setCenter(pos);
            }, function() {
                handleNoGeolocation(true);
            });
        }
        else {
            // Browser doesn't support Geolocation
            handleNoGeolocation(false);
        }
    }

    // Handle errors
    function handleNoGeolocation(errorFlag) {
        if (errorFlag) {
            var content = 'Error: The Geolocation service failed.';
        }
        else {
            var content = 'Error: Your browser doesn\'t support geolocation.';
        }
        // Options
        var options = {
            map: map,
            position: new google.maps.LatLng(60, 105),
            content: content
        };
        // Apply options
        var infowindow = new google.maps.InfoWindow(options);
        map.setCenter(options.position);
    }
    // Load map
    google.maps.event.addDomListener(window, 'load', initialize);
});