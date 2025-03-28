document.addEventListener("DOMContentLoaded", function () {

    let regionCityMap = JSON.parse('{{ region_city_mapping|safe }}');

    let regionSelect = document.getElementById("regionFilter");
    let citySelect = document.getElementById("cityFilter");
    let resetButton = document.getElementById("resetFilters");

    regionSelect.addEventListener("change", function () {
        let selectedRegion = regionSelect.value;

        if (!selectedRegion) return;

        let cities = regionCityMap[selectedRegion] || [];

        citySelect.innerHTML = '<option value="" selected disabled>Shaharni tanlang...</option>';

        cities.forEach(city => {
            let option = document.createElement("option");
            option.value = city[0];
            option.textContent = city[1];
            citySelect.appendChild(option);
        });

        citySelect.disabled = cities.length === 0;
    });

    resetButton.addEventListener("click", function () {
        regionSelect.value = "";
        citySelect.innerHTML = '<option value="" selected disabled>Shaharni tanlang...</option>';
        citySelect.disabled = true;
    });
});
