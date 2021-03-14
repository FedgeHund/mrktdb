import React, { Fragment } from 'react';

function Know_More() {
	// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
	return (
		<Fragment>

			<div className="know_more_container">
				<div className="container">
					<div className="row know_more">
						<div className="col-12">MrktDB 1.0 <br />Insights</div>
					</div>

					<div className="row">
						<div className="col-2">
							<div className="nav flex-column tabs_know" id="v-pills-tab" role="tablist" aria-orientation="vertical">
								<a className="nav-link tabs_know_heading active" id="v-pills-home-tab" data-toggle="pill" href="#v-pills-home" role="tab" aria-controls="v-pills-home" aria-selected="true">Institutional Holdings Lookup</a>
								<a className="nav-link tabs_know_heading" id="v-pills-profile-tab" data-toggle="pill" href="#v-pills-profile" role="tab" aria-controls="v-pills-profile" aria-selected="false">Trends for Individual Stocks</a>
								<a className="nav-link tabs_know_heading" id="v-pills-messages-tab" data-toggle="pill" href="#v-pills-messages" role="tab" aria-controls="v-pills-messages" aria-selected="false">Aggregated 13F Insights</a>
							</div>
						</div>

						<div className="col-8">
							<div className="tab-content tab_content" id="v-pills-tabContent">
								<div className="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab">
									Find out what biggest investors out there are holding in their portfolios.
									Lookup individual holdings and visualize trends for all filers of Form 13F. All
									institutional investment managers with at least $100 million in assets under
									management are required to file this form with SEC every quarter and disclose
									their long equity and options holdings.
								</div>
								<div className="tab-pane fade" id="v-pills-profile" role="tabpanel" aria-labelledby="v-pills-profile-tab">
									Look up individual stocks on dedicated dashboards that provide exclusive
									insights by combining market data and analysis from 13F filings. Find out if the
									interest in a particular stock is increasing or decreasing QoQ among
									institutional filers and/or hedge funds. Monitor metrics like number of filers
									holding the stock, total shares held across all filings, put/call ratio, net buys,
									etc… all of it in time series.
								</div>
								<div className="tab-pane fade" id="v-pills-messages" role="tabpanel" aria-labelledby="v-pills-messages-tab">
									We aggregate all of 13F data each quarter and bring out exclusive insights that
									can help you make informed decisions about your investments. Here you’ll
									find metrics like:
									1. Most popular stocks across all 13F filers and hedge funds
									2. Emerging favorite stocks across all filers
									3. Stocks falling out of favor among filers
									4. Best performing filers
									… and much more!
								</div>
							</div>
						</div>
					</div>

					<img src="../../../static/homepage/know_more_img.png" alt="know more image" className="know_more_image shadow" />
				</div>
			</div>

		</Fragment>
	);
}

export default Know_More;