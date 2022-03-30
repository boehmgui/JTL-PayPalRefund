"""
Project: PayPalRefund

Description:

Command line: python3 -m pytest tests/unittests/test_validator.py
"""
__author__ = "Guido Boehm"
__copyright__ = "Copyright 2022, PayPalRefund"
__filename__ = "test_pp_refund.py"
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

from src.pp_refund import main

from unittest import TestCase


class Test_pp_refund(TestCase):
    def test_invalid_cli_params(self):
        bad_values = [{'refund_details': {'capture_id': '', 'amount': '1.20', 'currency_code': 'EUR',
                                          'invoice_id': 'abc', 'note_to_payer': 'jjfjk jkhhjkgh'}},
                          {'refund_details': {'capture_id': 'unittest', 'amount': '1.20', 'currency_code': 'XYZ',
                                              'invoice_id': 'abc', 'note_to_payer': 'jjfjk jkhhjkgh'}},
                          {'refund_details': {'capture_id': 'unittest', 'amount': '1.20', 'invoice_id':
                                              'abc', 'note_to_payer': 'jjfjk jkhhjkgh'}},
                          {'refund_details': {'capture_id': 'unittest', 'currency_code': 'EUR',
                                              'invoice_id': 'abc', 'note_to_payer': 'jjfjk jkhhjkgh'}}
                      ]
        for i, value in enumerate(bad_values):
            with self.subTest(test_number=i):
                with self.assertRaises(SystemExit) as cm:
                    main(value)
                self.assertEqual(cm.exception.code, 2)
