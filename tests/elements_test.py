from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
import time


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            input_data = text_box_page.fill_all_fields()

            output_data = text_box_page.check_filled_form()

            assert input_data == output_data, "Incorrect data in textBox inputs"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()

            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()

            input_data = check_box_page.get_checked_checkboxes()

            output_data = check_box_page.get_output_result()

            assert input_data == output_data, "The checkboxes have not been checked"

    class TestRadioButton:

        def test_radio_btn(self, driver):
            radio_btn_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_btn_page.open()

            item = radio_btn_page.click_random_radio_btn()

            item_result = radio_btn_page.get_checked_radio_btn()

            assert (
                item == item_result
            ), "The random element does not match the selected one"

            click_item, selected_item = radio_btn_page.click_all_radio_button()

            assert click_item == selected_item, "Not all data matches the selection"

            cheked_data = ["yes", "impressive", "no"]
            for i in cheked_data:

                assert (
                    radio_btn_page.click_on_the_radio_btn(i)
                    == radio_btn_page.get_checked_radio_btn()
                ), f'Page element "{i}" is not clickable'

    class TestWebTable:

        def test_web_table_and_person(self, driver):

            web_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_page.open()
            for i in range(20):
                new_person = web_page.add_new_person_in_table()

                result_table = web_page.check_new_added_person()

                assert new_person in result_table, "Person is not found in the table"
