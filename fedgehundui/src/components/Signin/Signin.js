import React, { Fragment } from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import '../../../styles/signup/styles.css';
import { URL } from '../App.js';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
// file deepcode ignore no-mixed-spaces-and-tabs:

function Signin() {

    const [state, setState] = useState({
        email: "",
        password: "",
        errorMessage: ""
    });

    const { email, password, errorMessage } = state;

    const onFocus = (event) => {
        if (event.target.autocomplete) {
            event.target.autocomplete = "No";
        }
    };

    const handleChange = (name) => (e) => {
        setState({ ...state, [name]: e.target.value, errorMessage: '' })
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        axios.post("http://" + URL + "/auth/login/", {
            email,
            password
        },
            {
                headers: {
                    "Content-Type": 'application/json'
                }
            }
        )
            .then(function (response) {
                if (response.status == 200) {
                    window.location = "http://" + URL + "/"
                }
                else {
                    window.location = "http://" + URL + "/signin/"
                }
            })
            .catch(error => {
                setState({
                    errorMessage: error.response.data.email ||
                        error.response.data.password ||
                        error.response.data.non_field_errors
                })
            }
            )
    };


    return (
        <Fragment>
            <Navbar />
            <div className="main_div">
                <div className="signup_box p-3 shadow mb-5 signin_box">

                    <div className="col-sm-12">
                        <div className="row">
                            <div className="sign_up_text col-md-12 pt-5">Sign In</div>
                        </div>
                        <div className="row">
                            <span className="question col-sm-6 col-6">New to MrktDB? </span>
                            <Link to={"/signup"} className="signup_Link col-sm-6 col-6">Create an account</Link>
                        </div>
                    </div>

                    <form className="pt-4">
                        <div className="inputBox">
                            <input type="email" value={email} onChange={handleChange('email')} autoComplete="off" onFocus={onFocus} required />
                            <label>Email Address</label>
                        </div>

                        <div className="inputBox">
                            <input type="password" value={password} onChange={handleChange('password')} autoComplete="off" onFocus={onFocus} required />
                            <label>Password</label>
                        </div>

                        {/* <input type="submit" style={{ display: "none" }} /> */}
                    </form>

                    <div className="row">
                        <div className="col-md-6"></div>
                        <a href="#" className="col-md-6 forgotPassword">Forgot Password?</a>
                    </div>

                    <div className="row">
                        <div>{errorMessage && <p className="signinValidations">*{errorMessage}</p>}</div>
                    </div>

                    <div className="row pt-3">
                        <button id='signin' className="btn btn-primary shadow-sm offset-md-3 col-md-6 offset-sm-3 col-sm-6 offset-2 col-8 submit-btn" type="submit" onClick={handleSubmit}>
                            <span>Sign In</span>
                        </button>
                    </div>

                    <div className="row">
                        <span className="captcha col-md-8 offset-md-2 col-10 offset-1 pt-5 mt-4">Protected by reCAPTCHA and subject to the Google <a href="#" className="links">Privacy Policy</a> and <a href="#" className="links">Terms of service</a>.</span>
                    </div>

                </div>
            </div>
            <Footer />
        </Fragment>
    );
}

export default Signin;
