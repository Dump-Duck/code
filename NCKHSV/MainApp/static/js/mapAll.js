var map;

var infoWindow = document.getElementById('custom-info-window');
var infoContent = document.getElementById('info-content');

var divID = document.querySelectorAll('.id');
var divArea = document.querySelectorAll('.area');
var divPrice = document.querySelectorAll('.price');
var divLat = document.querySelectorAll('.lat'); 
var divLng = document.querySelectorAll('.lng'); 
var divAddress = document.querySelectorAll('.address'); 

var dataID = [];
var dataArea = [];
var dataPrice = [];
var dataLat = [];
var dataLng = [];
var dataAddress = [];

for(let i = 0; i < divID.length; i++) {
    let id = divID[i].getAttribute('data-id');
    dataID.push(id);
}

for(let i = 0; i < divArea.length; i++) {
    let area = parseFloat(divArea[i].getAttribute('data-area'));
    dataArea.push(area);
}

for(let i = 0; i < divPrice.length; i++) {
    let price = parseFloat(divPrice[i].getAttribute('data-price'));
    dataPrice.push(price);
}

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
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                scale: getScaleIcon(dataArea[i]),
                fillColor: getColor(dataPrice[i]),
                fillOpacity: 1,
                strokeWeight: 2,
                labelOrigin: new google.maps.Point(10, -10),
            }
        });

        function getScaleIcon(number) {
            if(number < 30) {
                return 5;
            } else if(number >= 30 && number <= 50) {
                return 7;
            } else { return 10; }
        }

        function getColor(value) {
            if(value < 3) {
                return '#3ad64c';
            } else if(value >= 3 && value < 5) {
                return '#e3e336';
            } else if(value >= 5 && value < 7) {
                return '#e09b24';
            } else { return '#e02424'; }
        }

        marker.addListener('click', function(){
            window.location.href = '/index/' + dataID[i];
        })

        marker.addListener('rightclick', function() {
            const url = '/info/' + dataID[i];

            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        infoContent.innerHTML = xhr.responseText;
                        infoWindow.style.display = 'block';
                        infoWindow.style.zIndex = 999;
                    }
                }
            };
            xhr.open('GET', url);
            xhr.send();
        })

        map.addListener('click', function() {
            infoWindow.style.display = 'none';
            infoWindow.style.zIndex = -1;
        })
    }

}

initMap();