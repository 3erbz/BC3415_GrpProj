// record audio
// var startButton = document.getElementById("start");
// var stopButton = document.getElementById("stop");
// var resultElement = document.getElementById("result");

// var recognition = new webkitSpeechRecognition();
// recognition.lang = window.navigator.language;
// recognition.interimResults = true;

// startButton.addEventListener("click", () => {
//   recognition.start();
// });
// stopButton.addEventListener("click", () => {
//   recognition.stop();
// });

// recognition.addEventListener("result", (event) => {
//   const result = event.results[event.results.length - 1][0].transcript;
//   resultElement.textContent = result;
// });

// // send data to python
// function sendData() {
//   var value = resultElement.textContent;
//   $.ajax({
//     url: "/explore/analysis",
//     type: "POST",
//     contentType: "application/json",
//     data: JSON.stringify({ value: value }),
//     success: function (response) {
//       document.getElementById("output").textContent = response.result;
//     },
//     error: function (error) {
//       console.log(error);
//     },
//   });
// }

// to gather data back from python

// testing function
function sendData() {
  console.log("test successful");
}
