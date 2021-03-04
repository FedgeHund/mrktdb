import React, { Fragment, useState, useRef, useEffect } from 'react';

const securityNames = [];

const SearchbarDropdown = (props) => {
	const { options, onInputChange } = props;
	const ulRef = useRef();
	const inputRef = useRef();

	useEffect(() => {
		inputRef.current.addEventListener('click', (event) => {
			event.stopPropagation();
			ulRef.current.style.display = 'flex';
			onInputChange(event);
		});

		document.addEventListener('click', (event) => {
			ulRef.current.style.display = 'none';
		});

		document.getElementById('results').style.display = 'none';


	}, []);

	let results;

	if (options.length) {
		results = (
			<ul id="results" className="list-group" ref={ulRef}>
				{options.slice(0, 7).map((option, index) => {
					return (
						<button
							type="button"
							key={index}
							onClick={(e) => {
								inputRef.current.value = option;
							}}
							className="list-group-item list-group-item-action"
						>
							{option}
						</button>
					);
				})}
			</ul>
		)
	} else {
		results = (
			<ul id="results" className="list-group" ref={ulRef}>
				<button type="button" className="list-group-item list-group-item-action no_results" disabled>No results found!</button>
			</ul>
		)
	}

	const changeCategory = (event) => {
		document.getElementById('btnGroupDrop1').innerHTML = event.target.innerHTML;
	}

	return (
		<form className="form-inline centered_form">
			<div className="lookup_form">

				<input className="form-control lookup_home" placeholder="Fund / Stock Lookup" onChange={onInputChange} ref={inputRef} />

				{results}

				<div className="btn-group search_btns" role="group" aria-label="Button group with nested dropdown">
					<div className="btn-group" role="group">
						<button id="btnGroupDrop1" type="button" className="dropdown-toggle search_type_button" data-bs-toggle="dropdown" aria-expanded="false">
							All Categories
    					</button>
						<ul className="dropdown-menu" aria-labelledby="btnGroupDrop1">
							<li><a className="dropdown-item" href="#" onClick={changeCategory}>All Categories</a></li>
							<li><a className="dropdown-item" href="#" onClick={changeCategory}>Stocks</a></li>
							<li><a className="dropdown-item" href="#" onClick={changeCategory}>Filers</a></li>
						</ul>
					</div>

					<button id='search' type="button" className="search"><i className="fas fa-search fa-rotate-90 search_icon"></i>Search</button>
				</div>


			</div>
		</form>

	);
};


function Search() {
	const [options, setOptions] = useState([]);

	const onInputChange = (event) => {
		setOptions(
			securityNames.filter((option) => option.includes(event.target.value.toUpperCase()))
		);
	};

	return (
		<SearchbarDropdown options={options} onInputChange={onInputChange} />
	);
}

function Hero_Section() {
	// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
	const [securityData, setSecurityData] = useState([]);

	async function getSecurityNames() {
		fetch('http://www.mrktdb.com/api/security', {
			headers: {
				'Content-Type': 'application/json',
				'Accept': 'application/json'
			}
		})
			.then(response => response.json())
			.then(data => setSecurityData(data));
	}

	useEffect(() => {
		getSecurityNames();
	}, []);

	securityData.map(d => securityNames.push(d.securityName));


	return (
		<Fragment>

			<div className="Background">
				<div className="contain">
					<div className="row">
						<div className="market_beating centered col-md-12">Find the next Market-Beating Portfolio</div>
					</div>
					<div className="">
						< Search />
					</div>
					<div className="row">
						<div className="col-xs-10 carousel_text col-md-7">MrktDB provides exclusive investment insights by giving you a sneak peek into the portfolio of world's most successful investors. Market Research is expensive, don't let that hold you back!</div>
					</div>
					<div className="row">
						<a href="" className="centered_carousel_link col-xs-12">Find out what the smartest investors are buying</a>
					</div>
				</div>
			</div>

		</Fragment >
	);
}

export default Hero_Section;