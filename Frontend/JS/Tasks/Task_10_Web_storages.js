function signup() {
    let un = document.getElementById("username").value;
    let pd = document.getElementById("password").value;

    localStorage.setItem("username", un);
    localStorage.setItem("password", pd);

    alert("Signup successful!");
    window.location.href = "Task_10_login.html";
}


function login() {
    let ln = document.getElementById("username").value;
    let lp = document.getElementById("password").value;

    let storedUser = localStorage.getItem("username");
    let storedPass = localStorage.getItem("password");

    if (ln === storedUser && lp === storedPass) {
        alert("Login successful!");
        window.location.href = "Task_10_home.html";
    } else {
        alert("Entered details are incorrect");
    }
}

localStorage.clear()
