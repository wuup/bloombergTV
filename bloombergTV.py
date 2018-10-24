#!/usr/bin/python3
from selenium import webdriver
import time
import threading

# export PATH=$PATH://home/debug/Repos/python-learning

def getProfile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    return profile

def openBrowser():
    browser = webdriver.Firefox(firefox_profile=getProfile())
    browser.get("https://www.bloomberg.com/live/us")
    time.sleep(1695)
    browser.quit()

def main():
    threading.Timer(1700, main).start()
    openBrowser()
    
if __name__ == "__main__":
    main()

