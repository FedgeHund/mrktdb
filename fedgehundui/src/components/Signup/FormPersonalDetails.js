import React, { Component, Fragment } from 'react';
import axios from 'axios';
import '../../../styles/signup/styles.css';
import { URL } from '../App.js';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';

export class FormPersonalDetails extends Component {

    constructor() {
        super();
        this.handleSubmit = this.handleSubmit.bind(this);
        this.continue = this.continue.bind(this);
        this.state = { errorMessage: "" };
    }

    continue = e => {
        e.preventDefault();
        this.props.nextStep();
    };

    back = e => {
        e.preventDefault();
        this.props.prevStep();
    };

    onFocus = event => {
        if (event.target.autocomplete) {
            event.target.autocomplete = "No";
        }
    };

    handleSubmit = async (e) => {
        e.preventDefault();

        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';

        await axios.post("http://" + "mrktdb.eba-brufwk2z.us-west-2.elasticbeanstalk.com" + "/profile/fields/", {
            "occupation": this.props.values.occupation,
            "company": this.props.values.company,
            "state": this.props.values.state,
            "city": this.props.values.city,
            "zip_code": this.props.values.zip_code,
            "phone": this.props.values.phone
        },
            {
                headers: {
                    "Content-Type": 'application/json',
                    "X-CSRFToken": 'csrftoken'
                }
            }
        )
            .then(function (response) {
                if (response.status == 201) {
                    //this.continue(e);
                }
                else {
                    //window.location = "http://127.0.0.1:8000/signin/"
                }
            }.bind(this))
            .catch(error => {
                this.setState({
                    errorMessage: error.response.data.occupation ||
                        error.response.data.company ||
                        error.response.data.state ||
                        error.response.data.city ||
                        error.response.data.zip_code ||
                        error.response.data.phone
                })
            }
            )
        this.continue(e);
    };

    render() {
        const { values, handleChange, step } = this.props;
        this.props.values;

        return (
            <Fragment>
                <Navbar />
                <div className="main_div">
                    <div className="signup_box p-3 shadow mb-5" style={{ height: "720px", top: "48%" }}>

                        <div className="col-sm-12">
                            <div className="row">
                                <div className="step col-md-12">Step {values.step} / 3</div>
                            </div>

                            <div className="row">
                                <div className="detail_heading col-md-8 offset-md-2">Let's get to know you a little better!</div>
                            </div>
                        </div>


                        <form method="post">
                            <div className="inputBox">
                                <input type="text" onChange={handleChange('occupation')} value={values.occupation} autoComplete="off" onFocus={this.onFocus} />
                                <label>Occupation</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('company')} value={values.company} autoComplete="off" onFocus={this.onFocus} />
                                <label>Company</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('state')} value={values.state} autoComplete="off" onFocus={this.onFocus} />
                                <label>State</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('city')} value={values.city} autoComplete="off" onFocus={this.onFocus} />
                                <label>City</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('zip_code')} value={values.zip_code} autoComplete="off" onFocus={this.onFocus} />
                                <label>Zip Code</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('phone')} value={values.phone} autoComplete="off" onFocus={this.onFocus} />
                                <label>Phone Number</label>
                            </div>
                            <div>{this.state.errorMessage && <p className="validations"> *{this.state.errorMessage} </p>}</div>
                        </form>

                        <div className="row">
                            <button className="btn btn-primary shadow-sm col-md-6 offset-md-3 submit-btn" type="submit" onClick={this.handleSubmit}>
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