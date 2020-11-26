import React, { Component, Fragment } from 'react';
import '../../../styles/navbar.css';
import logo from '../../../static/homepage/logo.png';
// file deepcode ignore no-mixed-spaces-and-tabs:

function Navbar() {
  return (
    <Fragment>
		<nav className="navbar fixed-top" style={{backgroundColor: "transparent"}}>
			<img src={logo} alt="Logo" className="offset-md-1 logo"/>
			<a className="MrktDB mr-auto">MrktDB</a>
			<form className="form-inline ml-auto mr-4">
				<input className="form-control lookup" placeholder="Fund / Stock Lookup"/>
				<button className="btn btn-outline-none search_btn" type="submit"><i className="fas fa-search fa-rotate-90 mr-2"></i>Search</button>
			</form>
			<div className="navbar-nav mr-4">
      			<a className="nav-item filers" href="#">13F Filers</a>
      		</div>
      		<div className="navbar-nav mr-5">
      			<a className="nav-item filers" href="#"><i class="fas fa-2x fa-circle"></i></a>
      		</div>
      		<div className="navbar-nav mr-5 menu">
      			<a className="nav-item filers" href="#"><i class="fas fa-2x fa-bars"></i></a>
      		</div>
		</nav>
	</Fragment>
  );
}

export default Navbar;