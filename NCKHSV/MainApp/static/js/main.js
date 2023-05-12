document.addEventListener('DOMContentLoaded', function () {
  let currentURL = window.location.href;
  let id = currentURL.substring(currentURL.lastIndexOf('/') + 1); // get id in url for replace URL
  let img = document.querySelector('#img_panolens').getAttribute('data-img');
  let newURL = currentURL.replace("/index/" + id, img); // replace "/index/<id>" with link of image

  const panorama = new PANOLENS.ImagePanorama(newURL);
  let imageContainer = document.querySelector('.image-container');

  const viewer = new PANOLENS.Viewer({
    container: imageContainer,
    autoRotate: true,
    autoRotateSpeed: 0.3,
    controlBar: true,
  });

  viewer.add(panorama); // display the panorama
});

