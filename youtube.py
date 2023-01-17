from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# path = "C://Users/91896/Downloads/chromedriver"


def launchBrowser():
    option = Options()
    option.headless = False
    driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.get("https://www.google.com")

    # to remain open
    # while(True):
    #     pass
launchBrowser()
