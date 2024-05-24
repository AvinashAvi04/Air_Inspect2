window.addEventListener("load",()=> {
    
    var ctx = document.getElementById('damageDetectedChart').getContext('2d');
    if (!ctx) {
        console.error("The canvas context is not available.");
        return;
    }
    // Directly create the chart without assigning it to a variable
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Minor Damage', 'Moderate Damage', 'Severe Damage'],
            datasets: [{
                data: [10, 20, 5],
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: { position: 'bottom' }
        }
    });
});
