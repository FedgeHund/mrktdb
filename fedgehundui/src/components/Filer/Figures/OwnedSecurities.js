import React, { useState, useEffect } from 'react';
import OwnershipHistory from "./OwnershipHistory"
import '../../../../styles/Filer/OwnedSecurities.css';

function OwnedSecurities(props) {
    var cik = props.cik;
    var [oldCIK, setOldCIK] = useState(null);
    const [cusip, setCusip] = useState();
    if (cik !== oldCIK) {
        setOldCIK(cik);
    }

    const [data, setData] = useState([]);
    var URL = "http://www.mrktdb.com/api/allownedsecurities/?cik=" + oldCIK;

    async function fetchUrl() {
        fetch(URL, {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

        })
            .then(response => response.json())
            .then(data => setData(data));
    }

    useEffect(() => {
        fetchUrl();
    }, [oldCIK]);


    if (typeof data !== 'undefined' && data.length > 0) {
        var optionItems = data.map((d) =>
            <option className="allOwnedSecuritiesDropdown" key={d.cusip} value={d.cusip}>{d.securityName}</option>
        );
    }

    function handleCusip(event) {
        setCusip(event.target.value);
    }

    return (
        <div>
            <p>Select security:</p>
            <select
                value={cusip}
                name="filer"
                onChange={handleCusip}
                className="allOwnedSecuritiesDropdown mb-5"
                onSelect={handleCusip}
            >
                {optionItems}
            </select>
            {typeof cusip !== 'undefined' && cusip.length > 0 ?
                <OwnershipHistory cik={oldCIK} cusip={cusip} />
                : <img src="../../../../static/fedgehundui/eg.png" alt="EG" width="100%" />}
        </div>
    )
}

export default OwnedSecurities;