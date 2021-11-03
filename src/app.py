import time
from selenium import webdriver
from selenium.webdriver.common import keys



def initialize_driver():
    return webdriver.Firefox(
        firefox_profile="C:\\Users\\User\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dm84h0jn.Discord Bot",
        executable_path="D:\\programming\\selenium\\geckodriver.exe")


driver = initialize_driver()
link = input("enter link\n")
driver.get(link)
time.sleep(1)
button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[2]/button")
button.click()
time.sleep(7)
chat = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div[2]/div[2]/textarea")
comb = ""
last_comb = ""
while True:
    while True:
        comb = chat.get_attribute("value")
        if len(comb) > 0 and comb[-1] == "!":
            comb = comb.lower()
            comb = comb[:-1]
            break
    chat.send_keys(keys.Keys.CONTROL + "A")
    chat.send_keys(keys.Keys.BACK_SPACE)
    data = open("data", 'r')
    for word in data:
        word = word.split("\n")[0]
        if comb in word.lower() and comb != last_comb:
            chat.send_keys(word)
            last_comb = comb
            print("found {}".format(word))
            time.sleep(1)
            chat.send_keys(keys.Keys.CONTROL + "A")
            chat.send_keys(keys.Keys.CONTROL + "C")
            chat.send_keys(keys.Keys.BACK_SPACE)
    comb = ""


