from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# browser.maximize_window() # For maximizing window
# browser.implicitly_wait(20) # gives an implicit wait for 20 seconds

browser.get("https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cp_36%3A1253503011&dc&fs=true&qid=1645954406&ref=sr_ex_n_1")

elem_list = browser.find_element(By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")

items = elem_list.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

for item in items:
    title = item.find_element(By.TAG_NAME, "h2").text
    price = "No Price Found"
    image = "No Image Found"
    link = item.find_element(By.CLASS_NAME, "a-link-normal").get_attribute("href")

    try:
        price = item.find_element(By.CSS_SELECTOR, ".a-price").text.replace("\n", ".")   
    except:
        pass

    try:
        image = item.find_element(By.CSS_SELECTOR, ".s-image").get_attribute("src")
    except:
        pass

    print(f"IMAGE: {image}")
    print(f"TITLE: {title}")
    print(f"PRICE: {price}")
    print(f"LINK: {link}\n")
  