from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:

        def test_text_box(self,driver):
            text_box_page = TextBoxPage(driver,'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            
            full_name,email,current_address,permanent_address = text_box_page.check_filled_form()

            print(full_name)
            print(email)
            print(current_address)
            print(permanent_address)