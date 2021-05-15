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

                    <div className="row mt-5">
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
                    </div>

                </div>
            </div>

            {/* <div>
                <SymbolInfo ticker={ticker} />
                <MiniChart ticker={ticker} />
                <CompanyProfile ticker={ticker} />
                <FundamentalData ticker={ticker} />
                <TechnicalAnalysis ticker={ticker} />
                <AdvancedChart ticker={ticker} />
                <SymbolOverview ticker={ticker} />
            </div> */}

            <Footer />

        </Fragment >
    );
}

export default Stock;