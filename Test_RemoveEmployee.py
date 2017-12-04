import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_EmployeeLogin(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome("C:\\chromedriver.exe")

   def test_EmployeeLogin(self):
       user = "instructor"
       pwd = "test1234"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://gs-food-pantry.herokuapp.com/admin/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.find_element_by_xpath("//*[@id='content-main']/div[3]/table/tbody/tr[3]/th/a").click()
       driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a").click()
       driver.find_element_by_xpath("//*[@id='employee_form']/div/div/p/a").click()
       driver.find_element_by_xpath("// *[ @ id = 'content'] / form / div / input[2]").click()
       time.sleep(2)
       assert "Employee deleted"
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()











