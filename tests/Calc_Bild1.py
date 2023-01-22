import os
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class TestCases:

    def setup_method(self):
        """
        Headless browser is just like a real browser with no User Interface(GUI).
        """

        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.get("https://testsheepnz.github.io/BasicCalculator.html")
        html = self.driver.find_element(by=By.TAG_NAME, value="html")
        html.send_keys(Keys.END)

    def test_bild1_Insert_strings_in_the_fields_First_and_Second_Number(self):

        """ insert strings, an error message should be displayed """

        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys("abc")  # tested with both string and numbers
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys("ogs")  # tested with both string and numbers
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        error_message = self.driver.find_element(by=By.ID, value="errorMsgField")
        assert 'is not a number' in error_message.text

    def test_bild1_option_integers_only(self):

        """ The system should display only integers numbers when click on 'integers only' """

        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys("86.56")  # insert float number
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys("75.31")  # insert float number
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="integerSelect").click()
        time.sleep(2)
        result = self.driver.find_element(by=By.ID, value="numberAnswerField").get_attribute('value')
        assert result.isdigit() == True



    def test_bild1_concatenate(self):

        """ Function "concatenate" - The system should concatenate de values inserted properly """
        text_input1 = 'TEST'
        text_input2 = 'uht56'

        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        drop_down_operation = Select(self.driver.find_element(by=By.ID, value="selectOperationDropdown"))
        time.sleep(2)
        drop_down_operation.select_by_value("4")  # select item by id - concatenate
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys(text_input1)  # insert string
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys(text_input2)  # insert string
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        result = self.driver.find_element(by=By.ID, value="numberAnswerField").get_attribute('value')
        assert result == f'{text_input1}{text_input2}'

    def test_bild1_add_insert_numbers_(self):

        """ Function "Add" - inserted both (integer and float numbers)
        The system should sum de numbers properly"""
        number1 = 65
        number2 = 67.86
        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys(number1)  # insert number
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys(number2)  # insert number
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        result = self.driver.find_element(by=By.ID, value="numberAnswerField").get_attribute('value')
        assert result == str(number1 + number2)


    def test_bild1_button_clear(self):

        """ The system should clear the field answer when click on "Clear """

        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys("98")  # insert number
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys("876")  # insert number
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="clearButton").click()
        time.sleep(2)
        result = self.driver.find_element(by=By.ID, value="numberAnswerField").get_attribute('value')
        assert result == ''

    def test_bild1_subtract_insert_numbers(self):

        """ Function "subtract" - inserted both(float and integer numbers)The system should
        subtract de numbers properly """
        number1 = 1500
        number2 = 110.43
        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        drop_down_operation = Select(self.driver.find_element(by=By.ID, value="selectOperationDropdown"))
        time.sleep(2)
        drop_down_operation.select_by_value("1")  # select item by id - subtract
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys(number1)  # insert number
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys(number2)  # insert number
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        result = self.driver.find_element(by=By.ID, value="numberAnswerField").get_attribute('value')
        assert result == str(number1 - number2)

    def test_bild1_multiply_insert_numbers_(self):

        """ Function "multiply" - insert numbers(float and integer) """

        number1 = 86.56
        number2 = 75.31
        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        drop_down_operation = Select(self.driver.find_element(by=By.ID, value="selectOperationDropdown"))
        time.sleep(2)
        drop_down_operation.select_by_value("2")  # select item by id - multiply
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys(number1)  # insert number
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys(number2)  # insert number(integer or float)
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        result = self.driver.find_element(by=By.ID, value="numberAnswerField").get_attribute('value')
        assert result == str(number1 * number2)

    def test_bild1_Divide_insert_numbers_(self):

        """ Function "divide" - inserted both(float and integer numbers)
        The system should divide the numbers properly """

        number1 = 86.56
        number2 = 75.31
        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        drop_down_operation = Select(self.driver.find_element(by=By.ID, value="selectOperationDropdown"))
        time.sleep(2)
        drop_down_operation.select_by_value("3")  # select item by id - divide
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys(number1)  # insert number
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys(number2)  # insert number
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        result = self.driver.find_element(by=By.ID, value="numberAnswerField").get_attribute('value')
        assert result == str(number1 / number2)

    def test_bild1_Divide_by_zero(self):

        """ Function "divide" - divide a number by zero
        The system should display an error message """

        number1 = 86.56
        number2 = 0
        drop_down_name = Select(self.driver.find_element(by=By.ID, value="selectBuild"))
        time.sleep(2)
        drop_down_name.select_by_value("1")  # select item by id - Bild 1
        time.sleep(2)
        drop_down_operation = Select(self.driver.find_element(by=By.ID, value="selectOperationDropdown"))
        time.sleep(2)
        drop_down_operation.select_by_value("3")  # select item by id - divide
        time.sleep(2)
        first_number = self.driver.find_element(by=By.NAME, value="number1")
        first_number.send_keys(number1)  # insert number
        time.sleep(2)
        second_number = self.driver.find_element(by=By.NAME, value="number2")
        second_number.send_keys(number2)  # insert zero
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="calculateButton").click()
        time.sleep(2)
        assert number2 != str(0), 'Divide by zero error! '