import React, { Fragment } from 'react';

function Know_More() {
// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
  	return (
    	<Fragment>

			<div className="know_more_container">
          		<div className="container">
          			<div className="row know_more">
          				<div className="col-12">Know more <br/>about us</div>
          			</div>

          			<div className="row">
					  	<div className="col-2">
					    	<div className="nav flex-column tabs_know" id="v-pills-tab" role="tablist" aria-orientation="vertical">
					      		<a className="nav-link tabs_know_heading active" id="v-pills-home-tab" data-toggle="pill" href="#v-pills-home" role="tab" aria-controls="v-pills-home" aria-selected="true">Institutional Holdings Lookup</a>
					      		<a className="nav-link tabs_know_heading" id="v-pills-profile-tab" data-toggle="pill" href="#v-pills-profile" role="tab" aria-controls="v-pills-profile" aria-selected="false">Holdings trends for Individual Stocks</a>
					      		<a className="nav-link tabs_know_heading" id="v-pills-messages-tab" data-toggle="pill" href="#v-pills-messages" role="tab" aria-controls="v-pills-messages" aria-selected="false">Best Performing Investor</a>
					    	</div>
					  	</div>

					  	<div className="col-8">
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

		</Fragment>
	);
}

export default Know_More;