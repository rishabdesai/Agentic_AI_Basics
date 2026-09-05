"""
.env file content

MODEL_PROVIDER=ollama
MODEL=llama3.2:3b
OPENWEATHERMAP_API_KEY=<<YOUR_OPENWEATHERMAP_API_KEY>>
OPENWEATHERMAP_BASE_URL=https://api.openweathermap.org/data/2.5/weather
JOKE_URL=https://official-joke-api.appspot.com/random_joke
"""


from langchain.tools import tool
from dotenv import load_dotenv
import requests
import os


# load configuration from .env file
load_dotenv()

# get the configurations
model = os.environ['MODEL']
model_provider = os.environ['MODEL_PROVIDER']
openweathermap_api_key = os.environ['OPENWEATHERMAP_API_KEY']
openweathermap_base_url = os.environ['OPENWEATHERMAP_BASE_URL']

@tool
def get_weather(city: str) -> str:
    """
    Description: used to get the real time weather information of a city.
    Arguments:
        city: the city of which weather information is required.
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


#test the weather tool
print(get_weather.invoke({'city':'pune'}))