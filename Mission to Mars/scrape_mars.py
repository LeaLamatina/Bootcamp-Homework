from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import time

def main():
	nasa_web = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
	jpl_web = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	nasa_twitter = "https://twitter.com/marswxreport?lang=en"
	facts_web = "https://space-facts.com/mars/"
	usgu_web = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

	list_of_stuff =[nasa_web]

	# Initiate headless driver for deployment
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	
	for site in list_of_stuff:
		a, b = mars_news(browser, site)
		# todo: something with a (title)
		# todo: somethin with b (paragraph)


	# news_title, news_paragraph = mars_news(browser)

	# Stop webdriver and return data
	browser.quit()
	return main


def mars_news(browser, website):
	browser.visit(website)

	# title of first article
	nasa_title = (bs(browser.html, 'html.parser').find('div', class_="content_title")).text.strip()

	# first paragraph of first article
	nasa_para = (bs(browser.html, 'html.parser').find('div', class_="article_teaser_body")).text.strip()

	return nasa_title, nasa_para


def space_image(browser):
	browser.visit(jpl_web)
	browser.find_by_id("full_image").click()

	# the browser tried to click too quickly so I had to add a sleep function
	time.sleep(5)
	browser.click_link_by_partial_text('more info')

	jpl_end = (bs(browser.html, 'html.parser').find('img', class_='main_image')['src'])

	full_jpl = (jpl_web + jpl_end)

	return full_jpl


def hemispheres(browser):
	# empty list for the string
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

	return hemisphere_img


def twitter_weather(browser):
	browser.visit(nasa_twitter)
	tweet = (bs(browser.html, 'html.parser').find('div', class_="js-tweet-text-container")).text.strip()

	return tweet


def mars_facts():
	mars_facts = pd.DataFrame(pd.read_html(facts_web)[0])
	facts_html = mars_facts.to_html()

	return facts_html

if __name__ == "__main__":

	# If running as script, print scraped data
	print(main())

