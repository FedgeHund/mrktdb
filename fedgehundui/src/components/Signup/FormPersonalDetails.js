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
				<div className="container signin_box shadow p-3 mb-5 bg-white col-md-4 offset-md-4" style={{height: "670px"}}>
                   <div className="col-sm-12 my-auto">
                   		<div className="row">
                            <div className="v9_2 col-md-12">Step {values.step} / 3</div>
                        </div>

                        <div className="row">
                            <div className="v8_3 col-md-10 offset-md-1">Let's get to know you a little better!</div>
                        </div>
                      
                   </div>
                   
    			<form>
                    <div className="row">
                        <input type="text" className="v12_4 col-md-9 offset-md-1" placeholder="Occupation" onChange={handleChange('occupation')} value={values.occupation} autoComplete="off" onFocus={this.onFocus}/>
                    </div>
                    <div className="row">
                        <input type="text" className="v12_4 col-md-9 offset-md-1" placeholder="Company" onChange={handleChange('company')} value={values.company} autoComplete="off" onFocus={this.onFocus}/>
                    </div> 
                    <div className="row">
                        <input type="text" className="v12_4 col-md-9 offset-md-1" placeholder="State" onChange={handleChange('state')} value={values.city} autoComplete="off" onFocus={this.onFocus}/>
                    </div>
                    <div className="row">
                        <input type="text" className="v12_4 col-md-9 offset-md-1" placeholder="City" onChange={handleChange('city')} value={values.city} autoComplete="off" onFocus={this.onFocus}/>
                    </div>
                    <div className="row">
                        <input type="text" className="v12_4 col-md-9 offset-md-1" placeholder="Zip Code" onChange={handleChange('zipCode')} value={values.firstName} autoComplete="off" onFocus={this.onFocus}/>
                    </div>  
                    <div className="row">
                        <input type="text" className="v12_4 col-md-9 offset-md-1" placeholder="Phone Number" onChange={handleChange('phone')} value={values.lastName} autoComplete="off" onFocus={this.onFocus}/>
                    </div>
			    </form>
    			
                <div className="row ">
                    <button className="btn shadow-sm col-md-3 offset-md-1 back-btn" type="submit" onClick={this.back}>
                        <span className="back-btn-text">Back</span>
                    </button>
                    <button className="btn btn-primary shadow-sm col-md-4 offset-md-3 submit-btn" type="submit" onClick={this.continue}>
                        <span>Skip</span>
                    </button>
                </div>
    			
    		</div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;