const button = document.querySelector("button");
const comment = document.querySelector(".comment");

button.addEventListener("click", function() {
  comment.classList.toggle("hidden");
});