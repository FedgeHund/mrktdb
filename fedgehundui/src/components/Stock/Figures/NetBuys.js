import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';

/*
Net Buys
    a.  For each stock, for each quarter, for each filer, sum up “change in shares” from previous quarter. This is available in holdings view.
*/

function NetBuys(props) {
    var ticker = props.ticker;
    var [oldTicker, setOldTicker] = useState(null);
    if (ticker !== oldTicker) {
        setOldTicker(ticker)
    }
    var quarters = [];
    var netBuys = [];

    const [data, setData] = useState([]);
    var URL = "http://www.mrktdb.com/api/netbuys/?ticker=" + oldTicker;

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
    }, [oldTicker])

    for (let i = 0; i < data.length; i++) {
        let q = data[i]["quarter"].toString();
        var quarterName = "".concat("Q", q.substring(4, 5), " ", q.substring(0, 4));
        quarters.push(quarterName);
        netBuys.push(data[i]["netBuys"]);
    }

    if (typeof quarters !== 'undefined' && quarters.length > 0) {
        var chartData = {
            labels: quarters,
            datasets: [
                {
                    label: 'Net Buys',
                    lineTension: 0,
                    borderColor: "#2F4F4F",
                    data: netBuys,
                    backgroundColor: [
                        'rgb(255,255,255)',
                    ],
                }
            ],
        }
    }

    return (
        <div>
            {typeof quarters !== 'undefined' && quarters.length > 0 ?
                <Line
                    data={chartData}
                    width={400}
                    height={400}
                    options={{
                        maintainAspectRatio: false,
                        scales: {
                            xAxes: [{
                                gridLines: {
                                    display: false
                                }
                            }],
                            yAxes: [{
                                gridLines: {
                                    display: false
                                }
                            }]
                        }
                    }}
                />
                : undefined}
        </div>
    )
}

export default NetBuys;