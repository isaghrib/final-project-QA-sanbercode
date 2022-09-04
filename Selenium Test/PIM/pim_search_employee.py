import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def login_success(self):
        browser = self.browser
        browser.find_element(By.NAME,"username").send_keys("Admin")
        browser.find_element(By.NAME,"password").send_keys("admin123")
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()

class SearchTest(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(60)
        self.browser.maximize_window()
        self.browser.get("https://opensource-demo.orangehrmlive.com/")
        
    def test_a_pim_dashboard(self):
        login_success(self)
        text_pim = self.browser.find_element(By.XPATH, ("/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6")).text

        self.assertEqual(text_pim, "PIM", "Bukan halaman PIM")

    def test_b_pim_search_employee_information_by_employeeName(self):
        login_success(self)
        time.sleep(3)
        browser = self.browser
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[1]/input").send_keys("Jo")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/span[text()='John  Smith']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)

        first_name = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]").text
        last_name = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[4]").text

        self.assertEqual(first_name, "John", "Bukan John")
        self.assertEqual(last_name, "Smith", "Bukan Smith")
    
    def test_c_pim_search_employee_information_by_employeeId(self):
        login_success(self)
        browser = self.browser
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("0011")
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(5)

        employee_id = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]").text
        first_name = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]").text
        last_name = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[4]").text

        self.assertEqual(first_name, "John", "Bukan John")
        self.assertEqual(last_name, "Smith", "Bukan Smith")
        self.assertEqual(employee_id, "0011", "Bukan Smith")

    def test_d_pim_search_employee_information_by_employementStatus(self):
        login_success(self)
        browser = self.browser
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[1]").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[3]/span[text()='Full-Time Contract']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(5)

        employee_status = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]").text
        self.assertIn("Full-Time Contract", employee_status)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()