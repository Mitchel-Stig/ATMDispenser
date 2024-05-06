from ATMDispenser import ATMDispenser
import unittest


class TestATMDispenser(unittest.TestCase):
    def setUp(self):
        self.atm = ATMDispenser()

    def test_20(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(20)

        assert self.atm.available_currency == {20: 9, 50: 10}

    def test_40(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(40)

        assert self.atm.available_currency == {20: 8, 50: 10}

    def test_50(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(50)

        assert self.atm.available_currency == {20: 10, 50: 9}

    def test_70(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(70)

        assert self.atm.available_currency == {20: 9, 50: 9}

    def test_80(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(80)

        assert self.atm.available_currency == {20: 6, 50: 10}

    def test_100(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(100)

        assert self.atm.available_currency == {20: 10, 50: 8}

    def test_150(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(150)

        assert self.atm.available_currency == {20: 10, 50: 7}

    def test_60(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(60)

        assert self.atm.available_currency == {20: 7, 50: 10}

    def test_110(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(110)

        assert self.atm.available_currency == {20: 7, 50: 9}

    def test_200(self):
        self.atm.initialize_currency({20: 8, 50: 3})
        self.atm.withdraw(200)

        assert self.atm.available_currency == {20: 3, 50: 1}

    def test_0(self):
        self.atm.initialize_currency({20: 10, 50: 10})
        self.atm.withdraw(0)

        assert self.atm.available_currency == {20: 10, 50: 10}

    def test_add_success(self):
        self.atm.initialize_currency({20: 10, 50: 10})

        self.atm.add_currency({20: 1})
        assert self.atm.available_currency == {20: 11, 50: 10}

        self.atm.add_currency({50: 1})
        assert self.atm.available_currency == {20: 11, 50: 11}

        self.atm.add_currency({20: 1, 50: 2})
        assert self.atm.available_currency == {20: 12, 50: 13}

    def test_remove_success(self):
        self.atm.initialize_currency({20: 10, 50: 10})

        self.atm.remove_currency({20: 1})
        assert self.atm.available_currency == {20: 9, 50: 10}

        self.atm.remove_currency({50: 1})
        assert self.atm.available_currency == {20: 9, 50: 9}

        self.atm.remove_currency({20: 1, 50: 2})
        assert self.atm.available_currency == {20: 8, 50: 7}

    def test_all_currency_success(self):
        self.atm.initialize_currency({1: 10, 2: 10, 5: 10, 10: 10, 20: 10, 50: 10, 100: 10})
        self.atm.withdraw(188)

        assert self.atm.available_currency == {1: 9, 2: 9, 5: 9, 10: 9, 20: 9, 50: 9, 100: 9}

    def test_30_fail_with_only_20s(self):
        self.atm.initialize_currency({20: 8})
        self.assertRaises(Exception, self.atm.withdraw, 30)

    def test_50_fail_with_not_enough_currency(self):
        self.atm.initialize_currency({10: 4})
        self.assertRaises(Exception, self.atm.withdraw, 50)
