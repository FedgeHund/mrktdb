import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';

function Ownershiphistory(props) {
    var cik = props.cik;
    var cusip = props.cusip;
    var [oldCIK, setOldCIK] = useState(null);
    var [oldCusip, setOldCusip] = useState(null);
    var quarters = [];
    var quantities = [];
    var marketValues = [];

    if (cik !== oldCIK) {
        setOldCIK(cik);
    }

    if (cusip !== oldCusip) {
        setOldCusip(cusip);
    }

    const [data, setData] = useState([]);
    var URL = "http://www.mrktdb.com/api/ownershiphistory/?cik=" + oldCIK + "&cusip=" + oldCusip;
    console.log(URL);

    async function fetchUrl() {
        // console.log(cik)
        fetch(URL, {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

        })
            .then(response => response.json())
            .then(data => setData(data));
    }
    console.log("This is CUSIP data:");
    console.log(data);
    if (typeof data !== 'undefined' && data.length > 0) {
        for (let i = 0; i < data.length; i++) {
            let q = data[i]["quarter"].toString();
            var quarterName = "".concat("Q", q.substring(4, 5), " ", q.substring(0, 4));
            quarters.push(quarterName);
            quantities.push(data[i]["quantity"]);
            marketValues.push(data[i]["marketValue"])
        }


        if (typeof marketValues !== 'undefined' && marketValues.length > 0) {
            var chartData = {
                datasets: [
                    {
                        type: 'line',
                        label: 'Market Value',
                        lineTension: 0,
                        data: marketValues,
                        backgroundColor: [
                            '#12232E',
                        ],
                        yAxisID: 'y-axis-2',
                    },
                    {
                        type: 'bar',
                        label: 'Quantity',
                        lineTension: 0,
                        data: quantities,
                        backgroundColor: [
                            '#12232E',
                        ],
                        yAxisID: 'y-axis-1',
                    }
                ],
            }

        }


    }

    const chartOptions = {
        responsive: true,
        tooltips: {
            mode: 'label'
        },
        scales: {
            xAxes: [
                {
                    display: true,
                    gridLines: {
                        display: false
                    },
                    labels: quarters,
                }
            ],
            yAxes: [
                {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    id: 'y-axis-1',
                    gridLines: {
                        display: false
                    },
                    labels: {
                        show: true
                    }
                },
                {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    id: 'y-axis-2',
                    gridLines: {
                        display: false
                    },
                    labels: {
                        show: true
                    }
                }
            ]
        }
    };


    useEffect(() => {
        fetchUrl();
    }, [oldCIK]);


    return (
        <div>
            {typeof quantities !== 'undefined' && quantities.length > 0 ?
                <div>
                    <Bar
                        data={chartData}
                        options={chartOptions}
                    />
                </div>
                : undefined}
        </div>)
}


export default Ownershiphistory;