async function loadCloud() {
    const r = await fetch("/api/cloud_data");
    const d = await r.json();

    document.getElementById("cloudInstances").innerHTML =
        d.instances.map(i => `<p>${i.name}: ${i.cpu}% CPU</p>`).join("");

    document.getElementById("cloudStorage").innerHTML =
        `<p>Storage Used: ${d.storage}%</p>`;

    const ctx = document.getElementById("cloudNet").getContext("2d");
    new Chart(ctx, {
        type: "line",
        data: {
            labels: d.network.map((_, i) => i),
            datasets: [{ label: "Network", data: d.network }]
        }
    });
}
loadCloud();
