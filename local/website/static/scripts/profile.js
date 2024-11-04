// Toggle the display of the profile description
function toggleDescription() {
  const descriptionContent = document.querySelector(".description-content");
  const arrow = document.querySelector(".arrow");

  if (
    descriptionContent.style.display === "none" ||
    descriptionContent.style.display === ""
  ) {
    descriptionContent.style.display = "block";
    arrow.classList.add("up"); // Add up class for upward arrow
  } else {
    descriptionContent.style.display = "none";
    arrow.classList.remove("up"); // Remove up class for downward arrow
  }
}

// Ensure the description is hidden on page load
document.addEventListener("DOMContentLoaded", function () {
  document.querySelector(".description-content").style.display = "none";
});

// time lag for image generation
