import React, { Fragment } from 'react';

function Get_Started() {
// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
  	return (
    	<Fragment>

			<div className="get_started_container">
	           	<div className="get_started_box shadow">
	           		<div className="row">
	           			<div className="exclusive_insights_text col-10 col-sm-8 col-md-10 col-lg-7 col-xl-7">Exclusive insights into the portfolios of the smartest investors on the platform of your choice!</div>
	           		</div>
	           		<div className="row">
	           			<div className="sign_up_personalized col-md-7 col-xs-10 col-10">Sign Up for personalised, experienced and exclusive content</div>
	           		</div>
	           		<a href="/signup">
		           		<button className="btn get_started_btn shadow-sm" type="submit">
	                        <span className="get_started_text">Get Started</span>
	                    </button>
                    </a>
	           	</div>
	           	<img src="../../../static/homepage/platform.png" alt="Platforms" className="platforms_img"/>
           	</div>

		</Fragment>
	);
}

export default Get_Started;