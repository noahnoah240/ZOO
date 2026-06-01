//event-listener en input/output definieren
document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("menu-toggle");
  const grid = document.getElementById("menu-container");
  if (!button || !grid) return;
//definieren wat er gebeurt nadat je de knop indrukt
  button.addEventListener("click", () => {
    grid.classList.toggle("visible");
  });
  
  // Favorite button functionality
  const favoriteBtn = document.getElementById("favorite-btn");
  if (favoriteBtn) {
    favoriteBtn.addEventListener("click", toggleFavorite);
  }
});

function toggleFavorite(e) {
  const btn = e.target.closest("#favorite-btn");
  if (!btn) return;

  const dierId = btn.dataset.dierId;
  if (!dierId) {
    console.error("Favorite button missing dier_id");
    return;
  }

  fetch("/api/favorite", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ dier_id: dierId })
  })
  .then(response => {
    if (response.status === 401) {
      window.location.href = "/login";
      return null;
    }
    return response.json().then(data => ({ status: response.status, data }));
  })
  .then(result => {
    if (!result) return;

    if (result.status !== 200) {
      console.error("Favorite API error:", result.data);
      return;
    }

    const icon = btn.querySelector(".favorite-icon");
    const text = btn.querySelector(".favorite-text");

    if (result.data.favorited) {
      btn.classList.add("favorited");
      icon.textContent = "★";
      text.textContent = "Favoriet";
    } else {
      btn.classList.remove("favorited");
      icon.textContent = "☆";
      text.textContent = "Als favoriet toevoegen";
    }
  })
  .catch(error => console.error("Error:", error));
}


