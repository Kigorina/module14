import unittest
from calc import calc_me


class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2, "+"), 3)

    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2, "-"), 2)

    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8, "*"), 98765432)

    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9, "/"), 12345679)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0, "/"), 'ERROR: Divide by zero!')

    #---------Тесты для новых функций---------------------------------------------#

    def test_oper_neg(self):
        """Возведение в степень"""
        self.assertEqual(calc_me(4, 2, "^"), 16)

    def test_mul(self):
        """Ввод символьных данных"""
        self.assertEqual(" ", " ", "*"), 'ERROR: now it is does not supported'

    def test_send_num1(self):
        """Запуск без переменных Число1"""
        self.assertEqual(calc_me(None, 2, "+"), 'ERROR: send me Number1')

    def test_send_num2(self):
        self.assertEqual(calc_me(2, None, "+"), 'ERROR: send me Number2')


if __name__ == '__main__':
    unittest.main(verbosity=2)
