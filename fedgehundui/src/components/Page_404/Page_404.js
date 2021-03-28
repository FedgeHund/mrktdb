import React, { Fragment } from 'react';
import { Link } from "react-router-dom";
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
import '../../../styles/page_404.css';

function Page_404() {

    return (
        <Fragment>

            <Navbar />

            <div className="container_404">
                <div className="_404">
                    <div className="row">
                        <div className="col-md-3">
                            <img className="left_404_img" src="../../../static/404/404_left.png" />
                        </div>
                        <div className="col-md-6">
                            <img className="middle_404_img" src="../../../static/404/404_middle.png" />
                        </div>
                        <div className="col-md-3">
                            <img className="right_404_img" src="../../../static/404/404_right.png" />
                        </div>
                    </div>
                    <div className="_404_content">
                        <div className="row">
                            <div className="col-md-12 _404_heading">404 : Page not found</div>
                        </div>
                        <div className="row">
                            <div className="col-md-9 _404_message">Not all those who wander are lost, but it seems you may have taken a wrong turn</div>
                        </div>
                        <div className="row">
                            <Link to={"/"}>
                                <button className="btn go_home_button shadow-sm" type="submit">
                                    <span className="go_home_text">Home</span>
                                </button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>

            <Footer />

        </Fragment >
    );
}

export default Page_404;