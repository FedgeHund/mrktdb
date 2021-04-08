import React, { useEffect } from 'react';
import '../../../../styles/security.css';

function FundamentalData(props) {
  const ticker = props.ticker;

  useEffect(() => {
    // Fundamental Data Widget
    const fundamentalData = document.createElement('script');
    fundamentalData.src = 'https://s3.tradingview.com/external-embedding/embed-widget-financials.js'
    fundamentalData.async = true;
    fundamentalData.innerHTML = JSON.stringify({
      "symbol": ticker,
      "colorTheme": "light",
      "isTransparent": false,
      "largeChartUrl": "",
      "displayMode": "regular",
      "width": "100%",
      "height": 830,
      "locale": "in"
    })
    document.getElementById("FundamentalData").appendChild(fundamentalData);

  }, [ticker]);

  return (
    <div>
      <div id="FundamentalData"></div>
    </div>
  )
}



export default FundamentalData;
