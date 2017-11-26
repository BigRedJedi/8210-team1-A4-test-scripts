import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        driver.get("http://gs-food-pantry.herokuapp.com")
        assert "Logged in"
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        client= "12345"
        Employee= "66102015"
        visit_type= "Regular"
        visit_date="2017-11-25"
        status="In progress"
        elem = driver.find_element_by_id("id_client")
        elem.send_keys(client)
        time.sleep(2)
        elem = driver.find_element_by_id("id_employee")
        elem.send_keys(Employee)
        time.sleep(2)
        elem = driver.find_element_by_id("id_visit_type")
        elem.send_keys(visit_type)
        time.sleep(2)
        elem = driver.find_element_by_id("id_visit_date").clear()
        elem = driver.find_element_by_id("id_visit_date")
        elem.send_keys(visit_date)
        time.sleep(2)
        elem = driver.find_element_by_id("id_status")
        elem.send_keys(status)
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        assert "Client Visit recorded"
        elem=driver.get("http://gs-food-pantry.herokuapp.com/visit")
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/table/tbody/tr[4]/td[7]/a").click()
        time.sleep(2)
        status="completed"
        elem=driver.find_element_by_id("id_status").clear()
        elem=driver.find_element_by_id("id_status")
        elem.send_keys(status)
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        assert "Successfully edited/updated client visit information"
        elem = driver.get("http://gs-food-pantry.herokuapp.com/visit")
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/table/tbody/tr[10]/td[8]/a").click()
        time.sleep(2)
       
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()