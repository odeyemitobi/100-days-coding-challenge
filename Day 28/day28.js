function login() {
  var username = document.getElementById("loginUsername").value;
  var password = document.getElementById("loginPassword").value;

  if (username === "yourUsername" && password === "yourPassword") {
    alert("Login successful!");
  } else {
    alert("Invalid username or password. Try again.");
  }
}

function signup() {
  var newUsername = document.getElementById("newUsername").value;
  var newPassword = document.getElementById("newPassword").value;

  alert("Account created for " + newUsername + ". You can now log in.");
}
