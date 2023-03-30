document.addEventListener('DOMContentLoaded', function () {
    const prevBtn = document.querySelector('.arrow_right-about');
    const nextBtn = document.querySelector('.arrow_left-about');
    const slide = document.getElementById('slideshow');
    const arr_hinh = [
        "/static/assets/img/20230129103403-1a75_wm.jpg",
        "/static/assets/img/20230129103403-4baa_wm.jpg",
        "/static/assets/img/20230129103403-5ab1_wm.jpg",
        "/static/assets/img/20230129103403-29ad_wm.jpg",
        "/static/assets/img/20230129103406-fe4e_wm.jpg",
    ];
    let currentIndex = 0;
    let timerId;
  
    function showSlide(index) {
      slide.setAttribute("src", arr_hinh[index]);
    }
  
    function prevSlide() {
      clearInterval(timerId); // Dừng slide tự động
      currentIndex--;
      if (currentIndex < 0) {
        currentIndex = arr_hinh.length - 1;
      }
      showSlide(currentIndex);
      autoSlide();
    }
  
    function nextSlide() {
      clearInterval(timerId); // Dừng slide tự động
      currentIndex++;
      if (currentIndex >= arr_hinh.length) {
        currentIndex = 0;
      }
      showSlide(currentIndex);
      autoSlide();
    }
  
    prevBtn.addEventListener('click', () => {
      prevSlide();
    });
    
    nextBtn.addEventListener('click', () => {
      nextSlide();
    });
    
    function autoSlide() {
      timerId = setInterval(() => {
        nextSlide();
      }, 3000);
    }
  
    showSlide(currentIndex);
    autoSlide();
  });
  