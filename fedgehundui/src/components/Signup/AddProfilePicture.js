import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.css';
import { URL } from '../App.js';
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
                    <div className="signup_box p-3 col-md-4 shadow mb-5" style={{ height: "600px", top: "44%" }}>

                        <div className="col-sm-12">
                            <div className="row">
                                <div className="step col-md-12">Step {values.step} / 3</div>
                            </div>

                            <div className="row">
                                <div className="sign_up_text col-md-10 offset-md-1 mt-4">Profile Picture</div>
                            </div>
                        </div>

                        <div className="row">
                            <img src="../static/global/profile_img.png" className="circle mt-5 m-auto" />
                        </div>

                        <div className="row mt-4">
                            <button className="btn shadow-sm col-md-3 offset-md-1 back-btn" type="submit" onClick={this.back}>
                                <span>Back</span>
                            </button>
                            <button className="btn btn-primary shadow-sm col-md-4 offset-md-3 submit-btn" type="submit" onClick={this.continue}>
                                <span>Continue</span>
                            </button>
                        </div>
                    </div>
                </div>
                <Footer />
            </Fragment>
        )
    }
}

export default FormPersonalDetails;