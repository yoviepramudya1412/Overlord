// ajax dropdown








// dropdown 
const dropdownButton = document.getElementById("dropdownButton");
const dropdownMenu = document.getElementById("dropdownMenu");
const hiddenInput = document.getElementById("hiddenInput");


dropdownButton.addEventListener("click", function() {
  dropdownMenu.classList.toggle("hidden");
});

dropdownMenu.addEventListener("click", function(event) {
  if (event.target.tagName === "LI") {
    const selectedOption = event.target.textContent;
    hiddenInput.value = selectedOption;
    dropdownButton.textContent = selectedOption;
    dropdownMenu.classList.add("hidden");
  }
});

window.addEventListener("click", function(event) {
  if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
    dropdownMenu.classList.add("hidden");
  }
});
const dropdownButton1 = document.getElementById("dropdownButton1");
const dropdownMenu1 = document.getElementById("dropdownMenu1");
const hiddenInput0 = document.getElementById("hiddenInput0");


dropdownButton1.addEventListener("click", function() {
  dropdownMenu1.classList.toggle("hidden");
});

dropdownMenu1.addEventListener("click", function(event) {
  if (event.target.tagName === "LI") {
    const selectedOption = event.target.textContent;
    hiddenInput0.value = selectedOption;
    dropdownButton1.textContent = selectedOption;
    dropdownMenu1.classList.add("hidden");
  }
});

window.addEventListener("click", function(event) {
  if (!dropdownButton1.contains(event.target) && !dropdownMenu1.contains(event.target)) {
    dropdownMenu1.classList.add("hidden");
  }
});
