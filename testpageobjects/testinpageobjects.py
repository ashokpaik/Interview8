from selenium.webdriver.common.by import By


class Testinpageobjects:

    def __init__(self, driver):
        self.driver = driver

    Name = (By.XPATH, "//input[@name='name']")

    def name(self):
        return self.driver.find_element(*Testinpageobjects.Name)

    Email = (By.NAME, "email")

    def email(self):
        return self.driver.find_element(*Testinpageobjects.Email)

    Password = (By.ID, "exampleInputPassword1")

    def password(self):
        return self.driver.find_element(*Testinpageobjects.Password)

    Check = (By.ID, "exampleCheck1")

    def check(self):
        return self.driver.find_element(*Testinpageobjects.Check)

    Select = (By.ID, "exampleFormControlSelect1")

    def select(self):
        return self.driver.find_element(*Testinpageobjects.Select)

    Radio = (By.ID, "inlineRadio2")

    def radio(self):
        return self.driver.find_element(*Testinpageobjects.Radio)

    Bday = (By.NAME, "bday")

    def bday(self):
        return self.driver.find_element(*Testinpageobjects.Bday)

    Btn = (By.CLASS_NAME, "btn-success")

    def btn(self):
        return self.driver.find_element(*Testinpageobjects.Btn)

    Alert = (By.CLASS_NAME, "alert-success")

    def alert(self):
        return self.driver.find_element(*Testinpageobjects.Alert)
