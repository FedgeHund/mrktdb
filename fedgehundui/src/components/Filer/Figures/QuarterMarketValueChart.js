import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { URL } from '../../App.js';

function QuarterMarketValueChart(props) {
    var cik = props.cik;
    const [data, setData] = useState([]);
    var quarterId = [];
    var marketValue = [];

    async function fetchUrl() {
        fetch('http://' + URL + '/api/quarterlyfiler/', {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => setData(data));
    }

    useEffect(() => {
        fetchUrl();
    }, [cik]);

    console.log(data);


    for (let i = 0; i < data.length; i++) {
        if (data[i]["cik"] == cik) {
            // console.log(data[i]);
            let q = data[i]["quarter"].toString();
            var quarterName = "".concat("Q", q.substring(0, 1), " ", q.substring(1, 5));
            quarterId.push(quarterName);
            marketValue.push(data[i]["marketValue"]);
        }
    }

    if (typeof marketValue !== 'undefined' && marketValue.length > 0) {
        var chartData = {
            labels: quarterId.reverse(),
            datasets: [
                {
                    label: 'Market Value',
                    lineTension: 0,
                    data: marketValue.reverse(),
                    backgroundColor: [
                        '#12232E',
                    ],
                }
            ],
        }
    }

    return (
        <div>
            {typeof marketValue !== 'undefined' && marketValue.length > 0 ?
                <div>
                    <p> {console.log(marketValue)}</p>
                    <Line
                        data={chartData}
                        width={700}
                        height={500}
                        options={{ maintainAspectRatio: false }}
                    />
                </div>
                : undefined}
        </div>
    )
}


export default QuarterMarketValueChart;