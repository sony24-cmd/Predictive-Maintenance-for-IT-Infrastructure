async function loadCharts() {
    const r = await fetch("/api/sensor_logs");
    const data = await r.json();

    const labels = data.map(d => d.time);
    const cpu = data.map(d => d.cpu);
    const mem = data.map(d => d.memory);
    const disk = data.map(d => d.disk);

    new Chart(cpuChart, { type: "line",
        data: { labels, datasets: [{ label:"CPU", data: cpu }] }
    });

    new Chart(memChart, { type: "line",
        data: { labels, datasets: [{ label:"Memory", data: mem }] }
    });

    new Chart(diskChart, { type: "bar",
        data: { labels, datasets: [{ label:"Disk", data: disk }] }
    });
}
loadCharts();
