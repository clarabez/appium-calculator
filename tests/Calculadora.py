import unittest
from webdriver.Webdriver import Driver
from pageobjects.Calc import Calculadora


class CalculadoraHome(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.quit()

    def test_one(self):
        launch = Calculadora(self.driver)
        launch.go_produtos()

    def test_two(self):
        launch = Calculadora(self.driver)
        launch.go_carrinho

    def test_three(self):
        launch = Calculadora(self.driver)
        launch.go_conta
