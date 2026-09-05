from langchain.tools import tool
import yfinance as yf
import requests
import os

# configurations
openweathermap_api_key = os.environ['OPENWEATHERMAP_API_KEY']
openweathermap_base_url = os.environ['OPENWEATHERMAP_BASE_URL']
joke_url = os.environ['JOKE_URL']

@tool
def get_weather(city: str) -> str:
    """
    Description: used to get the real time weather information of a city.
    Arguments:
        city: The name of exactly one city for which weather information is required.
    Returns: JSON formatted string which contains the real time weather information of a city.
    """

    # build the final url
    url = f"{openweathermap_base_url}?appid={openweathermap_api_key}&units=metric&q={city}"
    # print(f"sending request to url: {url}")
    # print(f"fetching weather information of city = {city}")

    # send the request and get the response
    response = requests.get(url)

    # check if the response is success
    if response.status_code == 200:
        # return the response body
        return response.text
    else:
        # error while sending the request
        return f"No weather information is avaialable for {city}"

@tool
def get_stock_info(symbol: str) -> str:
    """
    Description: returns the stock information of selected symbol.
    Arguments:
        symbol: symbol whose stock information is required.
    Returns: Stock price in $ of selected stock symbol.
    """
    # get the stock info
    # stock_info = yfinance.download(symbol)
    # return stock_info

    stock = yf.Ticker(symbol)
    price = stock.info['regularMarketPrice']
    return f"current price of {symbol} is ${price}"

@tool
def tell_me_a_joke():
    """
    Description: Returns a randome joke.
    """
    # send the request
    response = requests.get(joke_url)

    # check if the response is success
    if response.status_code == 200:
        # return the response body
        return response.text
    else:
        # error while sending the request
        return f"No joke available at the moment"

# test the weather tool
# print(get_weather.invoke({'city': 'pune'}))

# test the get_stock_info tool
# print(get_stock_info.invoke({'symbol': 'AAPL'}))

# test the joke tool
# print(tell_me_a_joke.invoke({}))