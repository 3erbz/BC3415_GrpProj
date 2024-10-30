function generateImage() {
  const firstName = document.getElementById("firstName").innerHTML;
  console.log(firstName + " was sent");
  $.ajax({
    url: "/process",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ firstName: firstName }),
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.log(error);
    },
  });
}
