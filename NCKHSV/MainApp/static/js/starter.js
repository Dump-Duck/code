document.addEventListener('DOMContentLoaded', function () {
    const slider = document.querySelector(".slider");
    const sliderMain = document.querySelector(".slider-main");
    const sliderItems = document.querySelectorAll(".slider-item");
    const nextBtn = document.querySelector(".slider-next");
    const prevBtn = document.querySelector(".slider-prev");
    const dotItems = document.querySelectorAll(".slider-dot-item");
    const sliderItemWidth = sliderItems[1].offsetWidth;
    console.log("sliderItemWidth",sliderItemWidth);
    const slidesLength = sliderItems.length;
    // sliderMain.style.width = `${slidesLength * sliderItemWidth}px`;
    let postionX = 0;
    let index = 0;

    nextBtn.addEventListener("click", function(){
        handleChangeSlide(1);
    });
    prevBtn.addEventListener("click", function(){
        handleChangeSlide(-1);
    });
    [ ...dotItems].forEach((item) =>
     item.addEventListener("click", function (e){
        [ ...dotItems].forEach(el=> el.classList.remove("active"));
        e.target.classList.add("active");
        const slideIndex = parseInt(e.target.dataset.index);
        index = slideIndex;
        postionX = -1*index * sliderItemWidth;
        console.log(index);
        sliderMain.style = `transform: translateX(${postionX}px)`;
       
    })
    );
    function handleChangeSlide(direction) {
        if(direction === 1) {
            // console.log("next slide");
           
            if (index>= slidesLength-1) {
                index = slidesLength-1;
                return;
            }
           
            postionX = postionX - sliderItemWidth;
            console.log(" handleChangeSlide ~ postionX",postionX);
            sliderMain.style = `transform: translateX(${postionX}px)`;
            // console.log(index);
            index++;
        }
        else if (direction === -1) {
            
            if (index <=0){
                index = 0;
                return;
            } 
            postionX = postionX + sliderItemWidth;
            sliderMain.style = `transform: translateX(${postionX}px)`;
            console.log("prew slide")
            index --;
        }
        [ ...dotItems].forEach(el=> el.classList.remove("active"));
        dotItems[index].classList.add("active");
    }
});
// search
let names = [
    "Hà Đông",
    "Đống Đa",
    "Hồ Tây",
    "Long Biên",
    "Nam Từ Liêm",
    "Bắc Từ Liêm",
    "Mỹ Đình",
    "Xuân Đỉnh",
    "Đại Học Mỏ-Địa chất",
    "Đại học Tài Nguyên Môi Trường",
    "Đại Học Ngân Hàng",
    "Học Viên Tài Chính",
    "Đại học Công nghiệp",
    "Đại học Thủy Lợi",
    "Đại học Công Đoàn",
    "Đại Học Bách khóa",
    "Đại học Kinh tế Quốc Dân"
  ];
  //Sort names in ascending order
  let sortedNames = names.sort();
  
  //reference
  let input = document.getElementById("input");
  
  //Execute function on keyup
  input.addEventListener("keyup", (e) => {
    //loop through above array
    //Initially remove all elements ( so if user erases a letter or adds new letter then clean previous outputs)
    removeElements();
    for (let i of sortedNames) {
      //convert input to lowercase and compare with each string
  
      if (
        i.toLowerCase().startsWith(input.value.toLowerCase()) &&
        input.value != ""
      ) {
        //create li element
        let listItem = document.createElement("li");
        //One common class name
        listItem.classList.add("list-items");
        listItem.style.cursor = "pointer";
        listItem.setAttribute("onclick", "displayNames('" + i + "')");
        //Display matched part in bold
        let word = "<b>" + i.substr(0, input.value.length) + "</b>";
        word += i.substr(input.value.length);
        //display the value in array
        listItem.innerHTML = word;
        document.querySelector(".list").appendChild(listItem);
      }
    }
  });
  function displayNames(value) {
    input.value = value;
    removeElements();
  }
  function removeElements() {
    //clear all the item
    let items = document.querySelectorAll(".list-items");
    items.forEach((item) => {
      item.remove();
    });
  }