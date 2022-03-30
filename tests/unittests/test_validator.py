"""
Project: Descriptors
Filename: test_validator.py
Description

Command line: python3 -m pytest tests/unittests/test_validator.py
"""
__author__ = "Guido Boehm"
__filename__ = "test_validator.py"
__credits__ = [""]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Guido Boehm"
__email__ = "olb@family-boehm.de"
__status__ = "Prototype"
__copyright__ = """
Copyright 2022, Guido Boehm
All Rights Reserved. 
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE. 
"""

from src.Validator_Classes import IntegerField, CharField, CurrencyField

import unittest


class TestIntegerField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        """
        creates an object for the subsequent tests
        Args:
            min_ (int/None): lower bound
            max_ (int/None): upper bound

        Returns:

        """
        obj = type('TestClass', (), {'age': IntegerField(min_, max_)})
        return obj()

    def test_set_age_ok(self):
        """Tests that valid values can be assigned/retrieved"""
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_values = range(min_, max_)

        for i, value in enumerate(valid_values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_invalid(self):
        """Tests that invalid values raise ValueErrors"""
        min_ = -10
        max_ = 10
        obj = self.create_test_class(min_, max_)
        bad_values = list(range(min_ - 5, min_))
        bad_values += list(range(max_ + 1, max_ + 5))
        bad_values += [10.5, 1 + 0j, 'abc', (1, 2)]

        for i, value in enumerate(bad_values):
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.age = value

    def test_class_get(self):
        """Tests that class attribute retrieval returns the descriptor instance"""
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)
        self.assertIsInstance(obj_class.age, IntegerField)

    def test_set_age_min_only(self):
        """Tests that we can specify a min value only"""
        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(min_, min_ + 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_max_only(self):
        """Tests that we can specify a max value only"""
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        values = range(max_ - 100, max_, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_no_limits(self):
        """Tests that we can use IntegerField without any limits at all"""
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(-100, 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)


class TestCharField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        """
        creates object ths is subjected to the tests
        Args:
            min_ (int/None): lower bound
            max_ (int/None): upper bound

        Returns:

        """
        obj = type('TestClass', (), {'name': CharField(min_, max_)})
        return obj()

    def test_set_name_ok(self):
        """Tests that valid values can be assigned/retrieved"""
        min_ = 1
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(min_, max_)

        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_invalid(self):
        """Tests that invalid values raise ValueErrors"""
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)
        bad_lengths = list(range(min_ - 5, min_))
        bad_lengths += list(range(max_ + 1, max_ + 5))
        for i, length in enumerate(bad_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.name = value

    def test_class_get(self):
        """Tests that class attribute retrieval returns the descriptor instance"""
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)
        self.assertIsInstance(obj_class.name, CharField)

    def test_set_name_min_only(self):
        """Tests that we can specify a min length only"""
        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(min_, min_ + 100, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_min_negative_or_none(self):
        """Tests that setting a negative or None length results in a zero length"""
        obj = self.create_test_class(-10, 100)
        self.assertEqual(type(obj).name._min, 0)
        self.assertEqual(type(obj).name._max, 100)

        obj = self.create_test_class(None, None)
        self.assertEqual(type(obj).name._min, 0)
        self.assertIsNone(type(obj).name._max)

    def test_set_name_max_only(self):
        """Tests that we can specify a max length only"""
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(max_ - 100, max_, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_no_limits(self):
        """Tests that we can use CharField without any limits at all"""
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(0, 100, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)


class TestCurrencyField(unittest.TestCase):
    @staticmethod
    def create_test_class():
        """
        creates object ths is subjected to the tests

        """
        obj = type('TestClass', (), {'name': CurrencyField()})
        return obj()

    def test_currency_ISO_length(self):
        """Tests that currency ISO value can obly be 3 chars long"""
        """Tests that invalid values raise ValueErrors"""
        obj = self.create_test_class()
        bad_lengths = list(range(0, 3))
        bad_lengths += list(range(4, 6))
        for i, length in enumerate(bad_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.name = value

    def test_currency_bad_type(self):
        """Tests that currency ISO value is a str"""
        """Tests that invalid values raise ValueErrors"""
        obj = self.create_test_class()
        bad_value = [1, 1.0, None]
        for i, value in enumerate(bad_value):
            with self.subTest(test_number=1):
                with self.assertRaises(ValueError):
                    obj.name = value

    def test_currency_bad_value(self):
        """Tests that invalid currency ISO code raise ValueErrors"""
        obj = self.create_test_class()
        bad_value = ['ABC', 'XYZ']
        for i, value in enumerate(bad_value):
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.name = value

    def test_currency_good_value(self):
        """Tests that invalid currency ISO code raise ValueErrors"""
        obj = self.create_test_class()
        bad_value = ['EUR', 'USD', 'BZD']
        for i, value in enumerate(bad_value):
            with self.subTest(test_number=i):
                obj.name = value
