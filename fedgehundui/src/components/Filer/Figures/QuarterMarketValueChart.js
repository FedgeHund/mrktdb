import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { URL } from '../../App.js';

function QuarterMarketValueChart(props) {
    var cik = props.cik;
    var [oldCIK, setOldCIK] = useState(null);
    var quarters = [];
    var marketValue = [];
    if (cik !== oldCIK) {
        setOldCIK(cik);
    }

    const [data, setData] = useState([]);
    var URL = "http://www.mrktdb.com/api/quarterlymarketvaluechart/?cik=" + oldCIK;

    async function fetchUrl() {
        fetch(URL, {
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
    }, [oldCIK]);

    for (let i = 0; i < data.length; i++) {
        let q = data[i]["quarter"].toString();
        var quarterName = "".concat("Q", q.substring(4, 5), " ", q.substring(0, 4));
        quarters.push(quarterName);
        marketValue.push(data[i]["marketValue"]);
    }

    if (typeof marketValue !== 'undefined' && marketValue.length > 0) {
        var chartData = {
            labels: quarters,
            datasets: [
                {
                    label: 'Market Value',
                    lineTension: 0,
                    data: marketValue,
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