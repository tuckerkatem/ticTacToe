#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

###################################################################################################
#	This script is meant to verify the banner options are present on the Assignment Home Page.
#	This script also verifies buttons based on the login state of the user. 
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
		
def login_using_github():
	print('')
	print('-----------------------------------------------------------------')
	print('Logging into CodePen using GitHub')
	print('-----------------------------------------------------------------')
	print('')
	
	loginButton = driver.find_element(By.XPATH, log_in)
	loginButton.click()
	
	githubLogin = driver.find_element(By.XPATH, '//*[@id="login-with-github"]')
	githubLogin.click()
	
	username = 'tuckerkatem@gmail.com'
	usernameField = driver.find_element(By.XPATH, '//*[@id="login_field"]')
	usernameField.send_keys(username)
	
	password = 'dAK9w2rtL.-@NjF4teaXJFE*H'
	passwordField = driver.find_element(By.XPATH, '//*[@id="password"]')
	passwordField.send_keys(password)
	
	signInButton = driver.find_element(By.XPATH, '//*[@id="login"]/div[3]/form/div/input[12]')
	signInButton.click()
	time.sleep(4)
	
def verify_options_logged_in():
	pin_item = '//*[@id="main-header"]/div/span/button[1]'
	check_exists_by_xpath(pin_item, '"Pin Item" Button')
	
	pinned_items = '//*[@id="main-header"]/div/span/button[2]'
	check_exists_by_xpath(pinned_items, '"View Pinned Items" Button')
	
	profile_link = '//*[@id="sessionUserAvatar"]'
	check_exists_by_xpath(profile_link, '"User Profile" Options Menu')

###################################################################################################

print('')
print('###################################################################################################')
print('')
print('THIS SCRIPT WILL VERIFY THE BANNER OPTIONS ON THE "QA INTERVIEW ASSIGNMENT" PAGE')
print('')
print('###################################################################################################')
print('')
    
driver = webdriver.Chrome('/Users/ktucker/Documents/WebDriver/chromedriver')

# Start Chromedriver
start_webdriver()

# Close any Ads
close_ads()
    
# Verify the page title
assignmentTitle = 'QA Interview Assignment'
verify_page_title(assignmentTitle)
time.sleep(2)

###################################################################################################

# Verify the different banner options that are visible regardless of login status
titleXpath = '//*[@id="editable-title-span"]'
check_exists_by_xpath(titleXpath, '"Project Title" Link')

calendlyLink = '//*[@id="main-header"]/div/div/div/div/a'
check_exists_by_xpath(calendlyLink, '"Calendly Code Home" Link')

follow_link = '//*[@id="main-header"]/div/div/div/div/button'
check_exists_by_xpath(follow_link, '"+Follow Calendly" Link')

heart_button = '//*[@id="main-header"]/div/div/div/div/button'
check_exists_by_xpath(heart_button, '"Love This Code" Link')

view_editor = '//*[@id="main-header"]/div/a[1]'
check_exists_by_xpath(view_editor, '"View in Editor" Link')

###################################################################################################

# Determine if we are signed into CodePen or not 
loginButton = '//*[@id="main-header"]/div/a[3]'
check = check_exists_by_xpath(loginButton, '"Log In" Button')

if check == True:
	print('')
	print('-----------------------------------------------------------------')
	print('Confirmed that the user is not currently logged into CodePen.')
	print('-----------------------------------------------------------------')
	print('')
	time.sleep(2)
	print('')
	print('-----------------------------------------------------------------')
	print('Validating the "Sign Up" and "Log In" buttons.')
	print('-----------------------------------------------------------------')
	print('')
	
	sign_up = '//*[@id="main-header"]/div/a[2]'
	check_exists_by_xpath(sign_up, '"Sign Up" Button')
	
	log_in = '//*[@id="main-header"]/div/a[3]'
	check_exists_by_xpath(log_in, '"Log In" Button')
	
	login_using_github()
	
	verify_options_logged_in()
	
if check == False:
	print('')
	print('-----------------------------------------------------------------')
	print('Confirmed that the user is currently logged into CodePen.')
	print('-----------------------------------------------------------------')
	print('')
	time.sleep(2)
	print('')
	print('-----------------------------------------------------------------')
	print('Validating the banner options that appear once signed in.')
	print('-----------------------------------------------------------------')
	print('')
	verify_options_logged_in()
	
print('')	
print('###################################################################################################')
print('')
print('THIS IS THE END OF THE BANNER OPTIONS SCRIPT.')
print('')
print('###################################################################################################')
print('')

driver.quit()

###################################################################################################