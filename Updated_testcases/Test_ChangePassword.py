import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_EmployeeLogin(unittest.TestCase):

   def setUp(self):
       #self.driver = webdriver.Chrome("C:\\chromedriver.exe")
       self.driver = webdriver.Chrome()

   def test_EmployeeLogin(self):
       user = "test"
       pwd = "test@1234"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://gs-food-pantry.herokuapp.com/portfolio/login/?next=/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.find_element_by_link_text("Account Settings").click()
       driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[2]/div/div/div/div/div/div/p[2]/a").click()
       elem = driver.find_element_by_id("id_old_password")
       elem.send_keys("test@1234")
       elem = driver.find_element_by_id("id_new_password1")
       elem.send_keys("test1234")
       elem = driver.find_element_by_id("id_new_password2")
       elem.send_keys("test1234")
       elem.send_keys(Keys.RETURN)
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
