import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Navbar from './Layout/Navbar';
import Signin from './Layout/Signin';
import UserForm from './Signup/UserForm';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

class App extends Component {
  render() {
    return (
    	<Fragment>
      		<Router>
	      		<Switch>
		          	<Route path="/" exact component={() => <UserForm />} />
		          	<Route path="/signin" exact component={() => <Signin />} />
		        </Switch>     		
      		</Router>
      	</Fragment>
    );
  }
}


ReactDOM.render(<App />, document.getElementById('app'));