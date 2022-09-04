import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_login_success(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click() #login
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"span.oxd-userdropdown-tab").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click() #logout
        time.sleep(1)

    def test_b_login_fail_invalid_username(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("son")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
        time.sleep(5)

        #validasi
        text_fail_login = browser.find_element(By.CSS_SELECTOR,"p.oxd-text.oxd-text--p.oxd-alert-content-text").text

        self.assertEqual(text_fail_login, 'Invalid credentials', 'ga sesuai')

    def test_c_login_fail_invalid_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("admin")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
        time.sleep(5)

        #validasi
        text_fail_login = browser.find_element(By.CSS_SELECTOR,"p.oxd-text.oxd-text--p.oxd-alert-content-text").text

        self.assertEqual(text_fail_login, 'Invalid credentials', 'ga sesuai')
    
    def test_d_login_fail_blank_username(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
        time.sleep(5)

        #validasi
        text_fail_username = browser.find_element(By.CSS_SELECTOR,"span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message").text

        self.assertEqual(text_fail_username, 'Required', 'ga sesuai')

    def test_e_login_fail_blank_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("admin")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
        time.sleep(5)

        #validasi
        text_fail_password = browser.find_element(By.CSS_SELECTOR,"span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message").text

        self.assertEqual(text_fail_password, 'Required', 'ga sesuai')
    
    def test_e_login_fail_blank_username_password(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
        time.sleep(5)

        #validasi
        text_fail_required_username = browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text
        text_fail_required_password = browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text

        self.assertEqual(text_fail_required_username, 'Required', 'ga sesuai')
        self.assertEqual(text_fail_required_password, 'Required', 'ga sesuai')
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()