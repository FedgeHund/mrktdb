import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.css';

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
				<div className="main_div">
                   <div className="signup_box p-3 shadow mb-5" style={{height: "670px"}}>

                        <div className="col-sm-12">
                            <div className="row">
                                <div className="almost_text col-md-10 offset-md-1">Almost there!</div>
                            </div>
                        </div>
                   
            			<div className="uploaded_pic"><span className="circle"></span></div>

                        <div className="row">
                            <div className="create_message col-md-12">Hi, {values.firstName}</div>
                        </div>
                        
                        <div className="row">
                            <div className="created_email col-md-12">{values.email}</div>
                        </div>

                        <div className="row">
                            <button className="btn btn-primary shadow-sm col-md-8 offset-md-2 submit-btn" style={{marginTop: "40px"}} type="submit" onClick={this.continue}>
                                <span>Go to your homepage</span>
                            </button>
                        </div>

                        <div className="row">
                            <span className="captcha col-md-8 offset-md-2">By creating this account you will agree with the <a href="#" className="v12_22">Privacy Policy </a> and <a href="#" className="v12_22">Terms &amp; Conditions </a>of MrktDB.</span>
                        </div>             
    			    </div>
    		    </div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;