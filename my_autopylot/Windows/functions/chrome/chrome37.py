import sys
from selenium.common.exceptions import WebDriverException, TimeoutException

from my_autopylot.CrashHandler import report_error
from my_autopylot.Toolkit import DisableLogger


class ChromeBrowser:
    def __init__(self):
        self.browser_driver = None

    def open_browser(self, dummy_browser: bool = True, profile: str = "Default", incognito: bool = False, ):
        """
        Args:
            dummy_browser (bool, optional): True to open dummy browser. 
            Defaults: True.
            profile (str, optional): Profile name to open. 
            Defaults: "Default".
            incognito (bool, optional): True to open incognito browser. 
            Defaults: False.
        Returns:
            bool: Whether the function is successful or failed.
            driver: The driver object.
        """

        import selenium.webdriver as webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        import os
        from selenium.webdriver.chrome.options import Options
        import helium

        self.options = Options()

        self.options.add_argument("--start-maximized")
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging', 'enable-automation'])

        status = False

        try:
            with DisableLogger():
                if not dummy_browser:
                    self.options.add_argument(
                        "user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data".format(os.getlogin()))
                    self.options.add_argument(
                        f"profile-directory={profile}")
                if incognito:
                    self.options.add_argument("--incognito")
                self.browser_driver = webdriver.Chrome(
                    ChromeDriverManager().install(), options=self.options)
                helium.set_driver(self.browser_driver)
                helium.Config.implicit_wait_secs = 60
                status = True
        except Exception as e:
            print(f"Error while creating browser driver: {e}")
        finally:
            return [status, self.browser_driver]

    def navigate(self, url: str = ''):
        """Navigate through the url after the session is started.
        Args:
            url (str, optional): Url which you want to visit. 
            Defaults: "".
        Returns:
            bool: Whether the function is successful or failed.
        """

        status = False
        import helium
        helium.set_driver(self.browser_driver)
        try:
            if not url:
                helium.go_to("https://www.pybots.ai")
            else:
                helium.go_to(url)
        except:
            print("Error while navigating to url")
        else:
            status = True

        finally:
            return [status]

    def write(self, text: str = '', user_visible_text_element: str = ""):
        """Write a string in browser, if user_visible_text_element is given it writes on the given element.
        Args:
        text (str, optional): String which has be written. 
        Defaults: "".
        user_visible_text_element (str, optional): The element which is visible(Like : Sign in). 
        Defaults: "".
        Returns:
        bool: Whether the function is successful or failed.
        """

        status = False
        import helium
        helium.set_driver(self.browser_driver)
        try:

            if text and user_visible_text_element:
                helium.write(text, into=user_visible_text_element)
                status = True
            if text and not user_visible_text_element:
                helium.write(text)
                status = True

            sys.exit()
        except AttributeError:
            print("Invalid Input. Please check the given input.")

            sys.exit()
        except TimeoutException:
            print(
                "Element not found. Please check the given input or change browser_set_waiting_time().")

            sys.exit()
        except Exception as e:
            report_error(e)

        finally:
            return [status]

    def mouse_click(self, User_Visible_Text_Element: str = "", element: str = "", double_click: bool = False, right_click: bool = False):
        """Click on the given element.
        Args:
            User_Visible_Text_Element (str, optional): The element which is visible(Like : Sign in). 
            Defaults: "".
            element (str, optional): Use locate_element to get element and use to click. 
            Defaults: "".
            double_click (bool, optional): True to perform a Double click. 
            Defaults: False.
            right_click (bool, optional): True to perform a Right click. 
            Defaults: False.
        Returns:
            bool: Whether the function is successful or failed.
        """
        import helium
        status = False
        helium.set_driver(self.browser_driver)

        try:
            if not double_click and not right_click:
                if User_Visible_Text_Element and not element:
                    helium.click(User_Visible_Text_Element)
                if not User_Visible_Text_Element and element:
                    helium.click(helium.S(element))
                status = True
            if double_click and not right_click:
                if User_Visible_Text_Element and not element:
                    helium.doubleclick(User_Visible_Text_Element)
                if not User_Visible_Text_Element and element:
                    helium.doubleclick(helium.S(element))
                status = True
            if right_click and not double_click:
                if User_Visible_Text_Element and not element:
                    helium.rightclick(User_Visible_Text_Element)
                if not User_Visible_Text_Element and element:
                    helium.rightclick(helium.S(element))
                status = True

        except AttributeError:
            print("Invalid Input. Please check the given input.")

            sys.exit()
        except Exception as e:
            report_error(e)

        finally:
            return [status]

    def mouse_hover(self, User_Visible_Text_Element: str = "", element: str = "", ):
        """Performs a Mouse Hover over the Given User Visible Text Element
        Args:
            User_Visible_Text_Element (str, optional): The element which is visible(Like : Sign in). 
            Defaults: "".
        Returns:
            bool: Whether the function is successful or failed.
        """
        status = False
        import helium
        try:
            if User_Visible_Text_Element and not element:
                helium.hover(helium.Text(User_Visible_Text_Element))
            if not User_Visible_Text_Element and element:
                helium.hover(helium.S(element))
            status = True
        except Exception as e:
            report_error(e)

        finally:
            return [status]

    def scroll(self, direction: str = "down", weight=3):
        """Scrolls the browser window.
        Args:
            direction (str, optional): The direction to scroll. Defaults: "down".u,d,l,r
            weight  : The weight of the scroll. Defaults: 3. 3 corresponds to 300 pixs
        Returns:
            bool: Whether the function is successful or failed.
        """
        status = False
        import helium
        helium.set_driver(self.browser_driver)
        scroll_pixs = int(weight)
        try:
            if direction.lower() == "down":
                helium.scroll_down(scroll_pixs)
            elif direction.lower() == "up":
                helium.scroll_up(scroll_pixs)
            elif direction.lower() == "left":
                helium.scroll_left(scroll_pixs)
            elif direction.lower() == "right":
                helium.scroll_right(scroll_pixs)

            status = True
        except Exception as e:
            report_error(e)

        finally:
            return [status]

    def key_press(self, key_1: str = "", key_2: str = ""):
        """Type text using Browser Helium Functions and press hot keys.
        Args:
            key_1 (str): Keys you want to simulate or string you want to press 
            Eg: "tab" or "Murali". Defaults: ""
            key_2 (str, optional): Key you want to simulate with combination to key_1. 
            Eg: "shift" or "escape". Defaults: ""

        Returns:
            bool: Whether the function is successful or failed.
        """
        status = False

        from selenium.webdriver.common.keys import Keys

        browser_keys = {"enter": Keys.ENTER, "shift": Keys.SHIFT, "tab": Keys.TAB, "alt": Keys.ALT,
                        "escape": Keys.ESCAPE, "esc": Keys.ESCAPE, "ctrl": Keys.CONTROL, "control": Keys.CONTROL}
        try:

            hot_keys = list(browser_keys.keys())

            if set([key_1.lower(), key_2.lower()]).issubset(hot_keys):
                key_1 = browser_keys[key_1.lower()]
                key_2 = browser_keys[key_2.lower()]

                self.browser_driver.switch_to.active_element.send_keys(
                    key_1, key_2)

            elif key_1.lower() in hot_keys and key_2.lower() not in hot_keys:
                key_1 = browser_keys[key_1.lower()]
                self.browser_driver.switch_to.active_element.send_keys(
                    key_1)

            elif key_2.lower() in hot_keys and key_1.lower() not in hot_keys:
                key_2 = browser_keys[key_2.lower()]
                self.browser_driver.switch_to.active_element.send_keys(
                    key_2)
            else:
                print("Invalid keys combination")
                return False
            status = True
        except TimeoutException:
            print(
                "Element not found. Please check the given input or change browser_set_waiting_time().")

        except AttributeError:
            print("Invalid Input. Please check the given input.")

            sys.exit()
        except Exception as e:
            report_error(e)

        finally:
            return [status]

    def hit_enter(self):
        """Hits enter KEY in Browser
        Returns:
            bool: Whether the function is successful or failed.
        """
        status = False
        import helium
        helium.set_driver(self.browser_driver)
        try:
            helium.press(helium.ENTER)
            status = True
        except Exception as e:
            report_error(e)
        finally:
            return [status]

    def wait_until(self, text: str = "", element: str = "t"):
        """Wait until a specific element is found.
        Args:
            text (str, optional): To wait until the string appears on the screen. 
            Eg: Export Successfull Completed. Defaults: ""
            element (str, optional): Type of Element Whether its a Text(t) or Button(b). 
            Defaults: "t - Text".
        Returns:
            bool: Whether the function is successful or failed.
        """
        import helium
        helium.set_driver(self.browser_driver)
        status = False
        try:

            if element.lower() == "t":
                helium.wait_until(helium.Text(text).exists, 10)  # text

            elif element.lower() == "b":
                helium.wait_until(helium.Button(
                    text).exists, 10)  # button
            status = True
        except TimeoutException:
            print(
                "Element not found. Please check the given input or change browser_set_waiting_time().")

            sys.exit()
        except Exception as e:
            report_error(e)

        finally:
            return [status]

    def refresh_page(self):
        """Refresh the current active browser page.
        Returns:
            bool: Whether the function is successful or failed.
        """
        status = False
        try:
            self.browser_driver.refresh()
            status = True
        except Exception as e:
            report_error(e)

        finally:
            return [status]

    def set_waiting_time(self, time: int = 10):
        """
        Set the waiting time for the self.browser_driver. If element is not found in the given time, it will raise an exception.
        Args:
            time ([int]): The time in seconds to wait for the element to be found.
        """
        status = False
        try:
            import helium
            helium.set_driver(self.browser_driver)
            helium.Config.implicit_wait_secs = int(time)
            status = True
        except Exception as e:
            report_error(e)
        finally:
            return [status]

    def find_element(self, element_xpath: str = ""):
        """Find the element using xpath.
        Args:
            element_xpath (str, optional): The xpath of the element. Defaults: ""
        Returns:
            bool: Whether the function is successful or failed.
        """
        status = False
        try:
            element = self.browser_driver.find_element_by_xpath(element_xpath)
            status = True
        except Exception as e:
            report_error(e)

        finally:
            return [status, element]

    def get_text(self, element_xpath: str = ""):
        """Get the text of the element.
        Args:
            element_xpath (str, optional): The xpath of the element. Defaults: ""
        Returns:
            bool: Whether the function is successful or failed.
            str: The text of the element.
        """
        status = False
        try:
            element = self.browser_driver.find_element_by_xpath(element_xpath)
            status = True
        except Exception as e:
            report_error(e)

        finally:
            return [status, element.text]

    def close(self):
        status = False
        try:
            self.browser_driver.close()
            self.browser_driver.quit()
            status = True
        except Exception as e:
            report_error(e)
        finally:
            return [status]

    def __str__(self):
        return f"Chrome Browser with options: {self.options.experimental_options} Profile : {self.profile}"
