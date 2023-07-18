function hide(hide_content_class_name, show_content_class_name, display_type, hide_btn_class_name, show_btn_class_name) {
    document.getElementsByClassName(hide_content_class_name)[0].style.display = "none";
    document.getElementsByClassName(show_content_class_name)[0].style.display = display_type;
    document.getElementsByClassName(hide_btn_class_name)[0].style.backgroundColor = "var(--bs-orange)";
    document.getElementsByClassName(hide_btn_class_name)[0].style.color = "var(--bs-white)";
    document.getElementsByClassName(show_btn_class_name)[0].style.backgroundColor = "var(--bs-white)";
    document.getElementsByClassName(show_btn_class_name)[0].style.color = "var(--bs-orange)";
}

hide("item_charts", "monthly_revenu_table", "table", "graph_hide_btn", "table_hide_btn");
function monthly_revenu_graph_hide() {
    hide("item_charts", "monthly_revenu_table", "table", "graph_hide_btn", "table_hide_btn");
}
function monthly_revenu_table_hide() {
    hide("monthly_revenu_table", "item_charts", "flex", "table_hide_btn", "graph_hide_btn");
}

const revenue_chart_ctx = document.getElementById("revenue_chart");
const count_chart_ctx = document.getElementById("count_chart");
revenue_chart();
count_chart();

function revenue_chart(){
    new Chart(revenue_chart_ctx, {
        data: {
        labels: monthly_sales_label,
        datasets: [
            {
                type: 'bar',
                label: 'Revenue',
                data: monthly_sales_sale_value,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(201, 203, 207, 0.2)'
                ],
                borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)' ,
                    'rgb(54, 162, 235)',
                    'rgb(153, 102, 255)',
                    'rgb(201, 203, 207)'
                ],
                borderWidth: 1,
            }
        ],
        },
        options: {
            indexAxis: 'y',
            scales: {
                y: {
                beginAtZero: true,
                },
            },
        },
    });
}    

function count_chart(){
    new Chart(count_chart_ctx, {
        data: {
        labels: monthly_sales_label,
        datasets: [
            {
                type: 'bar',
                label: 'Item Count',
                data: monthly_sales_count_value,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(201, 203, 207, 0.2)'
                ],
                borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(54, 162, 235)',
                    'rgb(153, 102, 255)',
                    'rgb(201, 203, 207)'
                ],
                borderWidth: 1,
            }
        ],
        },
        options: {
            indexAxis: 'y',
            scales: {
                y: {
                beginAtZero: true,
                },
            },
        },
    });
}    
