function sendData() {
  const firstName = document.getElementById("firstName").value;
  console.log("data sent");

  // hide elements
  document.getElementById("code-gif").hidden = true;
  document.getElementById("loader").hidden = false;
  document.getElementById("sign-up-header").hidden = true;

  $.ajax({
    url: "/process",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ firstName: firstName }),
    success: function (response) {
      console.log("success!");
      // show elements
      document.getElementById("profile-pic").hidden = false;
      document.getElementById("profile-pic-header").hidden = false;

      // hide loading bar
      document.getElementById("loader").hidden = true;
    },
    error: function (error) {
      console.log(error);
    },
  });
}
