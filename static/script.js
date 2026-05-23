//event-listener en input/output definieren
document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("grid-toggle");
  const grid = document.getElementById("grid-container");
  if (!button || !grid) return;
//definieren wat er gebeurt nadat je de knop indrukt
  button.addEventListener("click", () => {
    grid.classList.toggle("visible");
  });
});

const vollePath = window.location.pathname; // neemt de route
const laatste = vollePath.split("/").filter(Boolean).pop(); // neemt het laatste deel van de route