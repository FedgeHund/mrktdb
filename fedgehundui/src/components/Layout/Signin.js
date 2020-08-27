import React, { Component, Fragment } from 'react';
import '../../../styles/signin/styles.css';

function Signin() {
  return (
    <Fragment>
    		<div class="container signin_box shadow p-3 mb-5 bg-white">
                   <div class="col-sm-12 my-auto">
                        <div className="row">
                            <div class="v9_3 col-md-12">Sign in</div>
                        </div>
                        <div className="row">
                            <span class="v12_0 col-md-6">New to WolfStreet? </span>
                            <a href="#" class="v12_2 col-md-6">Create an account</a>
                        </div>  
                   </div>
                   
    			<form>
                    <div className="row">
			             <label class="v12_3 col-md-11 offset-md-1">Email Address</label>
                    </div>
                    <div className="row">
                        <input type="email" class="v12_4 col-md-9 offset-md-1"/>
                    </div>  
			        <div className="row">
                         <label class="v12_3 col-md-11 offset-md-1">Password</label>
                    </div>
                    <div className="row">
                        <input type="password" class="v12_4 col-md-9 offset-md-1"/>
                    </div>  
			    </form>

                <div className="row">
                    <a href="#" class="v12_8 col-md-11 offset-md-1">Forgot Password?</a>
                </div>
    			
                <div className="row">
                    <button class="btn btn-primary shadow-sm col-md-4 offset-md-4 submit-btn" type="submit">
                        <span>Sign in</span>
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
                    <span class="v12_21 col-md-8 offset-md-2">Protected by reCAPTCHA and subject to the Google <a href="#" class="v12_22">Privacy Policy</a> and <a href="#" class="v12_22">Terms of service</a>.</span>
                </div>
    			
    		</div>
	</Fragment>
  );
}

export default Signin;