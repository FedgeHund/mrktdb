import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Signin from './Signin/Signin';
import UserForm from './Signup/UserForm';
import Page_404 from './Page_404/Page_404';
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
            <Route path="/signup" exact component={() => <UserForm />} />
            <Route path="/signin" exact component={() => <Signin />} />
            <Route path="/404" exact component={() => <Page_404 />} />
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
};

let URL;
if (ENV_VARIABLES.ENVIRON == "dev")
  URL = ENV_VARIABLES.DEV_API_URL;
else
  URL = ENV_VARIABLES.PROD_API_URL;

export { URL };

ReactDOM.render(<App />, document.getElementById('app'));
