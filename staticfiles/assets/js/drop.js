document.addEventListener("DOMContentLoaded", function() {
  const dropdownButton = document.getElementById("dropdownButton");
  const dropdownMenu = document.getElementById("dropdownMenu");
  const hiddenInput = document.getElementById("hiddenInput");
  let isDropdownVisible = false;

  dropdownButton.addEventListener("click", function() {
    isDropdownVisible = !isDropdownVisible;
    dropdownMenu.style.display = isDropdownVisible ? "block" : "none";
  });

  dropdownMenu.addEventListener("click", function(event) {
    if (event.target.tagName === "LI") {
      const selectedOption = event.target.textContent;
      hiddenInput.value = selectedOption;
      dropdownButton.textContent = selectedOption;
      dropdownMenu.style.display = "none";
      isDropdownVisible = false;
    }
  });

  window.addEventListener("click", function(event) {
    if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
      dropdownMenu.style.display = "none";
      isDropdownVisible = false;
    }
  });

  const dropdownButton1 = document.getElementById("dropdownButton1");
  const dropdownMenu1 = document.getElementById("dropdownMenu1");
  const hiddenInput0 = document.getElementById("hiddenInput0");
  let isDropdownVisible1 = false;

  dropdownButton1.addEventListener("click", function() {
    isDropdownVisible1 = !isDropdownVisible1;
    dropdownMenu1.style.display = isDropdownVisible1 ? "block" : "none";
  });

  dropdownMenu1.addEventListener("click", function(event) {
    if (event.target.tagName === "LI") {
      const selectedOption = event.target.textContent;
      hiddenInput0.value = selectedOption;
      dropdownButton1.textContent = selectedOption;
      dropdownMenu1.style.display = "none";
      isDropdownVisible1 = false;
    }
  });

  window.addEventListener("click", function(event) {
    if (!dropdownButton1.contains(event.target) && !dropdownMenu1.contains(event.target)) {
      dropdownMenu1.style.display = "none";
      isDropdownVisible1 = false;
    }
  });

  
    const jenisPerlengkapanDropdown = document.getElementById("dropdownMenu1");
    const namaFasilitasDropdown = document.getElementById("dropdownMenu");

    // Mendefinisikan fungsi untuk mengisi dropdown jenis perlengkapan
    function populateJenisPerlengkapan() {
    // Mengirim permintaan Ajax untuk mendapatkan daftar jenis perlengkapan
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_jenis_perlengkapan/");
    xhr.onload = function () {
        if (xhr.status === 200) {
        const jenisPerlengkapanList = JSON.parse(xhr.responseText);
        // Menghapus semua opsi sebelumnya
        jenisPerlengkapanDropdown.innerHTML = "";
        // Menambahkan opsi jenis perlengkapan ke dalam dropdown
        jenisPerlengkapanList.forEach((jenisPerlengkapan) => {
            const option = document.createElement("li");
            option.textContent = jenisPerlengkapan;
            option.classList.add("block", "px-4", "py-2", "hover:bg-gray-100", "dark:hover:bg-gray-600", "dark:hover:text-white");
            option.addEventListener("click", function () {
            jenisPerlengkapanDropdown.textContent = jenisPerlengkapan;
            populateNamaFasilitas(jenisPerlengkapan);
            });
            jenisPerlengkapanDropdown.appendChild(option);
        });
        }
    };
    xhr.send();
    }

    // Mendefinisikan fungsi untuk mengisi dropdown nama fasilitas
    function populateNamaFasilitas(jenisPerlengkapan) {
    // Mengirim permintaan Ajax untuk mendapatkan daftar nama fasilitas
    const xhr = new XMLHttpRequest();
    xhr.open("GET", `/get_nama_fasilitas/?jenis_perlengkapan=${jenisPerlengkapan}`);
    xhr.onload = function () {
        if (xhr.status === 200) {
        const namaFasilitasList = JSON.parse(xhr.responseText);
        // Menghapus semua opsi sebelumnya
        namaFasilitasDropdown.innerHTML = "";
        // Menambahkan opsi nama fasilitas ke dalam dropdown
        namaFasilitasList.forEach((namaFasilitas) => {
            const option = document.createElement("li");
            option.textContent = namaFasilitas;
            option.classList.add("px-4", "py-2", "hover:bg-gray-100", "cursor-pointer");
            option.addEventListener("click", function () {
            namaFasilitasDropdown.textContent = namaFasilitas;
            });
            namaFasilitasDropdown.appendChild(option);
        });
        }
    };
    xhr.send();
    }

    // Memanggil fungsi untuk mengisi dropdown jenis perlengkapan saat halaman dimuat
    populateJenisPerlengkapan();
});