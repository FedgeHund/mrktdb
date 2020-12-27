import React, { Fragment } from 'react';

function Popular_Portfolios() {
// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
  	return (
    	<Fragment>

    		<div className="bg_color_large_screen">
				<div className="popular_portfolio_container">
           			<div className="popular_portfolio_carousel_static">
           				<div className="row no_pad">
           					<div className="popular_portfolio_on_mrktdb offset-md-2 col-md-10">Popular Portfolio <br/>on MrktDB</div>
           				</div>
           				<div className="row mt-5">
           					<div className="know_about_top_hedge_funds offset-md-2 col-md-10">Know about <br/>Top Hedge Funds</div>
           				</div>
           				<div className="row mt-5">
           					<div className="portfolio_name offset-2 col-12 mt-5">Bridgewater Associates</div>
           					<div className="portfolio_name offset-2 col-12 mt-2">Renaissance Technologies</div>
           					<div className="portfolio_name offset-2 col-12 mt-2">MAN Group</div>
           					<div className="portfolio_name offset-2 col-12 mt-2">AQR Capital Management</div>
           					<div className="portfolio_name offset-4 col-12 mt-4"><a href="#" className="more_portfolios_link">More <i className="fas fa-arrow-right fa-sm"></i></a></div>
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
						      		<div className="col-sm-4">
						      			<div className="portfolio_heading">1. <br/> <div>Bridgewater Associates</div> </div>
						      		</div>
						      		<div className="col-sm-4">
						      			<div className="portfolio_heading">2. <br/> <div>Renaissance Technologies</div> </div>
						      		</div>
						      		<div className="col-sm-4">
						      			<div className="portfolio_heading">3. <br/> <div>Man Group</div> </div>
						      		</div>
						      </div>
						      <div className="row carousel_row">
						      		<div className="col-4">
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ 5,961,121,000</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ 4,661,451,000</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ 3,261,121,000</span></div>
						      		</div>
						      </div>
						      <div className="row carousel_row">
						      		<div className="col-4">
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">7.8%</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">2.8%</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">1.4%</span></div>
						      		</div>
						      </div>
						      <div className="row carousel_row">
						      		<div className="col-4">
						      			<div className="top_holdings_text">Top Holdings</div>
						      		</div>
						      		<div className="col-4">
						      			<div className="top_holdings_text">Top Holdings</div>
						      		</div>
						      		<div className="col-4">
						      			<div className="top_holdings_text">Top Holdings</div>
						      		</div>
						      </div>
						      <div className="row carousel_row">
						      		<div className="col-4">
						      			<div className="top_holding_symbol_1">1. SPY <span className="top_holding_name">SPDR S&P 500 EFT Trust</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="top_holding_symbol_1">1. CMG <span className="top_holding_name">Chipotle Mexican Grill Inc.</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="top_holding_symbol_1">1. MCST <span className="top_holding_name">Microsoft Corporation</span></div>
						      		</div>
						      </div>
						      <div className="row carousel_row">
						      		<div className="col-4">
						      			<div className="top_holding_symbol">2. GLD <span className="top_holding_name">SPDR Gold Trust</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="top_holding_symbol">2. VRTX <span className="top_holding_name">Vertex Pharmaceutical Inc.</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="top_holding_symbol">2. ALIB <span className="top_holding_name">Alibaba Group</span></div>
						      		</div>
						      </div>
						      <div className="row carousel_row">
						      		<div className="col-4">
						      			<div className="top_holding_symbol">3. IVV <span className="top_holding_name">iShare Core S&P 500 EFT</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="top_holding_symbol">3. VRSN <span className="top_holding_name">Verisign Inc.</span></div>
						      		</div>
						      		<div className="col-4">
						      			<div className="top_holding_symbol">3. AMZN <span className="top_holding_name">Amazon</span></div>
						      		</div>
						      </div>
						    </div>


						    <div className="carousel-item">
						    	<div className="row carousel_row">
						      		<div className="col-sm-4">
						      			<div className="portfolio_heading">4. <br/> <div>AQR Capital Management</div> </div>
						      		</div>
						      		<div className="col-sm-4">
						      			<div className="portfolio_heading">5. <br/> <div>XXXXX XXXXXXXX</div> </div>
						      		</div>
						      		<div className="col-sm-4">
						      			<div className="portfolio_heading">6. <br/> <div>XXXX XXXX XXXXXXX</div> </div>
						      		</div>
								</div>
								<div className="row carousel_row">
										<div className="col-4">
											<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ 2,435,121,000</span></div>
										</div>
										<div className="col-4">
											<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ X,XXX,XXX,XXX</span></div>
										</div>
										<div className="col-4">
											<div className="portfolio_value_head">Portfolio Value: <span className="portfolio_value_number">$ X,XXX,XXX,XXX</span></div>
										</div>
								</div>
								<div className="row carousel_row">
										<div className="col-4">
											<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">1.4%</span></div>
										</div>
										<div className="col-4">
											<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">X.X%</span></div>
										</div>
										<div className="col-4">
											<div className="portfolio_value">Estimated one year return: <span className="portfolio_value_number">X.X%</span></div>
										</div>
								</div>
								<div className="row carousel_row">
										<div className="col-4">
											<div className="top_holdings_text">Top Holdings</div>
										</div>
										<div className="col-4">
											<div className="top_holdings_text">Top Holdings</div>
										</div>
										<div className="col-4">
											<div className="top_holdings_text">Top Holdings</div>
										</div>
								</div>
								<div className="row carousel_row">
										<div className="col-4">
											<div className="top_holding_symbol_1">1. VRSN <span className="top_holding_name">Verisign Inc.</span></div>
										</div>
										<div className="col-4">
											<div className="top_holding_symbol_1">1. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
										</div>
										<div className="col-4">
											<div className="top_holding_symbol_1">1. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
										</div>
								</div>
								<div className="row carousel_row">
										<div className="col-4">
											<div className="top_holding_symbol">2. GLD <span className="top_holding_name">SPDR Gold Trust</span></div>
										</div>
										<div className="col-4">
											<div className="top_holding_symbol">2. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
										</div>
										<div className="col-4">
											<div className="top_holding_symbol">2. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
										</div>
								</div>
								<div className="row carousel_row">
										<div className="col-4">
											<div className="top_holding_symbol">3. ALIB <span className="top_holding_name">Alibaba Group</span></div>
										</div>
										<div className="col-4">
											<div className="top_holding_symbol">3. XXX <span className="top_holding_name">XXXXXXXXXX</span></div>
										</div>
										<div className="col-4">
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
           		
           	</div>

		</Fragment>
	);
}

export default Popular_Portfolios;