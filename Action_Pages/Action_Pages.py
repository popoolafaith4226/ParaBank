import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginLocators.Locators import LoginLocator, Register


class LoginPages:
    def __init__(self,driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self,user_name):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.Username))
        username.send_keys(user_name)

    def password(self,user_password):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.Password))
        username.send_keys(user_password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.LoginButton))
        click_login_button.click()


class RegisterButton:
    def __init__(self, driver):
        self.driver = driver

    def click_register_button(self):
        click_the_register_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.RegisterButton))
        click_the_register_button.click()
        time.sleep(3)

    def input_firstname(self, user_firstname):
        input_the_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.FirstName))
        input_the_firstname.send_keys(user_firstname)
        time.sleep(3)

    def input_lastname(self, user_lastname):
        input_the_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.LastName))
        input_the_lastname.send_keys(user_lastname)
        time.sleep(3)

    def input_address(self, user_address):
        input_the_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.Address))
        input_the_address.send_keys(user_address)
        time.sleep(3)

    def input_city(self,user_city):
        input_the_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.City))
        input_the_city.send_keys(user_city)
        time.sleep(3)

    def input_state(self, user_state):
        input_the_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.State))
        input_the_address.send_keys(user_state)
        time.sleep(3)

    def input_zipcode(self, user_zipcode):
        input_the_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.ZipCode))
        input_the_zipcode.send_keys(user_zipcode)
        time.sleep(3)

    def input_phone_number(self, user_phone):
        input_the_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.Phone))
        input_the_address.send_keys(user_phone)
        time.sleep(3)

    def input_ssn(self, user_ssn):
        input_the_ssn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.SSN))
        input_the_ssn.send_keys(user_ssn)
        time.sleep(3)

    def input_username(self, user_username):
        input_the_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.UsernameSignUP))
        input_the_username.send_keys(user_username)
        time.sleep(3)

    def input_password(self, user_password):
        input_the_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.PasswordSignup))
        input_the_password.send_keys(user_password)
        time.sleep(3)

    def input_confirm_password(self, user_confirm_password):
        input_the_confirm_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.ConfirmPassword))
        input_the_confirm_password.send_keys(user_confirm_password)
        time.sleep(3)

    def click_submit_button(self):
        click_the_register_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.SubmitButton))
        click_the_register_button.click()
        time.sleep(3)

    def click_logout_button(self):
        click_the_logout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Register.LogoutButton))
        click_the_logout_button.click()
        time.sleep(3)

    def get_success_message_text(self):
        return self.driver.find_element(*Register.SuccessMessage).text

    def get_error_message_text(self):
        return self.driver.find_element(*Register.ErrorMessage).text



