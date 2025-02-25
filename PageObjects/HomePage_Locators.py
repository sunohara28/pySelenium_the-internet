from selenium.webdriver.common.by import By

class HomePageLocators:

    var_abtest_locator = (By.XPATH, "//a[@href='/abtest']")
    var_add_remove_elements_locator = (By.XPATH, "//a[@href='/add_remove_elements/']")
    var_basic_auth_locator = (By.XPATH, "//a[@href='/basic_auth']")
    var_broken_images_locator = (By.XPATH, "//a[@href='/broken_images']")
    var_challenging_dom_locator = (By.XPATH, "//a[@href='/challenging_dom']")
    var_checkboxes_locator = (By.XPATH, "//a[@href='/checkboxes']")
    var_context_menu_locator = (By.XPATH, "//a[@href='/context_menu']")
    var_digest_auth_locator = (By.XPATH, "//a[@href='/digest_auth']")
    var_disappearing_elements_locator = (By.XPATH, "//a[@href='/disappearing_elements']")
    var_drag_and_drop_locator = (By.XPATH, "//a[@href='/drag_and_drop']")
    var_dropdown_locator = (By.XPATH, "//a[@href='/dropdown']")
    var_dynamic_content_locator = (By.XPATH, "//a[@href='/dynamic_content']")
    var_dynamic_controls_locator = (By.XPATH, "//a[@href='/dynamic_controls']")
    var_dynamic_loading_locator = (By.XPATH, "//a[@href='/dynamic_loading']")
    var_entry_ad_locator = (By.XPATH, "//a[@href='/entry_ad']")
    var_exit_intent_locator = (By.XPATH, "//a[@href='/exit_intent']")
    var_download_locator = (By.XPATH, "//a[@href='/download']")
    var_upload_locator = (By.XPATH, "//a[@href='/upload']")
    var_floating_menu_locator = (By.XPATH, "//a[@href='/floating_menu']")
    var_forgot_password_locator = (By.XPATH, "//a[@href='/forgot_password']")
    var_login_locator = (By.XPATH, "//a[@href='/login']")
    var_frames_locator = (By.XPATH, "//a[@href='/frames']")
    var_geolocation_locator = (By.XPATH, "//a[@href='/geolocation']")
    var_horizontal_slider_locator = (By.XPATH, "//a[@href='/horizontal_slider']")
    var_hovers_locator = (By.XPATH, "//a[@href='/hovers']")
    var_infinite_scroll_locator = (By.XPATH, "//a[@href='/infinite_scroll']")
    var_inputs_locator = (By.XPATH, "//a[@href='/inputs']")
    var_jqueryui_menu_locator = (By.XPATH, "//a[@href='/jqueryui/menu']")
    var_javascript_alerts_locator = (By.XPATH, "//a[@href='/javascript_alerts']")
    var_javascript_error_locator = (By.XPATH, "//a[@href='/javascript_error']")
    var_key_presses_locator = (By.XPATH, "//a[@href='/key_presses']")
    var_large_locator = (By.XPATH, "//a[@href='/large']")
    var_windows_locator = (By.XPATH, "//a[@href='/windows']")
    var_nested_frames_locator = (By.XPATH, "//a[@href='/nested_frames']")
    var_notification_message_locator = (By.XPATH, "//a[@href='/notification_message']")
    var_redirector_locator = (By.XPATH, "//a[@href='/redirector']")
    var_download_secure_locator = (By.XPATH, "//a[@href='/download_secure']")
    var_shadowdom_locator = (By.XPATH, "//a[@href='/shadowdom']")
    var_shifting_content_locator = (By.XPATH, "//a[@href='/shifting_content']")
    var_slow_locator = (By.XPATH, "//a[@href='/slow']")
    var_tables_locator = (By.XPATH, "//a[@href='/tables']")
    var_status_codes_locator = (By.XPATH, "//a[@href='/status_codes']")
    var_typos_locator = (By.XPATH, "//a[@href='/typos']")
    var_tinymce_locator = (By.XPATH, "//a[@href='/tinymce']")

    def __init__(self,driver):
        self.driver = driver

    def abtest_locator(self):
        return self.driver.find_element(*HomePageLocators.var_abtest_locator)

    def add_remove_locator(self):
        return self.driver.find_element(*HomePageLocators.var_add_remove_elements_locator)

    def basic_auth_locator(self):
        return self.driver.find_element(*HomePageLocators.var_basic_auth_locator)

    def broken_image_locator(self):
        return self.driver.find_element(*HomePageLocators.var_broken_images_locator)

    def challenging_dom_locator(self):
        return self.driver.find_element(*HomePageLocators.var_challenging_dom_locator)