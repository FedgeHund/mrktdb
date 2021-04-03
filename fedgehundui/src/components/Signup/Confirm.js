import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.css';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';

export class FormPersonalDetails extends Component {
    continue = e => {
        e.preventDefault();
        this.props.nextStep();
    };

    back = e => {
        e.preventDefault();
        this.props.prevStep();
    };


    render() {
        const { values, handleChange, step } = this.props;
        this.props.values;

        return (
            <Fragment>
                <Navbar />
                <div className="main_div">
                    <div className="signup_box p-3 shadow mb-5" style={{ height: "670px", top: "47%" }}>

                        <div className="col-sm-12">
                            <div className="row">
                                <div className="almost_text col-md-10 offset-md-1">Almost there!</div>
                            </div>
                        </div>

                        <div className="row">
                            <img src="../static/global/profile_img.png" className="circle mt-2 m-auto" />
                        </div>

                        <div className="row">
                            <div className="create_message col-md-12 mt-4">Hi, {values.firstName}</div>
                        </div>

                        <div className="row">
                            <div className="created_email col-md-12">{values.email}</div>
                        </div>

                        <div className="row">
                            <button className="btn btn-primary shadow-sm col-md-8 offset-md-2 submit-btn" style={{ marginTop: "40px" }} type="submit" onClick={this.continue}>
                                <span>Go to your homepage</span>
                            </button>
                        </div>

                        <div className="row">
                            <span className="captcha col-md-8 offset-md-2">By creating this account you will agree with the <a href="#" className="links">Privacy Policy </a> and <a href="#" className="links">Terms &amp; Conditions </a></span>
                        </div>
                    </div>
                </div>
                <Footer />
            </Fragment>
        )
    }
}

export default FormPersonalDetails;