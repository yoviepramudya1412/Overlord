    var myMap = L.map('map').setView([5.549037601496668, 95.31928497494027], 11);

                                // Tambahkan layer peta
                                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                                    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
                                }).addTo(myMap);

                                function updateMarker(lat, lng) {
                                    if (marker) {
                                        myMap.removeLayer(marker);
                                    }
                                    marker = L.marker([lat, lng]).addTo(myMap);
                                }

                                var marker;
                                myMap.on('click', function (e) {
                                    if (marker) {
                                        myMap.removeLayer(marker);
                                    }
                                    marker = L.marker(e.latlng).addTo(myMap);
                                    var latitude = e.latlng.lat.toFixed(6);
                                    var longitude = e.latlng.lng.toFixed(6);
                                    document.getElementById('latitudeA').value = latitude;
                                    document.getElementById('longitudeB').value = longitude;
                                });
                                var latitudeInput = document.getElementById('latitudeA');
                                var longitudeInput = document.getElementById('longitudeB');
                                latitudeInput.addEventListener('input', function () {
                                    var latitude = parseFloat(latitudeInput.value);
                                    var longitude = parseFloat(longitudeInput.value);

                                    if (!isNaN(latitude) && !isNaN(longitude)) {
                                        updateMarker(latitude, longitude);
                                        myMap.setView([latitude, longitude], 13);
                                    }
                                });

                                longitudeInput.addEventListener('input', function () {
                                    var latitude = parseFloat(latitudeInput.value);
                                    var longitude = parseFloat(longitudeInput.value);

                                    if (!isNaN(latitude) && !isNaN(longitude)) {
                                        updateMarker(latitude, longitude);
                                        myMap.setView([latitude, longitude], 13);
                                    }
                                });
    
    const photoUpload = document.getElementById('file_input');
    const latitudeInput = document.getElementById('latitudeA');
    const longitudeInput = document.getElementById('longitudeB');

    photoUpload.addEventListener('change', function(event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function(event) {
        const image = new Image();
        image.src = event.target.result;

        image.onload = function() {
            EXIF.getData(image, function() {
            const latitude = EXIF.getTag(this, 'GPSLatitude');
            const longitude = EXIF.getTag(this, 'GPSLongitude');

            if (latitude && longitude) {
                const latitudeDecimal = convertDMSToDecimal(latitude);
                const longitudeDecimal = convertDMSToDecimal(longitude);

                latitudeInput.value = latitudeDecimal;
                longitudeInput.value = longitudeDecimal;
            } else {
                console.log('Metadata koordinat tidak ditemukan.');
            }
            });
        };
        };

        reader.readAsDataURL(file);
    });

    function convertDMSToDecimal(coordinate) {
        const degrees = coordinate[0].numerator;
        const minutes = coordinate[1].numerator;
        const seconds = coordinate[2].numerator / coordinate[2].denominator;

        return degrees + minutes / 60 + seconds / 3600;
    }