from splinter import Browser
from bs4 import BeautifulSoup as bs
import mission_to_mars.ipynb

app = Flask(__name__)

def init_browser():
  executable_path = {'executable_path': 'chromedriver.exe'}
  return Browser("chrome", **executable_path, headless=False)

def scrape():
  browser = init_browser()
  listings = {}

  url = "https://raleigh.craigslist.org/search/hhh?max_price=1500&availabilityMode=0"
  browser.visit(url)

  html = browser.html
  soup = bs(html, "html.parser")

  listings["headline"] = soup.find("a", class_="result-title").get_text()
  listings["price"] = soup.find("span", class_="result-price").get_text()
  listings["hood"] = soup.find("span", class_="result-hood").get_text()

  return listings