import React, { useEffect } from 'react';
import '../../../../styles/security.css';

function CompanyProfile(props) {
  const ticker = props.ticker;

  useEffect(() => {
    // Company Profile Widget
    const companyProfile = document.createElement('script');
    companyProfile.src = 'https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js'
    companyProfile.async = true;
    companyProfile.innerHTML = JSON.stringify({
      "symbol": ticker,
      "width": "100%",
      "height": 560,
      "colorTheme": "light",
      "isTransparent": true,
      "locale": "in"
    })
    document.getElementById("CompanyProfile").appendChild(companyProfile);

  }, [ticker]);

  return (
    <div>
      <div id="CompanyProfile"></div>
    </div>
  )
}



export default CompanyProfile;
