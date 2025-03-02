document.addEventListener('DOMContentLoaded', () => {
    // Function to send a prediction request to the backend API.
    async function fetchPrediction() {
      // Replace with your backend's URL once deployed
      const backendURL = 'https://github.com/Enthusiast-kaggle/trading_app/tree/main/backend';
  
      // Create the payload with example features.
      // In a real-world scenario, these values could come from user input or calculations.
      const payload = {
        feature1: 10,  // Example value; update as needed
        feature2: 20   // Example value; update as needed
      };
  
      try {
        const response = await fetch(backendURL, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        });
  
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
  
        const data = await response.json();
        return data;
      } catch (error) {
        console.error('Error fetching prediction:', error);
        return null;
      }
    }
  
    // Function to update the DOM with the prediction data
    async function updatePredictionDisplay() {
      const data = await fetchPrediction();
      if (!data) return;
  
      // Update a DOM element with the ID 'prediction' with the returned prediction.
      const predictionElement = document.getElementById('prediction');
      if (predictionElement) {
        predictionElement.textContent = data.prediction;
      }
    }
  
    // Initial update
    updatePredictionDisplay();
  
    // Optionally, update prediction periodically (every 10 seconds)
    setInterval(updatePredictionDisplay, 10000);
  });
  