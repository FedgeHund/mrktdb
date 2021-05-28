import React, { useState, useEffect } from 'react';
import OwnershipHistory from "./OwnershipHistory"

// http://www.mrktdb.com/api/ownershiphistory/?cik=0001037389&cusip=70159Q104
function OwnedSecurities(props) {
    var cik = props.cik;
    var [oldCIK, setOldCIK] = useState(null);
    const [cusip, setCusip] = useState();
    if (cik !== oldCIK) {
        setOldCIK(cik)
    }

    const [data, setData] = useState([]);
    var URL = "http://www.mrktdb.com/api/allownedsecurities/?cik=" + oldCIK;
    console.log(URL);

    async function fetchUrl() {
        // console.log(cik)
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


    // console.log(data);
    if (typeof data !== 'undefined' && data.length > 0) {
        // var securitiesData = [...data];
        var optionItems = data.map((d) =>
            <option key={d.cusip} value={d.cusip}>{d.securityName}</option>
        );
    }

    function handleCusip(event) {
        setCusip(event.target.value);
    }

    // {data.map(d => <div>{d.securityName}</div>)}
    return (
        <div>
            <select
                value={cusip}
                name="filer"
                onChange={handleCusip}
            >
                {optionItems}
            </select>
            <p>You selected {cusip}</p>
            {typeof cusip !== 'undefined' && cusip.length > 0 ?
                <OwnershipHistory cik={oldCIK} cusip={cusip} />
                : undefined}
        </div>
    )
}

export default OwnedSecurities;