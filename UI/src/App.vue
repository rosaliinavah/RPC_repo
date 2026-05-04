<script setup>

import {onMounted, ref, watch} from 'vue'
import axios from 'axios'
import L from 'leaflet'

const lat = ref(0)
const lng = ref(0)
const alt = ref(0)
const pt100 = ref(0)
const pt1000 = ref(0)
const map = ref()
const mapContainer = ref()
let marker = null
let browserWatchId = null


// Variables for GPS route
let path = []
let polyline = null

// Variable to decide whether browser GPS or PLC GPS is in use
const BrowserLocation = ref(false)

// Fetch PLC data from local server
const fetchData = async () => {
  if (BrowserLocation.value) return // not updated if browser GPS is in use

  const res = await axios.get("http://localhost:3000/api/plc/latest")

  pt100.value = res.data.pt100
  pt1000.value = res.data.pt1000
  lat.value = res.data.latitude
  lng.value = res.data.longitude
  alt.value = res.data.altitude


  //map.value.setView([lat.value, lng.value], 13);

  //L.marker([lat.value, lng.value],{draggable : true})
  //      .addTo(map.value)
  //      .on("dragend",(event)=> {
  //          console.log(event)
  //      });
}

// Watch lat/lng changes and move marker
  watch([lat, lng], ([newLat, newLng]) => {

    // Do nothing if map doesn't exist
    if (!map.value) return

    // Create marker only if values are valid
    if (!newLat || !newLng) return

    // Create marker only if it does not exist already
    if (!marker) {

      marker = L.marker([newLat, newLng], { draggable: true })
        .addTo(map.value)

      // Päivitä Vue koordinaatit kun marker liikkuu
      marker.on("dragend", (e) => {
        const pos = e.target.getLatLng()
        lat.value = pos.lat
        lng.value = pos.lng
      })

    } else {

      // Päivitä marker sijainti
      marker.setLatLng([newLat, newLng])
    }

    // Add point to route, but only if it is not almost at the same point as previous point.
    const last = path[path.length-1]

    if (!last ||
      Math.abs(last[0]-newLat) > 0.00001 ||
      Math.abs(last[1]-newLng) > 0.00001) {
      path.push([newLat,newLng])
    }

    // Deletes oldest path point if limit of 300 points is reached -> path is about 5mins
    if (path.length > 300) {
      path.shift()
    }

    // Piirrä polyline
    if (!polyline) {
      polyline = L.polyline(path, { color: "red" }).addTo(map.value)
    } else {
      polyline.setLatLngs(path)
    }


    // Keskitys karttaan vain jos marker liikkuu paljon
    if (!last || Math.abs(last[0]-newLat) > 0.0001 || Math.abs(last[1]-newLng) > 0.0001) {
    map.value.setView([newLat, newLng], map.value.getZoom())
    }
  })

onMounted(() => {
   map.value = L.map(mapContainer.value).setView([51.505, -0.09], 13);
   L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
     maxZoom: 19,
     attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map.value);

    // Set data update interval to 1s
    setInterval(fetchData, 1000);
})

function clearPath() {
  // Clear path data and polyline from map
  path = []
  if (polyline) {
    map.value.removeLayer(polyline)
    polyline = null
  }
  // Delete marker if exists
  //if (marker) {
  //  map.value.removeLayer(marker)
  //  marker = null
  //}
  // Focus map to the original position
  //map.value.setView([62.79030422105269, 22.839460372924805], 13)
}

function UseBrowserLocation() {
  BrowserLocation.value  = !BrowserLocation.value

  // Tyhjennä reitti ja polyline
  clearPath()
  if (BrowserLocation.value) {
    if (navigator.geolocation) {
        browserWatchId = navigator.geolocation.watchPosition((position) => {
          lat.value = position.coords.latitude;
          lng.value = position.coords.longitude;
          // When Browser Location button is clicked -> Move map to coordinate location. Set zoom (min=0 - max=18)
          //map.value.setView([lat.value, lng.value], 13);

          // Add pin marker to the map. Make it draggable, and update coordinates when pin is released
          //L.marker([lat.value, lng.value],{draggable : true})
          //.addTo(map.value)
          //.on("dragend",(event)=> {
          //   console.log(event)
          //});

      })
    }
  }
  else {
    // pysäytä browser GPS
    if (browserWatchId !== null) {
      navigator.geolocation.clearWatch(browserWatchId)
      browserWatchId = null
    }

    fetchData()
  }

}
</script>

<template>
<p>PT100: {{ pt100 }} °C</p>
<p>PT1000: {{ pt1000 }} °C</p>
<p>Altitude: {{ alt }} m</p>

<button @click="UseBrowserLocation" :style="{background: BrowserLocation.value ? '#4caf50' : '#ccc'}">Use browser location</button>

{{ lat }}  ,  {{ lng }}

<div ref="mapContainer" style="width: 400px;height: 400px;"></div>

</template>

<style scoped>

</style>