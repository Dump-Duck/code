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
    }, 5000);
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
    startSlideInterval();
  });
  
  nextBtn.addEventListener('click', () => {
    stopSlideInterval();
    currentIndex++;
    if (currentIndex >= slides.length) {
      currentIndex = 0;
    }
    showSlide(currentIndex);
    startSlideInterval();
  });
  

  startSlideInterval(); // bắt đầu chạy interval
});
