document.getElementById("anomBtn").onclick = () => {
    fetch("/api/anomaly_check")
        .then(res => res.json())
        .then(d => {
            document.getElementById("anomResult").innerHTML =
                `Value: ${d.value} — <b>${d.is_anomaly ? "ANOMALY" : "Normal"}</b>`;
        });
};
