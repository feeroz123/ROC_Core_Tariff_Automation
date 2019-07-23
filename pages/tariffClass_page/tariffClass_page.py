from base.base_page import BasePage

class tariffClass_page(BasePage):

    # Locators
    _tariffClassNameFilter = "grid_column_header_filtersearchGrid_tcsName"  #id
    _tariffClassNameField = "tcsName"   #id
    _tariffClassNameSearchButton = "//div[text()='Search']"     #xpath
    _commonTasks = "//div[text()='Common Tasks']"   #xpath
    _newTariffClass = "//div[text()='New']"  #xpath
    _clearButton = "clear"  #id

    def __init__(self, driver):
        super(tariffClass_page, self).__init__(driver)  # Passing the driver instance to parent/super class
        self.driver = driver

    def clearSearchResults(self):
        self.clickElement(self._clearButton)

    def searchTariffClassName(self, tariffClass_name):
        self.clearSearchResults()
        self.clickElement(self._tariffClassNameFilter)
        self.sendKeys(tariffClass_name, self._tariffClassNameField)
        self.clickElement(self._tariffClassNameSearchButton)

    def clickCommonTasks(self):
        self.clickElement(self._commonTasks, "xpath")

    def clickNewTariffClass(self):
        self.clickElement(self._newTariffClass, "xpath")

