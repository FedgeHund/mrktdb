import React, { Component } from 'react';
import FormUserDetails from './FormUserDetails';
import FormPersonalDetails from './FormPersonalDetails';
import AddProfilePicture from './AddProfilePicture';
import Confirm from './Confirm';
import Success from './Success';

export class UserForm extends Component {
	state = {
		step : 1,
		email : '',
		password : '',
		confPassword : '',
		firstName : '',
		lastName : '',
		occupation : '',
		company : '',
		city: '',
		profilePicture : '',
		state: '',
		zip_code: '',
		phone: '',
	}
	// file deepcode ignore React-stateUsedInStateUpdateMethod: <>
	// Proceed to next step
	nextStep = () => {
		const { step } = this.state;
		this.setState({
			step : step + 1
		});
	}

	// Revert to previous step
	prevStep = () => {
		const { step } = this.state;
		this.setState({
			step : step - 1
		});
	}

	// Handle fields change
	handleChange = input => e => {
		this.setState({[input] : e.target.value, errorMessage: ''});
	}

	render() {

		const { step } = this.state;
		const { firstName, lastName, email, occupation, city, company, password, confPassword, state, zip_code, phone } = this.state;
		const values = { firstName, lastName, email, occupation, city, company, step, password, confPassword, state, zip_code, phone };

		switch(step) {
			case 1: 
					return(
							<FormUserDetails 
								nextStep = {this.nextStep}
								handleChange = {this.handleChange}
								values = {values}
							/>
					)		
					
			case 2: 
					return(
						<FormPersonalDetails 
							nextStep = {this.nextStep}
							prevStep = {this.prevStep}
							handleChange = {this.handleChange}
							values = {values}
						/>
					)

			case 3: 
					return(
						<AddProfilePicture 
							nextStep = {this.nextStep}
							prevStep = {this.prevStep}
							handleChange = {this.handleChange}
							values = {values}
						/>
					)

			case 4: 
					return(
						<Confirm 
							nextStep = {this.nextStep}
							prevStep = {this.prevStep}
							handleChange = {this.handleChange}
							values = {values}
						/>
					)

			case 5: 
					return(
						<Success />
					)
		}
	}
}

export default UserForm
