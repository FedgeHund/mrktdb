import React, { Fragment } from 'react';
import { Link } from "react-router-dom";
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
import '../../../styles/page_404.css';

function Page_500() {

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
                            <img className="middle_404_img" src="../../../static/404/500_middle.png" />
                        </div>
                        <div className="col-md-3">
                            <img className="right_404_img" src="../../../static/404/404_right.png" />
                        </div>
                    </div>
                    <div className="_404_content">
                        <div className="row">
                            <div className="col-md-12 _404_heading">500 : Internal server error</div>
                        </div>
                        <div className="row">
                            <div className="col-md-9 _404_message">It's not you, it's us! Something went wrong on our end. Please try again</div>
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

export default Page_500;