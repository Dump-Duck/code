// Initialize and add the map
let map;
let lat = parseFloat(document.querySelector('#lat').getAttribute('data-lat'));
let lng = parseFloat(document.querySelector('#lng').getAttribute('data-lng'));
let title = document.querySelector('#title').getAttribute('data-title');

async function initMap() {
  // The location of Uluru
  const position = { lat: lat, lng: lng };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 15,
    center: position,
    mapId: "ADDRESS_OF_INN",
  });

  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    map: map,
    position: position,
    title: title,
  });
}

initMap();