import React, { useEffect } from 'react';

import { TradingViewEmbed, widgetType } from "react-tradingview-embed";
function SymbolOverview(props) {
  const ticker = props.ticker;
  return (
    <div>
      <TradingViewEmbed
        widgetType={widgetType.SYMBOL_OVERVIEW}
        widgetConfig={{
          "symbols": [
            [ticker]
          ],
          "chartOnly": false,
          "width": "100%",
          "height": 400,
          "locale": "in",
          "colorTheme": "light",
          "gridLineColor": "rgba(255, 242, 204, 1)",
          "trendLineColor": "#2196F3",
          "fontColor": "#787B86",
          "underLineColor": "rgba(66, 66, 66, 1)",
          "isTransparent": false,
          "autosize": false,
          "container_id": "tradingview_8bf04"
        }}
      />

    </div>
  )
}


export default SymbolOverview;
