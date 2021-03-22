import React, { Fragment, useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { withRouter } from 'react-router'
import { BrowserRouter as Router, Route, Switch, Link, useHistory } from "react-router-dom";

// var securityNames = ["APPLE INC", "AMAZON COM INC", "MICROSOFT CORP.", "FACEBOOK INC", "TESLA INC"];
var securityNames = []
var companyNames = ["BERKSHIRE HATHAWAY INC", "TIGER GLOBAL MANAGEMENT LLC", "AMAZON COM INC", "BRIDGEWATER ASSOCIATES, LP", "MAN GROUP PLC", "RENAISSANCE TECHNOLOGIES LLC", "BLACKROCK INC."];
var all_items = [];
//var default_items = ["BERKSHIRE HATHAWAY INC", "BLACKROCK INC.", "AMAZON COM INC", "WAL MART STORES INC", "COCA COLA CO", "APPLE INC", "BRIDGEWATER ASSOCIATES, LP"];


const SearchbarDropdown = (props) => {

	useEffect(() => {
		inputRef.current.addEventListener('click', (event) => {
			event.stopPropagation();
			ulRef.current.style.display = 'flex';
			onInputChange(event);
		});

		document.addEventListener('click', (event) => {
			if (ulRef.current != null) {
				ulRef.current.style.display = 'none';
			}
		});

		document.getElementById('results').style.display = 'none';
	}, [options]);


	const searchData = { props };
	const ulRef = useRef();
	const inputRef = useRef();
	const [options, setOptions] = useState([]);
	const history = useHistory();
	let results;

	if (options.length) {
		console.log(options);
		results = (
			<ul id="results" className="list-group" ref={ulRef}>
				{options.slice(0, 7).map((option, index) => {
					return (
						<a key={index}>
							{ option.ticker &&
								<button
									type="button"
									key={index}
									onClick={(e) => {
										inputRef.current.value = option.ticker;
										search_db(inputRef.current.value, searchData);
									}}
									className="list-group-item list-group-item-action"
								>
									<div className="ticker">{option.ticker}&nbsp;&nbsp;
									<span className="stock_name">{option.securityName}</span>
									</div>
								</button>
							}
						</a>
					);
				})
				}
			</ul >
		)
	} else {
		results = (
			<ul id="results" className="list-group" ref={ulRef}>
				<button type="button" className="list-group-item list-group-item-action no_results" disabled>No results found!</button>
			</ul>
		)
	}


	const onInputChange = (event) => {
		if (document.getElementById('btnGroupDrop1').innerHTML === 'All Categories') {
			setOptions(
				all_items.filter((option) => option.includes(event.target.value.toUpperCase()))
			);
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Stocks') {
			let security_url = `http://127.0.0.1:8000/api/security/?search=${event.target.value}`;

			async function getSecurityData() {
				const stocks = await fetch(security_url).then(response => response.json());
				return stocks;
			}

			getSecurityData().then(stocks => {
				securityNames = Object.values(stocks).map(stock => stock);
				//console.log(securityNames);
			});

			setOptions(
				securityNames.filter((option) => option.ticker.startsWith(event.target.value.toUpperCase()))
			);
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Filers') {
			let company_url = `http://127.0.0.1:8000/api/company/?search=${event.target.value}`;

			async function getFilersData() {
				const companies = await fetch(company_url).then(response => response.json());
				return companies;
			}

			getFilersData().then(companies => {
				companyNames = Object.values(companies).map(company => company.name.toUpperCase());
			});

			setOptions(
				companyNames.filter((option) => option.startsWith(event.target.value.toUpperCase()))
			);
		}
	}


	const changeCategory = (event) => {
		event.preventDefault();
		document.getElementById('btnGroupDrop1').innerHTML = event.target.innerHTML;
	}


	const search_db = (curr_value, searchData) => {
		if (document.getElementById('btnGroupDrop1').innerHTML === 'All Categories') {
			if (Object.values(props.searchData.company_data).filter(company => company.name.toUpperCase() === curr_value.toUpperCase()).length != 0) {
				const cik = Object.values(props.searchData.company_data).filter(company => company.name.toUpperCase() === curr_value.toUpperCase()).map((company) => company.cik);
				history.push(
					{
						pathname: `/filer/${cik[0]}`,
						state: { cik: cik[0] },
					}
				);
			}
			else {
				const sec_name = Object.values(props.searchData.security_data).filter(security => security.securityName.toUpperCase() === curr_value.toUpperCase()).map((security) => security.securityName);
				const ticker = Object.values(props.searchData.security_data).filter(security => security.securityName.toUpperCase() === curr_value.toUpperCase()).map((security) => security.ticker);
				history.push(
					{
						pathname: `/stock/${sec_name[0]} `,
						state: { SecName: sec_name[0], ticker: ticker[0] },
					}
				);
			}
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Stocks') {
			let stock_url = `http://127.0.0.1:8000/api/security/?search=${curr_value}`;

			async function getStockData() {
				const stock = fetch(stock_url).then(response => response.json());
				return stock;
			}

			getStockData().then(stock => {
				const sec_name = stock[0].securityName;
				const ticker = stock[0].ticker;

				history.push(
					{
						pathname: `/stock/${ticker} `,
						state: { SecName: sec_name, ticker: ticker },
					}
				);
			});
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Filers') {
			let company_url = `http://127.0.0.1:8000/api/company/?search=${curr_value}`;

			async function getFilersData() {
				const company = fetch(company_url).then(response => response.json());
				return company;
			}

			getFilersData().then(company => {
				const cik = company[0].cik;

				history.push(
					{
						pathname: `/filer/${cik} `,
						state: { cik: cik },
					}
				);
			});

		}
	}


	return (
		<form className="form-inline centered_form" onSubmit={search_db}>
			<div className="lookup_form">

				<input className="form-control lookup_home" placeholder="Fund / Stock Lookup" onChange={onInputChange} ref={inputRef} />

				{results}

				<div className="btn-group search_btns" role="group" aria-label="Button group with nested dropdown">
					<div className="btn-group" role="group">
						<button id="btnGroupDrop1" type="button" className="dropdown-toggle search_type_button" data-bs-toggle="dropdown" aria-expanded="false" onClick={(e) => { e.preventDefault(); }}>
							Stocks
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

	// const getData = async () => {
	// 	let company_url = 'http://127.0.0.1:8000/api/company/?search=';
	// 	let security_url = 'http://127.0.0.1:8000/api/security/?search=';

	// 	const company_data = await axios.get(company_url);
	// 	const security_data = await axios.get(security_url);

	// 	setSearchData({ security_data: security_data.data, company_data: company_data.data });
	// };

	// useEffect(() => {
	// 	getData();
	// }, []);

	// Object.values(searchData.security_data).map(security => securityNames.push(security.securityName));
	// Object.values(searchData.company_data).map(company => companyNames.push(company.name.toUpperCase()));

	// console.log(securityNames);
	// console.log(companyNames);

	// all_items = [...companyNames, ...securityNames];

	return (
		<Fragment>

			<div className="Background">
				<div className="contain">
					<div className="row">
						<div className="market_beating centered col-md-12">Find the next Market-Beating Portfolio</div>
					</div>
					<div className="">
						< SearchbarDropdown searchData={searchData} />
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

export default withRouter(Hero_Section);