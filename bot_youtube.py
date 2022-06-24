from selenium import webdriver
from selenium.webdriver.common.by import By
import time
path = "./Drivers/chromedriver"
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
listarep = ['gang signs freddie gibbs','Daft Punk - Veridis Quo x The Weeknd - In Your Eyes']

def reproducir_lista(listarep):
    for i in range(len(listarep)):
        time.sleep(2)
        driver.find_element(By.XPATH ,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").click()
        time.sleep(2)
        driver.find_element(By.XPATH ,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys(listarep[i])
        driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click()
        time.sleep(12000)
        driver.refresh()
reproducir_lista(listarep)

