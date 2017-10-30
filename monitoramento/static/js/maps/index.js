$(function() {
    getLocation(inicializeMap);

    function getLocation(callback) {
        /*if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                callback(position);
            });
        }
        else {
            callback();
        }
        */
        callback();
    }

    function inicializeMap(position) {
        if (position){
            var positionOptions = { center: [position.coords.latitude, position.coords.longitude], zoom: 12 };
        }
        else {
            var positionOptions = undefined;
        }

        var map = L.map('map', positionOptions);
        var realtime = L.realtime('https://wanderdrone.appspot.com/', {
            interval: 1 * 1000
        }).addTo(map);

        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        realtime.on('update', function () {
            map.fitBounds(realtime.getBounds(), {maxZoom: 3});
        });
    }
    
});


