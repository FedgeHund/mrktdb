import React, { Fragment } from 'react';
import '../../../styles/contactus.css';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';

function ContactUs() {

    const onFocus = (event) => {
        if(event.target.autocomplete)
        {
            event.target.autocomplete = "No";
        }
    };

  return (
    <Fragment>
    		  
        <Navbar />
            
            <div className="contact_us_container">
                <div className="contact_us">
                    <div className="row">
                       <div className="offset-md-1 col-md-6 contact_us_heading">Contact Us</div>
                    </div>

                    <div className="row mt-4">
                        <div className="offset-md-1 col-md-10 contact_notice">
                            Please note that <a href="/" className="link_to_homepage">mrktdb.com</a> is an aggregator of public SEC filings and is not affiliated with any of the companies displayed on the website. If you are trying to contact one of the companies listed here to obtain information on an account you have with them or to request a K-1, you must contact that company directly. We are not affiliated with any of the companies and cannot assist you.
                        </div>
                    </div>

                    <div className="row email_us">
                        <div className="offset-md-1 col-md-11">
                            Email us at:
                            <br></br>
                            contact@mrktdb.com
                            <br></br>
                            <br></br>
                            Or submit your comments anonymously using the form below.
                        </div>
                    </div>

                    <div className="row contact_form">
                        <div className="offset-md-1 col-md-10 offset-0 col-12">
                            <div className="contact_us_div">
                                <div className="contact_us_box col-md-12 p-3 shadow mb-5"> 

                                    <div className="row">
                                        <div className="col-md-5">

                                            <form className="message_inputs">
                                                <div className="inputBox">
                                                    <input type="text" autoComplete="off" onFocus={onFocus} required/>
                                                    <label>Name&nbsp; (Optional)</label>
                                                </div> 

                                                <div className="inputBox">
                                                    <input type="email" autoComplete="off" onFocus={onFocus} required/>
                                                    <label>Email Address&nbsp; (Optional)</label>
                                                </div>  
                                            </form>


                                            <div className="row mt-5">
                                                <div className="col-md-10 col-8 provide_email">If you don't provide an email, we will not be able to respond to your query!</div>
                                            </div>
                                        </div>

                                        <div className="col-md-6 col-10 mt-3 message_box">
                                            <div class="form-group">
                                                <label className="message">Message</label>
                                                <textarea className="form-control textarea_contact" rows="8"></textarea>
                                            </div>

                                            <button className="btn shadow-sm col-md-12 col-sm-12 col-12 send_message_btn" type="submit">
                                                <span>Send Message</span>
                                            </button>
                                          
                                        </div>

                                    </div>
                                </div>
                            </div>
                    </div>
                    </div>


                </div>
            </div>
        
        <Footer />

	</Fragment>
  );
}

export default ContactUs;