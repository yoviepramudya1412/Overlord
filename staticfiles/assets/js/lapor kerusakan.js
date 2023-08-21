$(document).ready(function() {
    // Tambahkan event listener untuk button jenis perlengkapan dropdown
    $('#jenisPerlengkapanDropdown').on('click', function() {
        // Panggil fungsi untuk mengisi dropdown jenis perlengkapan
        populateJenisPerlengkapanDropdown();
    });

    // Tambahkan event listener untuk button nama fasilitas dropdown
    $('#namaFasilitasDropdown').on('click', function() {
        // Panggil fungsi untuk mengisi dropdown nama fasilitas
        var jenisPerlengkapan = $('#hiddenJenisPerlengkapan').val();
        populateNamaFasilitasDropdown(jenisPerlengkapan);
    });

    // Fungsi untuk mengisi dropdown jenis perlengkapan
    function populateJenisPerlengkapanDropdown() {
        $.ajax({
            url: '/get_jenis_perlengkapan/',
            method: 'GET',
            success: function(response) {
                var jenisPerlengkapanDropdown = $('#jenisPerlengkapanDropdown').next('.dropdown-menu');
                jenisPerlengkapanDropdown.empty(); // Hapus opsi yang ada sebelumnya

                // Tambahkan opsi dropdown jenis perlengkapan
                response.forEach(function(jenisPerlengkapan) {
                    jenisPerlengkapanDropdown.append($('<a class="dropdown-item jenis-perlengkapan" href="#" data-value="' + jenisPerlengkapan + '">' + jenisPerlengkapan + '</a>'));
                });

                // Tambahkan event listener untuk opsi dropdown jenis perlengkapan
                $('.dropdown-item.jenis-perlengkapan').click(function() {
                    var selectedJenisPerlengkapan = $(this).data('value');
                    $('#jenisPerlengkapanDropdown').text(selectedJenisPerlengkapan);
                    $('#hiddenJenisPerlengkapan').val(selectedJenisPerlengkapan);
                });
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            }
        });
    }

    // Fungsi untuk mengisi dropdown nama fasilitas
    function populateNamaFasilitasDropdown(jenisPerlengkapan) {
        $.ajax({
            url: '/get_nama_fasilitas/',
            method: 'GET',
            data: { jenis_perlengkapan: jenisPerlengkapan },
            success: function(response) {
                var namaFasilitasDropdown = $('#namaFasilitasDropdown').next('.dropdown-menu');
                namaFasilitasDropdown.empty(); // Hapus opsi yang ada sebelumnya

                // Tambahkan opsi dropdown nama fasilitas
                response.forEach(function(namaFasilitas) {
                    namaFasilitasDropdown.append($('<a class="dropdown-item nama-fasilitas" href="#" data-value="' + namaFasilitas + '">' + namaFasilitas + '</a>'));
                });

                // Tambahkan event listener untuk opsi dropdown nama fasilitas
                $('.dropdown-item.nama-fasilitas').click(function() {
                    var selectedNamaFasilitas = $(this).data('value');
                    $('#namaFasilitasDropdown').text(selectedNamaFasilitas);
                    $('#hiddenNamaFasilitas').val(selectedNamaFasilitas);
                });
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            }
        });
    }

    // Tambahkan event listener untuk opsi dropdown status
    $('.dropdown-item.Kerusakan').click(function(e) {
        e.preventDefault();
        var selectedKerusakan = $(this).data('value');
        $('#hiddenInputKerusakan').val(selectedKerusakan);
        $('#dropdownMenuKerusakan').text(selectedKerusakan);
    });

    // // Tambahkan event listener untuk opsi dropdown kondisi
    // $('.dropdown-item.kondisi').click(function(e) {
    //     e.preventDefault();
    //     var selectedKondisi = $(this).data('value');
    //     $('#hiddenInputkondisi').val(selectedKondisi);
    //     $('#dropdownMenukondisi').text(selectedKondisi);
    // });
});
