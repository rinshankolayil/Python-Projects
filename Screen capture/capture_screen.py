import sys
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

script_name = sys.argv[0]

opts = Options()
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)

try:
    url = sys.argv[1]
    driver.get(url)
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width,page_height)
    driver.save_screenshot('s.png')
    driver.quit()
    print("SUCCESS")
except IndexError:
    print(f'Usage {script_name}')
