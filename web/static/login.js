// TODO
function login() {
  let error = document.getElementById("error");
  let username = document.getElementById("username").value; //username/email
  let password = document.getElementById("password").value;
  let rememberMe = document.getElementById("rememberMe").checked;
  let xhr = new XMLHttpRequest();
  xhr.open("POST", "/api/auth/login", true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Handle success response
      let response = JSON.parse(xhr.responseText);
      if (response.message == "sucsess") {
        window.location.href = "dashboard";
      }
    } else if (xhr.readyState === 4) {
      // Handle error response
      error.classList.remove("hidden");
      error.innerHTML = xhr.statusText;
    }
  };
  xhr.send(
    JSON.stringify({
      username: username, // username or email
      password: password,
      rememberMe: rememberMe,
    })
  );
}

submit = document.getElementById("submit");
submit.addEventListener("click", login);
