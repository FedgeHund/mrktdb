import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import '../../../styles/signup/styles.css';

export class FormUserDetails extends Component {
	continue = e => {
		e.preventDefault();
		this.props.nextStep();
	}

    onFocus = event => {
        if(event.target.autocomplete)
        {
            event.target.autocomplete = "whatever";
        }
    };

	render() {
		const { values, handleChange, step } = this.props;
		this.props.values;

		return (
			<Fragment>
				<div className="container-fluid">
                    <div className="row">
                        <div className="signin_box p-3 shadow mb-5 col-12 col-md-4 col-sm-6 offset-sm-3 offset-md-4">

                                <div className="col-sm-12 my-auto">
                               		<div className="row">
                                        <div className="v9_2 col-md-12">Step {values.step} / 3</div>
                                    </div>

                                    <div className="row">
                                        <div className="v9_3 col-md-12">Sign Up</div>
                                    </div>
                                    <div className="row">
                                        <span className="v12_0 col-sm-8">Already have an account? </span>
                                        <Link to={"/signin"} className="v12_2 col-sm-3">Sign In</Link>
                                    </div>  
                                </div>
                                   
                    			<form>
                                    <div className="row">
                			             <label className="v12_3 col-md-10 offset-md-1">Sign Up using email address</label>
                                    </div>
                                    <div className="row">
                                        <input type="email" className="v12_4 col-md-9 offset-md-1" placeholder="Email Address" onChange={handleChange('email')} value={values.email} autoComplete="off" onFocus={this.onFocus} required/>
                                    </div>  
                                    <div className="row">
                                        <input type="password" className="v12_4 col-md-9 offset-md-1" placeholder="Password" onChange={handleChange('password')} value={values.password}/>
                                    </div>  
                                    <div className="row">
                                        <input type="password" className="v12_4 col-md-9 offset-md-1" placeholder="Confirm Password" onChange={handleChange('confPassword')} value={values.confPassword}/>
                                    </div>  
                			    </form>
                    			
                                <div className="row">
                                    <button className="btn btn-primary shadow-sm col-md-4 offset-md-4 submit-btn" type="submit" onClick={this.continue}>
                                        <span>Continue</span>
                                    </button>
                                </div>

                				<div className="row">
                                    <span className="v12_21 col-md-8 offset-md-2">Protected by reCAPTCHA and subject to the Google <a href="#" className="v12_22">Privacy Policy</a> and <a href="#" className="v12_22">Terms of service</a>.</span>
                                </div>

                        </div>  
        			</div>
        		</div>
			</Fragment>
		)
	}
}

export default FormUserDetails;