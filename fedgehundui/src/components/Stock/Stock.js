import React, { Fragment, useEffect, useState } from 'react';
import { useLocation } from "react-router-dom";
import axios from 'axios';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
import '../../../styles/security.css';
import { URL } from '../App.js';
import TechnicalAnalysis from "./TradingView/TechnicalAnalysis"
import SymbolInfo from "./TradingView/SymbolInfo"
import CompanyProfile from "./TradingView/CompanyProfile"
import FundamentalData from "./TradingView/FundamentalData"
import AdvancedChart from "./TradingView/AdvancedChart"
import SymbolOverview from "./TradingView/SymbolOverview"
import FundsHoldingStockTable from "./FundsHoldingStockTable"
import NetBuys from "./Figures/NetBuys"
import NetSells from "./Figures/NetSells"
import NumberOfFilersHoldingStocks from "./Figures/NumberOfFilersHoldingStocks"
import SharesHeld from "./Figures/SharesHeld"

function Stock(props) {

    const [securityData, setSecurityData] = useState();
    const location = useLocation();

    //let securityName = props.match.params.securityName;
    let securityName = location.state.SecName;
    let ticker = location.state.ticker;

    // let thePath = window.location.href;
    // let securityName = thePath.substring(thePath.lastIndexOf('/') + 1);

    const getSecurityData = async () => {
        let particular_security_url = 'http://' + URL + '/api/security/?search=' + ticker;

        const particular_security = await axios.get(particular_security_url);

        setSecurityData(particular_security.data);
    };

    useEffect(() => {
        getSecurityData();
    }, [securityName, ticker]);

    return (
        <Fragment>

            <Navbar />
            <div className="security_container ">
                <div className="security">
                    {/* <div className="row">
                        <div className="security_heading col-6">{securityData ? securityData.securityName : null}</div>
                        <div className="security_toc col-5">TOC: {securityData ? securityData.titleOfClass : null}</div>
                    </div>
                    <div className="security_type">{securityData ? securityData.securityType : null}</div> */}

                    <div className="row">
                        <div className="col-12 col-lg-8">
                            <div className="row">
                                <div className="col-12 col-lg-8">
                                    <SymbolInfo ticker={ticker} />
                                </div>
                                <div className="col-12 col-lg-12 mt-5">
                                    <AdvancedChart ticker={ticker} />
                                </div>
                            </div>
                        </div>
                        <div className="col-12 col-lg-4 mt-lg-0 mt-5">
                            <CompanyProfile ticker={ticker} />
                        </div>
                    </div>

                    {/* <div className="row mt-5">
                        <div className="col-12 col-lg-8 mt-5">
                            <div className="row">
                                <div className="offset-2 col-8">
                                    <TechnicalAnalysis ticker={ticker} />
                                </div>
                            </div>
                        </div>
                        <div className="col-12 col-lg-4 mt-5">
                            <FundamentalData ticker={ticker} />
                        </div>
                    </div>

                    <div className="row mt-5">
                        <div className="col-12 mt-5">
                            <SymbolOverview ticker={ticker} />
                        </div>
                    </div> */}

                </div>
            </div>

            <div className="stock_charts_container">
                <div className="stock_charts_container_box">
                    <div className="row">
                        <div className="col-lg-6 col-12 mt-5">
                            <div className="stock_chart_wrapper shadow-sm">
                                <div className="row stock_chart_heading">
                                    <div className="col-4">
                                        <div className="ticker_in_chart_head_box text-center">
                                            <span className="ticker_in_chart_head">{ticker}</span>
                                        </div>
                                    </div>
                                    <div className="col-8 chart_heading">
                                        Net Buys
                                    </div>
                                </div>
                                <NetBuys ticker={ticker} />
                            </div>
                        </div>
                        <div className="col-lg-6 col-12 mt-5">
                            <div className="stock_chart_wrapper shadow-sm">
                                <div className="row stock_chart_heading">
                                    <div className="col-4">
                                        <div className="ticker_in_chart_head_box text-center">
                                            <span className="ticker_in_chart_head">{ticker}</span>
                                        </div>
                                    </div>
                                    <div className="col-8 chart_heading">
                                        Net Sells
                                    </div>
                                </div>
                                <NetSells ticker={ticker} />
                            </div>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col-lg-6 col-12 mt-5">
                            <div className="stock_chart_wrapper shadow-sm">
                                <div className="row stock_chart_heading">
                                    <div className="col-4">
                                        <div className="ticker_in_chart_head_box text-center">
                                            <span className="ticker_in_chart_head">{ticker}</span>
                                        </div>
                                    </div>
                                    <div className="col-8 chart_heading number_of_filer_holding_chart_heading">
                                        Number of Filers holding the Stock
                                    </div>
                                </div>
                                <NumberOfFilersHoldingStocks ticker={ticker} />
                            </div>
                        </div>
                        <div className="col-lg-6 col-12 mt-5">
                            <div className="stock_chart_wrapper shadow-sm">
                                <div className="row stock_chart_heading">
                                    <div className="col-4">
                                        <div className="ticker_in_chart_head_box text-center">
                                            <span className="ticker_in_chart_head">{ticker}</span>
                                        </div>
                                    </div>
                                    <div className="col-8 chart_heading">
                                        Total number of shares held
                                    </div>
                                </div>
                                <SharesHeld ticker={ticker} />
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="fundsHoldingStockTable_container">
                <div className="fundsHoldingStockTable_box">
                    <div className="row">
                        <div className="col-lg-5 col-md-7 shadow-sm p-3 fundsHoldingStockTable_section_heading">
                            <div className="funds_holding_stock_heading">
                                Funds Holding {ticker}
                            </div>
                            <div className="row via_13f_filings_heading">Via 13F Filings</div>
                        </div>
                    </div>
                    <div className="row mt-5">
                        <div className="col-12 mt-4">
                            <FundsHoldingStockTable ticker={ticker} />
                        </div>
                    </div>
                </div>
            </div>

            <Footer />

        </Fragment >
    );
}

export default Stock;