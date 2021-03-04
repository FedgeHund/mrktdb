import React, { Fragment, useState, useRef, useEffect } from 'react';
import axios from 'axios';

const securityNames = [];
const companyNames = [];
var all_items = [];

const SearchbarDropdown = () => {
	const ulRef = useRef();
	const inputRef = useRef();
	const [options, setOptions] = useState([]);


	const onInputChange = (event) => {
		if (document.getElementById('btnGroupDrop1').innerHTML === 'All Categories') {
			setOptions(
				all_items.filter((option) => option.includes(event.target.value.toUpperCase()))
			);
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Stocks') {
			setOptions(
				securityNames.filter((option) => option.includes(event.target.value.toUpperCase()))
			);
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Filers') {
			setOptions(
				companyNames.filter((option) => option.includes(event.target.value.toUpperCase()))
			);
		}
	}


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
		event.preventDefault();
		document.getElementById('btnGroupDrop1').innerHTML = event.target.innerHTML;
	}

	return (
		<form className="form-inline centered_form">
			<div className="lookup_form">

				<input className="form-control lookup_home" placeholder="Fund / Stock Lookup" onChange={onInputChange} ref={inputRef} />

				{results}

				<div className="btn-group search_btns" role="group" aria-label="Button group with nested dropdown">
					<div className="btn-group" role="group">
						<button id="btnGroupDrop1" type="button" className="dropdown-toggle search_type_button" data-bs-toggle="dropdown" aria-expanded="false" onClick={(e) => { e.preventDefault(); }}>
							All Categories
    					</button>
						<ul className="dropdown-menu" aria-labelledby="btnGroupDrop1">
							<li><a className="dropdown-item" href="#" onClick={changeCategory}>All Categories</a></li>
							<li><a className="dropdown-item" href="#" onClick={changeCategory}>Stocks</a></li>
							<li><a className="dropdown-item" href="#" onClick={changeCategory}>Filers</a></li>
						</ul>
					</div>

					<button id='search' type="submit" className="search"><i className="fas fa-search fa-rotate-90 search_icon"></i>Search</button>
				</div>

			</div>
		</form>

	);
};


function Hero_Section() {
	// file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
	const [searchData, setSearchData] = useState({ security_data: '', company_data: '' });

	const getData = async () => {
		let company_url = 'http://www.mrktdb.com/api/company';
		let security_url = 'http://www.mrktdb.com/api/security';

		const company_data = await axios.get(company_url);
		const security_data = await axios.get(security_url);

		setSearchData({ security_data: security_data.data, company_data: company_data.data });
	};

	useEffect(() => {
		getData();
	}, []);

	Object.values(searchData.security_data).map(security => securityNames.push(security.securityName));
	Object.values(searchData.company_data).map(company => companyNames.push(company.name.toUpperCase()));

	all_items = [...companyNames, ...securityNames];


	return (
		<Fragment>

			<div className="Background">
				<div className="contain">
					<div className="row">
						<div className="market_beating centered col-md-12">Find the next Market-Beating Portfolio</div>
					</div>
					<div className="">
						< SearchbarDropdown />
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