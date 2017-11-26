import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ClientVisit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_assignment4(self):
        user = "instructor"                                                                                             #Provide the Username
        pwd = "instructor1a"                                                                                            #Provide the Password
        driver = self.driver
        driver.maximize_window()
        driver.get("https://gs-food-pantry.herokuapp.com/admin")                                                               #Get the Heroku URL
        time.sleep(2)
        elem=driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem=driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://gs-food-pantry.herokuapp.com/admin")
        elem=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[4]/table/tbody/tr[2]/th/a").click()
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
        time.sleep(2)
        category="perishable"
        name="butter"
        slug="butter"
        description="we provide a good quality butter for bread"
        stock="25"
        elem = driver.find_element_by_id("id_category")
        elem.send_keys(category)
        time.sleep(2)
        elem = driver.find_element_by_id("id_name")
        elem.send_keys(name)
        time.sleep(2)
        elem = driver.find_element_by_id("id_slug")
        elem.send_keys(slug)
        time.sleep(2)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(description)
        time.sleep(2)
        elem = driver.find_element_by_id("id_stock")
        elem.send_keys(stock)
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
        time.sleep(3)
        assert "Product added successfully"

        elem=driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[4]/table/tbody/tr[5]/th/a").click()
        time.sleep(2)
        description="this is the new description"
        elem=driver.find_element_by_id("id_description")
        elem.send_keys(description)
        time.sleep(2)
        assert "Product edited successfully"

        elem=driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/p/a").click()
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
        time.sleep(5)
        assert "Product deleted successfully"


    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()