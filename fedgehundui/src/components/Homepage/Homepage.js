import React, { Fragment } from 'react';
import {useState, useEffect} from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'; 
import '../../../styles/homepage.css';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';

function Homepage() {

  return (
    <Fragment>
    		<Navbar />

			<div className="contain">
				<img src="../../../static/homepage/homepage_background.png" alt="background" className="Background"/>
				<div className="row">
					<div className="market_beating centered col-md-8">Find the next Market-Beating Portfolio</div>
				</div>
				<div className="row">
					<form className="form-inline centered_form">
						<input className="form-control lookup_home" placeholder="Fund / Stock Lookup"/>
						<button className="search" type="submit"><i className="fas fa-search fa-rotate-90 search_icon"></i>Search</button>
					</form>
				</div>
				<div className="row">
					<div className="carousel_text centered_carousel col-6">MrktDB provides exclusive investment insights by giving you a sneak peek into the portfolio of world's most successful investors. Market Research is expensive, don't let that hold you back!</div>
					<a href="" className="centered_carousel_link">Find out what the smartest investors are buying</a>
				</div>		
			</div>

			<div className="inside_db_container">
           		<div className="box"></div>
           		<div className="box_text">INSIDE OUR DATABASE</div>
	       		<div className="row">
	       			<div className="so_far_text col-5">SO FAR IN THE THIRD QUARTER OF 2020</div>
	       		</div>
				
	       		<div className="row">
	       			<div className="filer_stats col-1">3047</div>
	           		<div className="securities_stats">13K</div>
	           		<div className="hedgefund_stats">545</div>
	           		
	       		</div>

	       		<div className="row">
	       			<div className="filer_stat_type col-2">Filers</div>
	       			<div className="security_stat_type">Securities</div>
	       			<div className="fund_stat_type">Hedge Funds</div>
	       		</div>
           		
           		<img src="../../../static/homepage/lower_left.png" alt="left design" className="lower_left_design"/>
           		<img src="../../../static/homepage/right.png" alt="right design" className="right_design"/>
           </div>

           <div className="know_more_container">
          		<div className="container">
          			<div className="row">
          				<div className="know_more col-3">Know more about us</div>
          			</div>

          			<div className="row">
					  	<div className="col-2">
					    	<div className="nav flex-column tabs_know" id="v-pills-tab" role="tablist" aria-orientation="vertical">
					      		<a className="nav-link tabs_know_heading active" id="v-pills-home-tab" data-toggle="pill" href="#v-pills-home" role="tab" aria-controls="v-pills-home" aria-selected="true">Institutional Holdings Lookup</a>
					      		<a className="nav-link tabs_know_heading" id="v-pills-profile-tab" data-toggle="pill" href="#v-pills-profile" role="tab" aria-controls="v-pills-profile" aria-selected="false">Holdings trends for Individual Stocks</a>
					      		<a className="nav-link tabs_know_heading" id="v-pills-messages-tab" data-toggle="pill" href="#v-pills-messages" role="tab" aria-controls="v-pills-messages" aria-selected="false">Best Performing Investor</a>
					    	</div>
					  	</div>

					  	<div className="col-5">
					    	<div className="tab-content tab_content" id="v-pills-tabContent">
					      		<div className="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab">lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad minim veniam, quis nostrud  exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</div>
					      		<div className="tab-pane fade" id="v-pills-profile" role="tabpanel" aria-labelledby="v-pills-profile-tab">This section describes the trends for individual stocks</div>
					      		<div className="tab-pane fade" id="v-pills-messages" role="tabpanel" aria-labelledby="v-pills-messages-tab">This section is dedicated to showing information about the best performing investor in the recent time.</div>
					    	</div>
					  	</div>
					</div>

					<img src="../../../static/homepage/know_more_img.png" alt="know more image" className="know_more_image shadow"/>
          		</div>
           	</div>

           	<div className="what_is_13F_container">
           		<div className="box_13f"></div>
           		<div className="row">
	       			<div className="what_is_13f_text col-6">What is 13F?</div>
	       			<div className="col-1 key_takeaways_head">KEY TAKEAWAYS</div>
	       		</div>
	       		<div className="row">
	       			<div className="col-3 what_is_13f_content">
						The Securities and Exchange Commission's (SEC) form 13F is a quarterly report that is required to be filed by all institutional investment managers with at least $100 million in assets under management. It discloses their equity holdings and can provide some insights into what the smart money is doing in the market. However, studies have found that 13F filings also have serious flaws and can't be taken at face value.
					</div>
					<a href="#" className="col-3 know_more_13f">Know more<i className="fas fa-angle-double-right ml-1"></i></a>
	       		</div>
	       		<div className="row">
	       			<div className="key_takeaways_content col-3">
	       				The SEC’s form 13F must be filed quarterly by institutional investment managers with at least $100 million in assets under management.
	       				<br/>
	       				<br/>
						Congress intended these filings to provide transparency on the holdings of the nation’s biggest investors.
						<br/>
	       				<br/>
						Small investors frequently use these filings to determine what the “smart money” is doing in the market, but there are serious problems with the reliability and timeliness of the data.
	       			</div>
	       		</div>
           		<img src="../../../static/homepage/right.png" alt="left design" className="lower_left_design_13f"/>
           		<img src="../../../static/homepage/right.png" alt="right design" className="right_design_13f"/>
           	</div>

           	<div className="popular_portfolio_container">
           			<div className="popular_portfolio_carousel_static">
           				<div className="popular_portfolio_on_mrktdb">Popular Portfolio <br/>on MrktDB</div>
           				<div className="know_about_top_hedge_funds">Know about <br/>Top Hedge Funds</div>
           				<div className="portfolio_names">
           					<div className="portfolio_name">Bridgewater Associates</div>
           					<div className="portfolio_name">Renaissance Technologies</div>
           					<div className="portfolio_name">MAN Group</div>
           					<div className="portfolio_name">AQR Capital Management</div>
           					<div className="portfolio_name"><a href="#" className="more_portfolios_link">More <i className="fas fa-arrow-right fa-sm"></i></a></div>
           				</div>
           			</div>

           			<div className="popular_portfolios">
	           			<div className="row">
	           				<div className="as_of_date">As of 18/11/20, 10:16 am EDT</div>
	           			</div>
           				<div id="carouselExampleIndicators" className="carousel slide" data-interval="false">
						  <ol className="carousel-indicators">
						    <li data-target="#carouselExampleIndicators" data-slide-to="0" className="active"></li>
						    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
						  </ol>
						  <div className="carousel-inner">
						    <div className="carousel-item active">
						      <div className="row carousel_row">
						      		<div className="col-4">
						      			<div className="portfolio_heading">1. <br/> <div className="port_head">Bridgewater Associates</div> </div>
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ 5,961,121,000</span></div>
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">7.8%</span></div>
						      			<div className="top_holdings_text">Top Holdings</div>
						      			<div className="top_holding_symbol_1">1. SPY <span className="top_holding_name">SPDR S&P 500 EFT Trust</span></div>
						      			<div className="top_holding_symbol">2. GLD <span className="top_holding_name">SPDR Gold Trust</span></div>
						      			<div className="top_holding_symbol">3. IVV <span className="top_holding_name">iShare Core S&P 500 EFT</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="portfolio_heading">2. <br/> <div className="port_head">Renaissance Technologies</div> </div>
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ 4,661,451,000</span></div>
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">2.8%</span></div>
						      			<div className="top_holdings_text">Top Holdings</div>
						      			<div className="top_holding_symbol_1">1. CMG <span className="top_holding_name">Chipotle Mexican Grill Inc.</span></div>
						      			<div className="top_holding_symbol">2. VRTX <span className="top_holding_name">Vertex Pharmaceutical Inc.</span></div>
						      			<div className="top_holding_symbol">3. VRSN <span className="top_holding_name">Verisign Inc.</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="portfolio_heading">3. <br/> <div className="port_head">Man <br/> Group</div> </div>
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ 3,261,121,000</span></div>
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">1.4%</span></div>
						      			<div className="top_holdings_text">Top Holdings</div>
						      			<div className="top_holding_symbol_1">1. MCST <span className="top_holding_name">Microsoft Corporation</span></div>
						      			<div className="top_holding_symbol">2. ALIB <span className="top_holding_name">Alibaba Group</span></div>
						      			<div className="top_holding_symbol">3. AMZN <span className="top_holding_name">Amazon</span></div>
						      		</div>
						      </div>
						    </div>
						    <div className="carousel-item">
						      <div className="row carousel_row">
						      		<div className="col-4">
						      			<div className="portfolio_heading">4. <br/> <div className="port_head">AQR Capital Management</div> </div>
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ 2,435,121,000</span></div>
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">1.4%</span></div>
						      			<div className="top_holdings_text">Top Holdings</div>
						      			<div className="top_holding_symbol_1">1. VRSN <span className="top_holding_name">Verisign Inc.</span></div>
						      			<div className="top_holding_symbol">2. GLD <span className="top_holding_name">SPDR Gold Trust</span></div>
						      			<div className="top_holding_symbol">3. ALIB <span className="top_holding_name">Alibaba Group</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="portfolio_heading">5. <br/> <div className="port_head">XXXXX XXXXXXXX</div> </div>
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ X,XXX,XXX,XXX</span></div>
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">X.X%</span></div>
						      			<div className="top_holdings_text">Top Holdings</div>
						      			<div className="top_holding_symbol_1">1. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
						      			<div className="top_holding_symbol">2. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
						      			<div className="top_holding_symbol">3. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="portfolio_heading">6. <br/> <div className="port_head">XXXX XXXX <br/> XXXXXXX</div> </div>
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ X,XXX,XXX,XXX</span></div>
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">X.X%</span></div>
						      			<div className="top_holdings_text">Top Holdings</div>
						      			<div className="top_holding_symbol_1">1. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
						      			<div className="top_holding_symbol">2. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
						      			<div className="top_holding_symbol">3. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
						      		</div>
						      </div>
						    </div>
						  </div>
						  <a className="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
						    <span className="carousel-control-next-icon" aria-hidden="true"></span>
						    <span className="sr-only">Next</span>
						  </a>
						</div>
           			</div>
           	</div>

           	<div className="get_started_container">
	           	<div className="get_started_box shadow">
	           		<div className="row">
	           			<div className="exclusive_insights_text col-7">Exclusive insights into the portfolios of the smartest investors on the platform of your choice!</div>
	           		</div>
	           		<div className="row">
	           			<div className="sign_up_personalized col-7">Sign Up for personalised, experienced and exclusive content</div>
	           		</div>
                    <button className="btn get_started_btn shadow-sm" type="submit">
                        <span className="get_started_text">Get Started</span>
                    </button>
	           	</div>
	           	<img src="../../../static/homepage/platform.png" alt="Platforms" className="platforms_img"/>
           	</div>
          	
          	<Footer />

	</Fragment>
  );
}

export default Homepage;