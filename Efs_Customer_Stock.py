import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class EfS_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_assignment3(self):
        user = "instructor1a"                                                                                             #Provide the Username
        pwd = "instructor1a"                                                                                            #Provide the Password
        driver = self.driver
        driver.maximize_window()
        driver.get("https://nitheshefsblog.herokuapp.com/")                                                               #Get the Heroku URL
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(2)
        driver.get("https://nitheshefsblog.herokuapp.com/accounts/login/")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        #time.sleep(2)
        #elem.send_keys(Keys.RETURN)
        driver.get("https://nitheshefsblog.herokuapp.com/")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[11]/a").click()
        time.sleep(2)
        driver.get("https://nitheshefsblog.herokuapp.com/")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)
        driver.get("https://nitheshefsblog.herokuapp.com/investment/")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a").click()
        time.sleep(2)
        description = "New description added"
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(description)
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        driver.get("https://nitheshefsblog.herokuapp.com/investment/")
        time.sleep(2)
        driver.get("https://nitheshefsblog.herokuapp.com/")
        time.sleep(2)
        assert "Investment deleted"
        driver.get("https://nitheshefsblog.herokuapp.com/investment/")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        customer = "12056"
        category = "New Investment"
        description = "New Investment updated"
        acquired_value = "26"
        acquired_date = "2017-11-25"
        recent_value = "95"
        recent_date = "2017-11-26"
        elem = driver.find_element_by_id("id_customer")
        elem.send_keys(customer)
        time.sleep(2)
        elem = driver.find_element_by_id("id_category")
        elem.send_keys(category)
        time.sleep(2)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(description)
        time.sleep(2)
        elem = driver.find_element_by_id("id_acquired_value")
        elem.send_keys(acquired_value)
        time.sleep(2)
        elem = driver.find_element_by_id("id_acquired_date").clear()
        elem = driver.find_element_by_id("id_acquired_date")
        elem.send_keys(acquired_date)
        time.sleep(2)
        elem = driver.find_element_by_id("id_recent_value")
        elem.send_keys(recent_value)
        time.sleep(2)
        elem = driver.find_element_by_id("id_recent_date").clear()
        elem = driver.find_element_by_id("id_recent_date")
        elem.send_keys(recent_date)
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        assert "Investment Added"
        driver.get("https://nitheshefsblog.herokuapp.com")
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[4]/div/div/p[2]/a").click()
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        customer="12056"
        type="uno"
        sip="210"
        nav="129.2"
        numberof_units="25"
        created_date="2017-11-26 07:42:45"
        end_date="2017-11-26"
        elem = driver.find_element_by_id("id_customer")
        elem.send_keys(customer)
        time.sleep(1)
        elem = driver.find_element_by_id("id_type")
        elem.send_keys(type)
        time.sleep(1)
        elem = driver.find_element_by_id("id_sip")
        elem.send_keys(sip)
        time.sleep(1)
        elem = driver.find_element_by_id("id_nav")
        elem.send_keys(nav)
        time.sleep(1)
        elem = driver.find_element_by_id("id_numberof_units")
        elem.send_keys(numberof_units)
        time.sleep(1)
        elem = driver.find_element_by_id("id_created_date").clear()
        elem = driver.find_element_by_id("id_created_date")
        elem.send_keys(created_date)
        time.sleep(1)
        elem = driver.find_element_by_id("id_end_date").clear()
        elem = driver.find_element_by_id("id_end_date")
        elem.send_keys(end_date)
        time.sleep(1)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        assert "New mutual fund added successfully"
        elem=driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a").click()
        time.sleep(2)
        elem=driver.find_element_by_id("id_nav").clear()
        time.sleep(1)
        nav="183.25"
        elem=driver.find_element_by_id("id_nav")
        elem.send_keys(nav)
        time.sleep(2)
        elem=driver.find_element_by_xpath("/html/body/div/div/div/form/p[7]").click()
        time.sleep(2)
        assert "Mutual fund updated successfully"


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()