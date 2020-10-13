import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.scss';
import { URL } from '../App.js';

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
                    <div className="signup_box p-3 col-md-4 shadow mb-5" style={{height: "530px"}}>

                        <div className="col-sm-12">
                       		<div className="row">
                                <div className="step col-md-12">Step {values.step} / 3</div>
                            </div>

                            <div className="row">
                                <div className="sign_up_text col-md-10 offset-md-1">Profile Picture</div>
                            </div>
                        </div>
                    
                   
    			         <div className="uploaded_pic"><span className="circle"></span></div>
    			
                        <div className="row">
                            <button className="btn shadow-sm col-md-3 offset-md-1 back-btn" type="submit" onClick={this.back}>
                                <span>Back</span>
                            </button>
                            <button className="btn btn-primary shadow-sm col-md-4 offset-md-3 submit-btn" type="submit" onClick={this.continue}>
                                <span>Continue</span>
                            </button>
                        </div>
    			    </div>
    		    </div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;