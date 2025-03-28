document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("login-button").addEventListener("click", function (event) {

        let phone_number = document.getElementById("username").value;
        let password = document.getElementById("password").value;

        fetch("/api/account/login/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ phone_number: phone_number, password: password })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Login xatosi");
            }
            return response.json();
        })
        .then(data => {
            document.cookie = `token=${data.token}; path=/; Secure; HttpOnly`;
            alert("Tizimga muvaffaqiyatli kirdingiz!");
            window.location.href = "/account/profile/";
        })
        .catch(error => {
            console.error("Login xatosi:", error);
            alert("Login amalga oshmadi!");
        });
    });
});