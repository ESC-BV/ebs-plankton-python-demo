import os
import time
import requests
from typing import Tuple
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()

red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
reset = "\u001b[0m"
white = "\u001b[37m"
bold = "\u001b[1m"
dim = "\u001b[2m"

plankton_base_url = os.getenv("PLANKTON_API_BASE_URL")
plankton_api_key = os.getenv("PLANKTON_API_KEY")

headers = {
    'Content-Type': 'text/json; charset=utf-8', 
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3)',
    'Pragma': 'no-cache',
}

def fire_post_request(url: str, data: str, timeout: int = 30) -> Tuple[int, float, str | None]:
    headers["X-Plankton-ApiKey"]  = plankton_api_key
    try:
        start_time = time.time()
        response = requests.post(plankton_base_url + url, data = data, timeout = timeout, headers = headers, verify=False)
        end_time = time.time()
        time_taken = end_time - start_time
        return (response.status_code, time_taken, response.text)
    except Exception:
        return (0, 0, None)
    
def fire_put_request(url: str, data: str, timeout: int = 30) -> Tuple[int, float, str | None]:
    headers["X-Plankton-ApiKey"]  = plankton_api_key
    #try:
    start_time = time.time()
    response = requests.put(plankton_base_url + url, data = data, timeout = timeout, headers = headers, verify=False)
    end_time = time.time()
    time_taken = end_time - start_time
    return (response.status_code, time_taken, response.text)
    #except Exception:
    #    return (0, 0, None)

def fire_get_request(url: str, timeout: int = 30) -> Tuple[int, float, str | None]:
    headers["X-Plankton-ApiKey"]  = plankton_api_key
    try:
        start_time = time.time()
        response = requests.get(plankton_base_url + url, timeout = timeout, headers = headers, verify=False)
        end_time = time.time()
        time_taken = end_time - start_time
        return (response.status_code, time_taken, response.text)
    except Exception:
        return (0, 0, None)

def fire_delete_request(url: str, timeout: int = 30) -> Tuple[int, float, str | None]:
    headers["X-Plankton-ApiKey"]  = plankton_api_key
    try:
        start_time = time.time()
        response = requests.delete(plankton_base_url + url, timeout = timeout, headers = headers, verify=False)
        end_time = time.time()
        time_taken = end_time - start_time
        return (response.status_code, time_taken, response.text)
    except Exception:
        return (0, 0, None)

