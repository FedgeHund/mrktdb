import React, { Fragment, useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { withRouter } from 'react-router';
import { BrowserRouter as Router, Route, Switch, Link, useHistory } from "react-router-dom";

var securityNames = [{ securityName: "APPLE INC", ticker: "AAPL" }, { securityName: "AMAZON COM INC", ticker: "AMZN" }, { securityName: "MICROSOFT CORP.", ticker: "MSFT" }, { securityName: "FACEBOOK INC", ticker: "FB" }, { securityName: "TESLA INC", ticker: "TSLA" }];
var companyNames = [{ name: "BERKSHIRE HATHAWAY INC", cik: "0001067983" }, { name: "TIGER GLOBAL MANAGEMENT LLC", cik: "0001167483" }, { name: "BRIDGEWATER ASSOCIATES, LP", cik: "0001350694" }, { name: "MAN GROUP PLC", cik: "0001637460" }, { name: "RENAISSANCE TECHNOLOGIES LLC", cik: "0001037389" }, { name: "BLACKROCK INC.", cik: "0001364742" }];
var all_items = [];
//var default_items = ["BERKSHIRE HATHAWAY INC", "BLACKROCK INC.", "AMAZON COM INC", "WAL MART STORES INC", "COCA COLA CO", "APPLE INC", "BRIDGEWATER ASSOCIATES, LP"];


const SearchbarDropdown = () => {

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
	}, []);

	const ulRef = useRef();
	const inputRef = useRef();
	const [options, setOptions] = useState([]);
	const history = useHistory();
	let results;

	if (options.length) {
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
										search_db(inputRef.current.value);
									}}
									className="list-group-item list-group-item-action"
								>
									<div className="ticker">{option.ticker}&nbsp;&nbsp;
									<span className="stock_name">{option.securityName}</span>
									</div>
								</button>
							}
							{ option.cik &&
								<button
									type="button"
									key={index}
									onClick={(e) => {
										inputRef.current.value = option.cik;
										var type_cik = parseInt(option.cik)
										search_db(inputRef.current.value, type_cik);
									}}
									className="list-group-item list-group-item-action"
								>
									<div className="filer_name">{option.name.toUpperCase()}&nbsp;&nbsp;&nbsp;
									<span className="cik">CIK : {option.cik}</span>
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
				{/* <button type="button" className="list-group-item list-group-item-action no_results" disabled>No results found!</button> */}
			</ul>
		)
	}


	const onInputChange = (event) => {
		var toSearch = event.target.value;

		if (toSearch === '') {
			toSearch = 'a';
		}

		if (document.getElementById('btnGroupDrop1').innerHTML === 'All Categories') {
			let security_url = `http://www.mrktdb.com/api/security/?search=${toSearch}`;

			async function getSecurityData() {
				const stocks = await fetch(security_url).then(response => response.json());
				return stocks;
			}

			getSecurityData().then(stocks => {
				securityNames = Object.values(stocks).map(stock => stock);
			});

			let company_url = `http://www.mrktdb.com/api/company/?search=${toSearch}`;

			async function getFilersData() {
				const companies = await fetch(company_url).then(response => response.json());
				return companies;
			}

			getFilersData().then(companies => {
				companyNames = Object.values(companies).map(company => company);
			});

			all_items = [...companyNames, ...securityNames];

			function checkType(option) {
				if (option.ticker) {
					return (option.ticker.startsWith(event.target.value.toUpperCase()) || option.securityName.startsWith(event.target.value.toUpperCase()));
				} else if (option.cik) {
					return (option.name.toUpperCase().startsWith(event.target.value.toUpperCase()));
				}
			}

			setOptions(
				all_items.filter(checkType)
			);
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Stocks') {
			let security_url = `http://www.mrktdb.com/api/security/?search=${toSearch}`;

			async function getSecurityData() {
				const stocks = await fetch(security_url).then(response => response.json());
				return stocks;
			}

			getSecurityData().then(stocks => {
				securityNames = Object.values(stocks).map(stock => stock);
			});

			function tickerOrName(option) {
				return (option.ticker.startsWith(event.target.value.toUpperCase()) || option.securityName.startsWith(event.target.value.toUpperCase()));
			}

			setOptions(
				securityNames.filter(tickerOrName)
			);
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Filers') {
			let company_url = `http://www.mrktdb.com/api/company/?search=${toSearch}`;

			async function getFilersData() {
				const companies = await fetch(company_url).then(response => response.json());
				return companies;
			}

			getFilersData().then(companies => {
				companyNames = Object.values(companies).map(company => company);
			});

			setOptions(
				companyNames.filter((option) => option.name.toUpperCase().startsWith(event.target.value.toUpperCase()))
			);
		}
	}


	const changeCategory = (event) => {
		event.preventDefault();
		document.getElementById('btnGroupDrop1').innerHTML = event.target.innerHTML;
	}


	const search_db = (curr_value, type_cik) => {
		if (document.getElementById('btnGroupDrop1').innerHTML === 'All Categories') {
			if (Number.isInteger(type_cik)) {
				let company_url = `http://www.mrktdb.com/api/company/?search=${curr_value}`;

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
			else {
				let stock_url = `http://www.mrktdb.com/api/security/?search=${curr_value}`;

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
		}
		else if (document.getElementById('btnGroupDrop1').innerHTML === 'Stocks') {
			let stock_url = `http://www.mrktdb.com/api/security/?search=${curr_value}`;

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
			let company_url = `http://www.mrktdb.com/api/company/?search=${curr_value}`;

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

export default withRouter(Hero_Section);