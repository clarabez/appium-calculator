from webdriver import Webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class Calculadora:
    def __init__(self, driver):
        self.driver = driver
        self.result = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ID, 'com.android.calculator2:id/result'
        ))
        self.soma = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ACCESSIBILITY_ID, 'plus'
        ))
        self.divisao = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ACCESSIBILITY_ID, 'divide'
        ))
        self.multiplicacao = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ACCESSIBILITY_ID, 'multiply'
        ))
        self.subtracao = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ACCESSIBILITY_ID, 'minus'
        ))

    def clicar_numero(self, num):
        _n = str(num)
        self.driver.instance.find_element_by_ID, (MobileBy.ID, 'com.android.calculator2:id/digit_' + _n).click()
        assert _n in self.result, 'Resultado na Calculadora não é o que vc inseriu'

    def somando(self, num1, num2):
        _resultadopy = num1 + num2
        _resultadoappium = int(self.result.text)

        assert _resultadopy == _resultadoappium, 'Soma incorreta'
