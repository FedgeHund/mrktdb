import React, { useEffect } from 'react';
import '../../../../styles/security.css';

function TechnicalAnalysis(props) {
  const ticker = props.ticker;

  useEffect(() => {
    // Technical Analysis Widget
    const technicalAnalysis = document.createElement('script');
    technicalAnalysis.src = 'https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js'
    technicalAnalysis.async = true;
    technicalAnalysis.innerHTML = JSON.stringify({
      "interval": "1m",
      "width": "100%",
      "isTransparent": true,
      "height": 560,
      "symbol": ticker,
      "showIntervalTabs": true,
      "locale": "in",
      "colorTheme": "light"
    })
    document.getElementById("TechnicalAnalysis").appendChild(technicalAnalysis);

  }, [ticker]);

  return (
    <div>
      <div id="TechnicalAnalysis"></div>
    </div>
  )
}



export default TechnicalAnalysis;
