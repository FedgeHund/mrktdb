import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Signin from './Signin/Signin';
import UserForm from './Signup/UserForm';
import Homepage from './Homepage/Homepage';
import ContactUs from './ContactUs/ContactUs';
import FAQ from './FAQ/FAQ';
import Page_404 from './Page_404/Page_404';
import Page_500 from './Page_500/Page_500';
import Stock from './Stock/Stock';
import Filer from './Filer/Filer';
import { BrowserRouter as Router, Route, Switch, Redirect } from "react-router-dom";
import '../../templates/fedgehundui/global.css';
// file deepcode ignore no-mixed-spaces-and-tabskey: "value", 
// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and space"

class App extends Component {
  render() {

    const pathname = window.location.pathname;

    return (
      <Fragment>
        <Router>
          <Switch>
            <Redirect from="/:url*(/+)" to={pathname.slice(0, -1)} />
            <Route path="/" exact component={() => <Homepage />} />
            <Route path="/signup" exact component={() => <UserForm />} />
            <Route path="/signin" exact component={() => <Signin />} />
            <Route path="/contactus" exact component={() => <ContactUs />} />
            <Route path="/faq" exact component={() => <FAQ />} />
            <Route path="/stock/:securityName" render={(props) => <Stock {...props} />} />
            <Route path="/filer/:cik" render={(props) => <Filer {...props} />} />
            <Route path="/404" exact component={() => <Page_404 />} />
            <Route path="/500" exact component={() => <Page_500 />} />
            <Route component={() => <Page_404 />} />
          </Switch>
        </Router>
      </Fragment>
    );
  }
}

const ENV_VARIABLES = {
  ENVIRON: "prod",
  DEV_API_URL: "127.0.0.1:8000",
  PROD_API_URL: "mrktdb.eba-brufwk2z.us-west-2.elasticbeanstalk.com",
  // PROD_API_URL: "mrktdb.com",
};

let URL;
if (ENV_VARIABLES.ENVIRON == "dev")
  URL = ENV_VARIABLES.DEV_API_URL;
else
  URL = ENV_VARIABLES.PROD_API_URL;

export { URL };

ReactDOM.render(<App />, document.getElementById('app'));
