import React, { Component, Fragment } from 'react';
import '../../../styles/signup/styles.css';
import axios from 'axios';
import { URL } from '../App.js';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
import { getCookie } from '../Helpers/getCookie';
import { checkUser } from '../Helpers/checkUser';
// file deepcode ignore no-mixed-spaces-and-tabs:

export class Success extends Component {
	state = {
		firstname: ''
	}

	constructor() {
		super();
	}

	componentDidMount() {
		checkUser();
	}


	handleSubmit = async (e) => {

		var csrftoken = getCookie('csrftoken');

		await axios.post("http://" + URL + "/auth/logout/", {
		},
			{
				headers: {
					"Content-Type": 'application/json',
					'X-CSRFToken': csrftoken
				}
			}
		)
			.then(function (response) {
				if (response.status == 200) {
					console.log(response);
				}
				else {
					//window.location = "http://127.0.0.1:8000/signin/"
					console.log(response);
				}
			}.bind(this))

		window.location = "http://" + URL + "/signin/"
	};


	render() {

		return (
			<Fragment>
				<Navbar />
				<div className="main_div">
					{
						this.state.first_name ?
							<div>
								<div className="row">
									<div className="success_hello col-md-10 offset-md-1">Hi, {this.state.first_name}<br />{this.state.email}</div>
									<br />
									<div className="success_content1 col-md-10 offset-md-1">Congratulations on successfully signing up!</div>
								</div>
								<div className="row mt-5">
									<button className="btn btn-secondary shadow-sm col-sm-6 offset-sm-3 col-xs-8 offset-xs-2 col-8 offset-2 submit-btn mt-4" type="submit" onClick={this.handleSubmit}>
										<span>Sign out</span>
									</button>
								</div>
							</div>
							: <div className="success_hello col-md-10 offset-md-1">Successfully logged out!</div>
					}

				</div>
				<Footer />
			</Fragment>
		)
	}
}

export default Success;
