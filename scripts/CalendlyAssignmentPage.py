#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

###################################################################################################
#	This script is meant to verify the options once you click on the assignment Title Link.
###################################################################################################

def start_webdriver():
	driver.get('https://codepen.io/CalendlyQA/full/KKPQLmV')
	time.sleep(3)
	
def close_ads():
	ad_button = driver.find_element_by_xpath('//*[@id="bsa-footer"]/div/button')
	ad_button.click()
	time.sleep(3)

def check_exists_by_xpath(xpath, object):
    try:
        driver.find_element_by_xpath(xpath)
        print('')
        print('-------------------------------------------------------------------')
        print(f'Successfully verified that the element {object} exists.')
        print('-------------------------------------------------------------------')
        print('')
        time.sleep(1)
        return True
    except NoSuchElementException:
        return False

def verify_page_title(desiredTitle):
	title = driver.title
	print('')
	print('-------------------------------------------------------------------')
	print ('Validating that the desired title matches the actual page title.')
	print('-------------------------------------------------------------------')
	print('')
	
	if title == desiredTitle:
		print('')
		print('---------------------------------------------------------------------')
		print(f'Successfully validated that the title of this page is {desiredTitle}')
		print('---------------------------------------------------------------------')
		print('')
	else:
		print('')
		print('---------------------------------------------------------------------')
		print(f"Unable to validate that the title of this page is {desiredTitle}")
		print('---------------------------------------------------------------------')
		print('')
		
###################################################################################################

print('')
print('###################################################################################################')
print('')
print('THIS SCRIPT WILL VERIFY THE PAGE OPTIONS ONCE YOU CLICK ON THE ASSIGNMENT TITLE LINK.')
print('')
print('###################################################################################################')
print('')
    
driver = webdriver.Chrome('/Users/ktucker/Documents/WebDriver/chromedriver')

# Start Chromedriver
start_webdriver()

# Close any Ads
close_ads()

# Verify the Title Link Functionality
title_link = driver.find_element(By.ID, 'editable-title-span')
title_link.click()

###################################################################################################

# Verifying that the three main code blocks are showing on the page
html_block = '//*[@id="html-editor-title"]'
check_exists_by_xpath(html_block, '"HTML Code Block"')

css_block = '//*[@id="css-editor-title"]'
check_exists_by_xpath(css_block, '"CSS Code Block"')

js_block = '//*[@id="js-editor-title"]'
check_exists_by_xpath(js_block, '"JavaScript Code Block"')

###################################################################################################

# Verify the buttons along the bottom of the screen
console = '//*[@id="react-pen-footer"]/div[1]/div/div/button[1]'
check_exists_by_xpath(console, '"Console" Button')

assets = '//*[@id="react-pen-footer"]/div[1]/div/div/button[2]'
check_exists_by_xpath(assets, '"Assets" Button')

comments = '//*[@id="react-pen-footer"]/div[1]/div/div/button[3]'
check_exists_by_xpath(comments, '"Comments" Button')

keys = '//*[@id="react-pen-footer"]/div[1]/div/div/button[4]'
check_exists_by_xpath(keys, '"Keys" Button')

addToCollection = '//*[@id="react-pen-footer"]/div[2]/button[1]'
check_exists_by_xpath(addToCollection, '"Add To Collection" Button')

fork = '//*[@id="react-pen-footer"]/div[2]/button[2]'
check_exists_by_xpath(fork, '"Fork" Button')

embed = '//*[@id="react-pen-footer"]/div[2]/button[3]'
check_exists_by_xpath(embed, '"Embed" Button')

export = '//*[@id="react-pen-footer"]/div[2]/span[2]'
check_exists_by_xpath(export, '"Export" Button')

share = '//*[@id="react-pen-footer"]/div[2]/span[3]'
check_exists_by_xpath(share, '"Share" Button')

###################################################################################################

print('')	
print('###################################################################################################')
print('')
print('THIS IS THE END OF THE ASSIGNMENT PAGE OPTIONS SCRIPT.')
print('')
print('###################################################################################################')
print('')

driver.quit()

###################################################################################################
