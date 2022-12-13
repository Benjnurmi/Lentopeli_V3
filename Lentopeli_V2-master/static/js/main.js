'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */

const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);


// global variables

// icons
const blueIcon = L.divIcon({className: "blue-icon"});
const greenIcon = L.divIcon({className: "green-icon"});
// form for player name
document.querySelector("#player-form").addEventListener("submit", function() {
  evt.preventDefault();
  const playerName = document.querySelector("#player-input").value;
  document.querySelector("#player-modal").classList("hide");
});

// function to fetch data from API
async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error("invalid server input!")
    const data = await response.json();
    return data
}

// function to update game status
function updateStatus(status) {
  document.querySelector("#player-name").innerHTML = `Player: ${status.name}`;
  document.querySelector("#consumed").innerHTML = status.co2.consumed;
  document.querySelector("#points").innerHTML = status.co2.budget;
}
// function to show weather at Current Airport
function showWeather(airport) {
  document.querySelector("#current-airport-name").innerHTML = `Weather at ${airport.name}`;
  document.querySelector("#start-airport-temp").innerHTML = `${airport.weather.temp}°C`;
  document.querySelector("#start-weather-icon").src = airport.weather.icon;
  document.querySelector("#start-airport-conditions").innerHTML = airport.weather.description;
  document.querySelector("#start-airport-wind").innerHTML = `${airport.weather.wind.speed}m/s`;
}




// function to check if game is over


// function to set up game
// this is the main function that creates the game and calls the other functions
async function  gameSetup() {
  try {
      const gameData = await getData("testdata/newgame.json");
      console.log(gameData)
      updateStatus(gameData.status);

      for(let airport of gameData.location) {
        const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
        if (airport.active === true) {
          showWeather(airport)
          marker.bindPopup(`You are Here: <b>${airport.name}</b>`);
          marker.openPopup();
          marker.setIcon(greenIcon)
        } else {
          marker.setIcon(blueIcon)
        }

    }

  } catch (error) {
    console.log(error);
  }
  }

  gameSetup()



// event listener to hide goal splash
