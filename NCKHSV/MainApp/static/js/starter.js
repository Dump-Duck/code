// document.addEventListener('DOMContentLoaded', function () {
//     const slider = document.querySelector(".slider");
//     const sliderMain = document.querySelector(".slider-main");
//     const sliderItems = document.querySelectorAll(".slider-item");
//     const nextBtn = document.querySelector(".slider-next");
//     const prevBtn = document.querySelector(".slider-prev");
//     const dotItems = document.querySelectorAll(".slider-dot-item");
//     const sliderItemWidth = sliderItems[1].offsetWidth;
//     console.log("sliderItemWidth",sliderItemWidth);
//     const slidesLength = sliderItems.length;
//     // sliderMain.style.width = `${slidesLength * sliderItemWidth}px`;
//     let postionX = 0;
//     let index = 0;

//     nextBtn.addEventListener("click", function(){
//         handleChangeSlide(1);
//     });
//     prevBtn.addEventListener("click", function(){
//         handleChangeSlide(-1);
//     });
//     [ ...dotItems].forEach((item) =>
//      item.addEventListener("click", function (e){
//         [ ...dotItems].forEach(el=> el.classList.remove("active"));
//         e.target.classList.add("active");
//         const slideIndex = parseInt(e.target.dataset.index);
//         index = slideIndex;
//         postionX = -1*index * sliderItemWidth;
//         console.log(index);
//         sliderMain.style = `transform: translateX(${postionX}px)`;
       
//     })
//     );
//     function handleChangeSlide(direction) {
//         if(direction === 1) {
//             // console.log("next slide");
           
//             if (index>= slidesLength-1) {
//                 index = slidesLength-1;
//                 return;
//             }
           
//             postionX = postionX - sliderItemWidth;
//             console.log(" handleChangeSlide ~ postionX",postionX);
//             sliderMain.style = `transform: translateX(${postionX}px)`;
//             // console.log(index);
//             index++;
//         }
//         else if (direction === -1) {
            
//             if (index <=0){
//                 index = 0;
//                 return;
//             } 
//             postionX = postionX + sliderItemWidth;
//             sliderMain.style = `transform: translateX(${postionX}px)`;
//             console.log("prew slide")
//             index --;
//         }
//         [ ...dotItems].forEach(el=> el.classList.remove("active"));
//         dotItems[index].classList.add("active");
//     }
// });
    // var starterUrl = "{%static 'js/starter.js '%}";
   

    var arr_hinh= [ 
          "/static/assets/img/20230129103403-1a75_wm.jpg", 
          "/static/assets/img/20230129103403-4baa_wm.jpg", 
          "/static/assets/img/20230129103403-5ab1_wm.jpg",
          "/static/assets/img/20230129103403-29ad_wm.jpg",
          "/static/assets/img/20230129103406-fe4e_wm.jpg",
        ]

    var index = 0;
    function next1(){
        index++;
        if(index>=arr_hinh.length)
            index =0;
        var show = document.getElementById("show1");
        show.src=arr_hinh[index];
        // document.getElementById("dem").innerHTML = index+"/" + arr_hinh.length;
    }
    function prev1(){
        index--;
        if(index<0)
            index= arr_hinh.length -1;
        document.getElementById("show1").src = arr_hinh[index];
        // document.getElementById("dem").innerHTML = index+"/" + arr_hinh.length;
    }

///// starter file 2
    
    var arr_hinh= [ 
      "/static/assets/img/20230129103403-1a75_wm.jpg", 
      "/static/assets/img/20230129103403-4baa_wm.jpg", 
      "/static/assets/img/20230129103403-5ab1_wm.jpg",
      "/static/assets/img/20230129103403-29ad_wm.jpg",
      "/static/assets/img/20230129103406-fe4e_wm.jpg",

    ]

var index = 0;
function next2(){
    index++;
    if(index>=arr_hinh.length)
        index =0;
    var show = document.getElementById("show2");
    show.src=arr_hinh[index];
    // document.getElementById("dem").innerHTML = index+"/" + arr_hinh.length;
}
function prev2(){
    index--;
    if(index<0)
        index= arr_hinh.length -1;
    document.getElementById("show2").src = arr_hinh[index];
    // document.getElementById("dem").innerHTML = index+"/" + arr_hinh.length;
}


