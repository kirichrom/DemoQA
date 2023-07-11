from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.label import Label
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage
from project.resources.user import User
from project.utils.string_utils import StringUtils


class TextBoxPage(BasePage):
    TEXT_BOX_HEADER_LOCATOR = (By.XPATH, '//div[@class="main-header" and text() = "Text Box"]')
    USER_NAME_TEXT_BOX_LOCATOR = (By.XPATH, '//input[@id="userName"]')
    EMAIL_TEXT_BOX_LOCATOR = (By.XPATH, '//input[@id="userEmail"]')
    CUR_ADDRESS_TEXT_BOX_LOCATOR = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERM_ADDRESS_TEXT_BOX_LOCATOR = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, '//button[@id="submit"]')
    NAME_LABEL_LOCATOR = (By.XPATH, '//p[@id="name"]')
    EMAIL_LABEL_LOCATOR = (By.XPATH, '//p[@id="email"]')
    CUR_ADDRESS_LABEL_LOCATOR = (By.XPATH, '//p[@id="currentAddress"]')
    PERM_ADDRESS_LABEL_LOCATOR = (By.XPATH, '//p[@id="permanentAddress"]')

    def __init__(self):
        super().__init__(by_locator=TextBoxPage.TEXT_BOX_HEADER_LOCATOR, name=self.__class__.__name__)

        self.user_name_text_box = TextBox(by_locator=self.USER_NAME_TEXT_BOX_LOCATOR, name='User Name text box')
        self.email_text_box = TextBox(by_locator=self.EMAIL_TEXT_BOX_LOCATOR, name='Email text box')
        self.cur_address_text_box = TextBox(by_locator=self.CUR_ADDRESS_TEXT_BOX_LOCATOR,
                                            name='Current Address text box')
        self.perm_address_text_box = TextBox(by_locator=self.PERM_ADDRESS_TEXT_BOX_LOCATOR,
                                             name='Permanent Address text box')

        self.name_label = Label(by_locator=self.NAME_LABEL_LOCATOR, name='Name label')
        self.email_label = Label(by_locator=self.EMAIL_LABEL_LOCATOR, name='Email label')
        self.cur_address_label = Label(by_locator=self.CUR_ADDRESS_LABEL_LOCATOR, name='Current Address label')
        self.perm_address_label = Label(by_locator=self.PERM_ADDRESS_LABEL_LOCATOR, name='Permanent Address label')

        self.submit_button = Button(by_locator=self.SUBMIT_BUTTON_LOCATOR, name='Submit button')

    def fill_all_fields(self, user: User) -> None:
        self.user_name_text_box.send_text(text=user.full_name)
        self.email_text_box.send_text(text=user.email)
        self.cur_address_text_box.send_text(text=user.current_address)
        self.perm_address_text_box.send_text(text=user.permanent_address)

    def click_submit_button(self) -> None:
        self.submit_button.click()

    def get_labels_list(self) -> list:
        labels = [self.name_label.get_text(),
                  self.email_label.get_text(),
                  self.cur_address_label.get_text(),
                  self.perm_address_label.get_text()]
        return StringUtils.parse_text_from_labels(labels)
