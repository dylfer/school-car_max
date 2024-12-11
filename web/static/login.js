function login() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "api/auth/login", true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Handle success response
    } else if (xhr.readyState === 4) {
      // Handle error response
      console.error("Error:", xhr.statusText);
    }
  };
  xhr.send(
    JSON.stringify({
      email: email,
      password: password,
    })
  );
}
