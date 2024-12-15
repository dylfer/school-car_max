// TODO
function signup() {
  let error = document.getElementById("error");
  let username = document.getElementById("name").value;
  let password = document.getElementById("password").value;
  let confirmPassword = document.getElementById("confirmPassword").value;
  let email = document.getElementById("email").value;
  if (password !== confirmPassword) {
    error.classList.remove("hidden");
    error.innerHTML = "Passwords do not match";
    return;
  }
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
      username: username,
      email: email,
      password: password,
      rememberMe: rememberMe,
    })
  );
}

submit = document.getElementById("submit");
submit.addEventListener("click", signup);
