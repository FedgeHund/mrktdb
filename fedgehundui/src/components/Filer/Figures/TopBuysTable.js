import React, { useEffect, useState } from 'react';
import '../../../../styles/Filer/TopBuysTable.css';

// Issues
// Currently some data is null, when we have data for topBuychangePercent1
// Modify the code as:
// .toFixed(2) + " %";
// var topBuychangePercent1 = data[0]["changeInPositionPercent"].toFixed(2) + " %";
function TopBuysTable(props) {
    var cik = props.cik;
    var [oldCIK, setOldCIK] = useState(null);
    if (cik !== oldCIK) {
        setOldCIK(cik)
    }

    const [data, setData] = useState([]);
    var URL = "http://www.mrktdb.com/api/latestquartertopbuys/?cik=" + oldCIK;

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

    // Change this according to TopBuys
    if (typeof data !== 'undefined' && data.length > 0) {
        // Top Buys of the Quarter
        var topBuySymbol1 = data[0]["ticker"] ? data[0]["ticker"] : "-";
        var topBuySecurityName1 = data[0]["securityName"] ? data[0]["securityName"] : "-";
        var topBuySecurityType1 = data[0]["type1"] ? data[0]["type1"] : "-";
        var topBuyMarketValue1 = data[0]["marketValue"] ? data[0]["marketValue"] : "-";
        var topBuychangePercent1 = ((data[0]["changeInPositionPercent"]) ? (data[0]["changeInPositionPercent"].toFixed(2) + " %") : "-");

        var topBuySymbol2 = data[1]["ticker"] ? data[1]["ticker"] : "-";
        var topBuySecurityName2 = data[1]["securityName"] ? data[1]["securityName"] : "-";
        var topBuySecurityType2 = data[1]["type1"] ? data[1]["type1"] : "-";
        var topBuyMarketValue2 = data[1]["marketValue"] ? data[1]["marketValue"] : "-";
        var topBuychangePercent2 = ((data[1]["changeInPositionPercent"]) ? (data[1]["changeInPositionPercent"].toFixed(2) + " %") : "-");

        var topBuySymbol3 = data[2]["ticker"] ? data[2]["ticker"] : "-";
        var topBuySecurityName3 = data[2]["securityName"] ? data[2]["securityName"] : "-";
        var topBuySecurityType3 = data[2]["type1"] ? data[2]["type1"] : "-";
        var topBuyMarketValue3 = data[2]["marketValue"] ? data[2]["marketValue"] : "-";
        var topBuychangePercent3 = ((data[2]["changeInPositionPercent"]) ? (data[2]["changeInPositionPercent"].toFixed(2) + " %") : "-");

        var topBuySymbol4 = data[3]["ticker"] ? data[3]["ticker"] : "-";
        var topBuySecurityName4 = data[3]["securityName"] ? data[3]["securityName"] : "-";
        var topBuySecurityType4 = data[3]["type1"] ? data[3]["type1"] : "-";
        var topBuyMarketValue4 = data[3]["marketValue"] ? data[3]["marketValue"] : "-";
        var topBuychangePercent4 = ((data[3]["changeInPositionPercent"]) ? (data[3]["changeInPositionPercent"].toFixed(2) + " %") : "-");

        var topBuySymbol5 = data[4]["ticker"] ? data[4]["ticker"] : "-";
        var topBuySecurityName5 = data[4]["securityName"] ? data[4]["securityName"] : "-";
        var topBuySecurityType5 = data[4]["type1"] ? data[4]["type1"] : "-";
        var topBuyMarketValue5 = data[4]["marketValue"] ? data[4]["marketValue"] : "-";
        var topBuychangePercent5 = ((data[4]["changeInPositionPercent"]) ? (data[4]["changeInPositionPercent"].toFixed(2) + " %") : "-");
    }

    return (
        <div>
            <div className="row">
                <div className="col-11 table_head_col p-0 m-0">
                    <table className="table table-borderless table-hover table-responsive BiggestHoldings">
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
                                <td className="top_buys_left_table_symbol">{topBuySymbol1}</td>
                                <td>{topBuySecurityName1}</td>
                                <td>{topBuySecurityType1}</td>
                                <td>{topBuyMarketValue1}</td>
                                <td>{topBuychangePercent1}</td>
                            </tr>
                            <tr>
                                <td className="top_buys_left_table_symbol">{topBuySymbol2}</td>
                                <td>{topBuySecurityName2}</td>
                                <td>{topBuySecurityType2}</td>
                                <td>{topBuyMarketValue2}</td>
                                <td>{topBuychangePercent2}</td>
                            </tr>
                            <tr>
                                <td className="top_buys_left_table_symbol">{topBuySymbol3}</td>
                                <td>{topBuySecurityName3}</td>
                                <td>{topBuySecurityType3}</td>
                                <td>{topBuyMarketValue3}</td>
                                <td>{topBuychangePercent3}</td>
                            </tr>
                            <tr>
                                <td className="top_buys_left_table_symbol">{topBuySymbol4}</td>
                                <td>{topBuySecurityName4}</td>
                                <td>{topBuySecurityType4}</td>
                                <td>{topBuyMarketValue4}</td>
                                <td>{topBuychangePercent4}</td>
                            </tr>
                            <tr>
                                <td className="top_buys_left_table_symbol">{topBuySymbol5}</td>
                                <td>{topBuySecurityName5}</td>
                                <td>{topBuySecurityType5}</td>
                                <td>{topBuyMarketValue5}</td>
                                <td>{topBuychangePercent5}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}


export default TopBuysTable;