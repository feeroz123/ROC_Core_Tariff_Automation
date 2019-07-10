from base.base_page import BasePage

class home_page(BasePage):

    # Locators
    _navMenu = "navigationLabel"   #id
    _options = "options"   #id
    _logout = "logout"     #id
    _search = "//div[@id='navigationSearch']//input"    #xpath
    _tariffs = "id-Tariffs"     #id
    _confirmLogout = "//div[contains(@class,'roc-WindowBox')]//button[@id='yes']"   #xpath

    def __init__(self, driver):
        super(home_page, self).__init__(driver) # Passing the driver instance to parent/super class
        self.driver = driver

    def clickNavigationMenu(self):
        self.clickElement(self._navMenu)

    def clickOptions(self):
        self.clickElement(self._options)

    def goToTariffs(self):
        self.clickNavigationMenu()
        self.sendKeys("Tariffs", self._search)
        self.clickElement(self._tariffs)

    def logout(self):
        self.clickOptions()
        self.clickElement(self._logout)
        self.clickElement(self._confirmLogout, "xpath")
