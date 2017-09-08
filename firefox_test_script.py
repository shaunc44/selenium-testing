from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox() #create instance of Firefox browser object
driver.implicitly_wait(30) #launch in 30 seconds
driver.maximize_window()

# navigate to the application home page
driver.get("https://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear() # clear previous value in search box

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions") # new search value
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists = driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the test that is
# name of the search
i = 0
for listitem in lists:
    print (listitem)
    i += 1
    if (i > 10):
        break

# close the browser window
driver.quit()