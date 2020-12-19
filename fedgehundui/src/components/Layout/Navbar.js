import React, { Component, Fragment } from 'react';
import { useState, useEffect } from 'react';
import '../../../styles/navbar.css';
import logo from '../../../static/homepage/logo.png';
// file deepcode ignore no-mixed-spaces-and-tabs:

function Navbar() {
  const [navbar, setNavbar] = useState(false);

  const changeNavbarBackground = () => {
    if(window.scrollY >= 80) {
      setNavbar(true);
    } else {
      setNavbar(false);
    }
  }

  window.addEventListener('scroll', changeNavbarBackground);

  return (
    <Fragment>
		<nav className={navbar ? 'navbar active fixed-top' : 'navbar fixed-top'}>
			<img src={logo} alt="Logo" className="offset-1 logo"/>
			<a className="MrktDB mr-auto">MrktDB</a>
			<form className="form-inline">
        <div className="lookup_form_everywhere">
				  <input className="form-control lookup" placeholder="Fund / Stock Lookup"/>
				  <button className="btn btn-outline-none search_btn" type="submit"><i className="fas fa-search fa-rotate-90 search_icon"></i>Search</button>
        </div>
			</form>
			<div className="navbar-nav">
      			<a className="nav-item filers" href="#">13F Filers</a>
      		</div>
      		<div className="navbar-nav">
      			<a className="nav-item circle" href="#"><i class="fas fa-2x fa-circle"></i></a>
      		</div>
      		<div className="navbar-nav">
      			<a className="nav-item menu" href="#"><i class="fas fa-2x fa-bars"></i></a>
      		</div>
		</nav>
	</Fragment>
  );
}

export default Navbar;