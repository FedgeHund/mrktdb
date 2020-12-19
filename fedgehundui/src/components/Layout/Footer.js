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
              <div className="col-2 footer_section">Filers</div>
              <div className="col-10">
                <div className="footer_heading">13F Filers</div>
                <div className="row">
                  <a href="#" className="filer_items col-3"><div className="margin4">Latest Filings</div></a>
                  <a href="#" className="filer_items col-4"><div className="margin4">13F Searching</div></a>
                </div>
                <div className="row">
                  <a href="#" className="filer_items col-3"><div className="margin3">Popular Stocks</div></a>
                  <a href="#" className="filer_items col-4"><div className="margin3">13F Fund Performance Search</div></a>
                </div>
                <div className="row">
                  <a href="#" className="filer_items col-3"><div className="margin3">13F Trends</div></a>
                  <a href="#" className="filer_items col-4"><div className="margin3">13F Stock Screener</div></a>
                </div>
                <div className="row">
                  <a href="#" className="filer_items col-3"><div className="margin3">13F Statistics</div></a>              
                </div>
                <div className="horizontal_line margin5"></div>
              </div>
            </div>

            <div className="quick_links">
              <div className="row">
                <div className="col-2 footer_section">Quick links</div>
                <div className="col-10">
                  <div className="row">
                    <div className="footer_heading col-2">Help</div>
                    <div className="footer_heading col-3">Collaborate</div>
                    <div className="footer_heading col-2">Connect</div>
                    <div className="footer_heading col-3">Explore</div>
                    <div className="footer_heading col-2">Social Media</div>
                  </div>
                  <div className="row">
                    <a href="#" className="filer_items col-2"><div className="margin4">Our offerings</div></a>
                    <a href="#" className="filer_items col-3"><div className="margin4">Advertise with us</div></a>
                    <a href="#" className="filer_items col-2"><div className="margin4">Contact Us</div></a>
                    <a href="#" className="filer_items col-3"><div className="margin4">Email Newsletter</div></a>
                    <a href="#" className="filer_items col-2"><div className="margin4">Twitter</div></a>
                  </div>
                  <div className="row">
                    <a href="#" className="filer_items col-2"><div className="margin3">Getting started</div></a>
                    <a href="#" className="filer_items col-3"><div className="margin3">Business Resources</div></a>
                    <a href="#" className="filer_items col-2"><div className="margin3">Report a Bug</div></a>
                    <a href="#" className="filer_items col-3"><div className="margin3">Upcoming events</div></a>
                    <a href="#" className="filer_items col-2"><div className="margin3">Instagram</div></a>
                  </div>
                  <div className="row">
                    <a href="#" className="filer_items col-2"><div className="margin3">FAQ</div></a>
                    <a href="#" className="filer_items col-3"><div className="margin3"></div></a>
                    <a href="#" className="filer_items col-2"><div className="margin3">Sign in</div></a>
                    <a href="#" className="filer_items col-3"><div className="margin3"></div></a>
                    <a href="#" className="filer_items col-2"><div className="margin3">Facebook</div></a>
                  </div>
                  <div className="row">
                    <a href="#" className="filer_items col-2"><div className="margin3"></div></a>
                    <a href="#" className="filer_items col-3"><div className="margin3"></div></a>
                    <a href="#" className="filer_items col-2"><div className="margin3"></div></a>
                    <a href="#" className="filer_items col-3"><div className="margin3"></div></a>
                    <a href="#" className="filer_items col-2"><div className="margin3">LinkedIn</div></a>
                  </div>
                </div>
              </div>
            </div>

            <div className="row closing_row">
              <div className="col-2" style={{textAlign: "left"}}>
                <img src="../../../static/homepage/logo2.png" alt="White logo" className="white_logo"/>
              </div>
              <div className="col-8">
                <div className="row">
                  <div className="closing_headings col-2">Disclaimer</div>
                  <div className="closing_headings col-2">Trademarks</div>
                  <div className="closing_headings col-3">Privacy Policy</div>
                  <div className="col-5 stamp_div">
                    <img src="../../../static/homepage/logo3.png" alt="Developed In" className="stamp"/>
                  </div>
                </div>
                <div className="row closing_content margin3">
                  <div className="col-8">MrktDB™ is a registered trademark of MrktDB Technologies Inc. <br/> MrktDB™ LOGO is a registered Trademark of MrktDB Technologies Inc.
                    <div className="margin2">COPYRIGHT- all text and design. COPYRIGHT ©MrktDB Technologies Inc. 2020- All Rights Reserved</div>
                  </div>
                </div>
                <div className="row closing_content margin2">
                  
                </div>
                
                
              </div>
            </div>
            
          </div>  
        </div>
    </Fragment>
  );
}

export default Footer;