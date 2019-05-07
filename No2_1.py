import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
s=requests.get("https://www.ptt.cc/bbs/CareerPlan/M.1557205299.A.05C.html")
print(s)

