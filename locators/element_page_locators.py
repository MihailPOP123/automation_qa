from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME =  (By.CSS_SELECTOR,"input[id='userName']")
    EMAIL = (By.CSS_SELECTOR,"input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR,"textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR,"textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR,"button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR,'#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR,'#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR,'#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR,'#output #permanentAddress')


class CheckBoxPageLocators:
    
    OPEN_SWITCHER = (By.CSS_SELECTOR,"span[class='rc-tree-switcher rc-tree-switcher_close']")
    CLOSED_SWITCHER = (By.CSS_SELECTOR,"span[class='rc-tree-switcher rc-tree-switcher_open']")
    ITEM_LIST = (By.CSS_SELECTOR,"span[class='rc-tree-checkbox']")
    ARIA_CHECKED = (By.CSS_SELECTOR,"span[aria-checked='true']")
    OUTPUT_RESULT = (By.CSS_SELECTOR,"span[class='text-success']")

class RadioButtonPageLocators:
    
    CHECK_LABEL = (By.CSS_SELECTOR,"label[class='form-check-label']")
    OUTPUT_SELECTED = (By.CSS_SELECTOR,"span[class='text-success']")

    YES_RADIO_BTN = (By.CSS_SELECTOR,"label[for='yesRadio']")
    IMPRESSIVE_RADIO_BTN = (By.CSS_SELECTOR,"label[for='impressiveRadio']")
    NO_RADIO_BTN = (By.CSS_SELECTOR,"label[for='noRadio']")

class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR,"button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR,"input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR,"input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR,"input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR,"input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR,"input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR,"button[id='submit']")