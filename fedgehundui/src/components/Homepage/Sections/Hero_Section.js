import React, { Fragment } from 'react';

function Hero_Section() {
// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
  	return (
    	<Fragment>

    		<div className="Background">
				<div className="contain">
					<div className="row">
						<div className="market_beating centered col-md-12">Find the next Market-Beating Portfolio</div>
					</div>
					<div className="">
						<form className="form-inline centered_form">
							<div className="lookup_form">
								<input className="form-control lookup_home" placeholder="Fund / Stock Lookup"/>
								<button className="search" type="submit"><i className="fas fa-search fa-rotate-90 search_icon"></i>Search</button>
							</div>
						</form>
					</div>
					<div className="row">
						<div className="col-xs-10 carousel_text col-md-7">MrktDB provides exclusive investment insights by giving you a sneak peek into the portfolio of world's most successful investors. Market Research is expensive, don't let that hold you back!</div>
					</div>
					<div className="row">
						<a href="" className="centered_carousel_link col-xs-12">Find out what the smartest investors are buying</a>
					</div>
				</div>
			</div>

		</Fragment>
	);
}

export default Hero_Section;