import React, { Component, Fragment } from 'react';
import '../../../styles/footer.css';
import logo from '../../../static/homepage/logo.png';
// file deepcode ignore no-mixed-spaces-and-tabs:

function Footer() {
	return (
		<Fragment>
			<div className="footer_container">
				<div className="footer_box">

					<div className="row">
						<div className="horizontal_lines_small_screen col-12 mb-2"></div>
						<div className="col-md-1 col-12 footer_section">Filers</div>
						<div className="horizontal_lines_small_screen col-12 mt-2"></div>
						<div className="offset-md-1 col-md-10 col-12 footer_heading margin_small10">13F Filers</div>
					</div>

					<div className="row margin6">
						<a href="#" className="filer_items offset-md-2 col-md-2 col-12 hover_effect hover_effect_row"><div className="margin_small6">Latest Filings&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
						<a href="#" className="filer_items col-md-4 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Searching&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
					</div>

					<div className="row">
						<a href="#" className="filer_items offset-md-2 col-md-2 col-12 hover_effect hover_effect_row"><div className="margin_small6">Popular Stocks&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
						<a href="#" className="filer_items col-md-4 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Fund Performance Search&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
					</div>

					<div className="row">
						<a href="#" className="filer_items offset-md-2 col-md-2 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Trends&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
						<a href="#" className="filer_items col-md-4 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Stock Screener&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
					</div>

					<div className="row">
						<a href="#" className="filer_items offset-md-2 col-md-3 col-12 hover_effect hover_effect_row"><div className="margin_small6">13F Statistics&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
					</div>


					<div className="row">
						<div className="horizontal_line margin10 offset-md-2 col-md-10 col-12 mb-2"></div>
					</div>


					<div className="quick_links">
						<div className="row">
							<div className="footer_heading offset-2 col-2">Help</div>
							<div className="footer_heading col-2">Collaborate</div>
							<div className="footer_heading col-2">Connect</div>
							<div className="footer_heading col-2">Explore</div>
						</div>

						<div className="row hover_effect_row margin6">
							<a href="#" className="filer_items offset-2 col-2 hover_effect"><div>Our offerings&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div>Advertise with us&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="/contactus" className="filer_items col-2 hover_effect"><div>Contact Us&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div>Email Newsletter&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
						</div>

						<div className="row hover_effect_row">
							<a href="#" className="filer_items offset-2 col-2 hover_effect"><div>How MrktDB works?&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div>Business Resources&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div>Report a Bug&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div>Upcoming events&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
						</div>

						<div className="row hover_effect_row">
							<a href="#" className="filer_items offset-2 col-2 hover_effect"><div>Getting started&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div>Sign in&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
						</div>

						<div className="row hover_effect_row">
							<a href="/faq" className="filer_items offset-2 col-2 hover_effect"><div>FAQ&nbsp; <i className="fas fa-arrow-right link_arrow"></i></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
							<a href="#" className="filer_items col-2 hover_effect"><div></div></a>
						</div>
					</div>

					<div className="quick_links_small_screen">
						<div className="row">
							<div className="col-12 footer_section">Quick links</div>
						</div>
						<div className="row">
							<div className="horizontal_lines_small_screen col-12 mt-2 horizontal_lines_small_screen_to_right"></div>
						</div>

						<div className="row margin_small10">
							<div className="footer_heading col-6">Help</div>
							<div className="footer_heading col-6">Connect</div>
						</div>

						<div className="row margin_small6">
							<a href="#" className="filer_items col-6 hover_effect"><div>Our offerings</div></a>
							<a href="#" className="filer_items col-6 hover_effect"><div>Contact Us</div></a>
						</div>

						<div className="row margin_small3">
							<a href="#" className="filer_items col-6 hover_effect"><div>How MrktDB works?</div></a>
							<a href="#" className="filer_items col-6 hover_effect"><div>Report a Bug</div></a>
						</div>

						<div className="row margin_small3">
							<a href="#" className="filer_items col-6 hover_effect"><div>Getting started</div></a>
							<a href="#" className="filer_items col-6 hover_effect"><div>Sign in</div></a>
						</div>

						<div className="row margin_small3">
							<a href="/faq" className="filer_items col-6 hover_effect"><div>FAQ</div></a>
						</div>


						<div className="row margin_small10">
							<div className="footer_heading col-6">Collaborate</div>
							<div className="footer_heading col-6">Explore</div>
						</div>

						<div className="row margin_small6">
							<a href="#" className="filer_items col-6 hover_effect"><div>Advertise with us</div></a>
							<a href="#" className="filer_items col-6 hover_effect"><div>Email Newsletter</div></a>
						</div>

						<div className="row margin_small3">
							<a href="#" className="filer_items col-6 hover_effect"><div>Business Resources</div></a>
							<a href="#" className="filer_items col-6 hover_effect"><div>Upcoming events</div></a>
						</div>



						<div className="row margin_small10">
							<div className="footer_heading col-6">Social Media</div>
						</div>

						<div className="row margin_small6">
							<a href="#" className="filer_items col-6 hover_effect"><div>Twitter</div></a>
						</div>

						<div className="row margin_small3">
							<a href="#" className="filer_items col-6 hover_effect"><div>Instagram</div></a>
						</div>

						<div className="row margin_small3">
							<a href="#" className="filer_items col-6 hover_effect"><div>Facebook</div></a>
						</div>

						<div className="row margin_small3">
							<a href="#" className="filer_items col-6 hover_effect"><div>LinkedIn</div></a>
						</div>

						<div className="row margin_small10">
							<div className="horizontal_lines_small_screen col-12"></div>
						</div>
					</div>



					<div className="row closing_row">
						<div className="logo_col col-md-2 col-12">
							<img src="../../../static/homepage/logo2.png" alt="White logo" className="white_logo" />
						</div>

						<div className="closing_headings col-md-2 col-4">Disclaimer</div>
						<div className="closing_headings col-md-2 col-2">Trademarks</div>
						<div className="closing_headings offset-md-0 col-md-4 offset-1 col-5">Privacy Policy</div>
					</div>

					<div className="row closing_content margin3 margin_small10">
						<div className="offset-md-2 col-md-6 col-12">MrktDB™ is a registered trademark of MrktDB Technologies Inc. MrktDB™ LOGO is a registered Trademark of MrktDB Technologies Inc.
                  <div className="row stamp_small_div">
								<br />
								<img src="../../../static/homepage/logo3.png" alt="Developed In" className="stamp_small mt-5 mb-3" />
							</div>
							<div className="margin3 margin_small6">COPYRIGHT- all text and design. COPYRIGHT ©MrktDB Technologies Inc. <br /> 2020- All Rights Reserved</div>
						</div>

						<div className="col-4 stamp_div">
							<img src="../../../static/homepage/logo3.png" alt="Developed In" className="stamp" />
						</div>
					</div>

				</div>
			</div>
		</Fragment>
	);
}

export default Footer;