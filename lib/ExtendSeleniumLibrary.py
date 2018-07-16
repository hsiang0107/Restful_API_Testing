import re
from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.base import keyword
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lib.ConfigHelper import ConfigHelper


class ExtendSeleniumLibrary(SeleniumLibrary):
    @keyword
    def list_should_have_values(self, locator, values, msg=None):
        result = self.get_list_items(locator)

        for option in values:
            if result.count(option) == 0:
                if msg is None:
                    msg = "can not find '%s' in the list %s" % (option, result)
                raise AssertionError(msg)

    @keyword
    def element_should_be_selected(self, locator):
        element = self.find_element(locator)
        if not element.is_selected():
            raise AssertionError("Element '%s' should have been selected but was not." % locator)

    @keyword
    def element_value_should_be(self, locator, value):
        element = self.find_element(locator)
        if not re.match(value, element.get_attribute('value')):
            raise AssertionError("Element '%s'\'s value should be %s but was not." % (locator, value))

    @keyword
    def check_product_in_log_query(self, product_path):
        node_container_selector = '.product-view.show li.hasFolder'
        node_postfix_selector = ' li'
        current_selector = node_container_selector
        current_tuple = None
        self._uncheck_all_products_in_log_query()
        for node in product_path:
            current_selector += node_postfix_selector
            tuples = self.find_elements('css=' + current_selector)
            for t in tuples:
                if t.text == node:
                    current_tuple = t
                    break
            if current_tuple is None:
                raise AssertionError('Product name %s is not found.' % node)
            if product_path[-1] == node:
                current_tuple.click()
                return
            else:
                current_tuple.find_element_by_css_selector('span.icon.collapse').click()

    def _uncheck_all_products_in_log_query(self):
        root_selector = '.product-view.show li.hasFolder > div'
        self.find_element('css=' + root_selector).click()

    @keyword
    def set_advanced_filter_in_log_query(self, criteria):
        criteria_key_selector = '.criteriaDropdownSelector'
        criteria_operator_selector = '.CriteriaPannel > .CriteriaRow:last-child > :nth-child(2)'
        criteria_value_selector = '.CriteriaPannel > .CriteriaRow:last-child > :nth-child(3)'
        self._set_drop_down_value(self.find_element('css=' + criteria_key_selector), criteria[0])
        self._set_drop_down_value(self.find_element('css=' + criteria_operator_selector), criteria[1])
        value_element = self.find_element('css=' + criteria_value_selector)
        if value_element.get_attribute('type') == 'text':
            value_element.send_keys(criteria[2])
        else:
            self._set_drop_down_value(value_element, criteria[2])

    def _set_drop_down_value(self, drop_down_element, value):
        drop_down_button_selector = 'button'
        drop_down_item_selector = 'li'
        drop_down_element.find_element_by_css_selector(drop_down_button_selector).click()
        items = drop_down_element.find_elements_by_css_selector(drop_down_item_selector)
        found = False
        for i in items:
            if i.text.lower() == value.lower():
                i.click()
                found = True
                break
        if not found:
            raise AssertionError('Cannot locate drop down item %s.' % value)

    @keyword
    def download_log_query_csv(self):
        export_button_selector = '.inner-btn.tm-btn.tm-btn-default:nth-child(3)'
        cancel_button_selector = '#btn_Cancel'
        self.find_element('css=' + export_button_selector).click()
        current_frame_selector = '#' + self.driver.execute_script('return self.name')
        self.driver.switch_to.parent_frame()
        parent_frame_selector = 'frame[name="%s"]' % self.driver.execute_script('return self.name')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.run_keyword('wait_until_element_is_not_visible', ['css=%s' % cancel_button_selector, 10], {})
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.frame(self.find_element('css=' + parent_frame_selector))
        self.driver.switch_to.frame(self.find_element('css=' + current_frame_selector))

    @keyword
    def parse_log_query_table_result(self):
        next_page_button_selector = '.tm-btn.tm-btn-pagination:nth-child(2)'
        ret = list([])
        ret.append(self._parse_log_query_table_header())
        self._render_entire_table()
        original_speed = self.run_keyword('set_selenium_speed', [0.01], {})
        while True:
            ret.extend(self._parse_log_query_table_body())
            next_button = self.find_element('css=' + next_page_button_selector)
            if next_button.is_enabled():
                next_button.click()
                self.run_keyword('wait_until_page_does_not_contain_element', ['css=%s' % '.data-table.loading'], {})
            else:
                break
        self.run_keyword('set_selenium_speed', [original_speed], {})
        return ret

    @keyword
    def get_cm_cookies(self, url, credential=None):
        config = ConfigHelper()
        if credential is None:
            user = config.get_data_from_config('CM', 'admin', 'account')
            pwd = config.get_data_from_config('CM', 'admin', 'password')
        else:
            user = credential['user']
            pwd = credential['pwd']
        # else:
        #     user = config.get_data_from_config('CM', 'admin', 'account')
        #     pwd = config.get_data_from_config('CM', 'admin', 'password')
        driver = webdriver.Chrome()
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtUserName")))
        driver.find_element_by_id("txtUserName").send_keys(user)
        driver.find_element_by_id("txtPassword").send_keys(pwd)
        driver.find_element_by_id("loginLink").click()
        cookies = driver.get_cookies()
        return cookies

    def _render_entire_table(self):
        current_pos = 0
        table_selector = '.table.table-bordered > tbody'
        total_width = self.driver.execute_script('return document.querySelector(\'%s\').scrollWidth' % table_selector)
        viewable_width = self.driver.execute_script('return document.querySelector(\'%s\').clientWidth' % table_selector)
        while current_pos < (total_width - viewable_width):
            current_pos = self.driver.execute_script('return document.querySelector(\'%s\').scrollLeft += %d' %
                                                     (table_selector, viewable_width))
        self.driver.execute_script('document.querySelector(\'%s\').scrollLeft = 0' % table_selector)

    def _parse_log_query_table_body(self):
        ret = []
        table_row_selector = '#react-table-rows > tr'
        content_rows = self.find_elements('css=' + table_row_selector)
        for row in content_rows:
            ret.append([cell.text for cell in row.find_elements_by_css_selector('td')])
        return ret

    def _parse_log_query_table_header(self):
        header_cell_selector = 'thead th'
        header_cells = self.find_elements('css=' + header_cell_selector)
        return [cell.text for cell in header_cells]
