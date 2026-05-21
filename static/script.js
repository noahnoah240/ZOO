document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("grid-toggle");
  const grid = document.getElementById("grid-container");
  if (!button || !grid) return;

  button.addEventListener("click", () => {
    grid.classList.toggle("visible");
  });
});