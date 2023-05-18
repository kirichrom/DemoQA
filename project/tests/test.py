from framework.utils.browser_utils import BrowserUtils
from project.pages.text_box_page import TextBoxPage
from project.utils.string_utils import StringUtils
from project.utils.user_generator import UserGenerator


class TestSuite:

    def test_fill_all_text_boxes(self):
        text_box_page = TextBoxPage()

        BrowserUtils.go_to_base_url()
        assert text_box_page.is_page_open(), 'Text Box page is not open'

        user = UserGenerator().get_random_user()
        user_attributes = StringUtils.remove_new_line_symbols([user.full_name, user.email, user.current_address,
                                                               user.permanent_address])

        text_box_page.fill_all_fields(user)
        text_box_page.click_submit_button()
        assert text_box_page.get_labels_list() == user_attributes
