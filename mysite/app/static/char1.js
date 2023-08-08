
// Fetch data from server
let label = '';
fetch('/plot')
    .then(response => response.json())
    .then(plot => {
        // Graph
        var ctx = document.getElementById("myChart");

        var myChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: plot.Xlabel,
                datasets: [
                    {
                        data: plot.nilai,
                        lineTension: 0,
                        backgroundColor: "transparent",
                        borderColor: "#007bff",
                        borderWidth: 4,
                        pointBackgroundColor: "#007bff",
                    },
                ],
            },
            options: {
                scales: {
                    yAxes: [
                        {
                            ticks: {
                                beginAtZero: false,
                            },
                        },
                    ],
                },
                legend: {
                    display: false,
                },
            },
        });
    })
    .catch(error => console.error('Error:', error));
