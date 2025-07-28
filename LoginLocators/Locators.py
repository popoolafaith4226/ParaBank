from selenium.webdriver.common.by import By

class LoginLocator:
    Username = (By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input')
    Password = (By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input')
    LoginButton = (By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input')


class Register:
    RegisterButton = (By.XPATH, '//*[@id="loginPanel"]/p[2]/a')
    FirstName = (By.XPATH, '//*[@id="customer.firstName"]')
    LastName = (By.XPATH, '//*[@id="customer.lastName"]')
    Address = (By.XPATH, '//*[@id="customer.address.street"]')
    City = (By.XPATH, '//*[@id="customer.address.city"]')
    State = (By.XPATH, '//*[@id="customer.address.state"]')
    ZipCode = (By.XPATH, '//*[@id="customer.address.zipCode"]')
    Phone = (By.XPATH, '//*[@id="customer.phoneNumber"]')
    SSN = (By.XPATH, '//*[@id="customer.ssn"]')
    UsernameSignUP = (By.XPATH, '//*[@id="customer.username"]')
    PasswordSignup = (By.XPATH, '//*[@id="customer.password"]')
    ConfirmPassword = (By.XPATH, '//*[@id="repeatedPassword"]')
    SubmitButton = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')
    LogoutButton = (By.XPATH, '//*[@id="leftPanel"]/ul/li[8]/a')
    SuccessMessage = (By.XPATH, '//*[@id="rightPanel"]/p')
    ErrorMessage = (By.XPATH, '//*[@id="customer.username.errors"]')





