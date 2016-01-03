#_*_ coding: utf8 _*_

from django.test import LiveServerTestCase
from django.contrib.auth.models import User

from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver import ActionChains

#from mezzanine.conf import settings

class AdminTestCase(LiveServerTestCase):
    #fixtures = ['mezzanine_required.json', 'mezzanine_optional.json','bornazadeh.json']

    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser.
        #settings.configure()
        '''User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com'
        )'''

        self.display = Display(visible=0, size=(800, 600))
        self.display.start()

        self.selenium = webdriver.Firefox()
        
        #self.selenium.maximize_window()
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        # Call tearDown to close the web browser
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

        pay_button = self.selenium.find_element_by_xpath('//input[@value="pay"]')
        pay_button.click()

        return_to_site_button = self.selenium.find_element_by_id("btn3")
        #return_to_site_button = self.selenium.find_element_by_xpath('//input[@value=" بازگشت به سایت مبدا "]')
        return_to_site_button.click()

        #self.selenium.get("%s/result" % self.live_server_url)
        self.assertIn("successful", self.selenium.page_source)

    def _test_create_user(self):
        """
        Django admin create user test
        This test will create a user in django admin and assert that
        page is redirected to the new user change form.
        """
        # Open the django admin page.
        # DjangoLiveServerTestCase provides a live server url attribute
        # to access the base url in tests
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/admin/")
        )
        #self.selenium.implicitly_wait(10)

        # Fill login information of admin
        username = self.selenium.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("admin")

        # Locate Login button and click it
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/en/admin/auth/user/add/")
        )

        # Fill the create user form with username and password
        self.selenium.find_element_by_id("id_username").send_keys("test")
        self.selenium.find_element_by_id("id_password1").send_keys("test")
        self.selenium.find_element_by_id("id_password2").send_keys("test")

        # Forms can be submitted directly by calling its method submit
        self.selenium.find_element_by_id("user_form").submit()
        self.assertIn("Change user", self.selenium.title)

    def _test_mobile_nav_menu(self):
        """
        mobile nav button works or not
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/about/'))
        self.selenium.implicitly_wait(20)
        self.selenium.set_window_size(800, 600)



        mobile_menu_btn = self.selenium.find_element_by_id("mobile-nav")
        mobile_menu_btn.click()

        action_chains = ActionChains(self.selenium)
        main_nav = self.selenium.find_element_by_id("navigation-mobile")
        mobile_nav = self.selenium.find_element_by_id("menu-nav-mobile")
        action_chains.move_to_element(main_nav)
        action_chains.click(mobile_nav)
        #action_chains.perform()

        about_page = self.selenium.find_element_by_link_text("ABOUT")


        about_page.click()
        self.assertIn("About", self.selenium.title)

        mobile_menu_btn = self.selenium.find_element_by_id("mobile-nav")
        mobile_menu_btn.click()
        gallery_page = self.selenium.find_element_by_link_text("GALLERY")
        gallery_page.click()
        self.assertIn("Gallery", self.selenium.title)

    def _test_nav_menu(self):
        """
        nav menu is clickable
        """

        self.selenium.get("%s" % self.live_server_url)
        self.selenium.implicitly_wait(20)
        #self.selenium.maximize_window()

        about_page = self.selenium.find_element_by_link_text("ABOUT")
        about_page.click()
        self.assertIn("About", self.selenium.title)

        gallery_page = self.selenium.find_element_by_link_text("GALLERY")
        gallery_page.click()
        self.assertIn("Gallery", self.selenium.title)

