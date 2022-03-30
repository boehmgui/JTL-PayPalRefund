"""
Project: Descriptors
Filename: Validator_Classes.py
Description

Classes for filed validation

"""
__author__ = "Guido Boehm"
__filename__ = "Validator_Classes.py"
__credits__ = [""]
__license__ = "GNU GPLv3"
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

import numbers

from src.utils.Currencies import Currencies

from abc import ABC, abstractmethod


class BaseValidator(ABC):
    """
    Base class for value validation
    """
    def __init__(self, min_=None, max_=None):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

    @abstractmethod
    def validate(self, value):
        """
        abstract validate method. This will need to be implemented specifically by each subclass
        Args:
            value: value that is subjetced to validation

        Returns:

        """
        pass

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.prop_name] = value


class IntegerField(BaseValidator):
    """
    Subclass that validates interger values
    """
    def validate(self, value):
        """
        validates the value
        Args:
            value: value that is subjected to validation

        Returns:

        Raises:
            ValueError: if conditions are not met

        """
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer.')
        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}.')
        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}')


class CharField(BaseValidator):
    """
    Subclass to validate strings
    """
    def __init__(self, min_=None, max_=None):
        min_ = max(min_ or 0, 0)
        super().__init__(min_, max_)

    def validate(self, value):
        """
        validates the value
        Args:
            value: value that is subjected to validation

        Returns:

        Raises:
            ValueError: if conditions are not met
        """
        # strip spaces
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string.')
        value = value.strip()
        if self._min is not None and len(value) < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min} chars.')
        if self._max is not None and len(value) > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max} chars')


class CurrencyField(BaseValidator):
    """
    validates the three-character ISO-4217 currency code that identifies the currency.
    Minimum length: 3.
    Maximum length: 3.
    """
    def __init__(self):
        pass

    def validate(self, value):
        if not isinstance(value, str) or len(value) != 3:
            raise ValueError(f'{value} must be a string and 3 charcters long.')
        if getattr(Currencies, value, None) is None:
            raise ValueError(f'{value} must be a valid ISO currency code')

