import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import '../../../styles/signup/styles.css';
import { URL } from '../App.js';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
import GoogleLoginBtn from './GoogleLoginBtn';
import { getCookie } from '../Helpers/getCookie';

export class FormUserDetails extends Component {

    constructor() {
        super();
        this.handleSubmit = this.handleSubmit.bind(this);
        this.continue = this.continue.bind(this);
        this.state = { errorMessage: "", buttonText: "Create Account" };
    }

    continue = e => {
        e.preventDefault();
        this.props.nextStep();
    }

    onFocus = event => {
        if (event.target.autocomplete) {
            event.target.autocomplete = "No";
        }
    };

    handleSubmit = async (e) => {
        e.preventDefault();

        var csrftoken = getCookie('csrftoken');

        await axios.post("http://" + URL + "/auth/logout/", {
        },
            {
                headers: {
                    "Content-Type": 'application/json',
                    "X-CSRFToken": csrftoken
                }
            }
        )
            .then(function (response) {
                if (response.status == 200) {
                    console.log(response);
                }
                else {
                    //window.location = "http://127.0.0.1:8000/signin/"
                    console.log(response);
                }
            }.bind(this))

        this.setState({ buttonText: "Creating..." });

        await axios.post("http://" + URL + "/auth/registration/", {
            "first_name": this.props.values.firstName,
            "last_name": this.props.values.lastName,
            "email": this.props.values.email,
            "password1": this.props.values.password,
            "password2": this.props.values.confPassword
        },
            {
                headers: {
                    "Content-Type": 'application/json',
                    "X-CSRFToken": csrftoken
                }
            }
        )
            .then(function (response) {
                if (response.status == 201) {
                    this.continue(e);
                }
                else {
                    //window.location = "http://127.0.0.1:8000/signin/"
                    console.log(response);
                }
            }.bind(this))
            .catch(error => {
                this.setState({
                    errorMessage: error.response.data.first_name ||
                        error.response.data.last_name ||
                        error.response.data.email ||
                        error.response.data.password1 ||
                        error.response.data.password2
                })
            }
            )
        this.setState({ buttonText: "Create Account" });
    };


    render() {
        const { values, handleChange, step } = this.props;
        this.props.values;

        return (
            <Fragment>
                <Navbar />
                <div className="formUserDetails_main_div">
                    <div className="signup_box p-3 shadow mb-5 formUserDetailsBox">

                        <div className="col-sm-12">
                            <div className="row">
                                <div className="step col-md-12">Step {values.step} / 3</div>
                            </div>

                            <div className="row">
                                <div className="sign_up_text col-md-12">Sign Up</div>
                            </div>
                            <div className="row">
                                <span className="already col-sm-8 col-8">Already have an account? </span>
                                <Link to={"/signin"} className="signin_Link col-sm-3 col-3">Sign In</Link>
                            </div>
                        </div>

                        <form>
                            {/* <input type="submit" style={{ display: "none" }} /> */}

                            <div className="row">
                                <label className="use_email col-md-10 offset-md-1">Sign Up using email address</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('firstName')} value={values.firstName} autoComplete="off" onFocus={this.onFocus} required />
                                <label>First Name</label>
                            </div>
                            <div className="inputBox">
                                <input type="text" onChange={handleChange('lastName')} value={values.lastName} autoComplete="off" onFocus={this.onFocus} required />
                                <label>Last Name</label>
                            </div>
                            <div className="inputBox">
                                <input type="email" onChange={handleChange('email')} value={values.email} autoComplete="off" onFocus={this.onFocus} required />
                                <label>Email Address</label>
                            </div>
                            <div className="inputBox">
                                <input type="password" onChange={handleChange('password')} value={values.password} autoComplete="off" onFocus={this.onFocus} required />
                                <label>Password</label>
                            </div>
                            <div className="inputBox">
                                <input type="password" onChange={handleChange('confPassword')} value={values.confPassword} autoComplete="off" onFocus={this.onFocus} required />
                                <label>Confirm Password</label>
                            </div>
                            <div>{this.state.errorMessage && <p className="validations"> *{this.state.errorMessage} </p>}</div>
                        </form>

                        <div className="row">
                            <button className="btn btn-primary shadow-sm col-sm-6 offset-sm-3 col-xs-8 offset-xs-2 col-8 offset-2 submit-btn" type="submit" onClick={this.handleSubmit}>
                                <span>{this.state.buttonText}</span>
                            </button>
                        </div>

                        <div className="row">
                            <div className="col-12 mt-4 or" align="center">OR</div>
                        </div>

                        <GoogleLoginBtn />

                        <div className="row">
                            <span className="captcha col-md-8 offset-md-2 col-sm-10 offset-sm-1">Protected by reCAPTCHA and subject to the Google <a href="#" className="links">Privacy Policy</a> and <a href="#" className="links">Terms of service</a>.</span>
                        </div>

                    </div>
                </div>
                <Footer />
            </Fragment>
        )
    }
}

export default FormUserDetails;