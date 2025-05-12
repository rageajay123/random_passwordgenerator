function generatePassword() {
  const filename = document.getElementById("filename").value;
  if (!filename) {
    alert("Please enter a filename.");
    return;
  }

  fetch("/generate", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ filename: filename })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("password").value = data.password;
  });
}
