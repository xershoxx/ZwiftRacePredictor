import time
from selenium import webdriver

class WebScraper:

    def __init__(self):
        self.username = "xershoxx"
        self.password = "sout!shiw!joun5ZOUC"
        self.driver = webdriver.Chrome("C:\\Users\\claud\\Documents\\Projects\\Zwiftpower_Race-Analysis\\prototype\\chromedriver.exe")

    def login(self):
        self.driver.get("https://zwiftpower.com")

        self.driver.find_element_by_id("username").send_keys(self.username)
        self.driver.find_element_by_id("password").send_keys(self.password)

        self.driver.find_element_by_class_name("btn-success").click()

    def get_page(self, url):
        self.driver.get(url)

        time.sleep(5)

        return self.driver.page_source