document.addEventListener('DOMContentLoaded', function () {
    const houseTypeSelect = document.getElementById("house_type");
    const provinceSelect = document.getElementById("province");
    const districtSelect = document.getElementById("district");
    const wardSelect = document.getElementById("ward");
    const priceSelect = document.getElementById("price");
    const areaSelect = document.getElementById("area");
    const filterButton = document.querySelector(".filterButton");
    
    // Add a separate event listener for each select element
    [houseTypeSelect, provinceSelect, districtSelect, wardSelect, priceSelect, areaSelect].forEach((select) => {
      select.addEventListener("change", () => {
        // If the user selects a non-default option for any select element, show the submit button
        if (houseTypeSelect.value !== "" || provinceSelect.value !== "" || districtSelect.value !== "" || wardSelect.value !== "" || priceSelect.value !== "" || areaSelect.value !== "") {
          filterButton.style.display = "block";
        } else {
          filterButton.style.display = "none";
        }
      });
    });
    
    // Add a separate event listener for the house type select element
    houseTypeSelect.addEventListener("change", () => {
      // If the user selects the default option, hide the submit button
      if (houseTypeSelect.value === "") {
        filterButton.style.display = "none";
      }
    });
    


})