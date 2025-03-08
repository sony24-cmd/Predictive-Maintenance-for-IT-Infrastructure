document.getElementById('capacityForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    // Get input values
    const cpuUsage = parseFloat(document.getElementById('cpuUsage').value);
    const memoryUsage = parseFloat(document.getElementById('memoryUsage').value);
    const diskUsage = parseFloat(document.getElementById('diskUsage').value);
    const networkUsage = parseFloat(document.getElementById('networkUsage').value);

    // Prepare data for the API request
    const inputData = {
        cpu_usage: cpuUsage,
        memory_usage: memoryUsage,
        disk_usage: diskUsage,
        network_usage: networkUsage
    };

    try {
        // Send data to the backend API
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputData)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Get the prediction result
        const result = await response.json();
        document.getElementById('predictionResult').textContent = `Predicted Capacity Requirement: ${result.predicted_capacity.toFixed(2)}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('predictionResult').textContent = 'Error predicting capacity requirement.';
    }
});

// Fetch and display all predictions
document.getElementById('viewPredictions').addEventListener('click', async function () {
    try {
        const response = await fetch('/predictions');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const predictions = await response.json();
        const predictionsList = document.getElementById('predictionsList');
        predictionsList.innerHTML = '<h2>All Predictions</h2>';

        if (predictions.length === 0) {
            predictionsList.innerHTML += '<p>No predictions found.</p>';
        } else {
            const table = document.createElement('table');
            table.innerHTML = `
                <tr>
                    <th>ID</th>
                    <th>CPU Usage</th>
                    <th>Memory Usage</th>
                    <th>Disk Usage</th>
                    <th>Network Usage</th>
                    <th>Predicted Capacity</th>
                </tr>
            `;

            predictions.forEach(prediction => {
                table.innerHTML += `
                    <tr>
                        <td>${prediction.id}</td>
                        <td>${prediction.cpu_usage}</td>
                        <td>${prediction.memory_usage}</td>
                        <td>${prediction.disk_usage}</td>
                        <td>${prediction.network_usage}</td>
                        <td>${prediction.predicted_capacity.toFixed(2)}</td>
                    </tr>
                `;
            });

            predictionsList.appendChild(table);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});