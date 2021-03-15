import React, { Fragment, useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';
import '../../../styles/filer.css';

function Filer(props) {

    const [filerData, setFilerData] = useState();

    let cik = props.match.params.cik;

    // let thePath = window.location.href;
    // let securityName = thePath.substring(thePath.lastIndexOf('/') + 1);

    const getFilerData = async () => {
        let particular_filer_url = 'http://www.mrktdb.com/api/company/' + cik + '/';

        const particular_filer = await axios.get(particular_filer_url);

        setFilerData(particular_filer.data);
        console.log(filerData);
    };

    useEffect(() => {
        getFilerData();
    }, [cik]);


    return (
        <Fragment>

            <Navbar />

            <div className="filer_container ">
                <div className="filer">
                    <div className="row">
                        <div className="filer_heading col-6">{filerData ? filerData.name : null}</div>
                        <div className="filer_cik col-5">CIK: {filerData ? filerData.cik : null}</div>
                    </div>
                    <div className="filer_address">{filerData ? filerData.address : null}</div>
                </div>
            </div>

            <Footer />

        </Fragment >
    );
}

export default Filer;