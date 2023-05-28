document.addEventListener('DOMContentLoaded', function() {
    var replyLinks = document.querySelectorAll('.reply');
    var commentReplies = document.querySelectorAll('.comment-reply');
    
    replyLinks.forEach(function(replyLink, index) {
      replyLink.addEventListener('click', function(event) {
        event.preventDefault();
        
        // Ẩn tất cả các phần tử "comment-reply"
        commentReplies.forEach(function(commentReply) {
          commentReply.style.display = 'none';
        });
        
        // Hiển thị phần tử "comment-reply" tương ứng với replyLink được nhấp
        commentReplies[index].style.display = 'block';
      });
    });
  });




  
// Tạo đánh giá ngôi sao
  document.addEventListener('DOMContentLoaded', function() {
    // Mã JavaScript của bạn ở đây
 
  
  // JavaScript code
  const starsContainer = document.getElementById('star-rating');
  const stars = Array.from(starsContainer.querySelectorAll('.star'));
  const ratingInput = document.getElementById('rating');
  const ratingInfo = document.getElementById('rating-info');
  
  let currentRating = 0;
  
  starsContainer.addEventListener('mouseover', function(event) {
    const star = event.target;
    const starIndex = stars.indexOf(star);
  
    stars.forEach((star, index) => {
      if (index <= starIndex) {
        star.classList.add('hover');
      } else {
        star.classList.remove('hover');
      }
    });
  });
  
  starsContainer.addEventListener('mouseout', function() {
    stars.forEach(star => {
      star.classList.remove('hover');
    });
  });
  
  starsContainer.addEventListener('click', function(event) {
    const star = event.target;
    const starIndex = stars.indexOf(star);
    const selectedRating = starIndex + 1;
  
    currentRating = selectedRating;
  
    stars.forEach((star, index) => {
      if (index < selectedRating) {
        star.classList.add('active');
      } else {
        star.classList.remove('active');
      }
    });
  
    ratingInput.value = selectedRating;
    ratingInfo.textContent = `Đánh giá: ${selectedRating} sao`;
  });
  
  // Set default rating and info
  stars.forEach((star, index) => {
    if (index < currentRating) {
      star.classList.add('active');
    } else {
      star.classList.remove('active');
    }
  });
  
  ratingInfo.textContent = currentRating > 0 ? `Đánh giá: ${currentRating} sao` : 'Chưa đánh giá';
});



// Tạo lượt thích
document.addEventListener('DOMContentLoaded', function() {
  var likeButton = document.getElementById("likeButton");
  var dislikeButton = document.getElementById("dislikeButton");
  var likeCount = document.getElementById("likeCount");
  var dislikeCount = document.getElementById("dislikeCount");
  
  // Kiểm tra xem có dữ liệu lưu trữ trong Local Storage hay không
  var storedLikes = localStorage.getItem("likes");
  var storedDislikes = localStorage.getItem("dislikes");
  
  // Khởi tạo số lượt thích và không thích từ dữ liệu lưu trữ (nếu có)
  var like = storedLikes ? parseInt(storedLikes) : 0;
  var dislike = storedDislikes ? parseInt(storedDislikes) : 0;
  
  // Cập nhật số lượt thích và không thích lên giao diện
  likeCount.textContent = like;
  dislikeCount.textContent = dislike;
  
  likeButton.addEventListener("click", function() {
    like++;
    likeCount.textContent = like;
    // Lưu số lượt thích vào Local Storage
    localStorage.setItem("likes", like.toString());
  });
  
  dislikeButton.addEventListener("click", function() {
    dislike++;
    dislikeCount.textContent = dislike;
    // Lưu số lượt không thích vào Local Storage
    localStorage.setItem("dislikes", dislike.toString());
  });
  
});