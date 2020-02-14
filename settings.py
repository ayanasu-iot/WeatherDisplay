import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
API_BASEURL = "https://api.openweathermap.org/data/2.5/weather?units=metric&id=1857766&appid="
ICON_BASEURL = "http://openweathermap.org/img/wn/"
