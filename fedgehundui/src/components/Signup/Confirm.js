import React, { Component, Fragment } from 'react';
import axios from 'axios';
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

    componentDidMount() {
        console.log(this.props.values)
    }

    handleSubmit = (e) => {
        e.preventDefault();

        axios.post("http://127.0.0.1:8000/auth/registration/", {
                "email": this.props.values.email,
                "password1": this.props.values.password,
                "password2": this.props.values.confPassword,
                "first_name": this.props.values.firstName,
                "last_name": this.props.values.lastName
            },
            {
                headers: {
                    "Content-Type": 'application/json'
                }
            }
        )
        .then(function(response) {
                if(response.status == 200){
                    window.location = "http://127.0.0.1:8000/auth/logout/"
                }
                else{
                    window.location = "http://127.0.0.1:8000/signin/"
                }
            })
        .catch(error => console.log(error))
    };


	render() {
		const { values, handleChange, step } = this.props;
		this.props.values;

		return (
			<Fragment>
				<div className="container signin_box shadow p-3 mb-5 bg-white col-md-4 offset-md-4">
                   <div className="col-sm-12 my-auto">

                        <div className="row">
                            <div className="v9_3 col-md-10 offset-md-1">Almost there!</div>
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
                    <button className="btn btn-primary shadow-sm col-md-6 offset-md-3 submit-btn" style={{marginTop: "40px"}} type="submit" onClick={this.continue} onClick={this.handleSubmit.bind(this)}>
                        <span>Create Account</span>
                    </button>
                </div>

                <div className="row">
                    <span className="v12_24 col-md-8 offset-md-2">By creating this account you will agree with the <a href="#" className="v12_22">Privacy Policy </a> and <a href="#" className="v12_22">Terms &amp; Conditions </a>of MrktDB.</span>
                </div>

                
    			
    		</div>
			</Fragment>
		)
	}
}

export default FormPersonalDetails;