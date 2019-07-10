from base.base_page import BasePage

class tariffs_page(BasePage):

    # Locators
    _tariffNameFilter = "tffName"   #id
    _commonTasks = "//div[text()='Common Tasks']"   #xpath
    _newTariff = "//div[text()='New']"  #xpath

    def __init__(self, driver):
        super(tariffs_page, self).__init__(driver)  # Passing the driver instance to parent/super class
        self.driver = driver

    def searchTariffName(self, tariff_name):
        self.sendKeys(tariff_name, self._tariffNameFilter)
        self.click_search_button()

    def clickCommonTasks(self):
        self.clickElement(self._commonTasks, "xpath")

    def clickNewTariff(self):
        self.clickElement(self._newTariff, "xpath")

