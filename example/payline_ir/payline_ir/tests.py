# _*_ coding: utf8 _*_

from django.test import LiveServerTestCase

from pyvirtualdisplay import Display

from selenium import webdriver


class AdminTestCase(LiveServerTestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()

        self.selenium = webdriver.Firefox()

        super(AdminTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        self.display.stop()
        super(AdminTestCase, self).tearDown()

    def test_payment(self):
        """
        payment will be successful.
        """

        self.selenium.get("%s/pay" % self.live_server_url)
        self.selenium.implicitly_wait(20)
        self.selenium.maximize_window()

        self.selenium.find_element_by_name("amount").send_keys("100000")

        pay_button = self.selenium \
            .find_element_by_xpath('//input[@value="pay"]')
        pay_button.click()

        return_to_site_button = self.selenium.find_element_by_id("btn3")

        return_to_site_button.click()

        self.assertIn("successful", self.selenium.page_source)
