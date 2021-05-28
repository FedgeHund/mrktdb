import React from 'react'
import '../../../styles/signup/styles.css';
import axios from "axios";
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import { useHistory } from "react-router-dom";
import { getCookie } from '../Helpers/getCookie';
import { URL } from '../App.js';

const CLIENT_ID = '697434274174-b3jeg526rn1da2vrn3si3d9or0t2c3to.apps.googleusercontent.com';

function GoogleSigninButton() {
    const history = useHistory();

    const onSuccess = async (res) => {
        // console.log('[Google Login Success]', res);
        var accesstoken = res.accessToken;
        var csrftoken = getCookie('csrftoken');

        let response = await axios.post(
            'http://' + URL + '/auth/google/',
            {
                access_token: accesstoken,
            },
            {
                headers: {
                    'Authorization': `${accesstoken}`,
                    "Content-Type": 'application/json',
                    "X-CSRFToken": csrftoken
                }
            },
        ).then((res) => {
            // console.log('REssss', res)
            history.push(
                {
                    pathname: `/`
                }
            );
        },
            (error) => {
                // console.log(error)
            }
        );
        // console.log('G Login', response);
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
                            <i className="fab fa-google"></i><span>&nbsp;&nbsp;&nbsp;Sign In using Google</span>
                        </button>
                    </div>
                )}
                onSuccess={onSuccess}
                onFailure={onFailure}
                cookiePolicy={'single_host_origin'}
                isSignedIn={false}
                disabled
            />
        </div>
    );
}

export default GoogleSigninButton;