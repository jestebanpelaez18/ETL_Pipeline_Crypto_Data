# Require libraries
import pandas as pd
import numpy as np
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format='%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./log_progress","a") as f:
        f.write(timestamp + ":" + message + '\n')

def extract(url):
    ''' This function aims to extract the required
    information from the CoinGecko and save it to a data frame. The
    function returns the data frame for further processing. '''
    # url = " https://api.coingecko.com/api/v3/ping?x_cg_demo_api_key=CG-MbEY8jPE4gh6VQGrJrCCF5st"
    data = requests.get(url)
    print(data.status_code)

extract("https://api.coingecko.com/api/v3/ping?x_cg_demo_api_key=CG-MbEY8jPE4gh6VQGrJrCCF5st")



