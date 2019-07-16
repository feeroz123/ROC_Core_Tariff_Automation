from base.base_page import BasePage

class HomePage(BasePage):

    # Locators
    _navMenu = "navigationLabel"   #id
    _options = "options"   #id
    _logout = "logout"     #id
    _search = "//div[@id='navigationSearch']//input"    #xpath
    _tariffs = "//div[@id='navigationSearch']//div[@id='id-Tariffs']"     #xpath
    _confirmLogout = "//div[contains(@class,'roc-WindowBox')]//button[@id='yes']"   #xpath

    def __init__(self, driver):
        super(HomePage, self).__init__(driver) # Passing the driver instance to parent/super class
        self.driver = driver

    def clickNavigationMenu(self):
        self.clickElement(self._navMenu)

    def clickOptions(self):
        self.clickElement(self._options)

    def navigateTo(self, targetScreenName):
        self.clickNavigationMenu()
        self.sendKeys(targetScreenName, self._search, "xpath")

        if targetScreenName == "Tariffs":
            self.clickElement(self._tariffs, "xpath")

    def logout(self):
        self.clickOptions()
        self.clickElement(self._logout)
        self.clickElement(self._confirmLogout, "xpath")
