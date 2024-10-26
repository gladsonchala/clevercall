import yfinance as yf
from langchain.tools import tool

@tool
def get_current_stock_price(symbol: str) -> float:
    """Get the current stock price for a given symbol."""
    try:
        stock = yf.Ticker(symbol)
        current_price = stock.info.get("regularMarketPrice", stock.info.get("currentPrice"))
        return current_price if current_price else None
    except Exception as e:
        print(f"Error fetching current price for {symbol}: {e}")
        return None

@tool
def get_company_profile(symbol: str) -> dict:
    """Get the company profile for a given symbol."""
    try:
        stock = yf.Ticker(symbol)
        profile = {
            "name": stock.info.get("longName"),
            "sector": stock.info.get("sector"),
            "industry": stock.info.get("industry"),
            "description": stock.info.get("longBusinessSummary"),
        }
        return profile
    except Exception as e:
        print(f"Error fetching profile for {symbol}: {e}")
        return {}

@tool
def get_analyst_recommendations(symbol: str) -> list:
    """Get analyst recommendations for a given stock symbol."""
    try:
        stock = yf.Ticker(symbol)
        recommendations = stock.recommendations.to_dict("records") if stock.recommendations is not None else []
        return recommendations
    except Exception as e:
        print(f"Error fetching recommendations for {symbol}: {e}")
        return []
