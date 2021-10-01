#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

###################################################################################################
#	This script is meant to verify the page options on the Calendly CodePen Home Page.
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
    	
def verify_pen_options(link):
	pens = driver.find_element(By.XPATH, link)
	pens.click()

	showcase = '//*[@id="profile-content-wrap"]/nav/a[1]'
	check_exists_by_xpath(showcase, '"Showcase" Banner Link')

	popular = '//*[@id="profile-content-wrap"]/nav/a[2]'
	check_exists_by_xpath(popular, '"Popular" Banner Link')

	allPens = '//*[@id="profile-content-wrap"]/nav/a[3]'
	check_exists_by_xpath(allPens, '"All Pens" Banner Link')

	templates = '//*[@id="profile-content-wrap"]/nav/a[4]'
	check_exists_by_xpath(templates, '"Templates" Banner Header')

	forked = '//*[@id="profile-content-wrap"]/nav/a[5]'
	check_exists_by_xpath(forked, '"Forked" Banner Link')
	
	loved = '//*[@id="profile-content-wrap"]/nav/a[6]'
	check_exists_by_xpath(loved, '"Loved" Banner Link')

	tags = '//*[@id="profile-content-wrap"]/nav/a[7]'
	check_exists_by_xpath(tags, '"Tags" Banner Link')

def verify_projects_options(link):
	projects = driver.find_element(By.XPATH, link)
	projects.click()

	allProjects = '//*[@id="profile-content-wrap"]/nav/a[1]]'
	check_exists_by_xpath(allProjects, '"All Projects" Banner Link')

	templates = '//*[@id="profile-content-wrap"]/nav/a[2]]'
	check_exists_by_xpath(templates, 'Templates Banner Header')

	forked = '//*[@id="profile-content-wrap"]/nav/a[3]'
	check_exists_by_xpath(forked, '"Forked" Banner Link')
	
	loved = '//*[@id="profile-content-wrap"]/nav/a[4]'
	check_exists_by_xpath(loved, '"Loved" Banner Link')

	tags = '//*[@id="profile-content-wrap"]/nav/a[5]'
	check_exists_by_xpath(tags, '"Tags" Banner Link')

def verify_collections_options(link):
	collections = driver.find_element(By.XPATH, link)
	collections.click()

	popular = '//*[@id="profile-content-wrap"]/nav/a[1]'
	check_exists_by_xpath(popular, '"Popular" Banner Link')

	allCollections = '//*[@id="profile-content-wrap"]/nav/a[2]'
	check_exists_by_xpath(allCollections, '"All Collections" Banner Link')
	
	loved = '//*[@id="profile-content-wrap"]/nav/a[3]'
	check_exists_by_xpath(loved, '"Loved" Banner Link')

###################################################################################################
 
print('')
print('###################################################################################################')
print('')
print('THIS SCRIPT WILL VERIFY THE PAGE OPTIONS ON THE CALENDLY CODEPEN HOME PAGE')
print('')
print('###################################################################################################')
print('')

driver = webdriver.Chrome('/Users/ktucker/Documents/WebDriver/chromedriver')

# Start WebDriver
start_webdriver()

# Close Out Any Ads
close_ads()

# Verify the Calendly Link Functionality
calendlyLink = '//*[@id="main-header"]/div/div/div/div/a'
calendly_link = driver.find_element_by_xpath(calendlyLink)
calendly_link.click()

# Verify the tab title, page title, and CodePen Username
codeTitle = 'Calendly on CodePen'
verify_page_title(codeTitle)

title = '//*[@id="profile-name-header"]/span[1]'
check_exists_by_xpath(title, 'Calendly Page Title')

username = '//*[@id="profile-username"]'
check_exists_by_xpath(username, 'Calendly CodePen Username')

###################################################################################################

# Verify the main banner options
pens = '//*[@id="react-page"]/div[4]/nav/a[1]'
check_exists_by_xpath(pens, 'Pens Banner Header')

projects = '//*[@id="react-page"]/div[4]/nav/a[2]'
check_exists_by_xpath(projects, 'Projects Banner Header')

collections = '//*[@id="react-page"]/div[4]/nav/a[3]'
check_exists_by_xpath(collections, 'Collections Banner Header')

###################################################################################################

# Verify the submenu items for the Pens Banner
verify_pen_options(pens)

# Verify the submenu items for the Project Banner
verify_projects_options(projects)

# Verify the submenu items for the Collections Banner
verify_collections_options(collections)

###################################################################################################

print('')	
print('###################################################################################################')
print('')
print('THIS IS THE END OF THE CALENDLY CODEPEN HOME PAGE SCRIPT.')
print('')
print('###################################################################################################')
print('')

driver.quit()

###################################################################################################