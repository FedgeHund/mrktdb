import React, { useEffect, useState } from 'react';
import '../../../../styles/Filer/TopBuysTable.css';

// Issues
// Currently some data is null, when we have data for topSellchangePercent1
// Modify the code as:
// .toFixed(2) + " %";
// var topSellchangePercent1 = data[0]["changeInPositionPercent"].toFixed(2) + " %";
function TopSellsTable(props) {
    var cik = props.cik;
    var [oldCIK, setOldCIK] = useState(null);
    if (cik !== oldCIK) {
        setOldCIK(cik)
    }

    const [data, setData] = useState([]);
    var URL = "http://www.mrktdb.com/api/latestquartertopsells/?cik=" + oldCIK;

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

    useEffect(() => {
        fetchUrl();
    }, [oldCIK]);

    // Change this according to TopSells
    console.log(data);
    if (typeof data !== 'undefined' && data.length > 0) {
        // Top Sells of the Quarter
        var topSellSymbol1 = ((data[0]["ticker"]) ? (data[0]["ticker"]) : "-");
        var topSellSecurityName1 = ((data[0]["securityName"]) ? (data[0]["securityName"]) : "-");
        var topSellSecurityType1 = ((data[0]["type1"]) ? (data[0]["type1"]) : "-");
        var topSellMarketValue1 = ((data[0]["marketValue"]) ? (data[0]["marketValue"]) : "-");
        var topSellchangePercent1 = ((data[0]["changeInPositionPercent"]) ? (data[0]["changeInPositionPercent"].toFixed(2) + " %") : "-");

        var topSellSymbol2 = ((data[1]["ticker"]) ? (data[1]["ticker"]) : "-");
        var topSellSecurityName2 = ((data[1]["securityName"]) ? (data[1]["securityName"]) : "-");
        var topSellSecurityType2 = ((data[1]["type1"]) ? (data[1]["type1"]) : "-");
        var topSellMarketValue2 = ((data[1]["marketValue"]) ? (data[1]["marketValue"]) : "-");
        var topSellchangePercent2 = ((data[1]["changeInPositionPercent"]) ? (data[1]["changeInPositionPercent"].toFixed(2) + " %") : "-");

        var topSellSymbol3 = ((data[2]["ticker"]) ? (data[2]["ticker"]) : "-");
        var topSellSecurityName3 = ((data[2]["securityName"]) ? (data[2]["securityName"]) : "-");
        var topSellSecurityType3 = ((data[2]["type1"]) ? (data[2]["type1"]) : "-");
        var topSellMarketValue3 = ((data[2]["marketValue"]) ? (data[2]["marketValue"]) : "-");
        var topSellchangePercent3 = ((data[2]["changeInPositionPercent"]) ? (data[2]["changeInPositionPercent"].toFixed(2) + " %") : "-");

        var topSellSymbol4 = ((data[3]["ticker"]) ? (data[3]["ticker"]) : "-");
        var topSellSecurityName4 = ((data[3]["securityName"]) ? (data[3]["securityName"]) : "-");
        var topSellSecurityType4 = ((data[3]["type1"]) ? (data[3]["type1"]) : "-");
        var topSellMarketValue4 = ((data[3]["marketValue"]) ? (data[3]["marketValue"]) : "-");
        var topSellchangePercent4 = ((data[3]["changeInPositionPercent"]) ? (data[3]["changeInPositionPercent"].toFixed(2) + " %") : "-");

        var topSellSymbol5 = ((data[4]["ticker"]) ? (data[4]["ticker"]) : "-");
        var topSellSecurityName5 = ((data[4]["securityName"]) ? (data[4]["securityName"]) : "-");
        var topSellSecurityType5 = ((data[4]["type1"]) ? (data[4]["type1"]) : "-");
        var topSellMarketValue5 = ((data[4]["marketValue"]) ? (data[4]["marketValue"]) : "-");
        var topSellchangePercent5 = ((data[4]["changeInPositionPercent"]) ? (data[4]["changeInPositionPercent"].toFixed(2) + " %") : "-");

    }

    return (
        <div>
            <div className="row">
                <div className="col-11 table_col p-0 m-0">
                    <table className="table table-borderless table-hover BiggestHoldings">
                        <thead>
                            <tr>
                                <th className="top_buys_left_table_head top_buys_biggest_holdings_table_headers">Symbol</th>
                                <th className="top_buys_biggest_holdings_table_headers">Security Name</th>
                                <th className="top_buys_biggest_holdings_table_headers">Security Type</th>
                                <th className="top_buys_biggest_holdings_table_headers">Market Change</th>
                                <th className="top_buys_right_table_head top_buys_biggest_holdings_table_headers">Value Change%</th>
                            </tr>
                        </thead>
                        <tbody className="top_buys_cells_content">
                            <tr>
                                <td className="top_buys_left_table_symbol">{topSellSymbol1}</td>
                                <td>{topSellSecurityName1}</td>
                                <td>{topSellSecurityType1}</td>
                                <td>{topSellMarketValue1}</td>
                                <td>{topSellchangePercent1}</td>
                            </tr>
                            <tr>
                                <td className="top_buys_left_table_symbol">{topSellSymbol2}</td>
                                <td>{topSellSecurityName2}</td>
                                <td>{topSellSecurityType2}</td>
                                <td>{topSellMarketValue2}</td>
                                <td>{topSellchangePercent2}</td>
                            </tr>
                            <tr>
                                <td className="top_buys_left_table_symbol">{topSellSymbol3}</td>
                                <td>{topSellSecurityName3}</td>
                                <td>{topSellSecurityType3}</td>
                                <td>{topSellMarketValue3}</td>
                                <td>{topSellchangePercent3}</td>
                            </tr>
                            <tr>
                                <td className="top_buys_left_table_symbol">{topSellSymbol4}</td>
                                <td>{topSellSecurityName4}</td>
                                <td>{topSellSecurityType4}</td>
                                <td>{topSellMarketValue4}</td>
                                <td>{topSellchangePercent4}</td>
                            </tr>
                            <tr>
                                <td className="top_buys_left_table_symbol">{topSellSymbol5}</td>
                                <td>{topSellSecurityName5}</td>
                                <td>{topSellSecurityType5}</td>
                                <td>{topSellMarketValue5}</td>
                                <td>{topSellchangePercent5}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}


export default TopSellsTable;