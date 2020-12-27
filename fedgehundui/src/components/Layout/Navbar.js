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

			<a href="/" className="offset-1"><img src={logo} alt="Logo" className="logo"/></a>
			<a href="/" className="MrktDB mr-auto">MrktDB</a>

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
				<a className="nav-item circle" href="#"><i className="fas fa-2x fa-circle"></i></a>
			</div>


			<div className="navbar-nav">

				<div id="menuToggle">
					<input type="checkbox" className="toggler"/>
					<div className="hamburger">
						<div></div>
					</div>


					<div id="menu">
						<div className="hamburger_container">
							<div className="menu_box">
								<div className="row margin_small15">
									<div className="col-md-1 col-sm-2 col-4 margin_small10">
										<img src="../../../static/homepage/logo2.png" alt="White logo" className="hamburger_white_logo"/>
									</div>
									<div className="col-md-1 mrktdb_white col-2 margin_small10">
										MrktDB
									</div>
									<div className="offset-md-5 col-md-2 offset-sm-2 col-sm-2 col-4 margin_small10">
										<a href="/signup" className="signup_menu">Sign Up</a>
									</div>
									<div className="col-md-2 col-sm-2 col-4 margin_small10">
										<a href="/signin" className="signup_menu">Sign In</a>
									</div>
								</div>

								<div className="row margin10">
									<div className="offset-md-2 col-md-1 menu_13f margin3">13F</div>
								</div>

								<div className="row">
									<a href="#" className="filer_items offset-md-2 col-md-2 col-12"><div className="margin6 margin_small6">Latest Filings</div></a>
									<a href="#" className="filer_items col-md-4 col-12"><div className="margin6 margin_small3">13F Searching</div></a>
								</div>

								<div className="row">
									<a href="#" className="filer_items offset-md-2 col-md-2 col-12"><div className="margin3 margin_small3">Popular Stocks</div></a>
									<a href="#" className="filer_items col-md-4 col-12"><div className="margin3 margin_small3">13F Fund Performance Search</div></a>
								</div>

								<div className="row">
									<a href="#" className="filer_items offset-md-2 col-md-2 col-12"><div className="margin3 margin_small3">13F Trends</div></a>
									<a href="#" className="filer_items col-md-4 col-12"><div className="margin3 margin_small3">13F Stock Screener</div></a>
								</div>

								<div className="row">
									<a href="#" className="filer_items offset-md-2 col-md-3 col-12"><div className="margin3 margin_small3">13F Statistics</div></a>              
								</div>

								<div className="row">
									<div className="horizontal_line margin10 offset-md-2 col-md-8 col-12 mb-2"></div>
								</div>



								<div className="quick_links">
									<div className="row">
										<div className="footer_heading offset-2 col-2">Help</div>
										<div className="footer_heading col-2">Collaborate</div>
										<div className="footer_heading col-2">Connect</div>
										<div className="footer_heading col-2">Explore</div>
									</div>

									<div className="row">
										<a href="#" className="filer_items offset-2 col-2"><div className="margin6">Our offerings</div></a>
										<a href="#" className="filer_items col-2"><div className="margin6">Advertise with us</div></a>
										<a href="#" className="filer_items col-2"><div className="margin6">Contact Us</div></a>
										<a href="#" className="filer_items col-2"><div className="margin6">Email Newsletter</div></a>
									</div>

									<div className="row">
										<a href="#" className="filer_items offset-2 col-2"><div className="margin3">How MrktDB works?</div></a>
										<a href="#" className="filer_items col-2"><div className="margin3">Business Resources</div></a>
										<a href="#" className="filer_items col-2"><div className="margin3">Report a Bug</div></a>
										<a href="#" className="filer_items col-2"><div className="margin3">Upcoming events</div></a>
									</div>

									<div className="row">
										<a href="#" className="filer_items offset-2 col-2"><div className="margin3">Getting started</div></a>
										<a href="#" className="filer_items col-2"><div className="margin3"></div></a>
										<a href="#" className="filer_items col-2"><div className="margin3">Sign in</div></a>
										<a href="#" className="filer_items col-2"><div className="margin3"></div></a>
									</div>

									<div className="row">
										<a href="#" className="filer_items offset-2 col-2"><div className="margin3">FAQ</div></a>
										<a href="#" className="filer_items col-2"><div className="margin3"></div></a>
										<a href="#" className="filer_items col-2"><div className="margin3"></div></a>
										<a href="#" className="filer_items col-2"><div className="margin3"></div></a>
									</div>
								</div>

								<div className="quick_links_small_screen">
									<div className="row">
										<div className="col-12 footer_section">Quick links</div>
									</div>
									<div className="row">
										<div className="horizontal_lines_small_screen col-12 mt-2"></div>
									</div>

									<div className="row margin_small10">
										<div className="footer_heading col-6">Help</div>
										<div className="footer_heading col-6">Connect</div>
									</div>

									<div className="row margin_small6">
										<a href="#" className="filer_items col-6"><div>Our offerings</div></a>
										<a href="#" className="filer_items col-6"><div>Contact Us</div></a>
									</div>

									<div className="row margin_small3">
										<a href="#" className="filer_items col-6"><div>How MrktDB works?</div></a>
										<a href="#" className="filer_items col-6"><div>Report a Bug</div></a>
									</div>

									<div className="row margin_small3">
										<a href="#" className="filer_items col-6"><div>Getting started</div></a>
										<a href="#" className="filer_items col-6"><div>Sign in</div></a>
									</div>

									<div className="row margin_small3">
										<a href="#" className="filer_items col-6"><div>FAQ</div></a>
									</div>


									<div className="row margin_small10">
										<div className="footer_heading col-6">Collaborate</div>
										<div className="footer_heading col-6">Explore</div>
									</div>

									<div className="row margin_small6">
										<a href="#" className="filer_items col-6"><div>Advertise with us</div></a>
										<a href="#" className="filer_items col-6"><div>Email Newsletter</div></a>
									</div>

									<div className="row margin_small3">
										<a href="#" className="filer_items col-6"><div>Business Resources</div></a>
										<a href="#" className="filer_items col-6"><div>Upcoming events</div></a>
									</div>



									<div className="row margin_small10">
										<div className="footer_heading col-6">Social Media</div>
									</div>               

									<div className="row margin_small6">
										<a href="#" className="filer_items col-6"><div>Twitter</div></a>
									</div>

									<div className="row margin_small3">
										<a href="#" className="filer_items col-6"><div>Instagram</div></a>
									</div>

									<div className="row margin_small3">
										<a href="#" className="filer_items col-6"><div>Facebook</div></a>
									</div>

									<div className="row margin_small3">
										<a href="#" className="filer_items col-6"><div>LinkedIn</div></a>
									</div>

									<div className="row margin_small10">
										<div className="horizontal_lines_small_screen col-12"></div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
      
		</nav> 

	
			
				
	</Fragment>
  );
}

export default Navbar;
