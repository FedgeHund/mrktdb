import React, { Fragment } from 'react';
import '../../../styles/homepage.css';
import Navbar from '../Layout/Navbar';
import Hero_Section from './Sections/Hero_Section';
import Inside_DB from './Sections/Inside_DB';
import Know_More from './Sections/Know_More';
import What_is_13f from './Sections/What_is_13f';
import Popular_Portfolios from "./Sections/Popular_Portfolios";
import Get_Started from "./Sections/Get_Started";
import Footer from '../Layout/Footer';

function Homepage() {
  // file deepcode ignore no-mixed-spaces-and-tabs: "Tabs and spaces"
  return (
    <Fragment>

      <Navbar />

      <Hero_Section />

      <Inside_DB />

      <Know_More />

      <What_is_13f />

      <Popular_Portfolios />

      <Get_Started />

      <Footer />

    </Fragment>
  );
}

export default Homepage;