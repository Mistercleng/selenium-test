import time

from e2e.page_factory.page_locator import LoginPageLocator
from e2e.utils.definition import BasePage
from selenium.webdriver.common.by import By




class LoginPage(BasePage):

    def validation_title(self):
        welcome_title = self.driver.title
        return welcome_title

    def validation_logon_name(self):
        login_screen = self.driver.find_element(By.CLASS_NAME, LoginPageLocator.LOGO_IMG)
        return login_screen

    def authentication_with_success(self,str_username,str_password):
        self.driver.find_element(By.ID, LoginPageLocator.USER_NAME).send_keys(str_username)
        self.driver.find_element(By.ID, LoginPageLocator.PASSWORD_FIELD).send_keys(str_password)
        self.driver.find_element(By.CSS_SELECTOR, LoginPageLocator.BUTTON_LOGIN).click()

    def validation_text_product(self):
        texto = self.driver.find_element(By.CLASS_NAME, LoginPageLocator.VALIDATION_PAGE_LOGIN).text
        return texto

    def validation_erro_message(self):
        erro_mesg = self.driver.find_element(By.XPATH, LoginPageLocator.ERRO_MSG).text
        return erro_mesg


    def logout_session(self):
        self.driver.find_element(By.CLASS_NAME,LoginPageLocator.BTN_MENU).click()
        time.sleep(2)
        self.driver.find_element(By.ID,LoginPageLocator.BTN_LOGOUT).click()
