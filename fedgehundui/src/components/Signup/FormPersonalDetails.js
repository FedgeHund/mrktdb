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
            event.target.autocomplete = "Whatever";
        }
    };

	render() {
		const { values, handleChange, step } = this.props;
		this.props.values;

		return (
			<Fragment>
				<div className="main_div">
                    <div className="signup_box p-3 shadow mb-5" style={{height: "700px"}}>

                        <div className="col-sm-12">
                       		<div className="row">
                                <div className="step col-md-12">Step {values.step} / 3</div>
                            </div>

                            <div className="row">
                                <div className="detail_heading col-md-10 offset-md-1">Let's get to know you a little better!</div>
                            </div>
                        </div>   

                   
            			<form>
                            <div className="inputBox">
                                <input type="text" onChange={handleChange('occupation')} value={values.occupation} autoComplete="off" onFocus={this.onFocus}/>
                                <label>Occupation</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('company')} value={values.company} autoComplete="off" onFocus={this.onFocus}/>
                                <label>Company</label>
                            </div> 

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('state')} value={values.state} autoComplete="off" onFocus={this.onFocus}/>
                                <label>State</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('city')} value={values.city} autoComplete="off" onFocus={this.onFocus}/>
                                <label>City</label>
                            </div>

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('zipCode')} value={values.zipCode} autoComplete="off" onFocus={this.onFocus}/>
                                <label>Zip Code</label>
                            </div>  

                            <div className="inputBox">
                                <input type="text" onChange={handleChange('phone')} value={values.phone} autoComplete="off" onFocus={this.onFocus}/>
                                <label>Phone Number</label>
                            </div>
        			    </form>
            			
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