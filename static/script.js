const form = document.getElementById("weather-form");
const cityInput = document.getElementById("city-input");
const errorMessage = document.getElementById("error-message");
const result = document.getElementById("result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const city = cityInput.value.trim();
  hideError();
  result.classList.add("hidden");

  if (!city) {
    showError("Please enter a city name.");
    return;
  }

  try {
    const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
    const data = await response.json();

    if (!response.ok) {
      showError(data.error || "Something went wrong.");
      return;
    }

    showResult(data);
  } catch (err) {
    showError("Network error. Please check your connection and try again.");
  }
});

function showError(message) {
  errorMessage.textContent = message;
  errorMessage.classList.remove("hidden");
}

function hideError() {
  errorMessage.classList.add("hidden");
}

function showResult(data) {
  const icon = document.getElementById("weather-icon");
  icon.src = `https://openweathermap.org/img/wn/${data.icon}@2x.png`;
  icon.alt = data.description;

  document.getElementById("result-city").textContent = `${data.city}, ${data.country}`;
  document.getElementById("result-description").textContent = data.description;
  document.getElementById("result-temp").textContent = `${data.temp_f}°F / ${data.temp_c}°C`;
  document.getElementById("result-feels-like").textContent =
    `${data.feels_like_f}°F / ${data.feels_like_c}°C`;
  document.getElementById("result-humidity").textContent = `${data.humidity}%`;
  document.getElementById("result-wind").textContent = `${data.wind_speed} m/s`;

  result.classList.remove("hidden");
}
