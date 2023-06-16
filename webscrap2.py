from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)

page_URL = "https://codeforces.com/problemset/page/"


def get_a_tags(url):
    driver.get(url)

    time.sleep(5)

    links = driver.find_elements(By.TAG_NAME, "span")

    ans = []

    for i in links:
        try:
            # Check if '/problems/' is in the href of the 'a' element
            if "/problemset/problem/" in i.get_attribute("href"):
                # If it is, append it to the list of links
                ans.append(i.get_attribute("href"))
        except:
            pass
    # Remove duplicate links using set
    ans = list(set(ans))
    return ans


my_ans = []

for i in range(1, 10):
    my_ans += (get_a_tags(page_URL + str(i)))

    # Remove any duplicates that might have been introduced in the process
    my_ans = list(set(my_ans))


with open('cf.txt', 'a') as f:
    # Iterate over each link in your final list
    for j in my_ans:
        # Write each link to the file, followed by a newline
        f.write(j+'\n')

# Print the total number of unique links found
print(len(my_ans))

# Close the browser
driver.quit()