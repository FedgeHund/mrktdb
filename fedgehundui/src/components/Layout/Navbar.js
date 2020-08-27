import React, { Component, Fragment } from 'react';
import '../../../styles/signin/styles.css';

function Navbar() {
  return (
    <Fragment>
    		<nav class="navbar sticky-top navcolor">
			  <a class="navbar-brand" href="#" style={{color: "white"}}>MrktDB</a>
			  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
			    <span class="navbar-toggler-icon"></span>
			  </button>

			  <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
			    <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
			    </ul>
			  </div>
			</nav>
	</Fragment>
  );
}

export default Navbar;