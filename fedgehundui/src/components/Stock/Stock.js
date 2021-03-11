import React, { Fragment, useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
import '../../../styles/security.css';

function Stock(props) {

    const [securityData, setSecurityData] = useState();

    let securityName = props.match.params.securityName;

    // let thePath = window.location.href;
    // let securityName = thePath.substring(thePath.lastIndexOf('/') + 1);

    const getSecurityData = async () => {
        let particular_security_url = 'http://www.mrktdb.com/api/security/' + securityName;

        const particular_security = await axios.get(particular_security_url);

        setSecurityData(particular_security.data);
    };

    useEffect(() => {
        getSecurityData();
    }, [securityName]);


    return (
        <Fragment>

            <Navbar />

            <div className="security_container ">
                <div className="security">
                    <div className="row">
                        <div className="security_heading col-6">{securityData ? securityData.securityName : null}</div>
                        <div className="security_toc col-5">TOC: {securityData ? securityData.titleOfClass : null}</div>
                    </div>
                    <div className="security_type">{securityData ? securityData.securityType : null}</div>
                </div>
            </div>

            <Footer />

        </Fragment >
    );
}

export default Stock;