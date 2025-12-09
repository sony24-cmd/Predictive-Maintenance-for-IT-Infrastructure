document.getElementById("loadData").onclick = load;

function load() {
    fetch("/api/sensor_logs")
        .then(res => res.json())
        .then(data => {
            const tbody = document.querySelector("#dataTable tbody");
            tbody.innerHTML = "";

            data.forEach(row => {
                tbody.innerHTML += `
                  <tr>
                    <td>${row.time}</td>
                    <td>${row.cpu}</td>
                    <td>${row.memory}</td>
                    <td>${row.disk}</td>
                    <td>${row.temp}</td>
                    <td>${row.network}</td>
                  </tr>`;
            });

            const avg = (key) => data.reduce((a,b)=>a+b[key],0)/data.length;

            document.getElementById("statsBox").innerHTML = `
                <p>Average CPU: ${avg("cpu").toFixed(2)}</p>
                <p>Average Memory: ${avg("memory").toFixed(2)}</p>
                <p>Average Disk: ${avg("disk").toFixed(2)}</p>
            `;
        });
}
