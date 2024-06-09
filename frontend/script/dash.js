window.onload = function() {
    var ctx1 = document.getElementById('pieChart').getContext('2d');
    var pieChart = new Chart(ctx1, {
        type: 'pie',
        data: {
            labels: ['Total Order', 'Customer Growth', 'Total Revenue'],
            datasets: [{
                data: [75, 357, 128],
                backgroundColor: ['#ff6384', '#36a2eb', '#cc65fe']
            }]
        },
        options: {
            responsive: true
        }
    });

    var ctx2 = document.getElementById('lineChart').getContext('2d');
    var lineChart = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            datasets: [{
                label: 'Orders',
                data: [12, 19, 3, 5, 2, 3, 7],
                borderColor: '#36a2eb',
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                fill: true
            }]
        },
        options: {
            responsive: true
        }
    });

    var ctx3 = document.getElementById('radarChart').getContext('2d');
    var radarChart = new Chart(ctx3, {
        type: 'radar',
        data: {
            labels: ['Eating', 'Drinking', 'Sleeping', 'Designing', 'Coding', 'Cycling', 'Running'],
            datasets: [{
                label: 'Activity',
                data: [65, 59, 90, 81, 56, 55, 40],
                borderColor: '#ff6384',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: true
            }]
        },
        options: {
            responsive: true
        }
    });

    var ctx4 = document.getElementById('barChart').getContext('2d');
    var barChart = new Chart(ctx4, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            datasets: [{
                label: '2020',
                data: [12, 19, 3, 5, 2, 3, 9, 10, 8, 6, 7, 4],
                backgroundColor: '#ff6384'
            }, {
                label: '2021',
                data: [14, 15, 5, 6, 7, 8, 10, 12, 9, 8, 6, 7],
                backgroundColor: '#36a2eb'
            }]
        },
        options: {
            responsive: true
        }
    });
};
