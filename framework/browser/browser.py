from framework.browser.browser_factory import BrowserFactory


class Browser:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = BrowserFactory().get_webdriver()
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None
