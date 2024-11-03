document.addEventListener('DOMContentLoaded', () => {
    const alertList = document.getElementById('alert-list');

    // Sample data for alerts
    const alerts = [
        { title: "Helmet Violation", description: "A vehicle detected without a helmet.", date: "2024-10-26" },
        { title: "Speed Violation", description: "Speed limit exceeded by vehicle #123", date: "2024-10-26" }
    ];

    alerts.forEach(alert => {
        const li = document.createElement('li');
        li.className = 'alert-item';
        li.innerHTML = `<h4>${alert.title}</h4><p>${alert.description}</p><small>${alert.date}</small>`;
        alertList.appendChild(li);
    });
});
