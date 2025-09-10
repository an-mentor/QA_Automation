from utils.log_utils import Logger

class BaseTest:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None

    def setup(self):
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        Logger.log_console(self.page)
        Logger.log_page_errors(self.page)
        Logger.log_dialogs(self.page)

    def teardown(self):
        input("Press Enter to close browser...")
        self.browser.close()

