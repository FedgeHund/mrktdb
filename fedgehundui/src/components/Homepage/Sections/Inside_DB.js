import React, { Fragment } from 'react';

function Inside_DB() {
// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
  	return (
    	<Fragment>

			<div className="inside_db_container">  

				<div className="box"></div>
				<div className="box_text">INSIDE OUR DATABASE</div> 

				<img src="../../../static/homepage/lower_left.png" alt="left design" className="lower_left_design"/>
           		<img src="../../../static/homepage/right.png" alt="right design" className="right_design"/>  

           		<div className="inside_db">
		       		<div className="row">
		       			<div className="so_far_text col-8 offset-2">SO FAR IN THE THIRD<br/> QUARTER OF 2020</div>
		       		</div>

		       		<div className="stats">
			       		<div className="row stat_container">
			       			<div className="filer_stats offset-2 col-2">3047</div>
			           		<div className="securities_stats offset-1 col-2">13K</div>
			           		<div className="hedgefund_stats offset-1 col-2">545</div>
			       		</div>
			  
			       		<div className="row stat_type_container">
			       			<div className="filer_stat_type offset-2 col-2">Filers</div>
			       			<div className="security_stat_type offset-1 col-2">Securities</div>
			       			<div className="fund_stat_type offset-1 col-3">Hedge Funds</div>
			       		</div>
		       		</div>
		       		
	       		</div>

           </div>

		</Fragment>
	);
}

export default Inside_DB;