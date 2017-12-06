import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_search1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
# search a client
    def test_search_client(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://gs-food-pantry.herokuapp.com/portfolio/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://gs-food-pantry.herokuapp.com")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='topNavBar']/ul/li[1]/a").click()
        time.sleep(5)
        # elem = driver.find_element_by_xpath("//*[@id='topNavBar']/ul/li[1]/ul/li[1]/a").click()
        # time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[2]/input")
        elem.send_keys("test")
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "search for the client number"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
