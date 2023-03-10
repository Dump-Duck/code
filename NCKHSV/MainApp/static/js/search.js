// search
 names = [
    "FPT",
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

  
  //Execute function on keyup
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#input').onkeyup = function() {
        let input = document.getElementById("input");
    //loop through above array
    //Initially remove all elements ( so if user erases a letter or adds new letter then clean previous outputs)
    removeElements();
    for (let i of sortedNames) {
      //convert input to lowercase and compare with each string
    //   let characters = i.split("");
    //   let spacedCharacters = characters.join(" ");
    if (
        i.toLowerCase().includes(input.value.toLowerCase()) &&
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
  }});
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

