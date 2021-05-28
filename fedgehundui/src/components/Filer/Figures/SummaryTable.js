import React, { useState, useEffect } from 'react';
import { URL } from '../../App.js';
import '../../../../styles/Filer/SummaryTable.css';

function SummaryTable(props) {
    var cik = props.cik;
    const [data, setData] = useState([]);
    var newFilerArray = [];


    async function fetchUrl() {
        fetch("http://" + URL + "/api/quarterlyfiler/", {
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


    for (let i = 0; i < data.length; i++) {
        if (data[i]["cik"] == cik) {
            newFilerArray.push(data[i]);
        }
    }

    if (typeof newFilerArray !== 'undefined' && newFilerArray.length > 0) {
        var currentMarketValue = newFilerArray[0]["marketValue"];
        var decreasedHoldings = newFilerArray[0]["decreasedHoldingsCount"];
        var increasedHoldings = newFilerArray[0]["increasedHoldingsCount"];
        var newPurchases = newFilerArray[0]["newHoldingsCount"];
        var soldOutOf = newFilerArray[0]["soldOutHoldingsCount"];
        var top10HoldingsPercent = "".concat(newFilerArray[0]["top10HoldingsPercent"].toFixed(2), " %");
    }


    return (
        <div>
            {typeof newFilerArray !== 'undefined' && newFilerArray.length > 0 ?
                <div className="row mt-4">
                    <div className="col-12">
                        <table className="table table-sm table-borderless table-condensed summaryTable pl-3 pr-3">
                            <thead>
                                <tr>
                                    <td className="summaryTableHeading pt-3 pl-3" colSpan="2">13F Summary</td>
                                </tr>
                            </thead>
                            <tbody >
                                <tr>
                                    <td className="summaryTableData pt-2 pl-3">Current Market Value</td>
                                    <td className="summaryTableValue pt-2 pr-3">$ {currentMarketValue}</td>
                                </tr>
                                <tr>
                                    <td className="summaryTableData pl-3">Decreased Holdings</td>
                                    <td className="summaryTableValue pr-3">{decreasedHoldings}</td>
                                </tr>
                                <tr>
                                    <td className="summaryTableData pl-3">Increased Holdings</td>
                                    <td className="summaryTableValue pr-3">{increasedHoldings}</td>
                                </tr>
                                <tr>
                                    <td className="summaryTableData pl-3">New Purchases</td>
                                    <td className="summaryTableValue pr-3">{newPurchases}</td>
                                </tr>
                                <tr>
                                    <td className="summaryTableData pl-3">Sold out of</td>
                                    <td className="summaryTableValue pr-3">{soldOutOf}</td>
                                </tr>
                                <tr>
                                    <td className="summaryTableData pl-3 pb-4">Top 10 holdings Percent</td>
                                    <td className="summaryTableValue pr-3 pb-4">{top10HoldingsPercent}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                : undefined}
        </div>
    )
}

export default SummaryTable;