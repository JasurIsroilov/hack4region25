var map;

document.addEventListener("DOMContentLoaded", function () {
    ymaps.ready(init);

    function init() {
        var defaultLocation = [41.2995, 69.2401];
        map = new ymaps.Map("map", {
            center: defaultLocation,
            zoom: 12
        });

        function setUserLocation(coords) {
            map.setCenter(coords, 14);
            var placemark = new ymaps.Placemark(coords, { balloonContent: "Sizning joylashuvingiz" });
            map.geoObjects.removeAll();
            map.geoObjects.add(placemark);

            let clinicLatitude = document.getElementById("latitude").value;
            let clinicLongitude = document.getElementById("longitude").value;
            let clinicName = document.getElementById("name").value;

            let clinic_coords = [clinicLatitude, clinicLongitude]
            var clinic_placemark = new ymaps.Placemark(clinic_coords, {balloonContent: clinicName},
                { preset: "islands#redIcon" })
            map.geoObjects.add(clinic_placemark);
        }

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                function (position) {
                    var userLocation = [position.coords.latitude, position.coords.longitude];
                    setUserLocation(userLocation);
                },
                function (error) {
                    console.warn("Joylashuv aniqlanmadi: " + error.message);
                }
            );
        }

        document.getElementById("get-location").addEventListener("click", function () {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    function (position) {
                        var userLocation = [position.coords.latitude, position.coords.longitude];
                        setUserLocation(userLocation);
                    },
                    function (error) {
                        alert("Joylashuv aniqlanmadi: " + error.message);
                    }
                );
            } else {
                alert("Brauzeringiz joylashuvni aniqlashni qo‘llab-quvvatlamaydi.");
            }
        });
        document.getElementById("call_103").addEventListener("click", function () {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;

                fetch("https://example.com/call_ambulance", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ latitude: lat, longitude: lon })
                })
                .then(response => response.json())
                .then(data => {
                    alert("Tez yordam chaqirildi!\nKoordinatalar: " + lat + ", " + lon);
                })
                .catch(error => {
                    alert("Xatolik: Tez yordamni chaqirishda muammo yuzaga keldi!" + "\nKoordinatalar: " + lat + ", " + lon);
                });

            }, function (error) {
                alert("Joylashuv aniqlanmadi: " + error.message);
            });
        } else {
            alert("Brauzeringiz joylashuvni qo‘llab-quvvatlamaydi.");
        }
        });

    }

});
