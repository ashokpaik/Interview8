import pytest
from selenium.webdriver.common.by import By

from testdata.testinpagedata import Testinpagedata
from testpageobjects.testinpageobjects import Testinpageobjects
from utilities.BaseClass import BaseClass


class Testinpage(BaseClass):

    @pytest.fixture(params=Testinpagedata.getTestData("Testcase1"))
    def getdata(self, request):
        return request.param

    def test_inpage(self, getdata):
        log = self.getLogger()
        log.info("Name is" + getdata["Firstname"])
        testinpageobject = Testinpageobjects(self.driver)
        testinpageobject.name().send_keys(getdata["Firstname"])
        testinpageobject.email().send_keys(getdata["Email"])
        testinpageobject.password().send_keys(getdata["Password"])
        testinpageobject.check().click()
        testinpageobject.select().send_keys("Female")
        testinpageobject.radio().click()
        testinpageobject.bday().send_keys(getdata["Birthday"])
        testinpageobject.btn().click()
        msg = testinpageobject.alert().text
        assert "Success" in msg
        self.driver.refresh()
