from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import time

def main():
	# variables for the urls to be scraped
  nasa_web = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
	jpl_web = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	nasa_twitter = "https://twitter.com/marswxreport?lang=en"
	facts_web = "https://space-facts.com/mars/"
	usgu_web = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

	# variables for commonly used actions
  executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)

  # --- MARS NEWS SCRAPE ---
  browser.visit(website)
	  # title of first article
	nasa_title = (bs(browser.html, 'html.parser').find('div', class_="content_title")).text.strip()
	  # first paragraph of first article
	nasa_para = (bs(browser.html, 'html.parser').find('div', class_="article_teaser_body")).text.strip()

  # --- JPL IMAGE SCRAPE ---
  browser.visit(jpl_web)
	browser.find_by_id("full_image").click()
	  # the browser tried to click too quickly so I had to add a sleep function
	time.sleep(5)
	browser.click_link_by_partial_text('more info')
    # creating variables to hold the full url
	jpl_end = (bs(browser.html, 'html.parser').find('img', class_='main_image')['src'])
	full_jpl = (jpl_web + jpl_end)

  # --- MARS TWITTER SCRAPE --
  browser.visit(nasa_twitter)
	tweet = (bs(browser.html, 'html.parser').find('div', class_="js-tweet-text-container")).text.strip()

  # --- MARS FACTS ---
  mars_facts = pd.DataFrame(pd.read_html(facts_web)[0])
	facts_html = mars_facts.to_html()

  # --- MARS HEMISPHERE PICTURES ---
  hemisphere_img = []

		# open the page
	browser.visit(usgu_web)
	links = browser.find_by_css("a.product-item h3")

		# loop through, grab the title and url and store it in a dictionary
	for link in range(len(links)):
		images= {}
		browser.find_by_css("a.product-item h3")[link].click()
		time.sleep(5)
		image_url = browser.find_link_by_text('Sample')
		images['img_url'] = image_url['href']
		browser.find_by_css('h2.title').text
		image_title = browser.find_by_css('h2.title').text
		images['title'] = image_title
		hemisphere_img.append({"title": image_title, "image_url": image_url})
		browser.back()

  mars_dictionary = {"nasa_title": nasa_title, "nasa_para": nasa_para, "full_jpl": full_jpl,
                    "tweet": tweet, "facts_html": facts_html, "hemisphere_img": hemisphere_img}
  browser.quit()

  #return a dictionary of all the information
  return mars_dictionary