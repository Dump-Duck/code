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
  // Lựa chọn các phần tử bằng lớp CSS
const likeButtons = document.querySelectorAll(".comment-footer .button#likeButton");
const dislikeButtons = document.querySelectorAll(".comment-footer .button#dislikeButton");
const likeCounts = document.querySelectorAll(".comment-footer .button#likeButton p#likeCount");
const dislikeCounts = document.querySelectorAll(".comment-footer .button#dislikeButton p#dislikeCount");

likeButtons.forEach((likeButton, index) => {
  likeButton.addEventListener("click", function() {
    likeCounts[index].textContent = parseInt(likeCounts[index].textContent) + 1;
    // Lưu số lượt thích vào Local Storage
    localStorage.setItem(`likes${index}`, likeCounts[index].textContent);
  });
});

dislikeButtons.forEach((dislikeButton, index) => {
  dislikeButton.addEventListener("click", function() {
    dislikeCounts[index].textContent = parseInt(dislikeCounts[index].textContent) + 1;
    // Lưu số lượt không thích vào Local Storage
    localStorage.setItem(`dislikes${index}`, dislikeCounts[index].textContent);
  });
});

// Khôi phục số lượt thích và không thích từ Local Storage khi tải lại trang
window.addEventListener("load", function() {
  likeCounts.forEach((likeCount, index) => {
    const storedLikes = localStorage.getItem(`likes${index}`);
    if (storedLikes) {
      likeCount.textContent = storedLikes;
    }
  });

  dislikeCounts.forEach((dislikeCount, index) => {
    const storedDislikes = localStorage.getItem(`dislikes${index}`);
    if (storedDislikes) {
      dislikeCount.textContent = storedDislikes;
    }
  });
});

});
// function submitComment(event) {
//   event.preventDefault();

//   var commentReply = event.target.closest('.comment-reply');
//   var inputComment = commentReply.querySelector('.input-reply-cmt');
//   var commentValue = inputComment.value;

//   var commentBodyContainer = commentReply.querySelector('.comment-body');
//   var submittedComment = commentReply.querySelector('#submitted-comment');

//   if (commentBodyContainer && submittedComment) {
//     commentBodyContainer.textContent = commentValue;
//     submittedComment.style.display = 'block';
//     submittedComment.textContent = 'Nội dung bình luận đã được gửi: ' + commentValue;
//   }

//   var commentFooter = commentReply.querySelector('.comment-footer-reply-cmt');
//   if (commentFooter) {
//     commentFooter.style.display = 'none';
//   }
// }
// document.addEventListener('DOMContentLoaded', function() {
//   var replyLinks = document.querySelectorAll('.reply');
//   var commentReplies = document.querySelectorAll('.comment-reply');
//   var submittedComments = [];

//   replyLinks.forEach(function(replyLink, index) {
//     replyLink.addEventListener('click', function(event) {
//       event.preventDefault();

//       // Ẩn tất cả các phần tử "comment-reply"
//       commentReplies.forEach(function(commentReply) {
//         commentReply.style.display = 'none';
//       });

//       // Hiển thị phần tử "comment-reply" tương ứng với replyLink được nhấp
//       commentReplies[index].style.display = 'block';

//       // Tìm nút submit trong phần reply
//       var submitButton = commentReplies[index].querySelector('.button-theme');

//       // Gán sự kiện click cho nút submit
//       submitButton.addEventListener('click', function(event) {
//         submitComment(event);
//       });
//     });
//   });

//   function submitComment(event) {
//     event.preventDefault();

//     var commentReply = event.target.closest('.comment-reply');
//     var inputComment = commentReply.querySelector('.input-reply-cmt');
//     var commentValue = inputComment.value;

//     var commentBodyContainer = commentReply.querySelector('.comment-body');
//     var submittedComment = commentReply.querySelector('#submitted-comment');

//     if (commentBodyContainer && submittedComment) {
//       commentBodyContainer.textContent = commentValue;
//       submittedComment.style.display = 'block';
//       submittedComment.textContent = 'Nội dung bình luận đã được gửi: ' + commentValue;
//     }

//     var commentFooter = commentReply.querySelector('.comment-footer-reply-cmt');
//     if (commentFooter) {
//       commentFooter.style.display = 'none';
//     }

//     submittedComments.push(commentReply);
//   }
// });
