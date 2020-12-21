import React, { Fragment } from 'react';

function Inside_DB() {
// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
  	return (
    	<Fragment>

			<div className="inside_db_container">
           		<div className="box"></div>
           		<div className="box_text">INSIDE OUR DATABASE</div>
	       		<div className="row">
	       			<div className="so_far_text col-xl-4 col-md-6 col-xs-6">SO FAR IN THE THIRD QUARTER OF 2020</div>
	       		</div>

	       		<div className="row stat_contain">
	       			<div className="filer_stats col-4">3047</div>
	           		<div className="securities_stats col-4">13K</div>
	           		<div className="hedgefund_stats col-4">545</div>
	       		</div>

	       		<div className="row">
	       			<div className="filer_stat_type">Filers</div>
	       			<div className="security_stat_type">Securities</div>
	       			<div className="fund_stat_type">Hedge Funds</div>
	       		</div>

				<img src="../../../static/homepage/lower_left.png" alt="left design" className="lower_left_design"/>
           		<img src="../../../static/homepage/right.png" alt="right design" className="right_design"/>
           </div>

		</Fragment>
	);
}

export default Inside_DB;