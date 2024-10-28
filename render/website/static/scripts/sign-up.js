function sendData() {
  const firstName = document.getElementById("firstName").value;
  console.log("data sent");

  // hide elements
  document.getElementById("code-gif").hidden = true;
  document.getElementById("sign-up-header").hidden = true;
  document.getElementById("generate-profile-pic").hidden = true;

  // show loading bar
  document.getElementById("loader").hidden = false;

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
      document.getElementById("submit-button").hidden = false;

      // hide loading bar
      document.getElementById("loader").hidden = true;
    },
    error: function (error) {
      console.log(error);
    },
  });
}
