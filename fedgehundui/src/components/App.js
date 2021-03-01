import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Signin from './Signin/Signin';
import UserForm from './Signup/UserForm';
import Homepage from './Homepage/Homepage';
import ContactUs from './ContactUs/ContactUs';
import FAQ from './FAQ/FAQ';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import '../../templates/fedgehundui/global.css';
// file deepcode ignore no-mixed-spaces-and-tabskey: "value", 
// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and space"

class App extends Component {
  render() {
    return (
    	<Fragment>
      		<Router>
	      		<Switch>
                <Route path="/" exact component={() => <Homepage />} />
		          	<Route path="/signup" exact component={() => <UserForm />} />
		          	<Route path="/signin" exact component={() => <Signin />} />
                <Route path="/contactus" exact component={() => <ContactUs />} />
                <Route path="/faq" exact component={() => <FAQ />} />
		        </Switch>     		
      		</Router>
      	</Fragment>
    );
  }
}

const ENV_VARIABLES = {
  ENVIRON: "prod",
  DEV_API_URL: "127.0.0.1:8000",
  PROD_API_URL: "mrktdbapi-prod.eba-tw27jjhn.us-west-2.elasticbeanstalk.com",
};

let URL;
if(ENV_VARIABLES.ENVIRON == "dev")
  URL = ENV_VARIABLES.DEV_API_URL;
else
  URL = ENV_VARIABLES.PROD_API_URL;

export { URL };

ReactDOM.render(<App />, document.getElementById('app'));
