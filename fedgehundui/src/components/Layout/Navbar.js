import React, { Fragment } from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { URL } from '../App.js';
import { Link } from 'react-router-dom';
import '../../../styles/navbar.css';
// file deepcode ignore no-mixed-spaces-and-tabs:

function Navbar() {
	const [navbar, setNavbar] = useState(false);
	const [firstname, setFirstname] = useState();
	const [errorMessage, seterrorMessage] = useState();

	const checkUser = async () => {
		await axios.get("http://" + URL + "/auth/user/", {
		},
			{
				headers: {
					"Content-Type": 'application/json'
				}
			}
		)
			.then(function (response) {
				if (response.status == 200) {
					console.log(response);
					setFirstname(response.data.first_name);
				}
				else {
					//window.location = "http://127.0.0.1:8000/signin/"
					console.log(response);
				}
			}).catch(error => {
				seterrorMessage(
					error
				)
			}
			)
	};

	useEffect(() => {
		checkUser();
	}, []);

	const getCookie = (name) => {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	const handleSubmit = async (e) => {

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

	const changeNavbarBackground = () => {
		if (window.scrollY >= 80) {
			setNavbar(true);
		} else {
			setNavbar(false);
		}
	}

	window.addEventListener('scroll', changeNavbarBackground);

	return (
		<Fragment>
			<nav className={navbar ? 'navbar active fixed-top shadow-sm' : 'navbar fixed-top'}>

				<Link to={"/signup"} className="MrktDB mr-auto ml-5" style={{ fontSize: "30px" }}>Stige Task Form</Link>

				{
					firstname ?
						<span>
							<Link to={"/signup"} className="signup_nav mr-5">Hi, {firstname}</Link>
							<Link to={"/signup"} onClick={handleSubmit} className="signup_nav mr-5">Sign out</Link>
						</span>
						:
						<span>
							<Link to={"/signup"} className="signup_nav mr-5">Sign Up</Link>
							<Link to={"/signin"} className="signup_nav mr-5">Sign In</Link>
						</span>
				}
			</nav>

		</Fragment>
	);
}

export default Navbar;
