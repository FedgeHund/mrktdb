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
				<div class="container signin_box shadow p-3 mb-5 bg-white col-md-4 offset-md-4">
                   <div class="col-sm-12 my-auto">

                        <div className="row">
                            <div class="v9_3 col-md-10 offset-md-1">Almost there!</div>
                        </div>
                      
                   </div>
                   
    			<div className="uploaded_pic"><span class="circle"></span></div>

                <div className="row">
                    <div className="create_message col-md-12">Hi, {values.firstName}</div>
                </div>
                
                <div className="row">
                    <div className="created_email col-md-12">{values.email}</div>
                </div>

                <div className="row">
                    <button className="btn btn-primary shadow-sm col-md-6 offset-md-3 submit-btn" style={{marginTop: "40px"}} type="submit" onClick={this.continue}>
                        <span>Create Account</span>
                    </button>
                </div>

                <div className="row">
                    <span class="v12_24 col-md-8 offset-md-2">By creating this account you will agree with the <a href="#" class="v12_22">Privacy Policy </a> and <a href="#" class="v12_22">Terms &amp; Conditions </a>of MrktDB.</span>
                </div>

                
    			
    		</div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;