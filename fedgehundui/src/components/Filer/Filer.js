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
import TopSellsTable from "./Figures/TopSellsTable";
import OwnedSecurities from "./Figures/OwnedSecurities"

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
        fetchUrl();
    }, [cik]);


    const [aum, setAum] = useState([]);
    var newFilerArray = [];

    async function fetchUrl() {
        fetch("http://" + URL + "/api/quarterlyfiler/", {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => setAum(data));
    }

    for (let i = 0; i < aum.length; i++) {
        if (aum[i]["cik"] === cik) {
            newFilerArray.push(aum[i]);
        }
    }

    var currentAUM;

    if (typeof newFilerArray !== 'undefined' && newFilerArray.length > 0) {
        currentAUM = newFilerArray[0]["marketValue"];
    }

    return (
        <Fragment>

            <Navbar />

            <div className="filer_container ">
                <div className="filer">
                    <div className="row">
                        <div className="col-md-6 col-12">
                            <div className="row filer_heading">
                                {filerData ? filerData.name : null}
                            </div>
                            <div className="row mb-4">
                                <div className="filer_address p-0">{filerData ? filerData.address : null}</div>
                            </div>
                            <div className="row filer_desc mt-5 d-inline-block">
                                <span className="filer_description">{filerData ? filerData.name : null}</span> is a Hedge Fund located out of <span className="filer_description">{filerData ? filerData.address : null}</span>. Their latest 13F filings show that they have at least ${currentAUM} AUM (Assets Under Management).
                            </div>
                        </div>
                        {/* <div className="filer_cik col-2">CIK: {filerData ? filerData.cik : null}</div> */}
                        <div className="offset-lg-1 col-lg-5 offset-xl-2 col-xl-4 offset-md-0 col-md-6 offset-0 col-12 mt-md-0 mt-5">
                            <SummaryTable cik={filerData ? filerData.cik : null} />
                        </div>
                    </div>
                </div>
            </div>

            <div className="market_value_graph_container">
                <div className="market_value_graph">
                    <div className="row mt-5 mb-5">
                        <div className="col-lg-5 col-md-7 shadow-sm mt-4 mb-4 p-3 filer_page_section_heading">
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
                        <div className="col-lg-5 col-md-7 shadow-sm mt-4 mb-4 p-3 filer_page_section_heading">
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
                        <div className="col-lg-6 col-12">
                            <div className="col-sm-10 shadow-sm mt-4 mb-5 p-3 filer_page_section_heading top_buysell_head">
                                <div className="total_market_value_heading">
                                    Top Buys of the Quarter
                                </div>
                                <div className="row filerName_in_marketValue_graph_head">{filerData ? filerData.name : null}</div>
                            </div>
                            <TopBuysTable cik={filerData ? filerData.cik : null} />
                        </div>
                        <div className="col-lg-6 col-12">
                            <div className="col-sm-10 shadow-sm mt-lg-4 mt-5 mb-5 p-3 filer_page_section_heading top_buysell_head">
                                <div className="total_market_value_heading">
                                    Top Sells of the Quarter
                                </div>
                                <div className="row filerName_in_marketValue_graph_head">{filerData ? filerData.name : null}</div>
                            </div>
                            <TopSellsTable cik={filerData ? filerData.cik : null} />
                        </div>
                    </div>
                </div>
            </div>

            <div className="ownership_history_container">
                <div className="ownership_history">
                    <div className="row mt-5 mb-5">
                        <div className="col-lg-7 col-md-8 shadow-sm mt-4 mb-2 p-3 filer_page_section_heading">
                            <div className="total_market_value_heading">
                                Ownership History
                            </div>
                            <div className="row filerName_in_marketValue_graph_head">Securities that {filerData ? filerData.name : null} has owned over the quarters</div>
                        </div>
                    </div>
                    <OwnedSecurities cik={filerData ? filerData.cik : null} />
                </div>
            </div>


            <Footer />

        </Fragment >
    );
}

export default Filer;