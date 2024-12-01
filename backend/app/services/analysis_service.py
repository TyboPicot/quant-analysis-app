import yfinance as yf
import talib

def moving_average_analysis(ticker, start_date, end_date):
    """Analyse basée sur les moyennes mobiles."""
    # Récupération des données depuis Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        return {"error": "No data found for the given ticker and date range"}

    # Calcul des moyennes mobiles
    data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
    data['SMA_200'] = talib.SMA(data['Close'], timeperiod=200)

    # Génération des signaux
    signals = []
    for i in range(1, len(data)):
        if data['SMA_50'][i] > data['SMA_200'][i] and data['SMA_50'][i-1] <= data['SMA_200'][i-1]:
            signals.append({"date": data.index[i].strftime("%Y-%m-%d"), "signal": "BUY"})
        elif data['SMA_50'][i] < data['SMA_200'][i] and data['SMA_50'][i-1] >= data['SMA_200'][i-1]:
            signals.append({"date": data.index[i].strftime("%Y-%m-%d"), "signal": "SELL"})

    # Retour des résultats
    return {
        "signals": signals,
        "cumulative_return": (data['Close'][-1] / data['Close'][0] - 1) * 100,
        "max_drawdown": min(data['Close'].pct_change().cumsum()) * 100,
        "sharpe_ratio": (data['Close'].pct_change().mean() / data['Close'].pct_change().std()) * (252 ** 0.5),
    }
