function generateImage() {
  const firstName = document.getElementById("firstName").innerHTML;
  console.log(firstName + " was sent");
  $.ajax({
    url: "/generate-image",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ firstName: firstName }),
    success: function (response) {
      console.log(response);
      const img = document.getElementById("img");
      img.src = `data:image/jpeg;base64,${response["img"]}`;
    },
    error: function (error) {
      console.log(error);
    },
  });
}
