import React from 'react'
import '../../../styles/signup/styles.css';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

const CLIENT_ID = '697434274174-b3jeg526rn1da2vrn3si3d9or0t2c3to.apps.googleusercontent.com';

function GoogleLoginBtn() {
    const onSuccess = (res) => {
        console.log('[Google Login Success] currentUser:', res.profileObj);
    }

    const onFailure = (res) => {
        console.log('[Google Login Failed] res:', res);
    }

    return (
        <div>
            <GoogleLogin
                clientId={CLIENT_ID}
                buttonText="Login"
                render={renderProps => (
                    <div className="row">
                        <button className="btn btn-primary shadow-sm col-md-8 offset-md-2 col-sm-10 offset-sm-1 col-xs-10 offset-xs-1 col-10 offset-1 submit-btn google_signup_btn" onClick={renderProps.onClick} disabled={renderProps.disabled}>
                            <i className="fab fa-google"></i><span>&nbsp;&nbsp;&nbsp;Sign Up using Google</span>
                        </button>
                    </div>
                )}
                onSuccess={onSuccess}
                onFailure={onFailure}
                cookiePolicy={'single_host_origin'}
                isSignedIn={true}
            />
        </div>
    );
}

export default GoogleLoginBtn;