import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.css';

function Navbar() {
  return (
    <Fragment>
    		<nav className="navbar sticky-top">
			  <a className="navbar-brand" href="#" style={{color: "white"}}>MrktDB</a>
			  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
			    <span className="navbar-toggler-icon"></span>
			  </button>

			  <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
			    <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
			    </ul>
			  </div>
			</nav>
	</Fragment>
  );
}

export default Navbar;