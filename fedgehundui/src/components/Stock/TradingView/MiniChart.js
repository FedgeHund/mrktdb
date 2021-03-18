import React from 'react';
import { TradingViewEmbed, widgetType } from "react-tradingview-embed";


function MiniChart(props) {
    const ticker = props.ticker;

    return (
        <div>
            <TradingViewEmbed
                widgetType={widgetType.MINI_CHART}
                widgetConfig={{
                    "symbol": ticker,
                    "width": "100%",
                    "height": 220,
                    "locale": "in",
                    "dateRange": "12M",
                    "colorTheme": "light",
                    "trendLineColor": "#37a6ef",
                    "underLineColor": "#E3F2FD",
                    "isTransparent": true,
                    "autosize": false,
                }}
            />

        </div>
    )
}

export default MiniChart;
