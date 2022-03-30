"""
Project: PayPalRefund
Filename: test_PayPalClasses.py
Description

Command line: python3 -m pytest tests/unittests/test_PayPalClasses.py
"""
__author__ = "Guido Boehm"
__filename__ = "test_PayPalClasses.py"
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

from src.PayPalClasses import PayPalAPI, Amount

import json
import requests
import requests_mock

from pathlib import Path
from unittest import TestCase

SCRIPT_PATH = Path(__file__).parent.absolute()
DATA_DIR = Path(SCRIPT_PATH, 'data')


class TestPayPalAPI(TestCase):

    @requests_mock.mock()
    def test_get_token_success(self, mock):
        paypal = PayPalAPI(client_id='abc', secret='123')
        url = PayPalAPI.baseurl + '/v1/oauth2/token'
        filename = Path(DATA_DIR, "token_success.json")
        with filename.open('r') as file:
            response = json.load(file)
        mock.post(url, json=response, status_code=200)
        paypal.get_token('/v1/oauth2/token')
        self.assertEqual(paypal.token, response['access_token'])

    @requests_mock.mock()
    def test_get_token_auth_failed(self, mock):
        paypal = PayPalAPI(client_id='abc', secret='123')
        url = PayPalAPI.baseurl + '/v1/oauth2/token'
        filename = Path(DATA_DIR, "token_auth_failed.json")
        with filename.open('r') as file:
            response = json.load(file)
        mock.post(url, json=response, status_code=401)
        with self.assertRaises(requests.exceptions.HTTPError):
            paypal.get_token('/v1/oauth2/token')


    def test_client_id(self):
        paypal = PayPalAPI(client_id='abc', secret='123')
        self.assertEqual(paypal.client_id, 'abc')
        self.assertEqual(paypal.secret, '123')
        with self.assertRaises(ValueError):
            paypal.client_id = 123
        with self.assertRaises(ValueError):
            paypal.client_id = ' '
        with self.assertRaises(ValueError):
            paypal.secret = 123
        with self.assertRaises(ValueError):
            paypal.secret = ' '


class TestAmount(TestCase):
    def test_either_value_none(self):
        """
        tests that ValueError is raised if either paremeter is None
        """
        bad_values = [(None, 'EUR'), ('1.11', None)]
        for i, value in enumerate(bad_values):
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    amount = Amount(*value)


    def test_bad_values(self):
        """
        tests that ValueError is raised if either paremeter is None
        Note: a value '1,11' would be a bad one as it does not represent a propper float. However, this is not
        covererd by the Amount class.
        PayPal's API will raise an HTTP 400 error if value does not conform to expected format
        """
        bad_values = [('1', 'ABC'), ('1', 'EUR'), ('1.11', 'ABC'), (1, 'EUR')]
        for i, value in enumerate(bad_values):
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    amount = Amount(*value)

    def test_amount_property(self):
        """
        test that the property a dictionary and correct values are returned
        """
        amount = Amount('1.11', 'EUR')
        self.assertDictEqual(amount.amount, {"value": '1.11', "currency_code": "EUR"})



def main(args=None):
    pass


if __name__ == "__main__":

    main()
