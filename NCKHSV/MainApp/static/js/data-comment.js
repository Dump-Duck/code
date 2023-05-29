document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("contact_form").addEventListener("submit", function(event) {
        var name = document.getElementById("name").value;
        var email = document.getElementById("email").value;
        var content = document.getElementById("content").value;
        var phone = document.getElementById("phone").value;
        
        if (name === "" || email === "" || content === "" || phone === "") {
          event.preventDefault();
          alert("Vui lòng nhập đủ thông tin.");
          return false;
        }
      });
  });

  document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("contact_form").addEventListener("submit", function(event) {
    var rating = document.getElementById("rating").value;
    var ratingInfo = document.getElementById("rating-info");

    if (rating === "") {
      event.preventDefault();
      ratingInfo.textContent = "Vui lòng chọn đánh giá.";
      ratingInfo.style.color = "red";
    }
  });
});