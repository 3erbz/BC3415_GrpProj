function sendData() {
  const firstName = document.getElementById("firstName").value;
  $.ajax({
    url: "/process",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ firstName: firstName }),
    success: function (response) {
      console.log(firstName + " sent");
    },
    error: function (error) {
      console.log(error);
    },
  });
}
