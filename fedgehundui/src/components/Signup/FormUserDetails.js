import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import '../../../styles/signup/styles.css';

export class FormUserDetails extends Component {

    constructor(){
        super();
        this.handleSubmit = this.handleSubmit.bind(this);
        this.continue = this.continue.bind(this);
        this.state = {errorMessage: ""};
    }

	continue = e => {
		e.preventDefault();
		this.props.nextStep();
	}

    onFocus = event => {
        if(event.target.autocomplete)
        {
            event.target.autocomplete = "No";
        }
    };


    handleSubmit = (e) => {
        e.preventDefault();

        axios.post("http://127.0.0.1:8000/auth/registration/", {
                "first_name": this.props.values.firstName,
                "last_name": this.props.values.lastName,
                "email": this.props.values.email,
                "password1": this.props.values.password,
                "password2": this.props.values.confPassword
            },
            {
                headers: {
                    "Content-Type": 'application/json'
                }
            }
        )
        .then(function(response) {
                if(response.status == 201){
                    this.continue(e);
                }
                else{
                    //window.location = "http://127.0.0.1:8000/signin/"
                }
            }.bind(this))
        .catch(error => {this.setState({errorMessage: error.response.data.first_name || 
                                                    error.response.data.last_name || 
                                                    error.response.data.email || 
                                                    error.response.data.password1 || 
                                                    error.response.data.password2})}
        )
    };


	render() {
		const { values, handleChange, step } = this.props;
		this.props.values;

		return (
			<Fragment>
				<div className="main_div">
                        <div className="signup_box p-3 shadow mb-5">

                                <div className="col-sm-12">
                               		<div className="row">
                                        <div className="step col-md-12">Step {values.step} / 3</div>
                                    </div>

                                    <div className="row">
                                        <div className="sign_up_text col-md-12">Sign Up</div>
                                    </div>
                                    <div className="row">
                                        <span className="question col-sm-8">Already have an account? </span>
                                        <Link to={"/signin"} className="signin_Link col-sm-3">Sign In</Link>
                                    </div>  
                                </div>
                                   
                    			<form>
                                    <div className="row">
                                        <label className="use_email col-md-10 offset-md-1">Sign Up using email address</label>
                                    </div>

                                    <div className="inputBox">
                                        <input type="text" onChange={handleChange('firstName')} value={values.firstName} autoComplete="off" onFocus={this.onFocus} required/>
                                        <label>First Name</label>
                                    </div>  
                                    <div className="inputBox">
                                        <input type="text" onChange={handleChange('lastName')} value={values.lastName} autoComplete="off" onFocus={this.onFocus} required/>
                                        <label>Last Name</label>
                                    </div>  
                                    <div className="inputBox">
                                        <input type="email" onChange={handleChange('email')} value={values.email} autoComplete="off" onFocus={this.onFocus} required/>
                                        <label>Email Address</label>
                                    </div>  
                                    <div className="inputBox">
                                        <input type="password" onChange={handleChange('password')} value={values.password} autoComplete="off" onFocus={this.onFocus} required/>
                                        <label>Password</label>
                                    </div>  
                                    <div className="inputBox">
                                        <input type="password" onChange={handleChange('confPassword')} value={values.confPassword} autoComplete="off" onFocus={this.onFocus} required/>
                                        <label>Confirm Password</label>
                                    </div>  
                                    <div>{ this.state.errorMessage && <p className="validations"> *{ this.state.errorMessage } </p> }</div>
                			    </form>

                                <div className="row">
                                    <button className="btn btn-primary shadow-sm col-sm-6 offset-sm-3 submit-btn" type="submit" onClick={this.handleSubmit}>
                                        <span>Create Account</span>
                                    </button>
                                </div>

                				<div className="row">
                                    <span className="captcha col-md-8 offset-md-2">Protected by reCAPTCHA and subject to the Google <a href="#" className="v12_22">Privacy Policy</a> and <a href="#" className="v12_22">Terms of service</a>.</span>
                                </div>

                        </div>  
        		</div>
			</Fragment>
		)
	}
}

export default FormUserDetails;