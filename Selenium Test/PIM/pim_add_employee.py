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


class addEmployeeTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(60)
        self.browser.maximize_window()
        self.browser.get("https://opensource-demo.orangehrmlive.com/")

    def test_a_pim_button_add(self):
        login_success(self)
        browser = self.browser
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        time.sleep(1)
        # validasi halaman add employee
        text_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/h6").text
        self.assertEqual(text_button, "Add Employee", "Bukan halaman Add Employee")

    def test_b_pim_nav_add_employee(self):
        login_success(self)
        browser = self.browser
        time.sleep(3)
        browser.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
        time.sleep(1)
        # validasi halaman add employee
        text_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/h6").text
        self.assertEqual(text_button, "Add Employee","Bukan halaman Add Employee")

    def test_c_pim_add_employee(self):
        login_success(self)
        browser = self.browser
        time.sleep(3)
        browser.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
        browser.find_element(By.NAME, "firstName").send_keys("Son")
        time.sleep(1)
        browser.find_element(By.NAME, "middleName").send_keys("Kakarot")
        time.sleep(1)
        browser.find_element(By.NAME, "lastName").send_keys("Goku")
        time.sleep(1)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        text_name_employee = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6").text
        self.assertEqual(text_name_employee, "Son Goku","Bukan Son Goku")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
