from selenium import webdriver # special import for selenium

browser = webdriver.Firefox() # opens firefox window
browser.get('https://automatetheboringstuff.com') # sends browser to url

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a')
elem.click()

elems = browser.find_elements_by_css_selector('p')
print(len(elems))

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()
browser.back() # goes back in browser
browser.forward()
browser.quit()
