from framework.browser.browser_factory import BrowserFactory


class Browser:
    """
    The Browser is a class that ensures the existence of only one instance
    of the Selenium driver throughout the application. It follows the Singleton design pattern,
    providing a global point of access to the driver object.
    """
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
