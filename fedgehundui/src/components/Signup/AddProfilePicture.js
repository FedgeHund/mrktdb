import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.css';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';

export class AddProfilePicture extends Component {
    continue = e => {
        e.preventDefault();
        this.props.nextStep();
    };

    back = e => {
        e.preventDefault();
        this.props.prevStep();
    };

    render() {
        const { values } = this.props;
        this.props.values;

        return (
            <Fragment>
                <Navbar />
                <div className="addProfilePicture_main_div">
                    <div className="signup_box p-3 col-md-4 col-8 shadow mb-5 addProfilePictureBox">

                        <div className="col-sm-12">
                            <div className="row">
                                <div className="step col-md-12">Step {values.step} / 3</div>
                            </div>

                            <div className="row mt-4">
                                <div className="sign_up_text col-md-10 offset-md-1">Profile Picture</div>
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

export default AddProfilePicture;