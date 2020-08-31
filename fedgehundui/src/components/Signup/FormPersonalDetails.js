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
				<div class="container signin_box shadow p-3 mb-5 bg-white col-md-4 offset-md-4">
                   <div class="col-sm-12 my-auto">
                   		<div className="row">
                            <div class="v9_2 col-md-12">Step {values.step} / 3</div>
                        </div>

                        <div className="row">
                            <div class="v8_3 col-md-10 offset-md-1">Let's get to know you a little better!</div>
                        </div>
                      
                   </div>
                   
    			<form>
                    <div className="row">
                        <input type="text" class="v12_4 col-md-9 offset-md-1" placeholder="First Name *" onChange={handleChange('firstName')} value={values.firstName} autoComplete="off" onFocus={this.onFocus}/>
                    </div>  
                    <div className="row">
                        <input type="text" class="v12_4 col-md-9 offset-md-1" placeholder="Last Name *" onChange={handleChange('lastName')} value={values.lastName} autoComplete="off" onFocus={this.onFocus}/>
                    </div>  
                    <div className="row">
                        <input type="text" class="v12_4 col-md-9 offset-md-1" placeholder="Occupation" onChange={handleChange('occupation')} value={values.occupation} autoComplete="off" onFocus={this.onFocus}/>
                    </div>
                    <div className="row">
                        <input type="text" class="v12_4 col-md-9 offset-md-1" placeholder="Company" onChange={handleChange('company')} value={values.company} autoComplete="off" onFocus={this.onFocus}/>
                    </div> 
                    <div className="row">
                        <input type="text" class="v12_4 col-md-9 offset-md-1" placeholder="City" onChange={handleChange('city')} value={values.city} autoComplete="off" onFocus={this.onFocus}/>
                    </div> 
			    </form>
    			
                <div className="row ">
                    <button class="btn shadow-sm col-md-3 offset-md-1 back-btn" type="submit" onClick={this.back}>
                        <span class="back-btn-text">Back</span>
                    </button>
                    <button class="btn btn-primary shadow-sm col-md-4 offset-md-3 submit-btn" type="submit" onClick={this.continue}>
                        <span>Continue</span>
                    </button>
                </div>
    			
    		</div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;