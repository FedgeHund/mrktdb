import React, { Fragment, useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
import { URL } from '../App.js';
import '../../../styles/Filer/filer.css';
import SummaryTable from "./Figures/SummaryTable";
import QuarterMarketValueChart from "./Figures/QuarterMarketValueChart";
import BiggestHoldingsTable from "./Figures/BiggestHoldingsTable";
import TopBuysTable from "./Figures/TopBuysTable";

function Filer(props) {

    const [filerData, setFilerData] = useState();

    let cik = props.match.params.cik;

    // let thePath = window.location.href;
    // let securityName = thePath.substring(thePath.lastIndexOf('/') + 1);

    const getFilerData = async () => {
        let particular_filer_url = 'http://' + URL + '/api/company/?search=' + cik;

        const particular_filer = await axios.get(particular_filer_url);

        setFilerData(particular_filer.data[0]);
    };

    useEffect(() => {
        getFilerData();
    }, [cik]);

    return (
        <Fragment>

            <Navbar />

            <div className="filer_container ">
                <div className="filer">
                    <div className="row">
                        <div className="col-6">
                            <div className="row filer_heading">
                                {filerData ? filerData.name : null}
                            </div>
                            <div className="row">
                                <div className="filer_address p-0">{filerData ? filerData.address : null}</div>
                            </div>
                        </div>
                        {/* <div className="filer_cik col-2">CIK: {filerData ? filerData.cik : null}</div> */}
                        <div className="offset-2 col-4">
                            <SummaryTable cik={filerData ? filerData.cik : null} />
                        </div>
                    </div>
                </div>
            </div>

            <div className="market_value_graph_container">
                <div className="market_value_graph">
                    <div className="row mt-5 mb-5">
                        <div className="col-5 shadow-sm mt-4 mb-4 p-3 filer_page_section_heading">
                            <div className="total_market_value_heading">
                                Total Market Value time series
                            </div>
                            <div className="row filerName_in_marketValue_graph_head">{filerData ? filerData.name : null}</div>
                        </div>
                    </div>
                    <QuarterMarketValueChart cik={filerData ? filerData.cik : null} />
                </div>
            </div>

            <div className="biggest_holdings_container">
                <div className="biggest_holdings">
                    <div className="row mt-5 mb-5">
                        <div className="col-5 shadow-sm mt-4 mb-4 p-3 filer_page_section_heading">
                            <div className="total_market_value_heading">
                                Biggest Holdings
                            </div>
                            <div className="row filerName_in_marketValue_graph_head">{filerData ? filerData.name : null}</div>
                        </div>
                    </div>
                    <BiggestHoldingsTable cik={filerData ? filerData.cik : null} />
                </div>
            </div>

            <div className="top_buys_container">
                <div className="top_buys">
                    <div className="row mt-5 mb-5">
                        <div className="col-5 shadow-sm mt-4 mb-4 p-3 filer_page_section_heading">
                            <div className="total_market_value_heading">
                                Top Buys of the Quarter
                            </div>
                            <div className="row filerName_in_marketValue_graph_head">{filerData ? filerData.name : null}</div>
                        </div>
                    </div>
                    <TopBuysTable cik={filerData ? filerData.cik : null} />
                </div>
            </div>

            <Footer />

        </Fragment >
    );
}

export default Filer;