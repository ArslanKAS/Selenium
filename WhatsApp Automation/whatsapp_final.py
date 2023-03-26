import re
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Open the CSV file
csv_file = open('contacts.csv', mode='w', newline='', encoding='utf-8')
# Creating a CSV writer and adding header
writer = csv.DictWriter(csv_file, fieldnames=['Contacts'])
writer.writeheader()

# Chrome Options
options = Options()
options.add_argument(r"user-data-dir=C:\Users\HAIER\Downloads\chrome-data")

# Start Driver and Open WhatsApp Web
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

# Wait for QR and Login
print("--"*50)
input("PRESS ENTER AFTER SCANNING QR :")
print("--"*50)
open_new_chat = WebDriverWait(driver, 35).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_3OtEr")))

# Enter New Chat
chat = open_new_chat.find_element(By.XPATH,'//span/div[3]/div/span')
chat.click()


# Locate Contact List
time.sleep(1)
contact_list = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div[2]")


# Initiate Action
actions = ActionChains(driver)

# Hover over Contacts
print("--"*50)
input("PRESS ENTER TO HOVER: ")
print("--"*50)
actions.move_to_element(contact_list).perform()

# Scroll Contacts
print("--"*50)
input("PRESS ENTER TO SCROLL: ")
print("--"*50)
driver.execute_script("arguments[0].scrollTop += 0.5 * arguments[0].offsetHeight;", contact_list)
time.sleep(2)

# Creating an Empty List
titles = []
prev_title_elements = []
# Creating a Loop to Fetch all Elements
while True:
    # Grab all Title Elements
    title_elements = contact_list.find_elements(By.XPATH,"//*[@class='_21S-L']//span[@title and @aria-label]")

    # Compare with previous title elements and iterate only if there's a change
    if title_elements != prev_title_elements:
        prev_title_elements = title_elements
 
    # Extract Title Attribute and Store in a List
    for element in title_elements:
        title = element.get_attribute("title")
        title = title.lower().strip().title()
        title = re.sub(r'[^\w\s]', '', title)
        if title not in titles:
            titles.append(title)
            writer.writerow({'Contacts': title})

    # Print the Titles
    titles = sorted(titles)
    print(titles)
    print(f"\nTotal Elements in List: {len(titles)}")

    
    # Scroll to next contacts when finished
    actions.move_to_element(contact_list).perform()
    driver.execute_script("arguments[0].scrollTop += 1.5 * arguments[0].offsetHeight;", contact_list)
    time.sleep(4)

    if len(titles) >= 100:
        break

# Close the CSV file
csv_file.close()
# Close the Driver
driver.quit()