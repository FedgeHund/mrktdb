import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.css';

export class FormPersonalDetails extends Component {

	render() {
		const { values, handleChange, step } = this.props;
		this.props.values;

		return (
			<Fragment>
				<div className="container signin_box shadow p-3 mb-5 bg-white col-md-8 offset-md-2">
                   <div className="col-sm-12 my-auto">

                        <div className="row">
                            <div className="success_content1 col-md-10 offset-md-1">Thank you for your submission</div>
                        </div>

                        <div className="row">
                            <div className="success_content2 col-md-10 offset-md-1">You will receive an email with further instructions</div>
                        </div>
                      
                   </div>
                
    			
    		</div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;