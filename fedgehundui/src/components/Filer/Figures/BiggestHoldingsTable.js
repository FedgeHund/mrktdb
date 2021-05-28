import React, { useState, useEffect } from 'react';
import '../../../../styles/Filer/BiggestHoldingsTable.css';

// Issues:
// Price is to be converted to whole number or it is to be displayed as decimal
// Add border radius / make table border curved
function BiggestHoldingsTable(props) {
    var cik = props.cik;
    var [oldCIK, setOldCIK] = useState(null);
    if (cik !== oldCIK) {
        setOldCIK(cik)
    }

    const [data, setData] = useState([]);
    var URL = "http://www.mrktdb.com/api/latestquarterbiggestholdings/?cik=" + oldCIK;

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

    if (typeof data !== 'undefined' && data.length > 0) {
        // Top 5 Biggest Holdings
        var symbol1 = data[0]["ticker"] ? data[0]["ticker"] : "-";
        var securityName1 = data[0]["securityName"] ? data[0]["securityName"] : "-";
        var securityType1 = data[0]["type1"] ? data[0]["type1"] : "-";
        var price1 = data[0]["lastPrice"] ? Math.round(data[0]["lastPrice"]) : "-";
        var marketValue1 = data[0]["marketValue"] ? data[0]["marketValue"] : "-";
        var weightPercent1 = data[0]["weightPercent"] ? data[0]["weightPercent"].toFixed(2) + " %" : "-";

        var symbol2 = data[1]["ticker"] ? data[1]["ticker"] : "-";
        var securityName2 = data[1]["securityName"] ? data[1]["securityName"] : "-";
        var securityType2 = data[1]["type1"] ? data[1]["type1"] : "-";
        var price2 = data[1]["lastPrice"] ? Math.round(data[1]["lastPrice"]) : "-";
        var marketValue2 = data[1]["marketValue"] ? data[1]["marketValue"] : "-";
        var weightPercent2 = data[1]["weightPercent"] ? data[1]["weightPercent"].toFixed(2) + " %" : "-";

        var symbol3 = data[2]["ticker"] ? data[2]["ticker"] : "-";
        var securityName3 = data[2]["securityName"] ? data[2]["securityName"] : "-";
        var securityType3 = data[2]["type1"] ? data[2]["type1"] : "-";
        var price3 = data[2]["lastPrice"] ? Math.round(data[2]["lastPrice"]) : "-";
        var marketValue3 = data[2]["marketValue"] ? data[2]["marketValue"] : "-";
        var weightPercent3 = data[2]["weightPercent"] ? data[2]["weightPercent"].toFixed(2) + " %" : "-";

        var symbol4 = data[3]["ticker"] ? data[3]["ticker"] : "-";
        var securityName4 = data[3]["securityName"] ? data[3]["securityName"] : "-";
        var securityType4 = data[3]["type1"] ? data[3]["type1"] : "-";
        var price4 = data[3]["lastPrice"] ? Math.round(data[3]["lastPrice"]) : "-";
        var marketValue4 = data[3]["marketValue"] ? data[3]["marketValue"] : "-";
        var weightPercent4 = data[3]["weightPercent"] ? data[3]["weightPercent"].toFixed(2) + " %" : "-";

        var symbol5 = data[4]["ticker"] ? data[4]["ticker"] : "-";
        var securityName5 = data[4]["securityName"] ? data[4]["securityName"] : "-";
        var securityType5 = data[4]["type1"] ? data[4]["type1"] : "-";
        var price5 = data[4]["lastPrice"] ? Math.round(data[4]["lastPrice"]) : "-";
        var marketValue5 = data[4]["marketValue"] ? data[4]["marketValue"] : "-";
        var weightPercent5 = data[4]["weightPercent"] ? data[4]["weightPercent"].toFixed(2) + " %" : "-";
    }


    return (
        <div>
            <div className="row">
                <div className="col-lg-9 col-md-11 table_col p-0 m-0">
                    <table className="table table-borderless table-hover table-responsive BiggestHoldings">
                        <thead>
                            <tr>
                                <th className="left_table_head biggest_holdings_table_headers">Symbol</th>
                                <th className="biggest_holdings_table_headers">Security Name</th>
                                <th className="biggest_holdings_table_headers">Security Type</th>
                                <th className="biggest_holdings_table_headers">Price</th>
                                <th className="biggest_holdings_table_headers">Market Value (x1000)</th>
                                <th className="right_table_head biggest_holdings_table_headers">% Weight</th>
                            </tr>
                        </thead>
                        <tbody className="biggest_holdings_content">
                            <tr>
                                <td className="left_table_symbol">{symbol1}</td>
                                <td>{securityName1}</td>
                                <td>{securityType1}</td>
                                <td>{price1}</td>
                                <td>{marketValue1}</td>
                                <td>{weightPercent1}</td>
                            </tr>
                            <tr>
                                <td className="left_table_symbol">{symbol2}</td>
                                <td>{securityName2}</td>
                                <td>{securityType2}</td>
                                <td>{price2}</td>
                                <td>{marketValue2}</td>
                                <td>{weightPercent2}</td>
                            </tr>
                            <tr>
                                <td className="left_table_symbol">{symbol3}</td>
                                <td>{securityName3}</td>
                                <td>{securityType3}</td>
                                <td>{price3}</td>
                                <td>{marketValue3}</td>
                                <td>{weightPercent3}</td>
                            </tr>
                            <tr>
                                <td className="left_table_symbol">{symbol4}</td>
                                <td>{securityName4}</td>
                                <td>{securityType4}</td>
                                <td>{price4}</td>
                                <td>{marketValue4}</td>
                                <td>{weightPercent4}</td>
                            </tr>
                            <tr>
                                <td className="left_table_symbol">{symbol5}</td>
                                <td>{securityName5}</td>
                                <td>{securityType5}</td>
                                <td>{price5}</td>
                                <td>{marketValue5}</td>
                                <td>{weightPercent5}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}

export default BiggestHoldingsTable;