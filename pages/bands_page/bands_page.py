from base.base_page import BasePage

class bands_page(BasePage):

    # Locators
    _bandNameFilter = "grid_column_header_filtersearchGrid_bandType$bdtName"  #id
    _bandNameSearchButton = "//div[text()='Search']"     #xpath
    _commonTasks = "//div[text()='Common Tasks']"   #xpath
    _newBand = "//div[text()='New']"  #xpath
    _clearButton = "clear"  #id

    def __init__(self, driver):
        super(bands_page, self).__init__(driver)  # Passing the driver instance to parent/super class
        self.driver = driver

    def clearSearchResults(self):
        self.clickElement(self._clearButton)

    def clickCommonTasks(self):
        self.clickElement(self._commonTasks, "xpath")

    def clickNewBand(self):
        self.clickElement(self._newBand, "xpath")

