import React, { Fragment, useEffect } from 'react';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';

function Stock() {

    const [isLoading, setIsLoading] = useState(true);
    const [data, setData] = useState();

    useEffect(() => {
        fetch(`http://www.mrktdb.com/api/security/${securityName}`, {})
            .then((res) => res.json())
            .then((response) => {
                setData(response);
                setIsLoading(false);
                console.log(`http://www.mrktdb.com/api/security/${securityName}`);
                console.log(data);
            })
            .catch((error) => console.log(error));
    }, [securityName]);

    return (
        <Fragment>

            <Navbar />



            <Footer />

        </Fragment>
    );
}

export default Stock;