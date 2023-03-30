document.addEventListener('DOMContentLoaded', function () {
  const prevBtn = document.querySelector('.left-carousel-control');
  const nextBtn = document.querySelector('.right-carousel-control');
  const slides = document.querySelectorAll('.carousel-slide');

  let currentIndex = 0;
  let intervalId;

  function showSlide(index) {
    slides.forEach((slide) => {
      slide.classList.remove('active');
    });
    slides[index].classList.add('active');
  }

  function startSlideInterval() {
    const startTime = Date.now();
    intervalId = setInterval(() => {
      const elapsedTime = Date.now() - startTime;
      const seconds = Math.floor(elapsedTime / 1000);
      const index = seconds % slides.length;
      showSlide(index);
    }, 2000);
  }

  function stopSlideInterval() {
    clearInterval(intervalId);
  }

  prevBtn.addEventListener('click', () => {
    stopSlideInterval();
    currentIndex--;
    if (currentIndex < 0) {
      currentIndex = slides.length - 1;
    }
    showSlide(currentIndex);
  });
  
  nextBtn.addEventListener('click', () => {
    stopSlideInterval();
    currentIndex++;
    if (currentIndex >= slides.length) {
      currentIndex = 0;
    }
    showSlide(currentIndex);
  });
  

  startSlideInterval(); // bắt đầu chạy interval
});
document.addEventListener('DOMContentLoaded', function () {
var arr_hinh = [ 
  "/static/assets/img/20230129103403-1a75_wm.jpg", 
  "/static/assets/img/20230129103403-4baa_wm.jpg", 
  "/static/assets/img/20230129103403-5ab1_wm.jpg",
  "/static/assets/img/20230129103403-29ad_wm.jpg",
  "/static/assets/img/20230129103406-fe4e_wm.jpg",
];

var index = 0;
var intervalId = null;
function stopAutoSlide() {
  clearInterval(intervalId);
  intervalId = null;
}

function next1() {
  stopAutoSlide()
  index++;
  if (index >= arr_hinh.length) {
      index = 0;
  }
  var show = document.getElementById("show1");
  show.src = arr_hinh[index];
  // document.getElementById("dem").innerHTML = index+"/" + arr_hinh.length;
}

function prev1() {
  stopAutoSlide()
  index--;
  if (index < 0) {
      index = arr_hinh.length - 1;
  }
  var show = document.getElementById("show1");
  show.src = arr_hinh[index];
  // document.getElementById("dem").innerHTML = index+"/" + arr_hinh.length;
}

function startAutoSlide() {
  intervalId = setInterval(next1, 2000);
  intervalId = setInterval(prev1, 2000);

}



startAutoSlide();
})

