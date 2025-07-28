import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Action_Pages.Action_Pages import LoginPages, RegisterButton
from Config.Config import Config


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")

def login(driver_setup):
    driver = driver_setup
    login_page = LoginPages(driver)
    login_page.login_url(Config.BASEURL)
    return login_page


# def signup(driver_setup):
#     driver = driver_setup
#     login_page = LoginPages(driver)
#     login_page.login_url(Config.BASEURL)
#     return login_page


def test_user_registration(login):

    the_register_button = RegisterButton(login.driver)
    the_register_button.click_register_button()

    the_user_firstname = RegisterButton(login.driver)
    the_user_firstname.input_firstname(Config.FirstName)

    the_user_lastname =  RegisterButton(login.driver)
    the_user_lastname.input_lastname(Config.LastName)

    the_user_address = RegisterButton(login.driver)
    the_user_address.input_address(Config.Address)

    the_user_city = RegisterButton(login.driver)
    the_user_city.input_city(Config.City)

    the_user_state = RegisterButton(login.driver)
    the_user_state.input_state(Config.State)

    the_user_zipcode = RegisterButton(login.driver)
    the_user_zipcode.input_zipcode(Config.ZipCode)

    the_user_phone = RegisterButton(login.driver)
    the_user_phone.input_phone_number(Config.PhoneNumber)

    the_user_ssn = RegisterButton(login.driver)
    the_user_ssn.input_ssn(Config.SSN)

    the_user_username = RegisterButton(login.driver)
    the_user_username.input_username(Config.UserName)

    the_signup_password = RegisterButton(login.driver)
    the_signup_password.input_password(Config.Password)

    the_confirm_password = RegisterButton(login.driver)
    the_confirm_password.input_confirm_password(Config.ConfirmPassword)

    the_submit_button = RegisterButton(login.driver)
    the_submit_button.click_submit_button()


    # assertion for success registration

def test_success_registration(login):

    success_message = RegisterButton(login.driver).get_success_message_text()
    assert success_message == "Your account was created successfully. You are now logged in."


    the_logout_button = RegisterButton(login.driver)
    the_logout_button.click_logout_button()



def test_user_signup_with_same_email(login):
    the_register_button = RegisterButton(login.driver)
    the_register_button.click_register_button()

    the_user_firstname = RegisterButton(login.driver)
    the_user_firstname.input_firstname(Config.FirstName)

    the_user_lastname =  RegisterButton(login.driver)
    the_user_lastname.input_lastname(Config.LastName)

    the_user_address = RegisterButton(login.driver)
    the_user_address.input_address(Config.Address)

    the_user_city = RegisterButton(login.driver)
    the_user_city.input_city(Config.City)

    the_user_state = RegisterButton(login.driver)
    the_user_state.input_state(Config.State)

    the_user_zipcode = RegisterButton(login.driver)
    the_user_zipcode.input_zipcode(Config.ZipCode)

    the_user_phone = RegisterButton(login.driver)
    the_user_phone.input_phone_number(Config.PhoneNumber)

    the_user_ssn = RegisterButton(login.driver)
    the_user_ssn.input_ssn(Config.SSN)

    the_user_username = RegisterButton(login.driver)
    the_user_username.input_username(Config.UserName)

    the_signup_password = RegisterButton(login.driver)
    the_signup_password.input_password(Config.Password)

    the_confirm_password = RegisterButton(login.driver)
    the_confirm_password.input_confirm_password(Config.ConfirmPassword)

    the_submit_button = RegisterButton(login.driver)
    the_submit_button.click_submit_button()

    # assertion for used username
def error_username_response(login):

    error_message = RegisterButton(login.driver).get_error_message_text()
    assert error_message == "This username already exists."

# login
def test_user_login(login):

    the_username = LoginPages(login.driver)
    the_username.enter_username(Config.UserName)

    the_password = LoginPages(login.driver)
    the_password.password(Config.Password)

    the_login_button = LoginPages(login.driver)
    the_login_button.click_login_button()

