from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
# path = "C://Users/91896/Downloads/chromedriver"
# document.querySelector("#text > a")
#text > a
option = Options()

option.headless = False
driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))


def launchBrowser():
    driver.implicitly_wait(5)
    driver.get("https://www.youtube.com/results?search_query=programming")

    time.sleep(10)
    allChannelsLink = driver.find_elements(By.CSS_SELECTOR, "#text > a")
    print("runnning")

    link = list(dict.fromkeys((map(lambda a: a.get_attribute("href"), allChannelsLink))))
    # print(link)
    # to make the url open for 2 mins
    # time.sleep(120)

    # to remain open
    # while(True):
    #     pass
    return link


def urlDetail(url):
    i=0
    details = []
    for link in url:
        driver.get(f"{link}/about")
        name = driver.find_element(By.CSS_SELECTOR, "#text").text
        subs = driver.find_element(By.CSS_SELECTOR,"#subscriber-count").text
        desc = driver.find_element(By.CSS_SELECTOR,"#description").text

        objs = {
            "Name" : name,
            "Total Subscriber" : subs,
            "Description" : desc
        }

        details.append(objs)

        # print(name)
        i=i+1
    print(i)
    return details

def kunalNotification():
    driver.get("https://www.youtube.com/@KunalKushwaha/videos")
    time.sleep(7)
    latestVideo = driver.find_element(By.CSS_SELECTOR,"#metadata-line > span:nth-child(4)").text
    # print(latestVideo)
    timeString = latestVideo.split()
    print(timeString)
    T = int(timeString[0])
    print(T)
    if(timeString[1]=="days" and T==1):
        print("new video")
    elif(timeString[1]=="hours" and T<=12):
        print("new video")
    else:
        print("no new video")

if __name__ == "__main__":
    allChannelsUrl = launchBrowser()
    # print(allChannelsUrl)
    allChannelsDetails =  urlDetail(allChannelsUrl)
    print(json.dumps(allChannelsDetails,indent=4))

    # noti = kunalNotification()


#metadata-line > span:nth-child(4)

#metadata-line > span:nth-child(4)

#metadata-line

#meta > ytd-video-meta-block
#metadata-line