import React, { Fragment } from 'react';
import {useState, useEffect} from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'; 
import '../../../styles/signup/styles.scss';

import Navbar from '../Layout/Navbar';

function Homepage() {

  return (
    <Fragment>
           <Navbar />
	</Fragment>
  );
}

export default Homepage;