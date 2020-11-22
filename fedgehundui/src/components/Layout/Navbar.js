import React, { Component, Fragment } from 'react';
import '../../../styles/navbar.css';
import logo from '../../../static/logo.png';
// file deepcode ignore no-mixed-spaces-and-tabs:

function Navbar() {
  return (
    <Fragment>
		<nav className="navbar sticky-top">
			<img src={logo} alt="Logo" className="offset-md-2 logo"/>
			<a className="MrktDB">MrktDB</a>
			<form className="form-inline mr-auto offset-md-5">
				<input className="form-control lookup" type="search" placeholder="Fund / Stock Lookup" style={{textDecoration: "None", outline: "None"}}/>
				<button className="btn btn-outline-none my-2 my-sm-0" type="submit">Search</button>
			</form>
		</nav>
	</Fragment>
  );
}

export default Navbar;