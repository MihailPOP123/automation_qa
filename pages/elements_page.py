from locators.element_page_locators import TextBoxPageLocators,CheckBoxPageLocators,RadioButtonPageLocators,WebTablePageLocators
from pages.base_page import BasePage
from generator.generator import generated_person
from selenium.common.exceptions import TimeoutException

import random
import time

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address 


        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return  full_name,email,current_address,permanent_address


    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        
        return full_name,email,current_address,permanent_address
    
class CheckBoxPage(BasePage):
    
    locators = CheckBoxPageLocators()

    def open_full_list(self):

        while True:
            try:
                switcher = self.element_is_visible(self.locators.OPEN_SWITCHER)
                switcher.click()
            except TimeoutException:
                
                break



    def click_random_checkbox(self):

        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        
        random.shuffle(item_list)

        for item in item_list:
            
            item.click()

               
    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.ARIA_CHECKED)
        data = []
       
        for box in checked_list:
            data.append(box.get_attribute("aria-label").replace('Select ',''))
            
        return str(sorted(data)).replace(' ','').replace('.doc','').lower()
    
    def get_output_result(self):
        result_list =  self.element_are_present(self.locators.OUTPUT_RESULT)
        result_data = []
        
        for item in result_list:
            result_data.append(item.text)
            
        return str(sorted(result_data)).replace(' ','').lower()


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def click_all_radio_button(self):
        item_list = self.element_are_visible(self.locators.CHECK_LABEL)
        
        data_click = []
        data_selected = []
        for item in item_list:
            item.click()
            data_click.append(item.text)

            selected_item = self.get_checked_radio_btn()
            data_selected.append(selected_item)

        return data_click,data_selected
    
    def click_on_the_radio_btn(self,choice):

        choices = {
            'yes':self.locators.YES_RADIO_BTN,
            'impressive':self.locators.IMPRESSIVE_RADIO_BTN,
            'no':self.locators.NO_RADIO_BTN,
        }

        radio = self.element_is_visible(choices[choice])
        
        radio.click()

        return radio.text


        
    def click_random_radio_btn(self):
        item_list = self.element_are_visible(self.locators.CHECK_LABEL)

        random_item = random.choice(item_list)

        random_item.click()

        return random_item.text

        
    def get_checked_radio_btn(self):

        item_selected = self.element_is_present(self.locators.OUTPUT_SELECTED)

        return item_selected.text

class WebTablePage(BasePage):
    
    locators = WebTablePageLocators()
    

        
