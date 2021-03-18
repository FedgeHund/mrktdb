import React from 'react';
import { TradingViewEmbed, widgetType } from "react-tradingview-embed";


function AdvancedChart(props) {
    const ticker = props.ticker;

    return (
        <div>
            <TradingViewEmbed
                widgetType={widgetType.ADVANCED_CHART}
                widgetConfig={{
                    "width": "97%",
                    "height": 610,
                    "symbol": ticker,
                    "interval": "D",
                    "timezone": "Etc/UTC",
                    "theme": "light",
                    "style": "1",
                    "locale": "in",
                    "toolbar_bg": "#f1f3f6",
                    "enable_publishing": false,
                    "allow_symbol_change": true,
                    "container_id": "tradingview_50709"
                }}
            />

        </div>
    )
}

export default AdvancedChart;
