from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.label import Label
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage
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

        self.user_name_text_box = TextBox(self.USER_NAME_TEXT_BOX_LOCATOR, 'User Name text box')
        self.email_text_box = TextBox(self.EMAIL_TEXT_BOX_LOCATOR, 'Email text box')
        self.cur_address_text_box = TextBox(self.CUR_ADDRESS_TEXT_BOX_LOCATOR, 'Current Address text box')
        self.perm_address_text_box = TextBox(self.PERM_ADDRESS_TEXT_BOX_LOCATOR, 'Permanent Address text box')
        self.submit_button = Button(self.SUBMIT_BUTTON_LOCATOR, 'Submit button')
        self.name_label = Label(self.NAME_LABEL_LOCATOR, 'Name label')
        self.email_label = Label(self.EMAIL_LABEL_LOCATOR, 'Email label')
        self.cur_address_label = Label(self.CUR_ADDRESS_LABEL_LOCATOR, 'Current Address label')
        self.perm_address_label = Label(self.PERM_ADDRESS_LABEL_LOCATOR, 'Permanent Address label')

    def fill_all_fields(self, user):
        self.user_name_text_box.send_text(user.full_name)
        self.email_text_box.send_text(user.email)
        self.cur_address_text_box.send_text(user.current_address)
        self.perm_address_text_box.send_text(user.permanent_address)

    def click_submit_button(self):
        self.submit_button.click()

    def get_labels_list(self):
        labels = [self.name_label.get_text(),
                  self.email_label.get_text(),
                  self.cur_address_label.get_text(),
                  self.perm_address_label.get_text()]
        return StringUtils.parse_text_from_labels(labels)
