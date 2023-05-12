var map;

var divLat = document.querySelectorAll('.lat');
var divLng = document.querySelectorAll('.lng');
var divAddress = document.querySelectorAll('.address');

var dataLat = [];
var dataLng = [];
var dataAddress = [];

for(let i = 0; i < divLat.length; i++) {
    let lat = parseFloat(divLat[i].getAttribute('data-lat'));
    dataLat.push(lat);
}

for(let i = 0; i < divLng.length; i++) {
    let lng = parseFloat(divLng[i].getAttribute('data-lng'));
    dataLng.push(lng);
}

for(let i = 0; i < divAddress.length; i++) {
    let data = divAddress[i].getAttribute('data-address');
    dataAddress.push(data);
}

var coordinates = [];
if(dataLat.length == dataLng.length) {
    for(let i = 0; i < dataLat.length; i++) {
        let combinedData = {lat: dataLat[i], lng: dataLng[i]};
        coordinates.push(combinedData);
    }
}

async function initMap() {
    const locateHaNoi = {lat: 21.000565963535767, lng: 105.82102947082825};
    const { Map } = await google.maps.importLibrary("maps");

    map = new Map(document.getElementById("map"), {
        zoom: 12.99999,
        center: locateHaNoi,
        mapId: "MAP_ALL"
    });

    for(let i = 0; i < coordinates.length; i++) {
        const marker = new google.maps.Marker({
            map: map,
            position: coordinates[i],
            title: dataAddress[i],
        });
    }
}

initMap();