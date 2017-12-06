import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_edit(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

# edit and existing client
   def test_edit_client(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://gs-food-pantry.herokuapp.com/portfolio/login/?next=/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://gs-food-pantry.herokuapp.com")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='topNavBar']/ul/li[1]/a").click()
       time.sleep(10)
       elem = driver.find_element_by_xpath("//*[@id='topNavBar']/ul/li[1]/ul/li[1]/a").click()
       # elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[2]/div/div/div/div[1]/div/div/p[2]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='userTbl']/tbody/tr/td[9]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_id("id_name").clear()
       elem = driver.find_element_by_id("id_address").clear()
       elem = driver.find_element_by_id("id_client_number").clear()
       elem = driver.find_element_by_id("id_city").clear()
       elem = driver.find_element_by_id("id_zipcode").clear()
       elem = driver.find_element_by_id("id_email").clear()
       time.sleep(5)
       elem = driver.find_element_by_id("id_name")
       elem.send_keys("Rachel Green")
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("929 s Avenue")
       elem = driver.find_element_by_id("id_client_number")
       elem.send_keys("785589")
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Lincoln")
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys("68108")
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("rgreen@gmail.com")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div/div/div/div/div/form/div[9]/div/button").click()
       time.sleep(10)
       assert "Edited Existing Client"
       # delete client
       elem = driver.find_element_by_xpath("//*[@id='userTbl']/tbody/tr/td[10]/a").click()
       time.sleep(5)
       alert = driver.switch_to.alert
       alert.accept()
       time.sleep(3)
       assert "deleted existing client"

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
       unittest.main()
