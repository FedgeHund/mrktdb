import React, { useEffect } from 'react';
import '../../../../styles/security.css';

function SymbolInfo(props) {
  const ticker = props.ticker;

  useEffect(() => {
    // Symbol Info Widget
    const symbolInfo = document.createElement('script');
    symbolInfo.src = 'https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js'
    symbolInfo.async = true;
    symbolInfo.innerHTML = JSON.stringify({
      "symbol": ticker,
      "width": "100%",
      "locale": "in",
      "colorTheme": "light",
      "isTransparent": true
    })
    document.getElementById("SymbolInfo").appendChild(symbolInfo);

  }, [ticker]);

  return (
    <div>
      <div id="SymbolInfo"></div>
    </div>
  )
}



export default SymbolInfo;
