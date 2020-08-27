import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Navbar from './Layout/Navbar';
import Signin from './Layout/Signin';

class App extends Component {
  render() {
    return (
    	<Fragment>
      		<Navbar />
      		<Signin />
      	</Fragment>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));