import React, { Component, Fragment } from 'react';
import {useState, useEffect} from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'; 
import '../../../styles/signin/styles.css';

function Signin() {

    const [state, setState] = useState({
        email: '',
        password: '',
    });

    const{email, password} = state;

    const handleChange = (name) => (e) => {
        setState({...state, [name]: e.target.value})
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        axios.post("http://127.0.0.1:8000/auth/login/", {
                email,
                password
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


  return (
    <Fragment>
    		<div className="container signin_box shadow p-3 mb-5 bg-white col-md-4 offset-md-4">
                   <div className="col-sm-12 my-auto">
                        <div className="row">
                            <div className="v9_3 col-md-12">Sign In</div>
                        </div>
                        <div className="row">
                            <span className="v12_0 col-md-6">New to MrktDB? </span>
                            <Link to={"/"} className="v12_2 col-md-6">Create an account</Link>
                        </div>  
                   </div>
                   
    			<form>
                    <div className="row">
			             <label className="v12_3 col-md-11 offset-md-1">Email Address</label>
                    </div>
                    <div className="row">
                        <input type="email" value={email} onChange = {handleChange('email')} className="v12_4 col-md-9 offset-md-1" required/>
                    </div>  
			        <div className="row">
                         <label className="v12_3 col-md-11 offset-md-1">Password</label>
                    </div>
                    <div className="row">
                        <input type="password" value={password} onChange = {handleChange('password')} className="v12_4 col-md-9 offset-md-1" required/>
                    </div>  
			    </form>

                <div className="row">
                    <a href="#" className="v12_8 col-md-11 offset-md-1">Forgot Password?</a>
                </div>
    			
                <div className="row">
                    <button className="btn btn-primary shadow-sm col-md-4 offset-md-4 submit-btn" type="submit" onClick={handleSubmit}>
                        <span>Sign In</span>
                    </button>
                </div>

    {/*         <div className="row">
                    <span class="v12_13 col-md-6">Or</span>
                </div>
				
                <div className="row">
                    <button class="v12_14 btn btn-outline-info col-md-6 offset-md-3" type="submit">Continue with Google</button>
                </div>

                 <div className="row">
                    <button class="v12_15 btn btn-outline-info col-md-6 offset-md-3" type="submit">Continue with Facebook</button>
                </div>
	*/}			
				<div className="row">
                    <span className="v12_21 col-md-8 offset-md-2">Protected by reCAPTCHA and subject to the Google <a href="#" className="v12_22">Privacy Policy</a> and <a href="#" className="v12_22">Terms of service</a>.</span>
                </div>
    			
    		</div>
	</Fragment>
  );
}

export default Signin;