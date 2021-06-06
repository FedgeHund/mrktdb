import React, { useState, useEffect } from 'react';
import '../../../styles/Stock/FundsHoldingStockTable.css';
import Pagination from "./Pagination";

function FundsHoldingStockTable(props) {
    var ticker = props.ticker;
    var [oldTicker, setOldTicker] = useState(null);
    if (ticker !== oldTicker) {
        setOldTicker(ticker)
    }

    const [currentPage, setCurrentPage] = useState(1);
    const [rowsPerPage] = useState(10);

    const [data, setData] = useState([]);

    var URL = "http://www.mrktdb.com/api/fundsholdingstock/?ticker=" + oldTicker;

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
    }, [oldTicker]);

    // Get current posts
    const indexOfLastRow = currentPage * rowsPerPage;
    const indexOfFirstRow = indexOfLastRow - rowsPerPage;
    const currentRows = data.slice(indexOfFirstRow, indexOfLastRow);

    // Change page
    const paginate = (pageNumber) => {
        if (pageNumber <= Math.ceil(data.length / rowsPerPage) && pageNumber > 0)
            setCurrentPage(pageNumber);
    }

    return (
        <div>
            <div className="row">
                <div className="col-12 funds_holding_stock_div p-0 m-0">
                    <table className="table table-borderless table-hover table-responsive FundsHoldingStockTable">
                        <thead className="funds_holding_stock_head">
                            <tr className="funds_holding_stock_head_row">
                                <th className="biggest_holdings_table_headers">Fund</th>
                                <th className="biggest_holdings_table_headers">Shares held</th>
                                <th className="biggest_holdings_table_headers">Market Value (x100)</th>
                                <th className="biggest_holdings_table_headers">% of Portfolio</th>
                                <th className="biggest_holdings_table_headers">Prior % of Portfolio</th>
                                <th className="biggest_holdings_table_headers">Change in Shares</th>
                                <th className="biggest_holdings_table_headers">Change of Value</th>
                                <th className="biggest_holdings_table_headers">Change In Position Percent</th>
                                <th className="biggest_holdings_table_headers">Source</th>
                                <th className="biggest_holdings_table_headers">Quarter</th>
                            </tr>
                        </thead>
                        <tbody className="funds_holding_stock_content">
                            {currentRows.map((val, key) => {
                                return (
                                    <tr key={key}>
                                        <td className="fundsHoldingStockName">{val.filerName}</td>
                                        <td>{val.quantity ? val.quantity : "-"}</td>
                                        <td>$ {val.marketValue ? val.marketValue / 100 : "-"}</td>
                                        <td>{val.weightPercent ? val.weightPercent.toFixed(2) + " %" : "-"}</td>
                                        <td>{val.previousWeightPercent ? val.previousWeightPercent.toFixed(2) + " %" : "-"}</td>
                                        {(val.positionType === "Increased" || val.positionType === "New") ?
                                            <td className="shares_increased">{val.changeInShares ? val.changeInShares : "-"}</td>
                                            : <td className="shares_decreased">{val.changeInShares ? val.changeInShares : "-"}</td>
                                        }
                                        <td>{val.changeOfValue ? val.changeOfValue.toFixed(2) : "-"}</td>
                                        {(val.positionType === "Increased" || val.positionType === "New") ?
                                            <td className="shares_increased text-center">{val.changeInPositionPercent ? val.changeInPositionPercent.toFixed(2) + " %" : "-"}</td>
                                            : <td className="shares_decreased text-center">{val.changeInPositionPercent ? val.changeInPositionPercent.toFixed(2) + " %" : "-"}</td>
                                        }
                                        <td>{val.sourceType ? val.sourceType : "-"}</td>
                                        <td>{val.quarter}</td>
                                    </tr>
                                )
                            })}
                        </tbody>
                    </table>
                    <Pagination rowsPerPage={rowsPerPage} totalRows={data.length} paginate={paginate} currentPage={currentPage} />
                </div>
            </div>
        </div>
    )
}

export default FundsHoldingStockTable;