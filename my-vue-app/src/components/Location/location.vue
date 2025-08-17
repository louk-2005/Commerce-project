<script setup>
import { onMounted } from 'vue'
import * as L from 'leaflet'
import axios from 'axios'

let map

// Map layers
const baseLayers = {
  "simple": L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'),
  "bright": L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png'),
  "dark": L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'),
  "satellite": L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}')
}

onMounted(async () => {
  map = L.map('map', {
    center: [40.730610, -73.935242],
    zoom: 5,
    layers: [baseLayers["simple"]],
    zoomControl: true
  })

  // Layer control
  L.control.layers(baseLayers).addTo(map)

  // Fetch locations from API
  try {
    const response = await axios.get('http://localhost:8000/accounts/locations/')
    const locations = response.data

    locations.forEach((loc) => {
      const lat = parseFloat(loc.latitude)
      const lng = parseFloat(loc.longitude)

      if (!isNaN(lat) && !isNaN(lng)) {
        L.marker([lat, lng])
          .addTo(map)
          .bindPopup(`
            <div style="text-align: start; max-width: 250px;">
              <h4>${loc.name}</h4>
              <p>${loc.description}</p>
              <img src="${loc.image}" alt="${loc.name}" />
            </div>
          `)
      }
    })
  } catch (error) {
    console.error('❌ Error loading locations:', error)
  }
})
</script>

<template>
  <div class="location">
    <div class="location-box">
      <div class="location-content">
        <div id="map" class="location-info"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
:deep(.leaflet-popup-content-wrapper),
:deep(.leaflet-popup-tip) {
  border-radius: 0 !important;
}

:deep(.leaflet-popup-content) {
  padding: 0 !important;
  margin: 15px 0 !important;
  overflow: hidden !important;
  border-radius: 0 !important;
  text-align: left;
  direction: ltr;
  font-family: "Arial", sans-serif;
}

:deep(.leaflet-popup-content) p {
  margin: 5px 15px 15px;
}

:deep(.leaflet-popup-content) h4 {
  margin: 0 15px;
}

:deep(.leaflet-popup-content) img {
  display: block;
  margin: 0 auto !important;
  max-width: 220px;
  max-height: 150px;
}

.location-info {
  height: 500px;
}
/* Responsive Map */
@media (max-width: 1024px) {
  .location-info {
    height: 400px;
  }
}

@media (max-width: 768px) {
  .location-info {
    height: 300px;
  }
}

@media (max-width: 480px) {
  .location-info {
    height: 250px;
  }
}

</style>
