document.addEventListener('DOMContentLoaded', () => {
    const data = {
        helmetUsage: 75,
        numberPlateDetected: 90,
        speedLimitCompliance: 85
    };

    document.getElementById('helmet-usage').textContent = `${data.helmetUsage}%`;
    document.getElementById('number-plate-detected').textContent = `${data.numberPlateDetected}%`;
    document.getElementById('speed-limit-compliance').textContent = `${data.speedLimitCompliance}%`;

    // Additional analytics logic can go here
});
