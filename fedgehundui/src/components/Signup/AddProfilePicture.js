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
				<div className="container propic_box shadow p-3 mb-5 bg-white col-md-4 offset-md-4">
                   <div className="col-sm-12 my-auto">
                   		<div className="row">
                            <div className="v9_2 col-md-12">Step {values.step} / 3</div>
                        </div>

                        <div className="row">
                            <div className="v7_3 col-md-10 offset-md-1">Profile Picture</div>
                        </div>
                      
                   </div>
                   
    			<div className="uploaded_pic"><span className="circle"></span></div>
    			
                <div className="row">
                    <button className="btn shadow-sm col-md-3 offset-md-1 back-btn" type="submit" onClick={this.back}>
                        <span className="back-btn-text">Back</span>
                    </button>
                    <button className="btn btn-primary shadow-sm col-md-4 offset-md-3 submit-btn" type="submit" onClick={this.continue}>
                        <span>Continue</span>
                    </button>
                </div>
    			
    		</div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;