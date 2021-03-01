import React, { Fragment } from 'react';
import '../../../styles/faq.css';
import Navbar from '../Layout/Navbar';
import Footer from '../Layout/Footer';

function FAQ() {

    const onFocus = (event) => {
        if(event.target.autocomplete)
        {
            event.target.autocomplete = "No";
        }
    };

  return (
    <Fragment>
    		  
        <Navbar />
            
            <h1>FAQ</h1>
        
        <Footer />

	</Fragment>
  );
}

export default FAQ;