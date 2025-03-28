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

function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function getAllCookies() {
    return document.cookie.split('; ').reduce((cookies, cookie) => {
        let [name, value] = cookie.split('=');
        cookies[name] = decodeURIComponent(value);
        return cookies;
    }, {});
}

function loadClinics() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                var userLocation = {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude
                };
                let token = getCookie("access_token");

                fetch("/api/clinics/nearest/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${token}`
                    },
                    body: JSON.stringify(userLocation)
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Serverdan noto‘g‘ri javob keldi");
                    }
                    return response.json();
                })
                .then(data => {
                    if (!Array.isArray(data.clinics)) {
                        throw new Error("Clinics is not an array");
                    }
                    data.clinics.forEach(clinic => {
                        var clinicPlacemark = new ymaps.Placemark(
                            [clinic.latitude, clinic.longitude],
                            { balloonContent: clinic.name },
                            { preset: "islands#redIcon" }
                        );
                        map.geoObjects.add(clinicPlacemark);
                    });
                })
                .catch(error => console.error("Klinikalarni yuklashda xatolik:", error));
            },
            function (error) {
                console.warn("Joylashuv aniqlanmadi: " + error.message);
            }
        );
    } else {
        console.warn("Brauzeringiz joylashuvni qo‘llab-quvvatlamaydi.");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    loadClinics();
});