const form = document.getElementById("form");
const chartContainer = document.getElementById("chart-container");

let chart = null; // Initialize chart variable

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  console.log("Form submitted");

  const location = document.getElementById("location").value;
  const fromDate = document.getElementById("from_date").value;
  const toDate = document.getElementById("to_date").value;

  const response = await fetch(
    `api.php?location=${location}&from_date=${fromDate}&to_date=${toDate}`
  );

  if (!response.ok) {
    console.error("An error occurred while fetching data:", response.statusText);
    return;
  }

  const data = await response.json();
  console.log("Data fetched from API:", data);

  const labels = data.map((item) => item.date);
  const aqiValues = data.map((item) => item.aqi);

  // Destroy existing chart if it exists
  if (chart) {
    chart.destroy();
  }

  // Remove the old canvas and create a new one
  const oldCanvas = document.getElementById("chart");
  if (oldCanvas) {
    oldCanvas.remove();
  }
  const newCanvas = document.createElement("canvas");
  newCanvas.id = "chart";
  chartContainer.appendChild(newCanvas);
  const ctx = newCanvas.getContext("2d");

  // Create a new chart with the updated data
  chart = createChart(ctx, labels, aqiValues);
});

function createChart(ctx, labels, aqiValues) {
  chartContainer.style.display = "block";

  return new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "AQI",
          data: aqiValues,
          borderColor: "rgba(75, 192, 192, 1)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

// Add this function to fetch locations and populate the select element
async function fetchLocations() {
    const response = await fetch('locations.php');
  
    if (!response.ok) {
      console.error("An error occurred while fetching locations:", response.statusText);
      return;
    }
  
    const locations = await response.json();
    const locationSelect = document.getElementById('location');
    
    locations.forEach(location => {
      const option = document.createElement('option');
      option.value = location.location;
      option.text = location.location;
      locationSelect.appendChild(option);
    });
  }
  
  // Call the fetchLocations function when the page loads
  fetchLocations();
  
